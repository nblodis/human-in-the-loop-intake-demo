# Human-in-the-Loop Intake

An original, deterministic Python demonstration of structured idea intake, completeness checks, risk indicators and explicit human approval boundaries. **No LLM is used**; this illustrates rules that might later complement an LLM interface.

## Try it

```bash
python src/triage.py data/example.json
python -m unittest discover -s tests -v
```

The evaluator identifies missing essentials, flags unsupported savings estimates or unreviewed sensitive-data use, and returns `NOT_GRANTED` for approval regardless of completeness. Data is fictional.

## Engineering tradeoffs

This small demo intentionally does not integrate AI models, third-party tools, authentication, persistence or enterprise policy. It illustrates human-review guardrails rather than a production-ready intake platform.

**Provenance:** Independently written example, not an employer system or internal prompt.
