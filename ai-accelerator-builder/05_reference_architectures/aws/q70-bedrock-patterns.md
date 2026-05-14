---
type: reference_note
platform: aws
status: draft
source: udemy-question-70
---

# 70: Implementation Patterns

## Scenario

A healthcare platform team is enabling multiple product groups to build GenAI applications on AWS by using Amazon Bedrock. The applications will be deployed in different AWS accounts and environments (dev, test, and production). The platform team must provide a consistent, repeatable way for teams to implement GenAI architectures that align with organizational best practices across security, reliability, and cost. Which approach will achieve this with the LEAST operational overhead?

## Common implementation patterns

- Use the AWS Well-Architected Tool with the AWS Well-Architected Generative AI Lens to define and review a standard GenAI architecture. Provide approved reusable infrastructure-as-code components (for example, AWS CDK or AWS CloudFormation templates) that...

## Common anti-patterns

- Avoid use AWS Organizations service control policies (SCPs) to restrict which AWS Regions and services can be used, and require all teams to use the same foundation model for every GenAI workload. because sCPs can help with governance controls, but they do...

## Architecture guidance

- The most effective low-overhead way to standardize GenAI implementations across many teams and deployment scenarios is to combine a repeatable architecture review process with reusable building blocks.
- The AWS Well-Architected Tool and the Generative AI Lens provide a consistent best-practices framework aligned to the Well-Architected pillars, and publishing approved infrastructure-as-code templates or constructs...
- Other approaches either rely on post-hoc auditing, add significant custom tooling overhead, or focus on restrictive governance controls without standardizing how solutions are designed and implemented.

## Domain

- Content Domain 1: Foundation Model Integration, Data Managem
