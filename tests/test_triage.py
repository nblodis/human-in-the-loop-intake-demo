import importlib.util
import unittest
from pathlib import Path
FILE = Path(__file__).resolve().parents[1] / "src" / "triage.py"
spec = importlib.util.spec_from_file_location("triage", FILE)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

class TriageTests(unittest.TestCase):
    def test_incomplete(self):
        result = module.evaluate({"problem": "Example"})
        self.assertEqual(result["status"], "NEEDS_DISCOVERY")
        self.assertEqual(len(result["follow_up_questions"]), 3)
        self.assertEqual(result["approval"], "NOT_GRANTED")

    def test_complete_requires_human_review(self):
        record = {key: "Example" for key in module.REQUIRED}
        result = module.evaluate(record)
        self.assertEqual(result["status"], "READY_FOR_HUMAN_REVIEW")
        self.assertEqual(result["approval"], "NOT_GRANTED")

    def test_risk_flags(self):
        result = module.evaluate({"estimated_savings": 12, "uses_sensitive_data": True})
        self.assertEqual(len(result["risk_flags"]), 2)
