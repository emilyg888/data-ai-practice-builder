---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-41
completeness: full
---

# 41: Implementation Patterns

## Scenario

A financial services company creates a multi-account generative AI (GenAI) development environment by using Amazon Bedrock FMs. Employees must authenticate through the corporate Microsoft Active Directory. Employees should only be able to access FMs based on their department assignments. The company requires consistent permissions across AWS accounts. The company requires control over which models each department can use. The solution must ensure Regional resilience for the authentication service. Which solution will meet these requirements with the LEAST operational overhead?

## Common implementation patterns

- Configure AWS IAM Identity Center as the identity federation service and connect to Active Directory. Create permission sets with model access policies that map to departments. Configure multi-account access with Regional failover.

## Common anti-patterns

- Avoid create IAM users in each AWS account that match the corporate Active Directory usernames. Establish cross-account roles with department-specific permissions that include condition keys for Amazon Bedrock model access. because creating individual IAM users that mirror...
- Avoid configure federation between Active Directory and Amazon Cognito. Create identity pools for each department. Use AWS STS to assume roles with specific Amazon Bedrock model access permissions in each account. because amazon Cognito can federate with Active Directory....
- Avoid configure SAML 2.0 federation directly by using IAM in each AWS account. Create IAM roles with trust policies for each department that include the SAML provider. Use condition keys to restrict model access based on department attributes. because this solution correctly...

## Architecture guidance

- IAM Identity Center provides centralized identity federation with Active Directory.
- IAM Identity Center provides consistent permissions across multiple accounts through permission sets.
- This solution supports department-based access control to AWS resources including Amazon Bedrock models.
