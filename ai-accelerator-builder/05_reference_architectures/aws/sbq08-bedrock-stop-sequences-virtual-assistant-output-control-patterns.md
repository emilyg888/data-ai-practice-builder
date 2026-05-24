---
type: reference_note
platform: aws
status: draft
source: aws-skill-builder-question-8
completeness: full
title: 8: Bedrock Stop Sequences for Virtual Assistant Output Control
pattern_family: bedrock_output_control_stop_sequences
aws_services:
  - Amazon Bedrock
related_controls:
topics:
  - bedrock stop sequences
  - virtual assistant output control
  - bedrock
  - bedrock output control stop sequences
use_cases:
  - architecture reference
---

# 8: Bedrock Stop Sequences for Virtual Assistant Output Control

## Pattern summary

Set stop sequences in the Bedrock model inference request to end virtual assistant output when a configured phrase appears.

## Scenario

A GenAI developer is building a virtual assistant application by using an Anthropic Claude model on Amazon Bedrock. The application sends user queries and expects conversational responses. The GenAI developer wants to configure the application to stop generating output after a specific phrase is generated in the response. Which solution will meet these requirements?

## Common implementation patterns

- Use the stop sequences parameter in the inference call to specify a trigger phrase.

## Architecture guidance

- You can use the stop sequences parameter to stop the model from generating a response.
- You can use the stop sequences parameter to stop the model after generating certain key phrases.
- This solution provides a built-in mechanism in the model's API to directly control output generation.

## AWS documentation validation

- Validated: Bedrock inference parameters include temperature, top-p, top-k, response length, penalties, and stop sequences; Converse API exposes a base inferenceConfig for common parameters.
- Documentation source: Bedrock inference parameters: https://docs.aws.amazon.com/bedrock/latest/userguide/inference-parameters.html
- Documentation source: Converse API inference config: https://docs.aws.amazon.com/bedrock/latest/userguide/conversation-inference-call.html
- Documentation source: Bedrock evaluations: https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html

## AWS-supported alternative patterns

- For repeatable behavior, lower randomness parameters and pair parameter changes with Bedrock evaluation jobs; for hard output termination, use stop sequences rather than prompt-only instructions.
- For every production implementation, verify current Region/model support, IAM permissions, service quotas, logging retention, encryption, and data-residency requirements in the target AWS account.
