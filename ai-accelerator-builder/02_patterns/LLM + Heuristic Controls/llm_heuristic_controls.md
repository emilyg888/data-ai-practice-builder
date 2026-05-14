---
type: pattern
status: draft
risk_level: medium
business_domains:
  - enterprise_ai
  - research_intelligence
  - knowledge_management
  - content_strategy
  - ai_governance
capability_layers:
  - paper_ingestion
  - theme_synthesis
  - position_building
  - heuristic_control_engine
  - memory_layer
  - evaluation_gate
  - post_generation
  - audit_and_traceability
ai_impact:
  - accelerates_research_synthesis
  - improves_theme_discovery
  - reduces_generic_outputs
  - enables_debatable_position_generation
  - strengthens_governed_ai_workflows
related_controls:
  - deduplication_rules
  - theme_reuse_controls
  - rejection_rules
  - output_validation
  - weighted_selection
  - evaluation_guardrails
  - memory_freshness_controls
  - audit_traces
---

# LLM + Heuristic Control Engine

## 1. Problem solved

Enterprise AI systems often fail when the LLM is asked to do too much.

In the AI paper research engine, the original goal was not to summarise research papers. The goal was to turn a pool of research papers into debatable enterprise AI positions that are novel, specific, relevant, and worth publishing.

Early versions asked the LLM to generate themes, judge theme quality, reject weak ideas, and select the final output. This created outputs that were locally plausible but globally inconsistent.

A theme could sound good in isolation, but fail the broader architecture test:

- Is it novel?
- Is it specific?
- Is it enterprise-relevant?
- Does it create tension or debate?
- Does it reframe the problem rather than repeat obvious AI commentary?

This pattern solves that problem by separating judgement from control.

The core design principle is:

**LLM proposes. Code enforces. Memory guides. Evaluation gates decide whether the output is publishable.**

## 2. When to use

Use this pattern when an AI workflow needs both creative reasoning and deterministic control.

It is especially useful when:

- outputs must be original, not generic
- the system needs to compare new ideas against previous ideas
- LLM-generated outputs must pass explicit quality gates
- multiple candidate outputs need to be ranked or rejected
- memory needs to influence future decisions
- the workflow requires consistency across runs
- the LLM should generate and reason, but not own the final control decision

Good use cases include:

- research paper synthesis engines
- thought leadership generation systems
- enterprise AI position builders
- analyst-assist workflows
- case investigation recommendation engines
- signal discovery engines
- governed RAG pipelines
- AI-generated policy or control drafting workflows

Do not use this pattern when the task is a simple one-off generation with no need for memory, comparison, rejection, or repeatable decision controls.

## 3. Business outcomes

This pattern helps move an AI workflow from a content generator to a governed decision-support engine.

Expected outcomes include:

- stronger quality control over AI outputs
- reduced generic or repetitive content
- better reuse of prior themes and decisions
- clearer separation between probabilistic reasoning and deterministic enforcement
- improved traceability of why an output was selected or rejected
- more consistent publishing or recommendation standards
- faster iteration on research-to-position workflows
- safer scaling of GenAI into enterprise operating processes

For the AI paper research engine, the business outcome is not simply more posts. It is a repeatable engine for finding strong themes in a research paper pool and turning them into debate-worthy enterprise AI positions.

## 4. Logical architecture

The logical architecture separates the workflow into five main layers:

1. **Input layer** — research paper pool and metadata
2. **LLM reasoning layer** — theme synthesis, tension detection, reframing, position building
3. **Heuristic control layer** — deterministic rules, validation, rejection, scoring, and selection
4. **Memory layer** — previous themes, reused concepts, rejected ideas, accepted patterns
5. **Evaluation gate** — final publishability decision and audit trace

