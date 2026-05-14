---
type: reference_note
platform: aws
status: draft
source: udemy-question-54
---

# 54: Prompt Patterns

## Scenario

A product enablement team is building an internal web portal that helps employees draft customer emails by using an Amazon Bedrock foundation model (FM). The team wants to deliver an accessible web UI quickly, standardize backend integration for future clients by using an API-first approach, and allow non-developers to adjust the prompt workflow (including branching and reusable prompt components) without redeploying application code. Which solution will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Build the web UI with AWS Amplify and use Amplify libraries for authentication. Define the backend as an Amazon API Gateway REST API created from an OpenAPI specification. Invoke an Amazon Bedrock Flow from an AWS Lambda integration behind the API so prompt...

## Common anti-patterns

- Avoid deploy a containerized web application on Amazon ECS behind an Application Load Balancer. Use AWS Step Functions to orchestrate a multi-step prompt chain that invokes the FM and stores intermediate results in Amazon DynamoDB. because this introduces...

## Architecture guidance

- The lowest-overhead solution combines a rapid front-end delivery mechanism with a standardized API contract and a managed, no-code workflow layer for prompt chaining.
- AWS Amplify accelerates building and hosting the web interface and common client capabilities.
- An OpenAPI-defined Amazon API Gateway interface provides an API-first contract that other clients can adopt consistently.

## Domain

- Content Domain 2: Implementation and Integration
