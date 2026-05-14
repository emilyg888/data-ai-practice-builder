---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-40
completeness: full
---

# 40: RAG Patterns

## Scenario

A company has a large collection of HTML documents. The documents contain articles with varying lengths and complex hierarchical structures. Headers identify each article. Each article contains multiple paragraphs that can range from a few sentences to several pages in length. A GenAI developer must build a RAG solution that preserves the relationships between articles and the articles' contained paragraphs. The solution must retrieve relevant content for user inquiries. The solution must minimize irrelevant or inaccurate responses. Which solution will meet these requirements?

## Common implementation patterns

- Create an AWS Lambda function that implements a custom hierarchical chunking strategy. Use the LangChain framework for the HTML documents. Deploy LangChain through a Lambda function layer. Create an Amazon Bedrock knowledge base with the documents. Use the Lambda function as the...

## Common anti-patterns

- Avoid create an Amazon Bedrock knowledge base with the HTML documents. Use the built-in hierarchical chunking strategy. Configure the chunking strategy with parent chunks and child chunks. Set the estimated sizes based on the average length observed in the documents. because...
- Avoid create an Amazon Bedrock knowledge base with the HTML documents. Use the built-in semantic chunking strategy. Configure the chunking strategy to divide the documents into chunks based on their semantic meaning and content rather than syntactic structure. because amazon...
- Avoid use Amazon Textract to extract the text from the HTML documents. Create chunk files based on the paragraph extractions from Amazon Textract. Upload the extractions to an Amazon S3 bucket. Create an Amazon Bedrock knowledge base with the chunked files. Use the no chunking...

## Architecture guidance

- Amazon Bedrock Knowledge Bases supports custom chunking through Lambda functions.
- This solution can process documents with highly variable lengths.
- A custom Lambda function with LangChain provides a specialized chunking strategy.
