---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-39
completeness: full
---

# 39: Implementation Patterns

## Scenario

A retail company is implementing a generative AI (GenAI) powered customer service system by using Amazon Bedrock. The system must handle product inquiries and answer various customer questions through the company's website. The system will have significant traffic load level variations throughout the year. The system must access the company's extensive product catalog and customer data. The company wants to improve performance while maintaining response quality and accuracy. Which combination of configurations will meet these requirements? (Select TWO.)

## Common implementation patterns

- Create Amazon Bedrock knowledge bases with RAG that incorporate the product catalog and customer data. Remove outdated product data regularly.
- Enable prompt caching for frequently asked questions and common inquiry patterns.

## Common anti-patterns

- Avoid implement response streaming on the FM. because response streaming can improve perceived latency. However, response streaming does not meet the requirement to handle variable traffic loads or to maintain accuracy when accessing company data.
- Avoid use Amazon Bedrock batch inference to process customer inquiry files. because batch inference can process many requests asynchronously. However, batch inference is not suitable for real-time customer service interactions. This configuration would introduce unnecessary...
- Avoid deploy multiple FMs in parallel in Amazon Bedrock. Use A/B testing to dynamically route customer inquiries based on model performance. because amazon Bedrock supports access to multiple FMs. A/B testing is an approach that you can use to compare model performance. However,...

## Architecture guidance

- You can create knowledge bases with RAG so that the system can incorporate an up-to-date product catalog and customer data.
- This configuration improves response accuracy and relevance by providing context from the company's specific information.
- Regularly removing outdated product data ensures that the knowledge base remains current.
