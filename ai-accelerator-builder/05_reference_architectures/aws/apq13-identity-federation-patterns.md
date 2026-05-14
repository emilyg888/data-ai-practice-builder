---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-13
completeness: full
---

# 13: Identity Federation Patterns

## Scenario

An airline company uses AWS Organizations to manage multiple AWS accounts. The company wants to use generative AI (GenAI) and Amazon Bedrock to enhance a computerized maintenance management system (CMMS). The company has an existing identity provider (IdP) based on Microsoft Entra ID. The company needs to ensure that only authorized employees can access Amazon Bedrock based on their job roles. The solution must provide centralized access control and integration with the existing IdP. Which combination of steps will meet these requirements? (Select TWO.)

## Common implementation patterns

- Configure AWS IAM Identity Center with Microsoft Entra ID as an external IdP. Use custom permission sets to control access to Amazon Bedrock.
- Set up SAML-based federation between Entra ID and IAM. Create IAM roles mapped to Entra ID groups with appropriate permissions to access Amazon Bedrock.

## Common anti-patterns

- Avoid create IAM roles for each job function. Implement cross-account access using AssumeRole API calls from the company's on-premises applications to access Amazon Bedrock. because iAM roles can define fine-grained permissions. You can use AssumeRole for cross-account...
- Avoid create Amazon Cognito user pools to authenticate users. Create Amazon Cognito identity pools to provide temporary AWS credentials with appropriate permissions to access Amazon Bedrock. because amazon Cognito provides managed user pools for authentication. Amazon Cognito...
- Avoid configure Amazon API Gateway as a proxy in front of Amazon Bedrock. Create custom authorization logic tied to Entra ID tokens. because to use API Gateway with custom authorization logic, you must build and maintain a proxy layer that validates Entra ID tokens and forwards...

## Architecture guidance

- You can use IAM Identity Center as a centralized way to manage access to multiple AWS accounts and applications.
- IAM Identity Center supports federation with external IdPs, including SCIM or Entra ID through SAML.
- This step provides centralized access control.
