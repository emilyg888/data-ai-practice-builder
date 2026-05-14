---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-32
completeness: full
---

# 32: Implementation Patterns

## Scenario

A company develops an AI-powered product support chat assistant for a website. The architecture requires the chaining of the following three LLM calls: The first LLM call classifies the sentiment of the messages. The second LLM call summarizes documents from a product database. The third LLM call creates the final response. The company wants to maintain versions of the LLM prompts. The company wants to be able to roll back quickly if a new prompt underperforms. Which solution will meet these requirements with the LEAST development effort?

## Common implementation patterns

- Create an Amazon Bedrock knowledge base to retrieve documents from the product database. Use Amazon Bedrock Prompt Management to store the LLM prompts for each of the three LLM calls. Orchestrate the three LLM calls in a sequential workflow by using Amazon Bedrock Flows.

## Common anti-patterns

- Avoid create an Amazon Bedrock knowledge base to retrieve documents from the product database. Use Amazon Bedrock Prompt Management to store the LLM prompts for each of the three LLM calls. Orchestrate the three LLM calls in a sequential workflow by using AWS Step Functions....
- Avoid create an Amazon Bedrock knowledge base to retrieve documents from the product database. Use AWS Systems Manager Parameter Store to store the LLM prompts for each of the three LLM calls. Orchestrate the three LLM calls in a sequential workflow by using Amazon Bedrock...
- Avoid use Amazon Q Business to retrieve documents from the product database. Use Amazon Bedrock Prompt Management to store the LLM prompts for each of the three LLM calls. Orchestrate the three LLM calls in a sequential workflow by using Amazon Bedrock Flows. because amazon Q...

## Architecture guidance

- Knowledge Bases is a managed RAG service that you can use to securely connect an LLM to enterprise data.
- Prompt Management provides lifecycle control for prompts.
- Flows is a visual orchestration service that you can use to chain multiple LLM calls.
