---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-68
completeness: full
---

# 68: Audit Logging Patterns

## Scenario

A company is developing an application by using Amazon Bedrock. Multiple development teams will access the application across different departments. The company uses AWS Organizations with OUs for each department. The company must enforce least privilege access to FMs and provide role-based access control (RBAC) for each department. The solution must integrate with the company's existing enterprise identity provider (IdP) for centralized governance. Only approved development teams should be allowed to invoke specific models. The solution must provide an auditable access trail. Which solution will meet these requirements MOST securely?

## Common implementation patterns

- Configure AWS IAM Identity Center with SAML federation from the enterprise IdP. Create permissions sets that restrict Amazon Bedrock model invocation for each OU. Create an SCP that prevents unauthorized actions outside of approved models.

## Common anti-patterns

- Avoid create identity-based IAM policies with model-specific conditions and Amazon Bedrock Guardrails ARNs. Set up Amazon EventBridge rules for anomaly detection and violation alerts. Use AWS CloudTrail to audit Amazon Bedrock API calls. because iAM identity-based policies can...
- Avoid deploy AWS PrivateLink connections for all development teams. Allow bedrock:InvokeModel permissions by attaching resource-based policies to Amazon Bedrock endpoints. because privateLink provides private, secure access to Amazon Bedrock without traversing the public...
- Avoid set up federated access through the enterprise IdP. Configure default model access by using Organizations service-linked role. Allow access to approved Amazon Bedrock FMs at the department OU level. because federated access through the enterprise IdP and service-linked...

## Architecture guidance

- IAM Identity Center provides centralized workforce access with support for SAML federation to enterprise IdPs.
- You can configure permissions sets that enforce least privilege IAM policies to scope access to specific Amazon Bedrock model actions for each department.
- You can apply SCPs at the OU level to provide an organizational guardrail that blocks non-approved actions.
