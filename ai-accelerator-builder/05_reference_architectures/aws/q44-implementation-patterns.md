---
type: reference_note
platform: aws
status: draft
source: udemy-question-44
---

# 44: Implementation Patterns

## Scenario

A regulated digital bank is launching a GenAI feature that uses an FM to generate customer-facing explanations for lending decisions. During audits, the bank must demonstrate which model version produced each explanation, which approved data sources were used to generate the response, and provide an immutable record of the decision workflow for later review. The team wants to meet these compliance requirements with the LEAST operational overhead. Which solution should the team implement?

## Common implementation patterns

- Create programmatic model cards in Amazon SageMaker AI for each approved model version and deployment. Use AWS Glue Data Catalog and metadata tagging to register and attribute approved data sources and transformations for lineage. Configure the application to...

## Common anti-patterns

- Avoid publish all model requests and responses to an Amazon OpenSearch Service domain and create OpenSearch Dashboards for auditors. Document model behavior in a shared wiki and require developers to manually update the wiki after each model change. because...

## Architecture guidance

- A practical compliance framework for FM deployments usually needs three complementary capabilities: standardized model documentation, traceability of data sources and transformations, and durable decision logs for audit...
- Programmatic model cards provide an auditable record of model purpose and versioned deployment context.
- A data catalog with metadata tagging and lineage allows the organization to prove which governed data sources were used (and how they were processed) in support of outputs.

## Domain

- Content Domain 3: AI Safety, Security, and Governance
