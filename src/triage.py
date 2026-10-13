"""Deterministic business-opportunity triage with human-only approval."""
import json
import sys
from pathlib import Path

REQUIRED = {
    "problem": "What problem occurs today?",
    "affected_users": "Who experiences the problem?",
    "current_process": "How is the work done now?",
    "desired_outcome": "What measurable outcome would improve?",
}

def evaluate(opportunity):
    if not isinstance(opportunity, dict):
        raise TypeError("expected a JSON object")
    questions = [q for key, q in REQUIRED.items() if not str(opportunity.get(key, "")).strip()]
    risks = []
    if opportunity.get("estimated_savings") and not opportunity.get("baseline_evidence"):
        risks.append("Estimated savings lack a documented baseline")
    if opportunity.get("uses_sensitive_data") is True and not opportunity.get("privacy_reviewed"):
        risks.append("Sensitive data requires privacy review before any implementation")
    return {
        "status": "NEEDS_DISCOVERY" if questions else "READY_FOR_HUMAN_REVIEW",
        "follow_up_questions": questions,
        "risk_flags": risks,
        "approval": "NOT_GRANTED",
    }

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Usage: triage.py opportunity.json")
    record = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    print(json.dumps(evaluate(record), indent=2))
