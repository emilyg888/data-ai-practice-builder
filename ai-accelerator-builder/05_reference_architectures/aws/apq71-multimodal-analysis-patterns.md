---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-71
completeness: full
---

# 71: Multimodal Analysis Patterns

## Scenario

A company has a mobile app for users to record short videos. On the app, users can apply proprietary video and audio codecs to enhance the videos locally. The company wants to add features to summarize content and generate transcripts. The company wants features to detect objects and identify celebrities in the videos. Which solution will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Use an Amazon S3 presigned URL to upload videos to Amazon S3. Configure Amazon S3 to send events to Amazon EventBridge. Create an EventBridge rule that invokes an AWS Step Functions state machine. Set up the state machine to orchestrate the processing steps by directly calling...

## Common anti-patterns

- Avoid use Amazon S3 PutObject to upload videos to Amazon S3. Create an S3 event notification that invokes an AWS Step Functions state machine. Set up the state machine to orchestrate processing by using AWS Lambda functions. Use Amazon Rekognition for object detection and...
- Avoid use Amazon S3 PutObject to upload videos to Amazon S3. Create an S3 event notification that invokes an AWS Lambda function. Configure the function to process videos in parallel. Use AWS Step Functions for error handling and retries. Use Amazon Rekognition for object...
- Avoid use an Amazon S3 presigned URL to upload videos to Amazon S3. Create an S3 event notification that invokes a Bedrock Data Automation (BDA) blueprint to orchestrate the processing steps. Use Amazon Rekognition for object detection and celebrity recognition. Use Amazon...

## Architecture guidance

- This solution implements secure video uploads by using S3 presigned URLs.
- This solution follows the principle of least privilege.
- EventBridge is a serverless event bus service that efficiently routes S3 events to Step Functions for workflow orchestration.
