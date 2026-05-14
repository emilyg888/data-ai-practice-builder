---
type: reference_note
platform: aws
status: draft
source: aws-skill-builder-question-11
completeness: full
---

# 11: Implementation Patterns

## Scenario

An education company built a content generation system on Amazon Bedrock. The system generates practice questions to quiz end users on a topic to test their knowledge. The system consumes a mix of curated data and scraped data in the topic domain. Reviewers must approve of the generated question-response sets before end users can access the sets. The company wants to improve the system by adding source lineage for the reviewers to verify the credibility of the content. Which combination of steps will meet these requirements with the LEAST operational overhead? (Select TWO.)

## Common implementation patterns

- Tag FM outputs with metadata from the data source.
- Register the curated and scraped input datasets with AWS Glue Data Catalog.

## Common anti-patterns

- Avoid enable Amazon Bedrock invocation logging and correlate the logs with the data source. because amazon Bedrock invocation logging can track model interactions. However, correlating logs with data sources would require additional operational overhead. You must manually correlate logs with data...
- Avoid use Amazon SageMaker Clarify to explain model predictions. because sageMaker Clarify is designed for model explainability and bias detection. Clarify is not designed to track source lineage. This step does not meet the requirement for source credibility verification. Learn more about Clarify.
- Avoid use AWS CloudTrail to log reviewer feedback actions. because cloudTrail logs AWS API calls. API calls can track actions that are taken by reviewers, such as approval or rejection. However, this step does not meet the requirement to verify the source lineage of the generated content. Using...

## Architecture guidance

- You can tag the outputs with metadata about the data sources.
- The generated questions are the outputs.
- The curated data and scraped data are the data sources.
