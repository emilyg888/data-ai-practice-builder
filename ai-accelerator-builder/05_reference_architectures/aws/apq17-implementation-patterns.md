---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-17
completeness: full
---

# 17: Implementation Patterns

## Scenario

A global investment company wants to use Amazon Bedrock to build a generative AI (GenAI) powered conversational assistant. The assistant needs to perform multiple tasks, including research and calculations. The assistant must analyze market data, process the latest news in the financial market, perform calculations, and generate investment insights. Which solution will meet these requirements?

## Common implementation patterns

- Create a system with a supervisor agent that orchestrates specialized sub-agents for quantitative analysis, news processing, and smart summarization.

## Common anti-patterns

- Avoid fine-tune an FM by using the market data, news in the financial market, and past analysis output as examples. In the context of a conversational flow, provide a system prompt that specifies instructions on how to achieve tasks such as performing calculations. because you...
- Avoid perform model distillation on an FM. In the context of a conversational flow, provide a system prompt that specifies instructions on how to achieve tasks such as performing calculations. because you can use model distillation to create a smaller and faster model that...
- Avoid create a decentralized network of agents where each agent independently processes data and communicates directly with end users. In the context of a conversational flow, provide a system prompt that specifies instructions on how to achieve tasks such as performing...

## Architecture guidance

- AI agents can connect to different systems, APIs, and data sources.
- AI agents can automate tasks.
- For an application that requires multiple agents to complete different tasks, you need a supervisor agent to manage the complex workflows of task-specific agents.
