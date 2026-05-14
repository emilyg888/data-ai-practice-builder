---
type: reference_note
platform: aws
status: draft
source: udemy-question-74
---

# 74: PII Protection For Bedrock Chat Patterns

## Scenario

A customer-support assistant summarizes chat conversations and proposes next-step actions. Users may submit names, emails, phone numbers, and account identifiers. The design must stop sensitive data from reaching the model or reappearing in outputs while preserving utility.

## Common implementation patterns

- Add a pre-processing step that detects PII and replaces it with stable placeholders before model invocation.
- Use placeholder formats such as `<NAME_1>` and `<PHONE_1>` so the model can preserve entity relationships without seeing raw values.
- Apply Amazon Bedrock Guardrails with PII masking on both prompt input and model output.
- Layer prompt-side masking and output-side guardrails together rather than relying on one control alone.
- Preserve a secure mapping between placeholders and original values outside the model path when downstream workflow steps need re-identification.

## Common anti-patterns

- Discarding any message that contains sensitive entities, which destroys useful context.
- Treating encryption at rest as sufficient protection for prompt-time privacy.
- Using Amazon Macie as a real-time control for interactive prompt masking.
- Sending raw chat transcripts to the FM and trying to clean them only after inference.
- Using a custom entity recognizer when built-in PII detection already covers the requirement with lower overhead.

## Architecture guidance

- Privacy controls for GenAI assistants should be real-time and in-path, not only storage-oriented.
- Consistent placeholder substitution usually preserves response quality better than blocking entire requests.
- Input controls and output controls should both be audited so teams can prove that sensitive content was masked before and after generation.
