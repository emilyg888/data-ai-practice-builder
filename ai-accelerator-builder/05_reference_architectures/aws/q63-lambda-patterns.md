---
type: reference_note
platform: aws
status: draft
source: udemy-question-63
---

# 63: Implementation Patterns

## Scenario

A financial services company runs a customer-support chatbot that calls an Amazon Bedrock text FM through the bedrock-runtime Converse API from an AWS Lambda function in us-east-1. During occasional regional service disruptions and quota spikes, the chatbot experiences timeouts and cannot respond to users. The company must keep the workload running even if the primary Region is impaired, and the company must keep inference within the United States for data residency requirements. Which solution will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Configure Amazon Bedrock Cross-Region Inference by creating a geographic inference profile limited to the United States, and update the application to invoke the inference profile so Bedrock can automatically route requests to an available Region within that...

## Common anti-patterns

- Avoid deploy the same FM behind two separate Amazon SageMaker AI real-time endpoints in us-east-1 and us-west-2, and use Amazon Route 53 failover routing to direct traffic to the healthy endpoint during outages. because this introduces significant operational...

## Architecture guidance

- Geographic Cross-Region Inference in Amazon Bedrock is designed to keep applications operating when a specific Region is disrupted or temporarily constrained by routing requests to another Region within an approved...
- Using an inference profile keeps the routing logic managed by Bedrock, which reduces the need to build and operate custom multi-Region failover infrastructure.
- Alternatives that rely only on capacity provisioning address throttling but not regional outages, and approaches that add orchestration or DNS failover typically increase operational burden and are not required for...

## Domain

- Content Domain 1: Foundation Model Integration, Data Managem
