---
type: reference_note
platform: aws
status: draft
source: udemy-question-28
title: 28: Outposts De-Identification Pattern for Bedrock Discharge Summaries
pattern_family: edge_deidentification_private_bedrock
aws_services:
  - AWS PrivateLink
  - Amazon Bedrock
  - AWS Outposts
related_controls:
  - access_control
  - pii_protection
  - private_networking
topics:
  - outposts de-identification pattern
  - bedrock discharge summaries
  - private networking
  - bedrock
  - access control
  - pii protection
  - edge de-identification private bedrock
use_cases:
  - document summarization
---

# 28: Outposts De-Identification Pattern for Bedrock Discharge Summaries

## Pattern summary

Keep patient records on AWS Outposts, de-identify text locally, and send only approved content to Bedrock through private connectivity.

## Scenario

A healthcare provider operates hospitals in multiple European countries. Patient records must remain inside each hospital’s on-premises data center to satisfy data residency requirements. The provider wants to use an Amazon Bedrock FM to generate short discharge summaries, but the solution must ensure that raw patient records do not traverse the public internet and that only approved, de-identified text is sent to the FM. Which solution meets these requirements with the LEAST operational overhead?

## Common implementation patterns

- Deploy the application’s ingestion and preprocessing components on AWS Outposts in each hospital. Store patient records locally on Outposts and de-identify the text on Outposts. Use an Amazon VPC interface endpoint (AWS PrivateLink) to invoke the Amazon...

## Architecture guidance

- The key design objective is a cross-environment architecture where sensitive data stays local to satisfy residency rules, while still allowing controlled FM access.
- Running ingestion and preprocessing on AWS Outposts keeps patient records in the hospital data center and enables local enforcement of de-identification before any model invocation.
- Private connectivity to Amazon Bedrock through a VPC interface endpoint (AWS PrivateLink) helps ensure secure routing without traversing the public internet.

## AWS documentation validation

- Validated: AWS documents interface VPC endpoints for private Amazon Bedrock connectivity, including private DNS and endpoint policies to control access through the endpoint.
- Validated: Private Bedrock access through interface VPC endpoints is documented; the local/edge de-identification portion remains an application architecture control that must be validated against the chosen edge platform and data-residency requirements.
- Documentation source: Bedrock interface VPC endpoints / PrivateLink: https://docs.aws.amazon.com/bedrock/latest/userguide/vpc-interface-endpoints.html
- Documentation source: Bedrock PrivateLink endpoints: https://docs.aws.amazon.com/bedrock/latest/userguide/vpc-interface-endpoints.html
- Documentation source: Guardrail sensitive information filters: https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-sensitive-filters.html

## AWS-supported alternative patterns

- For regulated environments, combine Bedrock interface endpoints with endpoint policies, IAM conditions, and organization SCPs; validate supported endpoint names for runtime, agent runtime, and control-plane calls.
- If data can leave the site after redaction, use PrivateLink plus strict IAM and logging; if raw data cannot leave, keep preprocessing/de-identification local and send only minimized prompts to Bedrock.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.

## Domain

- Content Domain 2: Implementation and Integration
