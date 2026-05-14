---
type: reference_note
platform: aws
status: draft
source: udemy-question-39
---

# 39: Implementation Patterns

## Scenario

An insurance company is building an internal GenAI assistant that drafts claim denial letters by using an Amazon Bedrock FM. Company policy requires a licensed adjuster to review and approve (or edit) each draft before the letter is sent to a customer. The company also wants to capture the adjuster’s rating and final approved text for later analysis. Review times can vary from minutes to hours. Which solution will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Use Amazon API Gateway to accept the request and start an AWS Step Functions state machine. The state machine invokes the Amazon Bedrock FM to create a draft, stores the draft and status in Amazon DynamoDB, notifies adjusters (for example, through Amazon...

## Common anti-patterns

- Avoid send each prompt to an Amazon SQS queue. Have adjusters read messages directly from the queue, write approvals back to a second queue, and have a Lambda consumer send the final letter to the customer. because this approach places workflow coordination...

## Architecture guidance

- A human-in-the-loop design needs an explicit approval step, durable storage of the draft and the reviewer’s edits/ratings, and orchestration that can span variable human response times.
- A managed workflow service can coordinate the end-to-end process: generate the draft with the FM, route it to a reviewer for approval, and continue only after the review is complete.
- Exposing a dedicated feedback endpoint simplifies collecting structured reviewer decisions and ratings, and storing this information in a low-maintenance database enables traceability and later evaluation.

## Domain

- Content Domain 2: Implementation and Integration
