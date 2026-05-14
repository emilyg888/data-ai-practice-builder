---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-34
completeness: full
---

# 34: AgentCore Runtime Patterns

## Scenario

z34/75 Question A company is developing an AI agent by using Amazon Bedrock AgentCore Runtime. The agent needs to authenticate users from an existing Microsoft Entra ID environment. Users must access the agent securely by using corporate credentials. The company wants to implement OpenID Connect (OIDC) integration. The OIDC integration must validate tokens from the company's identity provider (IdP) and allow access only to users with valid corporate credentials. Which solution will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Configure AgentCore Identity with Microsoft as an inbound provider. Set the allowed audiences to the application ID from Microsoft Entra ID.

## Common anti-patterns

- Avoid create an Amazon Cognito user pool with Microsoft Entra ID as a SAML IdP. Configure AgentCore Runtime to use Amazon Cognito for authentication. because amazon Cognito can integrate with Microsoft Entra ID. However, this solution requires the configuration and maintenance...
- Avoid set up AWS IAM Identity Center with Microsoft Entra ID as an external IdP. Configure AgentCore Runtime to use IAM roles for authentication. because with IAM Identity Center, you must configure external IdP mappings and IAM roles. Therefore, this solution requires...
- Avoid deploy an Amazon API Gateway REST API with a custom AWS Lambda authorizer. Configure the authorizer to validate Microsoft Entra ID tokens and forward authenticated requests to AgentCore Runtime. because to implement a custom Lambda authorizer, you must develop, test, and...

## Architecture guidance

- AgentCore Identity supports Microsoft Entra ID as an inbound IdP for OIDC authentication.
- For setup, you must configure the discovery URL to the Microsoft v2.0 OIDC metadata endpoint.
- Then, you set the allowed audiences to match the application ID from the Microsoft Entra ID application registration.
