# Use Case: Analyst-in-the-Loop Controls for Fraud AI Recommendations

## Source
- Profile: https://www.linkedin.com/in/emily-gao-291177a/
- Post URL: https://www.linkedin.com/posts/emily-gao-291177a_reusableaiaccelerators-enterpriseai-semanticlayer-share-7457348849179971585-s5BA
- Post Title: Semantic_Foundry for Governed Enterprise AI
- Post ID: 7457348849179971585

## Post Insight Summary
The post explicitly distinguishes assistive fraud alerting from automated adverse customer action. It recommends encoding approved/disallowed use, required caveats, access restrictions, and human-review requirements in semantic assets for high-risk domains.

## Business Context
- Industry: Banking
- Domain: Fraud Operations and Responsible AI
- Stakeholders: Fraud Investigations, Customer Operations, Compliance, Legal, Responsible AI Office

## Problem Statement
Fraud models can be accurate yet still create regulatory and customer-harm risk if outputs are used as fully automated decision triggers. Teams need explicit usage controls that constrain how AI recommendations are consumed operationally.

## Proposed AI/Data Use Case
- Objective: Enforce analyst review policies for fraud alerts generated from AI models.
- Primary User: Fraud investigator.
- Decision Type: Human decision with AI recommendation support.
- Frequency: Real-time for each alert.

## Inputs
- Structured data: Fraud score, risk features, account and transaction context.
- Unstructured data: Investigation notes, policy caveats.
- Governance metadata: Approved use, disallowed use, certification blockers.

## Outputs
- Recommendation: Triage priority and suggested investigation path.
- Decision support: Required caveats and rationale presented to analyst.
- Control enforcement: Blocked actions for disallowed automated usage.

## Workflow
1. Receive fraud alert and model outputs.
2. Attach semantic usage policy and caveat metadata.
3. Require analyst acknowledgment of caveats.
4. Allow only permitted actions in case tooling.
5. Log reviewer decision and policy compliance evidence.

## Success Metrics
- Business KPI: Reduced inappropriate automated adverse actions.
- Model KPI: Stable alert quality with explainability coverage.
- Operational KPI: High policy-compliant resolution rate.

## Risks and Controls
- Automation bias risk: Mandatory analyst review and evidence capture.
- Compliance risk: Hard guardrails for disallowed use cases.
- Access risk: Restrict privileged actions by role and certification status.
- Audit risk: Persist caveat acknowledgment and final decision lineage.

## MVP Scope
- In scope: One fraud workflow with policy-driven action controls.
- Out of scope: Full enterprise case management redesign.
- Timeline: 3-5 weeks for controlled pilot.

## Traceability
- Derived from post claim(s):
  - "A fraud alert should support analyst review. It should not become an automated adverse action against a customer."
  - "The semantic package explicitly defines approved use, disallowed use, required caveats, human review requirements, access restrictions, certification blockers."