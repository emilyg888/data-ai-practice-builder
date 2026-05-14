---
type: reference_note
platform: aws
status: draft
source: udemy-question-73
---

# 73: Bedrock Agent Evaluation And Trace Patterns

## Scenario

An internal IT-support assistant uses an Amazon Bedrock agent, knowledge-base retrieval, and Lambda-backed action groups. The team needs a repeatable way to detect tool loops and verify that the agent completes tasks efficiently.

## Common implementation patterns

- Use managed Bedrock agent evaluations against a representative prompt dataset to measure task completion and tool-use effectiveness.
- Enable trace capture for both test and production invocations so multi-step agent behavior can be inspected later.
- Analyze trace logs with CloudWatch Logs Insights to quantify repeated action-group calls, failed tool sequences, and unnecessary hops.
- Define agent-quality metrics around outcome completion, tool efficiency, and loop frequency rather than latency alone.
- Test instruction and tool-description changes with the same dataset before release so regressions are measurable.

## Common anti-patterns

- Building a fully custom judge-and-orchestrate evaluation pipeline before using managed Bedrock evaluation features.
- Using SageMaker Model Monitor as the primary control for Bedrock agent task-completion quality.
- Measuring only HTTP success and latency with synthetic canaries while ignoring whether the agent actually solved the task.
- Failing to persist traces, which makes repeated-tool-call problems hard to diagnose.
- Updating tool descriptions or instructions without re-running repeatable agent-evaluation scenarios.

## Architecture guidance

- Agent observability should combine score-based evaluation with trace-based inspection.
- Loop detection should be treated as a first-class operational metric for multi-tool agents.
- In regulated environments, traces should preserve the sequence of retrievals, action invocations, and reasoning steps needed for post-incident review.
