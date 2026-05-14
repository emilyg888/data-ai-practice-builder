---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-64
completeness: full
---

# 64: SageMaker Deployment Patterns

## Scenario

A financial services company wants to develop a generative AI (GenAI) application that provides personalized recommendations to users. A GenAI developer uses Amazon SageMaker AI to build the application. The application must process complex financial data and comply with regulations. The GenAI developer must implement a comprehensive fairness evaluation framework. The framework must detect subtle biases in model responses across different socioeconomic groups, age brackets, and geographic regions. Which solution will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Use SageMaker Clarify for automatic bias detection. Use FM evaluations (FMEval) with CrowS-Pairs datasets. Configure Amazon CloudWatch metrics for demographic disparity monitoring.

## Common anti-patterns

- Avoid deploy real-time performance monitoring by using Amazon CloudWatch. Implement role-based access controls (RBAC). Use Amazon Comprehend for sentiment analysis of model outputs. because cloudWatch monitoring and RBAC are important for application security. However, this...
- Avoid create custom evaluation datasets across demographic groups. Implement batch transform jobs for testing. Configure automatic model re-training when bias is detected. because you can create custom evaluation datasets and implement batch transform jobs to help test model...
- Avoid use SageMaker Model Monitor to continuously evaluate model predictions for bias drift. Set up automated alerts when bias metrics exceed thresholds. because model Monitor can detect data drift. However, Model Monitor is not designed for comprehensive fairness evaluation...

## Architecture guidance

- Clarify provides comprehensive bias detection capabilities across different demographic groups.
- Clarify can automatically identify potential unfairness in model responses.
- You can use FMEval with CrowS-Pairs datasets to test for stereotypical biases.
