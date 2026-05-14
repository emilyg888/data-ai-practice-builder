---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-59
completeness: full
---

# 59: Knowledge Base Patterns

## Scenario

A GenAI developer must use Amazon Q Business to enhance an internal content management system (CMS) for a company. The company wants users to be able to search, query, and receive AI-assisted insights from the company's data. The company has technical documentation in the CMS and internal knowledge bases with proprietary guidelines. The company has enterprise directory services for authentication, strict role-based access controls (RBAC), and compliance and governance policies for data access. Which combination of steps will meet these requirements with MINIMAL operational overhead? (Select TWO.)

## Common implementation patterns

- Configure Amazon Q Business with data source connectors to integrate the CMS and internal knowledge bases. Use AWS IAM Identity Center authentication for RBAC.
- Configure Amazon Q Business data sources with automatic content synchronization and security group mapping for access control.

## Common anti-patterns

- Avoid configure Amazon Q Business with custom Amazon API Gateway endpoints for content access. Enable SAML-based SSO through AWS IAM Identity Center. Create AWS Lambda functions that validate access permissions before serving responses. because you can use API Gateway to create...
- Avoid configure Amazon Q Business with enterprise Active Directory integration. Create data source filters based on security groups. Create Amazon CloudWatch alarms to monitor unauthorized access attempts to knowledge bases. because active Directory integration provides...
- Avoid create custom AWS Lambda functions to process and index documentation before importing the documentation into Amazon Q Business knowledge bases. because lambda is a serverless compute service that runs custom code in response to events. Creating custom Lambda functions for...

## Architecture guidance

- Amazon Q Business data source connectors are managed integration points that provide secure connections to external content systems.
- IAM Identity Center is a centralized service to manage user access and permissions across AWS accounts.
- This step uses built-in connectors to integrate content securely.
