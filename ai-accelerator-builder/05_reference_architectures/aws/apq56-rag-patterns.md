---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-56
completeness: full
---

# 56: RAG Patterns

## Scenario

A company developed a tool to assist customer support representatives. The tool summarizes relevant support documents for the case that a customer support representative works on. The tool uses a custom RAG system. The system is backed by a third-party vector store that stores document embeddings. The RAG system retrieves the top-k relevant chunks based on the current support case. The generative model that summarizes the documents runs on Amazon Bedrock. Recently, customer support representatives report that the summaries are contextually irrelevant and do not directly relate to the support cases. A GenAI developer verifies that the chunks retrieved from the vector store have high embedding similarity scores. The GenAI developer validates that the embedding model produces accurate representations and that the chunking strategy is consistent. The GenAI developer wants to improve the summarization to return more contextually relevant summaries. The GenAI developer wants to continue using Amazon Bedrock hosted models. The GenAI developer does not want to re-train any LLMs. Which strategies will improve the relevance of retrieved context? (Select TWO.)

## Common implementation patterns

- Migrate to using Amazon Bedrock Knowledge Bases for retrieval. Configure reranking when retrieving chunks.
- Add a reranking step after initial retrieval by invoking a rerank model in Amazon Bedrock. Configure the rerank model to rescore and sort retrieved chunks before generation.

## Common anti-patterns

- Avoid fine-tune the underlying model on company-specific documents to increase the contextual relevance of the summaries. because fine-tuning the underlying model can improve the quality of the summaries themselves or the domain alignment. However, this strategy does not improve...
- Avoid increase the number of retrieved documents to ensure that more contextually relevant documents are included in the generation process. because increasing the number of retrieved documents can make relevance worse. This strategy adds more low-value results instead of...
- Avoid re-chunk the source documents into larger segments to capture more context for the summarization model to use. because larger chunks could decrease relevance by including more unrelated text in each chunk. This strategy can impair embedding similarity scoring. This...

## Architecture guidance

- Reranking is a feature of Amazon Bedrock that reorders chunks based on relevancy to the query.
- Knowledge Bases provides built-in reranking mechanisms that improve contextual relevance.
- You can migrate to an Amazon Bedrock knowledge base to offload relevance scoring.
