#!/usr/bin/env python3
"""Validate prompt cases and recorded evidence; never launch or impersonate a model."""

import argparse
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
ARMS = {"none", "prior", "candidate"}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, "duplicate JSON key: " + key)
        result[key] = value
    return result


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique_object)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def validate_suite(data, skills):
    require(isinstance(data, dict) and data.get("schema_version") == 1, "unsupported suite schema")
    cases = data.get("cases")
    require(isinstance(cases, list) and cases, "cases must be a nonempty list")
    found = {}
    covered = set()
    for case in cases:
        require(isinstance(case, dict), "case must be an object")
        identity = case.get("id")
        require(isinstance(identity, str) and re.fullmatch(r"[A-Z][0-9]{2}", identity), "invalid case ID")
        require(identity not in found, "duplicate case ID: " + identity)
        require(nonempty(case.get("prompt")), "missing prompt: " + identity)
        routing = case.get("routing", {})
        require(isinstance(routing, dict), "routing must be an object")
        targets = routing.get("any_of")
        require(isinstance(targets, list) and all(isinstance(x, str) for x in targets), "invalid routing targets")
        require(len(set(targets)) == len(targets) and set(targets) <= skills, "duplicate or unknown routing target")
        require(type(routing.get("none")) is bool and routing["none"] == (not targets), "inconsistent negative control")
        rubric = case.get("rubric")
        require(isinstance(rubric, dict) and set(rubric) == {"contract", "scope", "evidence"}, "invalid rubric dimensions")
        require(all(nonempty(v) for v in rubric.values()), "empty rubric")
        found[identity] = case
        covered.update(targets)
    require(covered == skills, "suite does not cover the installed skill inventory")
    require(any(c["routing"]["none"] for c in cases), "suite needs a negative control")
    return found


def template(case, arm, suite_hash):
    require(arm in ARMS, "invalid arm")
    return {
        "schema_version": 1, "suite_sha256": suite_hash, "case": case["id"],
        "arm": arm, "status": "not-run", "reason": None,
        "pack_commit": None, "repetition": 1,
        "environment": {key: None for key in ("model", "settings", "harness", "permissions", "isolation")},
        "trace": {"path": None, "sha256": None}, "loaded_skills": None,
        "reviewer": None,
        "grades": {key: {"status": "unavailable", "evidence": None} for key in case["rubric"]},
    }


def validate_record(record, cases, suite_hash, directory, skills):
    require(isinstance(record, dict) and record.get("schema_version") == 1, "unsupported record schema")
    require(record.get("suite_sha256") == suite_hash, "suite hash mismatch")
    identity = record.get("case")
    require(isinstance(identity, str) and identity in cases, "unknown case")
    arm = record.get("arm")
    require(isinstance(arm, str) and arm in ARMS, "invalid arm")
    status = record.get("status")
    require(status in ("not-run", "unavailable", "completed"), "invalid run status")
    if status != "completed":
        if status == "unavailable":
            require(nonempty(record.get("reason")), "unavailable run needs a reason")
        return {"status": status, "routing": "unavailable", "behavior": "unavailable"}
    require(type(record.get("repetition")) is int and record["repetition"] > 0, "invalid repetition")
    commit = record.get("pack_commit")
    if arm == "none":
        require(commit is None, "no-pack arm cannot have a pack commit")
    else:
        require(isinstance(commit, str) and re.fullmatch(r"[0-9a-f]{40}", commit), "pin a full pack commit")
    environment = record.get("environment")
    require(isinstance(environment, dict), "missing environment")
    for key in ("model", "settings", "harness", "permissions", "isolation"):
        require(nonempty(environment.get(key)), "missing environment: " + key)
    require(nonempty(record.get("reviewer")), "missing reviewer identity/configuration")
    trace = record.get("trace")
    require(isinstance(trace, dict) and nonempty(trace.get("path")), "missing trace")
    relative = Path(trace["path"])
    require(not relative.is_absolute() and ".." not in relative.parts, "trace must stay within the record directory")
    base = directory.resolve()
    path = base / relative
    require(not any(p.is_symlink() for p in [path, *path.parents] if p != base and base in p.parents), "trace symlinks are forbidden")
    require(path.is_file() and path.resolve().is_relative_to(base), "trace is not a local regular file")
    raw = path.read_bytes()
    require(bool(raw.strip()) and digest(raw) == trace.get("sha256"), "empty trace or trace hash mismatch")
    loaded = record.get("loaded_skills")
    require(isinstance(loaded, list) and all(isinstance(x, str) for x in loaded), "record observed loaded skills, not null")
    require(len(set(loaded)) == len(loaded) and set(loaded) <= skills, "duplicate or unexpected loaded skill")
    if arm == "none":
        require(not loaded, "no-pack arm loaded pack skills")
        routing = "not-applicable"
    else:
        expected = cases[identity]["routing"]
        matched = not loaded if expected["none"] else bool(set(loaded) & set(expected["any_of"]))
        routing = "pass" if matched else "fail"
    grades = record.get("grades")
    require(isinstance(grades, dict) and set(grades) == set(cases[identity]["rubric"]), "missing or unknown grade dimension")
    statuses = []
    for grade in grades.values():
        require(isinstance(grade, dict) and grade.get("status") in ("pass", "fail", "unavailable"), "invalid grade")
        require(nonempty(grade.get("evidence")), "every grade needs trace evidence or an unavailable reason")
        statuses.append(grade["status"])
    behavior = "fail" if "fail" in statuses else "unavailable" if "unavailable" in statuses else "pass"
    outcome = "recorded-fail" if "fail" in (routing, behavior) else "incomplete" if behavior == "unavailable" else "recorded-pass"
    return {"status": outcome, "routing": routing, "behavior": behavior}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("check")
    create = sub.add_parser("template")
    create.add_argument("case")
    create.add_argument("--arm", required=True, choices=sorted(ARMS))
    validate = sub.add_parser("validate")
    validate.add_argument("record", type=Path)
    args = parser.parse_args()
    try:
        suite = ROOT / "evals/cases.json"
        skills = {p.parent.name for p in (ROOT / "skills").glob("*/SKILL.md")}
        cases = validate_suite(read_json(suite), skills)
        suite_hash = digest(suite.read_bytes())
        if args.command == "check":
            result = {"cases": len(cases), "skills": len(skills), "model_runs": "not assessed"}
        elif args.command == "template":
            require(args.case in cases, "unknown case")
            result = template(cases[args.case], args.arm, suite_hash)
        else:
            result = validate_record(read_json(args.record), cases, suite_hash, args.record.parent, skills)
        print(json.dumps(result, indent=2))
        if args.command == "validate":
            return {"recorded-pass": 0, "recorded-fail": 1}.get(result["status"], 3)
        return 0
    except (ValueError, OSError) as error:
        print(str(error), file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
