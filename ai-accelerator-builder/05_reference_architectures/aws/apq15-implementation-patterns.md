---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-15
completeness: full
---

# 15: Implementation Patterns

## Scenario

A GenAI developer deployed an AI assistant by using an FM in Amazon Bedrock. Users report that when asking similar questions, sometimes the responses are inconsistent. The GenAI developer needs to quantitatively assess the model's sensitivity to slight variations in input questions by using a prompt dataset provided by users. Which solution will quantitatively evaluate the model's responses across similar input variations?

## Common implementation patterns

- Create a model evaluation job in Amazon Bedrock using the user-provided prompt dataset. Configure evaluation metrics for response consistency analysis. Measure the statistical variance in model outputs across similar input variations.

## Common anti-patterns

- Avoid use an Anthropic Claude model in Amazon Bedrock with a temperature setting of 0. Create an AWS Lambda function that calculates Levenshtein distances between responses for similar prompts. because setting the temperature parameter to 0 can reduce randomness in the token...
- Avoid deploy an evaluation pipeline using Amazon Bedrock Knowledge Bases and Amazon Titan Embeddings. Calculate semantic similarity scores between responses for similar prompts. Analyze the distribution of embedding distances to quantify consistency. because embedding-based...
- Avoid set up an Amazon Bedrock agent with systematic testing workflows. Use the agent's orchestration capabilities to process similar prompts in parallel. Analyze semantic coherence through custom evaluation metrics. because agents are designed to orchestrate task execution and...

## Architecture guidance

- Model evaluation jobs in Amazon Bedrock support custom prompt datasets.
- Model evaluation jobs can produce computed scores and metrics that help you assess the effectiveness of a model and knowledge base.
- The robustness metric specifically assesses the sensitivity of generated responses based on small variations in the input questions.
