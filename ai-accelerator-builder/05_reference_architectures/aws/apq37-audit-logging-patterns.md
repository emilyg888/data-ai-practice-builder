---
type: reference_note
platform: aws
status: draft
source: aws-pretest-question-37
completeness: full
---

# 37: Audit Logging Patterns

## Scenario

A large company is using Amazon Bedrock. The company wants to limit access to FMs to specific AWS and Anthropic models within designated development accounts. The company strictly prohibits third-party marketplace models. The company requires comprehensive logging of all model interactions for auditing purposes. The company uses AWS Organizations and AWS IAM Identity Center for account and user management. A security team must implement the solution while maintaining operational efficiency. Which combination of steps will meet these requirements with MINIMAL operational overhead? (Select TWO.)

## Common implementation patterns

- Create an SCP that denies bedrock:InvokeModel\* actions for unapproved or marketplace models by using the bedrock:ModelID condition key. Apply the policy to the root of the organization. Enable Amazon Bedrock model invocation logging.
- Create a permission set in IAM Identity Center that allows bedrock:InvokeModel\* actions only for specific AWS and Anthropic model ARNs by using IAM policy conditions. Apply the permission set to designated development accounts.

## Common anti-patterns

- Avoid create an RCP that denies access to marketplace models and unapproved built-in models. Apply the policy to the designated development accounts in the organization. Use a condition block to allow only approved AWS and Anthropic model IDs for bedrock:InvokeModel\* actions....
- Avoid deploy AWS CloudFormation StackSets to provision standardized IAM roles across development accounts. Create IAM roles that allow access to only approved AWS and Anthropic models. Enable AWS CloudTrail logging for all Amazon Bedrock interactions. because stackSets can...
- Avoid create a custom AWS Config rule to detect when Amazon Bedrock model invocations include unapproved model IDs. Configure Amazon EventBridge to capture the noncompliant findings and invoke an AWS Lambda function. Configure the function to notify the security team and remove...

## Architecture guidance

- SCPs provide organization-wide preventive controls.
- SCPs can effectively deny access to marketplace models across all accounts.
- You can scope bedrock:InvokeModel\* actions to only approved AWS and Anthropic model IDs.