```text
┌──────────────────────────────────────────────────────────────┐
│                    Research Paper Pool                       │
│        papers, abstracts, chunks, metadata, notes             │
└───────────────────────────────┬──────────────────────────────┘
                                │
                                ▼
┌──────────────────────────────────────────────────────────────┐
│                     Theme Synthesis                          │
│  LLM detects themes, tensions, debates, weak signals          │
└───────────────────────────────┬──────────────────────────────┘
                                │
                                ▼
┌──────────────────────────────────────────────────────────────┐
│                     Position Builder                         │
│  LLM reframes the problem and drafts candidate positions      │
└───────────────────────────────┬──────────────────────────────┘
                                │
                                ▼
┌──────────────────────────────────────────────────────────────┐
│                 Heuristic Control Engine                     │
│  dedupe | reject | validate | score | select | enforce        │
└───────────────┬───────────────────────────────┬──────────────┘
                │                               │
                ▼                               ▼
┌─────────────────────────────┐   ┌────────────────────────────┐
│          Memory Layer        │   │       Evaluation Gate       │
│ prior themes, reuse history, │   │ novelty, specificity,       │
│ rejected ideas, accepted     │   │ enterprise relevance,       │
│ patterns, decision traces    │   │ debate strength, quality    │
└───────────────┬─────────────┘   └─────────────┬──────────────┘
                │                               │
                └───────────────┬───────────────┘
                                ▼
┌──────────────────────────────────────────────────────────────┐
│                      Post Generator                          │
│        publishable post, rationale, trace, rejected options   │
└──────────────────────────────────────────────────────────────┘
```

The critical architectural split is:

| Responsibility | LLM | Heuristics / Code | Memory | Evaluation |
|---|---:|---:|---:|---:|
| Synthesis across papers | Yes | No | Supports | Reviews |
| Detecting tension | Yes | No | Supports | Scores |
| Reframing problems | Yes | No | Supports | Scores |
| Drafting positions | Yes | No | Supports | Reviews |
| Deduplication | No | Yes | Supports | Reviews |
| Theme reuse control | No | Yes | Yes | Reviews |
| Rejection rules | No | Yes | Supports | Yes |
| Output validation | No | Yes | Supports | Yes |
| Final weighted selection | No | Yes | Yes | Yes |
| Audit trace | No | Yes | Yes | Yes |

## 5. Reference architecture options

### Option A — Local-first research engine

Best for experimentation, personal knowledge systems, thought leadership workflows, and low-cost iteration.

```text
Local papers / notes
        ↓
Local parser and chunker
        ↓
Local or hosted LLM
        ↓
Python heuristic control engine
        ↓
Local memory store: JSON, SQLite, DuckDB, or vector index
        ↓
Evaluation report and generated post
```

Recommended when:

- the system is still evolving
- cost control matters
- experimentation speed is more important than enterprise integration
- the user wants full visibility into prompts, outputs, and control logic

### Option B — Governed enterprise workflow

Best for teams that need shared evaluation standards, auditability, and repeatable publishing controls.

```text
Document repository / research source
        ↓
Ingestion and metadata service
        ↓
LLM orchestration service
        ↓
Policy and heuristic control engine
        ↓
Theme memory and decision registry
        ↓
Evaluation gate
        ↓
Human review / approval
        ↓
Published content or decision artefact
```

Recommended when:

- multiple analysts or authors contribute
- outputs need review and approval
- themes must be governed across time
- rejected and accepted outputs need traceability
- the organisation wants reusable AI-assisted research workflows

### Option C — AI workbench control-plane pattern

Best for maturing the pattern into a reusable enterprise accelerator.

```text
Prompt registry
Retrieval profile registry
Heuristic rule registry
Evaluation metric registry
Memory / theme registry
Run trace store
Approval workflow
Promotion pipeline
```

Recommended when:

- prompts, rules, and evaluation gates need versioning
- different use cases share the same control pattern
- there is a need to promote workflow bundles from experimentation to production
- governance needs to be embedded before the LLM output reaches business users

## 6. Required capabilities

### LLM capabilities

- theme synthesis
- cross-paper comparison
- tension detection
- contrarian framing
- problem reframing
- position drafting
- narrative generation
- explanation of reasoning at a summary level

