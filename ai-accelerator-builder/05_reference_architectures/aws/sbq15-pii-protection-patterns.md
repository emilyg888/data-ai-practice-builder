---
type: reference_note
platform: aws
status: draft
source: aws-skill-builder-question-15
completeness: partial
---

# 15: PII Protection Patterns

## Scenario

A financial services company wants to develop a mobile app that will help users with account inquiries and general account information. The company has a large amount of email exchange data between customers and support staff to use as source material. The data is stored in an Amazon S3 bucket and contains personally identifiable information (PII) that should not appear in search results. Which solution will meet these requirements?

## Common implementation patterns

- Use a retrieval architecture with deterministic PII detection and redaction in the indexing or retrieval path rather than relying on prompts to suppress sensitive content.

## Common anti-patterns

- Avoid use Amazon Kendra to enable enterprise search of the email data that is stored in Amazon S3. Integrate Amazon Kendra with an Amazon Bedrock FM. Use a system prompt to identify and remove PII during query processing. because amazon Kendra provides enterprise search capabilities and can...

## Architecture guidance

- Amazon Kendra provides enterprise search capabilities and can integrate with Amazon Bedrock FMs.
- However, using system prompts to handle PII during query processing is not a reliable or secure approach for sensitive financial data.
- A system prompt cannot ensure the consistent identification and removal of PII.

## Source Notes

- The source export is partial for this question, so the endorsed pattern is inferred from the preserved prompt, answer key, and visible explanation text.
