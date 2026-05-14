---
type: reference_note
platform: aws
status: draft
source: udemy-question-34
---

# 34: Prompt Patterns

## Scenario

A customer support SaaS provider is building an internal assistant that uses Amazon Bedrock to draft replies to incoming support tickets. Tickets are ingested from email and chat and often include noisy text such as email signatures, legal disclaimers, and inconsistent formatting. The assistant’s outputs are inconsistent because key details such as product names and case identifiers are not always clearly presented in the prompt. The team wants to improve response quality and consistency by enhancing the input text before invoking the FM, without building a custom model. Which solution will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Add an AWS Lambda preprocessing step that calls Amazon Comprehend to extract key entities (such as product names and case identifiers) and normalize or redact noisy/sensitive content. Then use an Amazon Bedrock text model to reformat the cleaned ticket into a...

## Common anti-patterns

- Avoid approaches that add custom operational overhead without improving governance, quality, or resilience.

## Architecture guidance

- When an FM receives inconsistent, noisy prompts, output quality and consistency often degrade because important details are buried in irrelevant text.
- A low-overhead way to address this is to add a preprocessing layer: use AWS Lambda to orchestrate input cleaning, use Amazon Comprehend to extract key entities and help normalize/redact problematic content, and then use...
- The primary FM then receives a clearer, more consistent prompt, which improves response quality without the additional complexity and cost of model customization.

## Domain

- Content Domain 1: Foundation Model Integration, Data Managem
