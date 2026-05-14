---
type: reference_note
platform: aws
status: draft
source: udemy-question-20
---

# 20: Throughput Patterns

## Scenario

A fintech company’s GenAI team is building an internal assistant that generates short compliance summaries by invoking an Amazon Bedrock text model. The assistant is called synchronously from an API, and users expect responses in near real time. During predictable weekday peaks, the team receives throttling errors from Bedrock and must increase available throughput while continuing to use the same model and keeping operational overhead low. Which deployment approach will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Purchase Amazon Bedrock provisioned throughput for the model and invoke the model by using the provisioned model ARN as the modelId during inference. This is the managed or lower-overhead approach called out as correct in the exam explanation.

## Common anti-patterns

- Avoid deploy a fine-tuned version of the model to an Amazon SageMaker AI real-time endpoint and update the application to invoke the SageMaker endpoint for all requests. because this introduces additional operational overhead to provision and manage an...

## Architecture guidance

- Provisioned throughput in Amazon Bedrock is the most direct way to increase and stabilize model throughput for predictable demand while keeping operations simple.
- It preserves the existing Bedrock integration pattern and avoids building and managing separate hosting infrastructure.
- Retry strategies help handle transient errors but cannot guarantee additional capacity, and batch inference is not suitable for synchronous interactive use cases.

## Domain

- Content Domain 2: Implementation and Integration
