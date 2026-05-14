---
type: reference_note
platform: aws
status: draft
source: udemy-question-31
---

# 31: Agent Orchestration Patterns

## Scenario

A platform engineering team is building an internal “Ops Copilot” that autonomously troubleshoots application incidents. The team uses AWS Agent Squad to route each user request to one of several specialized Strands agents (for example, an incident triage agent and a runbook agent). Users expect the assistant to remember conversation context within a session and also retain longer-term preferences (for example, preferred service names and escalation rules) across multiple sessions. The team wants a serverless approach that minimizes the amount of custom state-management code they must build and operate. Which solution meets these requirements with the LEAST operational overhead?

## Common implementation patterns

- Store per-session conversation history in Amazon DynamoDB and store long-term preferences as separate DynamoDB items. Pass the session identifier between the routed agents so each agent can fetch and update the state as needed. This is the managed or...

## Common anti-patterns

- Avoid deploy the Strands agents on Amazon ECS with AWS Fargate and store state locally in the container file system so agents can reuse memory between requests. Use AWS Agent Squad only for routing decisions. because container-local storage is not a durable...

## Architecture guidance

- The core challenge is maintaining both short-term conversational state (what was said earlier in the current interaction) and durable long-term memory (user preferences and extracted insights) while coordinating that...
- A managed agent runtime with built-in memory reduces custom engineering and operational burden because it provides purpose-built abstractions for sessions and long-term memory records, and it avoids building and...
- Alternatives such as using a general-purpose database, container-local storage, or a retrieval knowledge base can work in limited scenarios, but they either do not provide session semantics and durable multi-agent state...

## Domain

- Content Domain 2: Implementation and Integration
