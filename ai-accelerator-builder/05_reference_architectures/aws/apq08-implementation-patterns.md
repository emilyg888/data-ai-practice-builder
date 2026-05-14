---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-8
completeness: full
---

# 8: Implementation Patterns

## Scenario

A research company is using a customizable FM on Amazon Bedrock to develop an internal generative AI (GenAI) powered search interface. During testing, a GenAI developer discovers that the model's performance is suboptimal for a specific niche topic. The company has 3 TB of unlabeled proprietary research papers, technical documentation, and historical reports that cover the niche topic. The company wants the model to develop a deeper understanding of the niche topic's domain terminology, concepts, and relationships. The GenAI developer must improve the model's accuracy for the niche topic by using the proprietary data. Which solution will meet these requirements?

## Common implementation patterns

- Use the proprietary data to perform continued pre-training of the model in Amazon Bedrock.

## Common anti-patterns

- Avoid use the proprietary data to fine-tune the model in Amazon Bedrock. because fine-tuning is a technique that can improve model performance. However, fine-tuning requires training data in the form of labeled examples. The model learns to associate which types of outputs to...
- Avoid use the proprietary data as an input for knowledge distillation to transfer insights from the current model to a new model. because knowledge distillation is a technique that creates a smaller, more efficient model by transferring knowledge from a larger model. Knowledge...
- Avoid use an LLM to summarize the proprietary data. Incorporate the summary as a system prompt for the current model. because system prompts are instructions or context that can guide a model's behavior during inference. System prompts can provide context to the model. However,...

## Architecture guidance

- With continued pre-training, a model can learn from large amounts of unlabeled domain-specific data.
- This solution continues general language model training on new content.
- The model can develop a deeper understanding of the domain's terminology, concepts, and relationships from the 3 TB of proprietary data.
