---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-66
completeness: full
---

# 66: Knowledge Base Patterns

## Scenario

A company is implementing a RAG-based knowledge management system. The system will use Amazon Bedrock and Amazon OpenSearch Service. The system will ingest hundreds of new documents into the knowledge base on a daily basis. The system must maintain high accuracy and reliability for content across multiple departments. A GenAI developer wants to use Amazon Bedrock model evaluation to design a comprehensive evaluation process. The process must evaluate correctness, relevance, formality scale, and company-specific tone and style. The GenAI developer must run the evaluation on a weekly basis. The GenAI developer will create a RAG evaluation with LLM-as-a-judge and select the desired metrics. Which solution will meet these requirements MOST cost-effectively?

## Common implementation patterns

- Create a human-validated evaluation dataset. Create custom metrics for formality scale and company-specific tone and style.

## Common anti-patterns

- Avoid use an industry-standard benchmark dataset. Create custom metrics for formality scale and company-specific tone and style. because an industry-standard benchmark dataset lacks enterprise-specific context. The dataset might not accurately represent real production...
- Avoid use an industry-standard benchmark dataset. Create a human-based model evaluation for formality scale and company-specific tone and style. because an industry-standard benchmark dataset lacks enterprise-specific context. The dataset might not accurately represent real...
- Avoid create a human-validated evaluation dataset. Create a human-based model evaluation for formality scale and company-specific tone and style. because using a human-validated dataset is most suitable for this scenario. However, human-based model evaluation is less efficient...

## Architecture guidance

- A human-validated dataset ensures an accurate representation of enterprise-specific use cases, terminology, and content patterns.
- Using LLM-as-a-judge with custom metrics provides an automated, consistent, and scalable evaluation.
- You can design custom metrics to assess formality scale and company-specific tone and style with consistent criteria.
