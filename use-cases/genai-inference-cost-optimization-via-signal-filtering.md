# Use Case: GenAI Cost Optimization Through Signal Filtering

## Source
- Profile: https://www.linkedin.com/in/emily-gao-291177a/
- Post URL: https://www.linkedin.com/posts/emily-gao-291177a_aiarchitecture-kafka-aws-share-7452644703209967616-jz0k
- Post Title: Kafka Streams + Lambda Decisions for GenAI
- Post ID: 7452644703209967616

## Post Insight Summary
The post reports that low-value noise can be filtered before model invocation, while high-value signals still trigger AI. It frames cost optimization as a control problem solved upstream of model inference.

## Business Context
- Industry: Enterprise AI programs
- Domain: FinOps for AI platforms
- Stakeholders: FinOps, AI platform teams, data engineering, business sponsors

## Problem Statement
Inference spend grows rapidly when all events call expensive models. Without selective routing and filtering, cost rises faster than business value and ROI becomes hard to sustain.

## Proposed AI/Data Use Case
- Objective: Reduce unnecessary GenAI calls while preserving high-value decisions.
- Primary User: AI platform owner and FinOps analyst.
- Decision Type: Automated cost-aware invocation policy.
- Frequency: Continuous stream processing.

## Inputs
- Structured data: Event scores, business value signals, model cost per token/call.
- Policy inputs: Daily spend budget, per-channel thresholds, fallback model policy.
- Historical data: Conversion or action outcomes from prior AI calls.

## Outputs
- Invocation policy outcome: run premium model, run low-cost model, or skip.
- Cost telemetry: projected and actual spend by event cohort.
- Value telemetry: outcome lift for invoked events.

## Workflow
1. Score incoming events for expected business value.
2. Compare expected value against dynamic cost threshold.
3. Select model tier or suppress inference.
4. Log decision reason and cost estimate.
5. Evaluate spend-to-impact performance and tune thresholds.

## Success Metrics
- Business KPI: Increased ROI from AI-enabled workflows.
- Model KPI: Maintained quality on high-value invoked events.
- Operational KPI: Reduced total inference volume with bounded latency impact.

## Risks and Controls
- Quality regression risk: Shadow-evaluate suppressed events periodically.
- Budget shock risk: Add hard caps and emergency fallback routes.
- Bias risk: Ensure suppression logic does not systematically disadvantage cohorts.
- Transparency risk: Publish decision reasons and spend dashboards.

## MVP Scope
- In scope: One high-volume workflow with two model tiers.
- Out of scope: Enterprise-wide policy harmonization across all products.
- Timeline: 3-4 weeks for controlled experiment.

## Traceability
- Derived from post claim(s):
  - "Low-value noise filtered out."
  - "Tunable trigger rate, reduction in AI calls."
  - "Cost optimisation."
