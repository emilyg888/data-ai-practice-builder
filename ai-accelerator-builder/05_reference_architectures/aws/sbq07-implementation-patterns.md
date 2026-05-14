---
type: reference_note
platform: aws
status: draft
source: aws-skill-builder-question-7
completeness: partial
---

# 7: Implementation Patterns

## Scenario

A news media company wants to develop a content conformance tool that automatically reviews and adjusts articles to ensure compliance with a style guide. Journalists need a web-based article editor that provides real-time analysis of content upon request. When journalists click an "analyze" button, the system should immediately begin providing suggested revisions through the editor interface. Articles are tagged with content categories in the metadata. Examples of categories include news, sports, and editorial. The company wants to use an Amazon Bedrock FM to analyze content and provide immediate feedback through the web-based article editor interface. Which architecture will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Use a direct real-time request/response or streaming architecture for the editor workflow instead of queue-first processing so analysis begins immediately when users request it.

## Common anti-patterns

- Avoid implement an Amazon SQS queue for article ingestion. Create AWS Step Functions workflows to process content. Use AWS Lambda functions to determine the content category from metadata and invoke appropriate Amazon Bedrock models with style guide prompts. Store results in Amazon DynamoDB. Use an...

## Architecture guidance

- Amazon SQS and Lambda provide reliable processing capabilities.
- Amazon SQS is a queuing service where messages must be polled for processing.
- Therefore, this architecture does not meet the requirement for immediate feedback through the web-based article editor interface.

## Source Notes

- The source export is partial for this question, so the endorsed pattern is inferred from the preserved prompt, answer key, and visible explanation text.
