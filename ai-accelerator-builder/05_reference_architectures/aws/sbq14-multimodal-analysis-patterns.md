---
type: reference_note
platform: aws
status: draft
source: aws-skill-builder-question-14
completeness: partial
---

# 14: Multimodal Analysis Patterns

## Scenario

A company wants to create an application to analyze fashion trends. The application must analyze videos and photos from public fashion shows to understand style elements and trends. The solution must store the extracted information and provide a dashboard that summarizes the fashion trends. Which solution will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Use managed multimodal extraction and analytics services that can process video and image content, persist extracted features, and feed a dashboard without custom media-analysis code.

## Common anti-patterns

- Avoid use Amazon EventBridge to trigger AWS Lambda functions that use Amazon QuickSight Q to analyze videos and photos from fashion shows. Store analysis results in Amazon S3. Deploy a QuickSight dashboard with ML-powered trend analysis. because quickSight Q provides integrated AI assistance in...

## Architecture guidance

- QuickSight Q provides integrated AI assistance in QuickSight.
- You can use QuickSight Q to create topics and ask questions about a specific topic inside a QuickSight dashboard.
- QuickSight Q helps users ask questions about data that is already located within a QuickSight dashboard.

## Source Notes

- The source export is partial for this question, so the endorsed pattern is inferred from the preserved prompt, answer key, and visible explanation text.
