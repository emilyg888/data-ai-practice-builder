---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-27
completeness: full
---

# 27: Implementation Patterns

## Scenario

A company is building a data retrieval and workflow system. The company uses an FM in Amazon Bedrock through an API call to build the system. The company wants to use AWS Step Functions in a structured way to make the FM break down each problem into a series of logical reasoning steps. Which solution will implement this reasoning pattern in the MOST consistent way?

## Common implementation patterns

- Create a state machine with ReAct pattern states. Configure each state to invoke the FM with specific prompts for observation, reasoning, and action planning. Use the built-in Step Functions error handling and retry logic for model invocations.

## Common anti-patterns

- Avoid create a state machine that implements chain-of-thought reasoning with explicit prompt templates for each step. Use Choice states to dynamically adjust the reasoning path based on intermediate responses. because this solution implements sequential reasoning steps. However,...
- Avoid create a state machine that attempts to parallelize all reasoning steps simultaneously. Configure concurrent FM invocations to process different aspects of the problem and aggregate results in a final state. because attempting to parallelize all reasoning steps...
- Avoid create a state machine that uses the ReAct pattern by passing all previous reasoning steps as context in each FM invocation. Store the complete conversation history in the Step Functions execution state and include the entire history with each new prompt. because passing...

## Architecture guidance

- You can use Step Functions to define state machines that implement complex logic through a series of steps and branches.
- The ReAct pattern provides a structured way for an FM to systematically break down and reason through each step of a complex problem.
- Using built-in Step Functions error handling ensures reliability in model invocation.
