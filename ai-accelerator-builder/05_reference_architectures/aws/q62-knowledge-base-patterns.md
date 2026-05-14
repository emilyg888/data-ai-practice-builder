---
type: reference_note
platform: aws
status: draft
source: udemy-question-62
---

# 62: Knowledge Base And RAG Patterns

## Scenario

A financial services firm wants to allow its internal developers to build proof-of-concept applications that call Amazon Bedrock directly from local Python scripts. The firm uses Okta for workforce identity and requires single sign-on with short-lived credentials (no long-term access keys). Security requirements state that developers must be able to perform inference against approved FMs but must not be able to manage models, agents, or knowledge bases. Which solution meets these requirements with the MOST secure, least-privilege access model?

## Common implementation patterns

- Configure IAM Identity Center with Okta as the identity provider. Create a permission set for the developer group with a custom IAM policy that allows only Amazon Bedrock Runtime actions (for example, InvokeModel and Converse) for approved models. Have...

## Common anti-patterns

- Avoid create one shared IAM role that has permissions to invoke Amazon Bedrock models. Distribute the role credentials to all developers and rotate the credentials quarterly. because sharing credentials prevents per-user accountability and violates the...

## Architecture guidance

- The most secure approach is to federate workforce identities from the enterprise identity provider into AWS and issue temporary credentials, then apply role-based access control with least-privilege IAM policies.
- Using IAM Identity Center with Okta satisfies the federation and short-lived credential requirements, while a custom permission set policy can restrict access to only Bedrock Runtime inference operations (such as...
- Approaches that rely on long-term access keys, shared credentials, or unsupported token types either violate the security requirements or cannot authorize requests to Amazon Bedrock.

## Domain

- Content Domain 2: Implementation and Integration
