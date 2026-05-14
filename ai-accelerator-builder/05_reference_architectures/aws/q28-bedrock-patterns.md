---
type: reference_note
platform: aws
status: draft
source: udemy-question-28
---

# 28: Implementation Patterns

## Scenario

A healthcare provider operates hospitals in multiple European countries. Patient records must remain inside each hospital’s on-premises data center to satisfy data residency requirements. The provider wants to use an Amazon Bedrock FM to generate short discharge summaries, but the solution must ensure that raw patient records do not traverse the public internet and that only approved, de-identified text is sent to the FM. Which solution meets these requirements with the LEAST operational overhead?

## Common implementation patterns

- Deploy the application’s ingestion and preprocessing components on AWS Outposts in each hospital. Store patient records locally on Outposts and de-identify the text on Outposts. Use an Amazon VPC interface endpoint (AWS PrivateLink) to invoke the Amazon...

## Common anti-patterns

- Avoid expose an Amazon API Gateway Regional endpoint that invokes Amazon Bedrock directly. Configure TLS for encryption in transit and rely on IAM authentication so hospitals can send patient records securely to the FM. because encryption in transit and IAM...

## Architecture guidance

- The key design objective is a cross-environment architecture where sensitive data stays local to satisfy residency rules, while still allowing controlled FM access.
- Running ingestion and preprocessing on AWS Outposts keeps patient records in the hospital data center and enables local enforcement of de-identification before any model invocation.
- Private connectivity to Amazon Bedrock through a VPC interface endpoint (AWS PrivateLink) helps ensure secure routing without traversing the public internet.

## Domain

- Content Domain 2: Implementation and Integration
