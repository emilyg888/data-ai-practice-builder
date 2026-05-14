---
type: pattern
status: draft
risk_level: medium
business_domains:
  - platform engineering
  - cloud enablement
  - AI experimentation
  - developer productivity
capability_layers:
  - infrastructure as code
  - environment configuration
  - stack composition
  - custom resource provisioning
  - lifecycle automation
ai_impact:
  - repeatable AI lab provisioning
  - faster experimentation on Bedrock workloads
  - lower persistence risk through teardown-first design
related_controls:
  - stack dependency ordering
  - environment-gated deployment
  - destroyable resource policy
  - parameter-based cross-stack integration
  - custom resource lifecycle management
---

# Ephemeral GenAI Lab IaC with Optional Stacks

## 1. Problem solved

This pattern solves the problem of standing up a reusable AWS GenAI lab without treating every experiment as a one-off manual build.

In this repo, the IaC method provides:

1. A repeatable way to provision the core Bedrock, Knowledge Base, S3, Lambda, and API resources.
2. A controlled way to add an optional event-driven trigger stack only when needed.
3. A teardown path that removes the lab cleanly so experimentation does not leave persistent cost behind.

The result is an infrastructure pattern optimized for learning, demos, and bounded experiments rather than long-lived production hosting.

## 2. When to use

Use this pattern when:

- you need fast, repeatable provisioning for an AI lab or proof of concept
- the environment should be easy to create and destroy
- some infrastructure capabilities are optional and should not always be deployed
- application code and infrastructure code should stay in one repository
- managed AI services require some provisioning steps that are awkward to express as plain static resources

## 3. Business outcomes

- Faster environment setup for developers and solution architects
- Lower cloud waste because resources are designed for full teardown
- Safer experimentation through feature-gated optional stacks
- Better consistency because deployment is script- and CDK-driven instead of console-driven
- Cleaner integration between infrastructure and application runtime through shared parameters and outputs

## 4. Logical architecture

The IaC flow in this repo works as follows:

1. `infrastructure/app.py` loads environment settings and synthesizes the CDK app.
2. The core stack, `AirLabStack`, is always instantiated and provisions the main AI lab runtime.
3. The optional `TriggerStack` is only created when `DEPLOY_TRIGGER_STACK=true`.
4. The trigger stack depends on the core stack and consumes values exported by it, including the API endpoint parameter name and tutor method ARN.
5. Deployment scripts bootstrap CDK, install dependencies, and deploy all selected stacks.
6. Destroy scripts reverse the lifecycle and remove the lab aggressively.

This gives the project a layered IaC structure:

- base platform stack for the main lab
- optional extension stack for event-driven AI triggering
- script-based operational wrapper for deploy and destroy

## 5. Reference architecture options

### Option A: Single-stack lab

Put all resources in one stack. This is simpler initially, but it couples the optional trigger path to the core lab and makes partial deployment less clean.

### Option B: Core stack plus optional extension stack

This is the method leveraged in this project. The main AI lab is deployed by default, and the trigger layer is enabled only when requested by environment flag.

### Option C: Fully decomposed multi-stack platform

Split networking, storage, AI runtime, knowledge base, and eventing into many stacks. This is better for production-scale ownership boundaries, but it would add unnecessary complexity for this lab.

## 6. Required capabilities

- CDK application entry point that can synthesize one or more stacks
- Environment-variable configuration for account, region, and feature toggles
- Cross-stack references or parameter sharing for dependent integrations
- Custom-resource support for services with lifecycle gaps in plain IaC
- Scripted bootstrap, deploy, and destroy flows
- Removal policies that match the lab’s ephemeral intent
- Asset packaging rules that keep Lambda deployment bundles focused

## 7. Control gates

- `DEPLOY_TRIGGER_STACK` controls whether the optional event stack is included at all
- `TriggerStack` explicitly depends on `AirLabStack`, which prevents invalid ordering
- SSM parameters are used to share runtime integration values across stacks
- Custom-resource behavior for Knowledge Base provisioning is gated by `ENABLE_REAL_KB_CALLS`
- Buckets and log groups use explicit lifecycle and removal settings aligned to lab teardown
- Deployment happens through scripts and Make targets, reducing ad hoc console drift

## 8. Delivery steps

1. Define the CDK app entry point and environment contract in `infrastructure/app.py`.
2. Model the core lab resources in `infrastructure/stacks/airlab_stack.py`.
3. Add custom-resource logic where managed AI resource lifecycle cannot be handled cleanly by static declarations alone.
4. Publish cross-stack integration values through SSM parameters or stack properties.
5. Add optional extension stacks behind explicit environment flags.
6. Wrap synthesis, bootstrap, deploy, and destroy in repository scripts and `Makefile` targets.
7. Validate both modes: core-stack-only deployment and core-plus-trigger deployment.

## 9. Common risks and failure modes

- Lab-oriented removal policies can destroy data that a production team expected to keep.
- Environment-variable drift can change deployment behavior across machines.
- Custom-resource logic can hide provisioning complexity inside Lambda code, which is harder to reason about than plain declarative resources.
- Cross-stack integration can fail if shared parameter names or method ARNs change without coordinated updates.
- Feature flags can create deployment combinations that are lightly tested.
- `cdk deploy --all` is convenient for a lab, but it is less selective than a production release flow.

## 10. Artefacts produced

- CDK app entry point in `infrastructure/app.py`
- Core infrastructure stack in `infrastructure/stacks/airlab_stack.py`
- Optional trigger infrastructure stack in `infrastructure/stacks/trigger_stack.py`
- Knowledge Base custom-resource provisioner in `knowledge_base/provisioner.py`
- Deployment and destroy scripts in `scripts/deploy.sh` and `scripts/destroy.sh`
- Convenience targets in `Makefile`
- SSM parameters, CloudFormation stacks, and stack outputs created by deployment

## 11. Example executive narrative

This project uses a pragmatic Infrastructure-as-Code pattern for AI experimentation on AWS. A Python CDK application provisions an ephemeral Bedrock lab as the default foundation, then conditionally adds an event-driven trigger stack when that capability is needed. The method favors repeatability, low residual cost, and fast iteration over production-grade permanence, which makes it well suited to internal learning environments, demos, and controlled architecture experiments.
