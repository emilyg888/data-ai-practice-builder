---
type: pattern
status: draft
risk_level: medium
business_domains:
  - education
  - architecture enablement
  - developer productivity
  - AI experimentation
capability_layers:
  - document ingestion
  - chunking and indexing
  - retrieval
  - prompt context assembly
  - response grounding
ai_impact:
  - grounded answers reduce generic model output
  - selective context injection keeps prompts task-specific
  - reusable knowledge assets improve consistency across workflows
related_controls:
  - chunking policy
  - knowledge base validation
  - top-k retrieval limits
  - explicit event-context injection
  - fallback when retrieval is unavailable
---

# RAG and Context Management over Bedrock Knowledge Base

## 1. Problem solved

This pattern solves the problem of making AI responses in the lab specific to the project’s AWS learning materials instead of relying only on model prior knowledge.

In this repo, the pattern does two things together:

1. it turns PDF course and study materials into retrievable knowledge assets
2. it builds prompts that combine user intent, retrieved knowledge, and optional event context in a controlled way

The result is a grounded copilot flow where the tutor agent can explain AWS architecture using repo-specific context rather than generic answers alone.

## 2. When to use

Use this pattern when:

- you have a bounded corpus of architecture or training documents
- model responses should be grounded in that corpus
- the same knowledge set must support multiple interaction channels
- some requests need additional runtime context, such as event payloads
- you want retrieval support without building a fully custom vector pipeline from scratch

## 3. Business outcomes

- More relevant architecture explanations because answers are grounded in ingested materials
- Better consistency across sessions because the same knowledge base is reused
- Lower prompt-engineering burden because retrieval supplies dynamic context
- Safer event-driven reasoning because live event payloads can be merged with curated background material
- Faster experimentation because the ingestion and retrieval path is already wired into the Bedrock lab

## 4. Logical architecture

The logical flow in this repo is:

1. PDF documents are read from `course-materials/`.
2. Text is normalized and chunked during ingestion.
3. Chunk payloads are uploaded into the document bucket in S3.
4. A Bedrock Knowledge Base is provisioned over the S3-backed document set and an S3 Vectors store.
5. At runtime, the tutor workflow sends the user question to Bedrock retrieval with `top_k=4`.
6. Retrieved passages are concatenated into the prompt as retrieval context.
7. Optional event payloads are serialized separately and injected as event context.
8. The final prompt contains question, event context, and retrieval context before Bedrock generation is called.

At implementation level:

- `knowledge_base/ingestion.py` handles PDF extraction and upload
- `knowledge_base/chunking.py` handles local chunking and whitespace normalization
- `knowledge_base/provisioner.py` manages Knowledge Base and data source lifecycle
- `tools/bedrock_client.py` performs retrieval and generation
- `agents/architecture_tutor.py` assembles the final grounded prompt

## 5. Reference architecture options

### Option A: Prompt-only generation

Send the user question directly to the model with no retrieval. This is simplest, but it gives the least project-specific grounding.

### Option B: RAG over managed Bedrock Knowledge Base

This is the pattern leveraged in this project. Documents are ingested into S3, indexed through Bedrock Knowledge Bases, and retrieved at runtime before generation.

### Option C: RAG plus live business context

This extends managed retrieval with runtime event payloads or request metadata. The project already uses this shape in the tutor flow when trigger-driven event context is present.

## 6. Required capabilities

- PDF extraction from source documents
- Repeatable chunking and upload into document storage
- A vector-backed Bedrock Knowledge Base
- Runtime retrieval API access
- Prompt composition that keeps question, retrieved text, and live context distinct
- Model invocation path that can proceed even when retrieval returns nothing
- Environment configuration for model IDs, region, bucket names, and knowledge base IDs

## 7. Control gates

- Retrieval only runs when `KNOWLEDGE_BASE_ID` is present and passes basic validation
- Runtime retrieval is bounded by `top_k=4`, which limits prompt growth
- Event context is injected explicitly from `payload["context"]`, not inferred implicitly
- The tutor prompt tells the model to say when context is insufficient instead of overclaiming
- Retrieval fallback is explicit: if no usable knowledge base exists, the flow continues with `No retrieval context available.`
- Knowledge Base provisioning supports dry-run mode so infrastructure can be validated before real KB API calls are enabled

## 8. Delivery steps

1. Provision the document bucket, vectors bucket, and Knowledge Base wiring through CDK.
2. Configure environment values for region, model IDs, bucket names, and Knowledge Base settings.
3. Ingest PDF source material from `course-materials/` into S3 with chunked JSON payloads.
4. Enable or validate Bedrock Knowledge Base provisioning and data source creation.
5. Use the shared `BedrockClient` to retrieve context for a user question at runtime.
6. Assemble the final prompt with separate sections for question, event context, and retrieval context.
7. Generate the answer and return both the response and metadata such as `context_count`.

## 9. Common risks and failure modes

- Retrieval quality depends on source document quality and chunking strategy.
- This repo currently has two chunking layers: local character-based chunking during ingestion and Bedrock fixed-size chunking during data source ingestion, which can create context fragmentation or duplication.
- If `KNOWLEDGE_BASE_ID` is unset or invalid, the runtime silently falls back to no retrieval context.
- Concatenating retrieved passages into one prompt section is simple, but it does not rank or summarize context before generation.
- Event context can dominate the answer if payloads are large or noisy.
- The RAG path is mainly exercised in the tutor workflow; other agents do not currently leverage the same retrieval layer.

## 10. Artefacts produced

- Chunked JSON document payloads in S3
- Bedrock Knowledge Base and data source configuration
- Vector-backed retrieval context for tutor requests
- Grounded prompts containing question, event context, and retrieved text
- Tutor responses with context metadata and optional diagrams

## 11. Example executive narrative

This project uses a lightweight RAG and context-management pattern built on Amazon Bedrock Knowledge Bases. Source PDFs are ingested into S3, indexed into a vector-backed knowledge base, and retrieved at runtime to ground tutor responses in project-specific AWS architecture material. When live event data is available, it is added as a separate context layer so the model can reason over both curated knowledge and current signals without treating them as the same source of truth.
