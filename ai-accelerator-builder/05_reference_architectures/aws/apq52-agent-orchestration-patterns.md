---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-52
completeness: full
---

# 52: Agent Orchestration Patterns

## Scenario

A company is using an Amazon Bedrock agent that assists customers. The company must implement comprehensive observability capabilities. The company wants to understand and track the agent's reasoning process in making decisions. The solution must provide detailed visibility into the agent's reasoning process. The solution must provide quick identification of potential hallucinations. Which solution will meet these requirements?

## Common implementation patterns

- Enable PreProcessingTrace, OrchestrationTrace, and PostProcessingTrace components with golden dataset validation and systematic trace analysis.

## Common anti-patterns

- Avoid implement OrchestrationTrace with CustomOrchestrationTrace analysis. Use Amazon CloudWatch metrics for token usage patterns and FM performance monitoring. Validate agent behavior against a golden dataset to detect anomalies. because orchestrationTrace provides insights...
- Avoid configure GuardrailTrace with RoutingClassifierTrace. Use ModelInvocationInput analysis to validate the agent's decision boundaries and response patterns. Compare outputs against a golden dataset. because guardrailTrace and RoutingClassifierTrace can help with I/O...
- Avoid combine FailureTrace monitoring with PostProcessingTrace analysis. Implement custom parser modes with override AWS Lambda functions for response validation. Use a golden dataset for periodic checks of output consistently. because failureTrace and PostProcessingTrace with...

## Architecture guidance

- This solution provides end-to-end visibility into the agent's reasoning process.
- Each step in the console or trace in the API includes these three essential components.
- Together these components provide complete coverage of the agent's processing pipeline.
