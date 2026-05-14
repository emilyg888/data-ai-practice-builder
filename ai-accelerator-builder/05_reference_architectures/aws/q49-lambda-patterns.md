---
type: reference_note
platform: aws
status: draft
source: udemy-question-49
---

# 49: Throughput Patterns

## Scenario

A media streaming provider uses an API Gateway endpoint backed by an AWS Lambda function to call an Amazon Bedrock FM that generates podcast episode summaries. The team wants to reduce cost by switching to a smaller FM and tuning inference parameters (for example, temperature and max token limits). Before rollout, the team must verify summary quality does not regress, quantify the latency-to-quality and cost-to-quality tradeoffs, and introduce the new configuration to production traffic gradually with an easy rollback path. Which combination of steps should the team take to meet these requirements with the LEAST operational overhead? (Select TWO.)

## Common implementation patterns

- Deploy two AWS Lambda versions behind a single alias: one version calling the existing FM configuration and one version calling the candidate configuration. Use AWS CodeDeploy canary deployments to shift a small percentage of production traffic to the...
- Create a prompt dataset in Amazon S3 that includes representative transcripts (or excerpts) and reference summaries. Run Amazon Bedrock Model Evaluations across multiple candidate FMs and parameter configurations by using an LLM-as-a-judge. Use Amazon...

## Common anti-patterns

- Avoid create an Amazon Bedrock custom model by fine-tuning the FM on past transcripts so the model learns the provider’s preferred style. Promote the fine-tuned model to production after a small set of spot checks by editors. because fine-tuning increases...

## Architecture guidance

- A systematic evaluation approach should first compare candidate foundation models and inference parameter settings on a consistent prompt dataset, using an evaluation method that produces repeatable quality scores.
- Then, the team should validate the chosen configuration under real production conditions with a controlled rollout mechanism that supports quick rollback.
- Amazon Bedrock Model Evaluations enables structured, repeatable multi-model and multi-configuration testing using a prompt dataset, and it can be paired with operational metrics (token counts and latency) to calculate...

## Domain

- Content Domain 5: Testing, Validation, and Troubleshooting
