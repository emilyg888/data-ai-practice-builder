---
type: reference_note
platform: aws
status: draft
source: aws-skill-builder-question-12
completeness: partial
---

# 12: Implementation Patterns

## Scenario

A cross-functional team is developing a generative AI (GenAI) application by using AWS services. The team needs to optimize developer productivity and enforce consistent integration patterns. The team needs to automate performance tuning and accelerate AI testing across multiple business units. The team wants to use Amazon Q Developer. The team must accelerate development workflows and maintain application quality. Which combination of steps will meet these requirements? (Select TWO.)

## Common implementation patterns

- Use Amazon Q Developer features that automate integration, testing, and tuning workflows rather than adding manual approval bottlenecks.

## Common anti-patterns

- Avoid use Amazon Q Developer to analyze code for security best practices and suggest compliance improvements. Implement a mandatory review process where all code changes must be manually approved by security teams before integration. because amazon Q Developer can help identify security issues and...

## Architecture guidance

- Amazon Q Developer can help identify security issues and suggest improvements.
- However, implementing a mandatory manual approval process for all code changes would create a bottleneck.
- This approach does not meet the requirements to optimize developer productivity and accelerate development workflows.

## Source Notes

- The source export is partial for this question, so the endorsed pattern is inferred from the preserved prompt, answer key, and visible explanation text.