### Heuristic capabilities

- deterministic deduplication
- similarity scoring
- rejection rules
- theme reuse rules
- novelty checks
- specificity checks
- enterprise relevance checks
- weighted ranking
- output schema validation
- forbidden-pattern detection
- minimum quality thresholds

### Memory capabilities

- accepted theme memory
- rejected theme memory
- prior post memory
- concept reuse tracking
- freshness tracking
- similarity comparison against previous outputs
- decision history
- run-level metadata

### Evaluation capabilities

- novelty score
- specificity score
- debate strength score
- enterprise relevance score
- non-generic content score
- architecture relevance score
- publishability decision
- rejection reason capture

### Operational capabilities

- prompt versioning
- run trace logging
- configuration-driven thresholds
- manual override
- output review
- rollback to prior prompts or rules
- test set of known strong and weak outputs

## 7. Control gates

The control gates define what the LLM is not allowed to decide alone.

### Gate 1 — Input eligibility

Checks whether the paper or document is suitable for the workflow.

Controls may include:

- valid file type
- minimum text length
- relevant topic domain
- duplicate paper detection
- metadata completeness

### Gate 2 — Theme quality

Checks whether candidate themes are strong enough to continue.

Controls may include:

- minimum specificity
- minimum novelty
- clear enterprise relevance
- explicit tension or debate
- rejection of generic AI claims

### Gate 3 — Memory conflict

Checks whether the theme has already been used too recently or too often.

Controls may include:

- similarity to previous posts
- reused phrase detection
- repeated argument detection
- freshness threshold
- theme cooldown period

### Gate 4 — Position strength

Checks whether the candidate position is worth debating.

Controls may include:

- clear claim
- non-obvious angle
- business implication
- architecture implication
- governance implication
- practical consequence

### Gate 5 — Output validation

Checks whether the generated output meets structural and quality standards.

Controls may include:

- required sections present
- title present
- no unsupported claims
- no generic conclusion
- no excessive repetition
- suitable tone and length

### Gate 6 — Final weighted selection

Scores and ranks candidates using deterministic logic.

Example scoring dimensions:

```text
final_score =
  novelty_score * 0.25
+ specificity_score * 0.20
+ debate_strength_score * 0.20
+ enterprise_relevance_score * 0.20
+ memory_freshness_score * 0.15
```

The LLM can propose candidate themes, but the final decision should be made by the control engine.

## 8. Delivery steps

### Step 1 — Define the target output

Clarify what the engine is meant to produce.

For this project, the target output is:

**A debatable enterprise AI position derived from one or more research papers.**

Not:

- a summary
- a generic post
- a list of paper highlights
- a model-generated opinion without controls

### Step 2 — Separate LLM responsibilities from control responsibilities

Define what the model can do and what code must enforce.

A useful rule:

**The LLM can generate judgement candidates. Code owns acceptance decisions.**

### Step 3 — Build the paper pool and metadata model

Capture:

- paper title
- authors
- source
- date
- abstract
- chunks
- topic tags
- extracted concepts
- run metadata

### Step 4 — Implement theme synthesis

Use the LLM to identify:

- recurring ideas
- tensions between papers
- emerging patterns
- unresolved debates
- assumptions worth challenging

### Step 5 — Implement the heuristic control engine

Start with simple deterministic rules:

- reject generic claims
- reject repeated themes
- reject weak enterprise relevance
- reject outputs without a clear position
- score novelty and specificity

Then gradually add weighted scoring.

### Step 6 — Add memory

Store:

- accepted themes
- rejected themes
- generated posts
- rejection reasons
- score history
- theme reuse history

Memory should guide future decisions, not simply store everything.

### Step 7 — Add evaluation gates

Define pass/fail checks and scoring thresholds.

For example:

- novelty score must be above threshold
- enterprise relevance must be explicit
- generic content score must be below threshold
- debate strength must be above threshold

