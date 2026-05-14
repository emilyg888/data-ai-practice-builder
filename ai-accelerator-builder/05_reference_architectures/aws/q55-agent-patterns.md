---
type: reference_note
platform: aws
status: draft
source: udemy-question-55
---

# 55: Agent Orchestration Patterns

## Scenario

A fintech customer support engineering team is building an internal GenAI assistant to help agents answer questions about the latest policies and procedures. The documents are stored in Amazon S3 and an internal Atlassian Confluence wiki, and the content changes frequently. The team wants the assistant’s answers to be grounded in the approved documents to reduce hallucinations and to avoid having to retrain a model whenever content is updated. Which architecture will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Create an Amazon Bedrock Knowledge Base that connects to Amazon S3 and Confluence as data sources. Configure an embedding model (such as Amazon Titan embeddings) and a managed vector store. Use the bedrock-agent-runtime RetrieveAndGenerate capability to...

## Common anti-patterns

- Avoid store the policy documents and their embedding vectors as items in Amazon DynamoDB. For each user query, use AWS Lambda to scan the table, calculate cosine similarity in code, select the top matches, and send those matches to an Amazon Bedrock model....

## Architecture guidance

- A managed RAG architecture is the best match when information changes frequently and the goal is to keep responses grounded in approved sources without retraining.
- Amazon Bedrock Knowledge Bases provide built-in ingestion from supported repositories, embedding generation, chunking, and semantic retrieval, and they integrate directly with a generation step (RetrieveAndGenerate).
- Adding Bedrock Guardrails with contextual grounding checks further enforces that responses stay aligned with retrieved context, reducing hallucinations while keeping the architecture simple to operate.

## Domain

- Content Domain 1: Foundation Model Integration, Data Managem
