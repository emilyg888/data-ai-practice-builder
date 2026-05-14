---
type: pattern
status: draft
risk_level: medium
business_domains:
  - education
  - architecture enablement
  - developer tooling
  - AI operations
capability_layers:
  - agent orchestration
  - task specialization
  - retrieval grounding
  - structured response handling
  - multi-channel invocation
ai_impact:
  - task-specific prompts improve output quality
  - shared retrieval context reduces generic answers
  - simple orchestration lowers implementation risk
related_controls:
  - explicit agent routing
  - bounded agent responsibilities
  - structured output contracts
  - shared runtime wrapper
  - event-to-agent gating
---

# Multi-Agent Task Router over Shared Bedrock Services

## 1. Problem solved

This pattern solves the problem of supporting different AI workflows without collapsing them into one oversized prompt and one overloaded handler.

In this repo, the multi-agent method separates three distinct jobs:

1. tutoring and explanation of AWS GenAI architecture
2. generation and evaluation of exam-style quizzes
3. review and scoring of architecture designs

Instead of a general-purpose agent deciding how to think, a lightweight orchestrator routes the request to a task-specific agent with a narrow prompt and a structured output contract.

## 2. When to use

Use this pattern when:

- one AI application needs several clearly different workflows
- each workflow benefits from a different prompt shape or response schema
- you want the simplicity of shared runtime infrastructure without merging all behavior into one agent
- some workflows need retrieval context while others do not
- the system must be callable from CLI, API, or event-driven entry points

## 3. Business outcomes

- Better answer quality because each agent is specialized for one job
- Easier maintenance because prompts and parsing logic stay local to each workflow
- Faster extension because new workflows can be added as new agents without rewriting the router
- Lower operational complexity than a fully autonomous multi-agent collaboration model
- Cleaner reuse across channels because the same agent logic works behind CLI and Lambda handlers

## 4. Logical architecture

The workflow in this repo is:

1. A caller enters through CLI, API Gateway, or the trigger pipeline.
2. The orchestrator or handler selects the correct agent based on the requested workflow.
3. The chosen agent builds a task-specific prompt.
4. The shared `BedrockClient` handles model invocation and, where needed, Knowledge Base retrieval.
5. The agent returns a structured `AgentResponse` with both output and metadata.
6. A shared wrapper normalizes API success and error responses.

The current agent set is:

- `ArchitectureTutorAgent`: grounded explanation with optional Mermaid diagram generation
- `QuizGeneratorAgent`: exam-style question generation and optional answer evaluation
- `ArchitectureReviewerAgent`: architecture scoring, risks, and recommendations

At implementation level:

- `agents/orchestrator.py` is the routing layer
- `agents/base.py` defines the shared response contract
- `agents/architecture_tutor.py`, `agents/quiz_generator.py`, and `agents/architecture_reviewer.py` hold task logic
- `tools/bedrock_client.py` centralizes Bedrock invocation and retrieval
- `tools/lambda_handlers/common.py` normalizes Lambda request parsing and error handling
- `runtime/cli.py` exposes the workflow locally
- the trigger path can invoke the tutor workflow with event context when rules allow it

## 5. Reference architecture options

### Option A: One generic agent

Use one prompt and one handler for every task. This is simple to start, but it quickly becomes harder to maintain, test, and control.

### Option B: Task-router multi-agent workflow

This is the pattern leveraged in this project. A central router dispatches to task-specialized agents that share the same Bedrock client and common runtime utilities.

### Option C: Collaborative agent swarm

Multiple agents reason together, hand off work, and coordinate dynamically. That is more flexible, but it adds complexity the repo does not need for its current scope.

## 6. Required capabilities

- A common agent interface with structured response objects
- A routing layer that maps workflow names to agent implementations
- Shared model and retrieval client utilities
- Task-local prompt design for each agent
- Response parsing or fallback logic for workflows that expect structured model output
- Common wrappers for transport concerns such as API parsing and error handling
- Optional event-context injection for triggered workflows

## 7. Control gates

- The orchestrator only allows known agent names, preventing implicit routing
- Each agent has a bounded responsibility and prompt shape
- Retrieval is used where grounding is valuable, rather than for every workflow
- API handlers normalize bad-request, upstream, and internal-error behavior consistently
- Review and quiz flows expect structured JSON-like outputs and include parse fallbacks
- Event-driven invocation is gated earlier by the trigger layer, so not every event reaches an agent

## 8. Delivery steps

1. Define a base agent contract that returns structured output and metadata.
2. Build a shared Bedrock client for generation and retrieval concerns.
3. Implement one agent per workflow with a narrow purpose and explicit prompt contract.
4. Add a thin orchestrator that maps workflow names to agents.
5. Reuse the same agent logic behind CLI and Lambda entry points.
6. Add fallback parsing for workflows that depend on model-generated JSON.
7. If event-driven invocation is needed, pass event context into the relevant agent rather than creating a separate agent copy.

## 9. Common risks and failure modes

- A “multi-agent” label can hide the fact that routing logic is still manual and brittle if naming conventions drift.
- Shared infrastructure can create hidden coupling if too much task logic moves into the common Bedrock client.
- Structured-output workflows can still fail when model JSON is malformed.
- Retrieval grounding can be uneven if the knowledge base is incomplete or low quality.
- Adding too many tiny agents can fragment the system without real benefit.
- A future need for cross-agent collaboration would require a different orchestration model than the current task router.

## 10. Artefacts produced

- Agent interface and response schema
- Task-specific agent implementations
- Central orchestrator for routing
- Shared Bedrock and retrieval client
- CLI and Lambda invocation paths
- Structured outputs such as explanations, diagrams, quizzes, and architecture reviews

## 11. Example executive narrative

This project uses a pragmatic multi-agent workflow pattern built around task specialization rather than autonomous coordination. A lightweight orchestrator routes requests to focused agents for tutoring, quiz generation, and architecture review, while all agents share the same Bedrock runtime and optional retrieval context. The approach keeps the system easy to reason about, easier to extend, and more reliable than a single overloaded prompt, while avoiding the cost and complexity of a collaborative agent swarm.
