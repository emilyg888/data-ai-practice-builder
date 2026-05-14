---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-45
completeness: full
---

# 45: Knowledge Base Patterns

## Scenario

A medical diagnostics company runs a chat-based AI application to help customers find appropriate tests from a catalog of diagnostic tests. Each test contains detailed descriptions, target conditions, specimen types, and specimen collection guidelines. The application uses Amazon Bedrock Knowledge Bases supported by Amazon OpenSearch Serverless to search the catalog of available diagnostic tests. Initially, the search provides sufficient recall. However, the search is unable to prioritize the most relevant documents. As a result, the company decides to continue using hybrid search. To achieve the desired accuracy, the company increases response results to 50 to pass to the LLM for summarization. The company experiences an increase in customer use of the application. The company notices an increase in token usage. Now, the company wants to reduce token usage for each customer interaction without impacting accuracy. Which solution will meet these requirements with the LEAST effort?

## Common implementation patterns

- Configure the knowledge base to invoke a reranker model. Pass only the top five ranked documents to the LLM for summarization.

## Common anti-patterns

- Avoid limit the context window by passing only the top five retrieved documents to the LLM for summarization. because limiting the context window to pass only five documents can reduce token usage. However, this solution does not solve the root problem of poor relevant ranking....
- Avoid reconfigure the chunking strategy to use semantic-based adaptive chunking with overlap. Reduce the retrieval set to the top ten documents to pass to the LLM for summarization. because adaptive semantic chunking with overlap is a strategy that you can use to improve...
- Avoid configure the knowledge base to use semantic search as the retrieval method. because semantic search retrieves results based on vector similarity rather than keywords alone. Semantic search can improve relevance. Semantic search provides good recall, but not precision. The...

## Architecture guidance

- Knowledge bases support reranker models that can reorder retrieval results to improve precision.
- You can enable reranking and limit the retrieval set to the top five ranked documents.
- This solution maintains accuracy while reducing the tokens that pass to the LLM.