### Step 8 — Generate the final post

Only generate the final post after the candidate theme or position passes the control gates.

The post generator should receive:

- selected theme
- supporting evidence
- position framing
- rejected alternatives if useful
- tone guidance
- target audience

### Step 9 — Capture the trace

Every run should produce a trace showing:

- papers used
- candidate themes generated
- scores assigned
- rejected candidates
- selected candidate
- memory matches
- final output
- evaluation result

### Step 10 — Iterate with a gold set

Maintain a small library of:

- strong themes
- weak themes
- good posts
- rejected posts
- known failure cases

Use this to test whether changes to prompts, rules, or scoring improve the engine.

## 9. Common risks and failure modes

### Risk 1 — The LLM becomes the judge of its own output

If the LLM generates, evaluates, and selects the final answer, the workflow can become persuasive but unreliable.

Mitigation:

- keep final selection in deterministic code
- use explicit scoring rules
- log rejection reasons
- compare against memory

### Risk 2 — Locally plausible but globally inconsistent output

A generated theme may sound strong in isolation but repeat prior ideas or fail the system-level objective.

Mitigation:

- use memory similarity checks
- compare against prior accepted and rejected themes
- apply global evaluation criteria

### Risk 3 — Generic AI commentary

The system may drift into safe claims such as “AI needs governance” or “data quality matters.”

Mitigation:

- reject generic phrases
- require a specific architecture implication
- require a debate or tension
- require enterprise operating-model relevance

### Risk 4 — Memory pollution

If every generated idea is stored as memory, the system may reinforce weak themes.

Mitigation:

- separate accepted, rejected, and experimental memory
- attach quality scores to memory
- apply retention and freshness rules
- periodically prune low-value entries

### Risk 5 — Over-engineered heuristics

Too many rules can block useful creativity.

Mitigation:

- start with a small number of high-value rules
- keep thresholds configurable
- allow human override
- review rejected outputs for false negatives

### Risk 6 — Evaluation becomes a checklist rather than a quality signal

A candidate may pass individual checks but still not be worth publishing.

Mitigation:

- include weighted scoring
- include final human review for high-impact outputs
- retain qualitative rationale
- review outcomes over time

### Risk 7 — Weak traceability

Without run traces, it becomes difficult to understand why one idea was selected and another was rejected.

Mitigation:

- capture scores, rule decisions, memory matches, and final rationale
- version prompts and rules
- store run-level metadata

## 10. Artefacts produced

This pattern should produce both business-facing and engineering-facing artefacts.

### Business-facing artefacts

- selected theme
- debate-worthy position
- generated post
- short executive narrative
- rejected theme summary
- reason for selection
- reason for rejection

### Engineering-facing artefacts

- prompt templates
- heuristic rule definitions
- scoring configuration
- memory schema
- evaluation criteria
- run trace
- test set of good and bad outputs
- threshold configuration
- workflow diagram

### Governance-facing artefacts

- control gate definitions
- rule-to-risk mapping
- evaluation report
- human review record
- decision trace
- memory retention policy
- prompt and rule version history

## 11. Example executive narrative

Most GenAI failures do not come from weak models. They come from asking the model to own too many responsibilities.

In the AI paper research engine, the LLM is not responsible for everything. It synthesises papers, detects tension, reframes problems, and proposes candidate positions. But deterministic controls decide what is allowed to proceed.

The architecture separates three responsibilities:

**LLMs decide what makes sense.**  
**Heuristics decide what is allowed.**  
**Memory decides what is still worth saying.**

That separation turns the system from a research content generator into a theme alchemy engine.

It does not simply summarise papers. It finds the strongest gems in the research paper pool, rejects weak or repetitive ideas, and produces enterprise AI positions that are specific, governed, and worth debating.

The broader enterprise lesson is simple:

Do not start GenAI architecture with the question, “What can the model do?”

Start with the more important question:

**What should the model not be responsible for?**

That is where governed AI architecture begins.
