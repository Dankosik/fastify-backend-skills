"""Synthetic contract tests, not model evaluations."""

import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location("eval_skills", ROOT / "scripts/eval_skills.py")
evaluation = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(evaluation)
SKILLS = {
    "typescript-implement", "typescript-idiomatic", "typescript-design", "typescript-async",
    "typescript-debugging", "typescript-performance", "typescript-build", "typescript-data",
    "typescript-integrations", "typescript-unit-testing", "fastify-plugins", "fastify-routes",
    "fastify-security", "fastify-observability", "fastify-testing",
}


class SuiteTests(unittest.TestCase):
    def setUp(self):
        self.data = evaluation.read_json(ROOT / "evals/cases.json")

    def test_checked_in_cases_cover_the_expected_inventory(self):
        self.assertEqual(len(evaluation.validate_suite(self.data, SKILLS)), 22)

    def test_duplicate_case_is_rejected(self):
        self.data["cases"].append(copy.deepcopy(self.data["cases"][0]))
        with self.assertRaisesRegex(ValueError, "duplicate case"):
            evaluation.validate_suite(self.data, SKILLS)

    def test_unknown_skill_is_rejected(self):
        self.data["cases"][0]["routing"]["any_of"] = ["invented-skill"]
        with self.assertRaisesRegex(ValueError, "unknown routing"):
            evaluation.validate_suite(self.data, SKILLS)

    def test_negative_control_cannot_require_a_skill(self):
        self.data["cases"][0]["routing"]["none"] = True
        with self.assertRaisesRegex(ValueError, "inconsistent negative"):
            evaluation.validate_suite(self.data, SKILLS)

    def test_missing_grade_dimension_is_rejected(self):
        del self.data["cases"][0]["rubric"]["evidence"]
        with self.assertRaisesRegex(ValueError, "rubric dimensions"):
            evaluation.validate_suite(self.data, SKILLS)

    def test_duplicate_json_keys_are_rejected(self):
        with self.assertRaisesRegex(ValueError, "duplicate JSON key"):
            json.loads('{"status":"fail","status":"pass"}', object_pairs_hook=evaluation.unique_object)


class RecordTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        suite = ROOT / "evals/cases.json"
        self.hash = evaluation.digest(suite.read_bytes())
        self.cases = evaluation.validate_suite(evaluation.read_json(suite), SKILLS)
        self.record = evaluation.template(self.cases["P02"], "candidate", self.hash)

    def validate(self):
        return evaluation.validate_record(self.record, self.cases, self.hash, self.root, SKILLS)

    def complete_synthetic_record(self):
        raw = b'SYNTHETIC UNIT TEST TRACE, NOT A MODEL RUN\n'
        (self.root / "trace.txt").write_bytes(raw)
        self.record.update(status="completed", pack_commit="a" * 40,
                           trace={"path": "trace.txt", "sha256": evaluation.digest(raw)},
                           loaded_skills=["typescript-idiomatic"], reviewer="synthetic-test-grader")
        self.record["environment"] = {key: "synthetic-test-value" for key in self.record["environment"]}
        self.record["grades"] = {key: {"status": "pass", "evidence": "synthetic trace line 1"} for key in self.record["grades"]}

    def test_new_record_is_not_a_pass(self):
        self.assertEqual(self.validate()["status"], "not-run")

    def test_unavailable_is_not_a_pass(self):
        self.record.update(status="unavailable", reason="no model runner")
        self.assertEqual(self.validate()["status"], "unavailable")

    def test_unavailable_needs_a_reason(self):
        self.record["status"] = "unavailable"
        with self.assertRaisesRegex(ValueError, "needs a reason"):
            self.validate()

    def test_complete_synthetic_record_is_labeled_recorded(self):
        self.complete_synthetic_record()
        self.assertEqual(self.validate(), {"status": "recorded-pass", "routing": "pass", "behavior": "pass"})

    def test_missing_trace_is_rejected(self):
        self.complete_synthetic_record()
        (self.root / "trace.txt").unlink()
        with self.assertRaisesRegex(ValueError, "local regular file"):
            self.validate()

    def test_modified_trace_is_rejected(self):
        self.complete_synthetic_record()
        (self.root / "trace.txt").write_text("modified", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "hash mismatch"):
            self.validate()

    def test_trace_cannot_escape_record_directory(self):
        self.complete_synthetic_record()
        self.record["trace"]["path"] = "../trace.txt"
        with self.assertRaisesRegex(ValueError, "within the record"):
            self.validate()

    def test_trace_symlink_is_rejected(self):
        self.complete_synthetic_record()
        (self.root / "link.txt").symlink_to(self.root / "trace.txt")
        self.record["trace"]["path"] = "link.txt"
        with self.assertRaisesRegex(ValueError, "symlinks"):
            self.validate()

    def test_no_pack_does_not_fail_positive_routing(self):
        self.complete_synthetic_record()
        self.record.update(arm="none", pack_commit=None, loaded_skills=[])
        self.assertEqual(self.validate(), {"status": "recorded-pass", "routing": "not-applicable", "behavior": "pass"})

    def test_contaminated_no_pack_arm_is_rejected(self):
        self.complete_synthetic_record()
        self.record.update(arm="none", pack_commit=None)
        with self.assertRaisesRegex(ValueError, "no-pack arm loaded"):
            self.validate()

    def test_failing_behavior_cannot_be_hidden_by_routing(self):
        self.complete_synthetic_record()
        self.record["grades"]["contract"]["status"] = "fail"
        self.assertEqual(self.validate()["status"], "recorded-fail")

    def test_unknown_grade_is_not_success(self):
        self.complete_synthetic_record()
        self.record["grades"]["contract"]["status"] = "unavailable"
        self.assertEqual(self.validate()["status"], "incomplete")

    def test_missing_evidence_is_rejected(self):
        self.complete_synthetic_record()
        self.record["grades"]["contract"]["evidence"] = ""
        with self.assertRaisesRegex(ValueError, "trace evidence"):
            self.validate()

    def test_wrong_routing_is_distinct_from_behavior(self):
        self.complete_synthetic_record()
        self.record["loaded_skills"] = ["fastify-observability"]
        self.assertEqual(self.validate(), {"status": "recorded-fail", "routing": "fail", "behavior": "pass"})

    def test_negative_control_rejects_pack_activation(self):
        self.complete_synthetic_record()
        self.record["case"] = "N01"
        self.assertEqual(self.validate()["routing"], "fail")

    def test_pinned_suite_is_required(self):
        self.record["suite_sha256"] = "0" * 64
        with self.assertRaisesRegex(ValueError, "suite hash"):
            self.validate()

    def test_pack_commit_must_be_full(self):
        self.complete_synthetic_record()
        self.record["pack_commit"] = "main"
        with self.assertRaisesRegex(ValueError, "full pack commit"):
            self.validate()

    def test_isolation_must_be_recorded(self):
        self.complete_synthetic_record()
        self.record["environment"]["isolation"] = None
        with self.assertRaisesRegex(ValueError, "isolation"):
            self.validate()


class RepositoryContractTests(unittest.TestCase):
    def test_suite_matches_actual_skills(self):
        skills = {p.parent.name for p in (ROOT / "skills").glob("*/SKILL.md")}
        evaluation.validate_suite(evaluation.read_json(ROOT / "evals/cases.json"), skills)


if __name__ == "__main__":
    unittest.main()
