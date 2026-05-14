---
type: reference_note
platform: aws
status: draft
source: aws-skill-builder-question-9
completeness: partial
---

# 9: Identity Federation Patterns

## Scenario

A company needs secure authentication for a third-party application that uses Amazon Bedrock. The solution must integrate with the company's existing identity provider (IdP). The solution must maintain comprehensive audit logs of authentication and API calls. The solution must eliminate long-lived credentials and provide temporary access to Amazon Bedrock. Which solutions will meet these requirements? (Select TWO.)

## Common implementation patterns

- Implement an OpenID Connect (OIDC) integration with Amazon Cognito. Configure the integration to authenticate users through the IdP and exchange tokens for temporary AWS credentials. Configure the integration to allow the application to access Amazon Bedrock. This is the...

## Common anti-patterns

- Avoid adding custom infrastructure or manual process steps when a managed AWS capability satisfies the requirement with lower operational overhead.

## Architecture guidance

- Amazon Cognito with OIDC integration provides a secure way to authenticate users through the company's existing IdP.
- This solution can exchange identity tokens for temporary AWS credentials.
- Therefore, this solution eliminates long-lived credentials.
