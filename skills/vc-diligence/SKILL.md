---
name: vc-diligence
description: An exhaustive, 1000-line enterprise-grade Venture Capital due diligence skill. Provides a massive, multi-stage workflow covering deep technical research, precise search methodologies, legal/commercial risk auditing, report synthesis, and advanced Excalidraw visual argumentation for any industry.
---

# VC Diligence Skill: The Ultimate Lead Partner Framework (V21 - Master Multi-Agent Discovery Edition)

This is the definitive handbook for executing the `vc-diligence` skill. It combines **Recursive Hypothesis-Driven Discovery** with **Hyper-Depth Content Harvesting**, **Specialized Architecture Auditing**, and **Iterative Report Expansion**. The goal is to produce an **intimate, 30+ page master audit** that identifies the technical plumbing, commercial moats, and legal red-flags of any startup.

## 0. PREREQUISITES & SETUP (CRITICAL)
Before executing this skill, ensure the following dependencies are installed to support diagram rendering:
1. **Python Playwright**: `pip install playwright`
2. **Browser Binaries**: `npx playwright install chromium`
3. **Internal Renderer**: This skill depends on the `excalidraw-diagram` skill's renderer located at `/Users/harrisonluo/.agents/skills/excalidraw-diagram/references/render_excalidraw.py`.
4. **Specialized Agents**: 
    - Use `architecture-auditor` for Phase 4 & 10.5 (Technical Teardown).
    - Use `excalidraw-diagram` for Phase 12 (Diagram Generation).

---

## 1. THE "HYPER-DEPTH" ANALYST MINDSET

### 1.1 The 30-Page Master Mandate
A brief summary is a failure. You are building an exhaustive legal and commercial case.
- **The Isomorphism Principle**: Diagrams must convey business logic through structure, not just labels. If you remove the text, the shape should still be the meaning.
- **The Education Test**: Could someone learn something concrete from the diagram? It must show actual formats, real event names, and concrete examples.
- **The Traceability Rule**: Every claim MUST be backed by a link or raw finding file.
- **Fact-Dense Writing**: Omit fluff. Use metrics, specific library names, and exact pricing.
- **Exhaustive Extraction**: Use `web_fetch` on 10-20 sources per wave. **Snippets are insufficient.** You MUST extract full text to construct detailed feature breakdowns.
- **The Search-to-Fetch Ratio**: For every Turn that includes a `google_web_search`, you MUST execute a corresponding `web_fetch` Turn for the top 3-5 high-signal results.

---

## 2. TABLE OF CONTENTS
1. [Phase 0: Workspace Architecture & Initialization](#3-phase-0-workspace-architecture--initialization)
2. [Phase 1: Objective-Oriented Recursive Search & Content Harvesting](#4-phase-1-objective-oriented-recursive-search--content-harvesting)
3. [Phase 2: MCP Service Discovery & Third-Party Intelligence](#5-phase-2-mcp-service-discovery--third-party-intelligence)
4. [Phase 3: The Founder Alpha & Team Audit](#6-phase-3-the-founder-alpha--team-audit)
5. [Phase 4: Specialized Technical Teardown (Architecture Auditor)](#7-phase-4-specialized-technical-teardown-architecture-auditor)
6. [Phase 5: Commercial, Financial & Unit Economic Diligence](#8-phase-5-commercial-financial--unit-economic-diligence)
7. [Phase 6: Market Dynamics, Competitive Moats & Exit Benchmarks](#9-phase-6-market-dynamics-competitive-moats--exit-benchmarks)
8. [Phase 7: The 2025-2026 AI Impact & Industry Trend Analysis](#10-phase-7-the-2025-2026-ai-impact--industry-trend-analysis)
9. [Phase 8: The Master VC Diligence Questionnaire (Exhaustive)](#11-phase-8-the-master-vc-diligence-questionnaire-exhaustive)
10. [Phase 9: Legal, Regulatory & Governance Risk Auditing](#12-phase-9-legal-regulatory--governance-risk-auditing)
11. [Phase 10: Visual Asset Acquisition & Content Richness](#13-phase-10-visual-asset-acquisition--content-richness)
12. [Phase 10.5: Formal Visual Design Specification](#135-phase-105-formal-visual-design-specification)
13. [Phase 11: Synthesis - Master Deliverables Protocol](#14-phase-11-synthesis---master-deliverables-protocol)
14. [Phase 11.5: The Iterative Master Expansion Step](#145-phase-115-the-iterative-master-expansion-step)
15. [Phase 12: Advanced Visual Argumentation (Skill Delegation)](#15-phase-12-advanced-visual-argumentation-skill-delegation)
16. [Phase 13: Formatting Audit (Tables vs. Bullets)](#16-phase-13-formatting-audit-tables-vs-bullets)
17. [Phase 14: Final Quality Assurance & Hand-off](#17-phase-14-final-quality-assurance--hand-off)

---

## 3. PHASE 0: WORKSPACE ARCHITECTURE & INITIALIZATION

```bash
mkdir -p diligence_[startup_name]/raw_findings/team
mkdir -p diligence_[startup_name]/raw_findings/tech
mkdir -p diligence_[startup_name]/raw_findings/market
mkdir -p diligence_[startup_name]/raw_findings/legal
mkdir -p diligence_[startup_name]/diagrams
mkdir -p diligence_[startup_name]/deliverables
mkdir -p diligence_[startup_name]/assets
```

---

## 4. PHASE 1: OBJECTIVE-ORIENTED RECURSIVE SEARCH & CONTENT HARVESTING

### 4.1 The Wave-Based Discovery Objectives (Hyper-Depth)

**Wave 0: Product DNA & User Persona (The Foundation)**
- **Central Question**: "What exactly is the product, how does it function for the end-user, and who are the core personas it serves?"
- **Guiding Mandate**: Understand the 'Jobs to be Done' before auditing the 'Right to Win'.
- **Discovery Specifics**: Feature inventory, user personas (Economic Buyer vs. Daily User), UX/Workflow mapping, and core value prop.
- **Example Evidence**: A 'How it Works' page; a user manual; onboarding tutorials; detailed customer testimonials.

**Wave 1: Identity, Trajectory & Capital Structure**
- **Central Question**: "Who is this company at its core, how much capital have they consumed, and what is their growth velocity?"
- **Discovery Specifics**:
    - **Legal Structure**: Identify parent entity, DBAs, and former names.
    - **Cap Table Proxies**: Hunt for funding announcements and SEC Form D filings.
    - **Hiring Velocity**: Search for "LinkedIn Headcount Growth" patterns or historical job postings.
- **Example Evidence**: A Press Release confirming funding rounds; a Crunchbase entry showing round intervals.

**Wave 2: Founder Alpha & Talent Density**
- **Central Question**: "Why is this specific team uniquely qualified to win this category, and what are their individual 'superpowers'?"
- **Discovery Specifics**:
    - **The 'Spike'**: Identify the world-class expertise of each founder (Academic, Serial, BigTech).
    - **Social Graph**: Search for testimonials, board seats, or past managers.
    - **Conflict/Cohesion**: Find evidence of past collaboration (worked together at X for Y years).
- **Example Evidence**: Google Scholar profiles; LinkedIn recommendations; academic publication history.

**Wave 3: Technical Architecture & Product Moat**
- **Central Question**: "Exactly how is this built, where are the structural bottlenecks, and is it a defensible moat or a thin wrapper?"
- **MANDATORY**: Use `web_fetch` on all technical docs, API references, and engineering blogs found.
- **Discovery Specifics**:
    - **Infrastructure Stack**: Identify the 'Plumbing' (AWS/GCP, DBs, LLM providers).
    - **Proprietary IP**: Search for internal project names, custom protocols, or patents.
    - **Performance Benchmarks**: Hunt for latency, throughput, or accuracy metrics.
- **Example Evidence**: API references; GitHub dependency audits; technical whitepapers.

**Wave 4: Market Dynamics & Competitive Displacement**
- **Central Question**: "Which $B+ market is being eaten, who are the incumbents being displaced, and what are the exit benchmarks?"
- **The Synthesis Mandate**: Do NOT search for "TAM SAM SOM." Search for **Atomic Facts**:
    - **Market Size Proxies**: "Total number of [Target User Profile]" or "Total addressable market of [Industry Sector]".
    - **Pricing Proxies**: "[Competitor] pricing" or "[Incumbent] revenue per user".
    - **Adoption Proxies**: "[Competitor] customer count".
- **Hypothesis-First (MANDATORY)**: Based on Waves 1-3, define the *disrupted market* and name the *likely incumbents* and *emerging challengers*.

### 4.2 Query Fanout Mandate
For every Central Question or Hypothesis, you MUST generate a **fanout of 3-5 distinct, multi-angle queries**.
- **Angle 1: Direct Discovery**: (e.g., `\"[Startup] [Topic]\"`)
- **Angle 2: Proxy Signals**: Search for indirect evidence (e.g., `\"[Topic] reviews\"`, `"hiring for [Topic]"`).
- **Angle 3: Technical/Source-Specific**: Target deep sources (`site:github.com`, `filetype:pdf`).
- **Angle 4: Competitive/Market Context**: (e.g., `\"[Startup] vs [Competitor]\"`).

### 4.3 The Search Critic & Intent SOP (Least-to-Most Protocol)
Before executing ANY query, apply **Least-to-Most Prompting**:
1. **Decomposition**: "Break the Central Question down into the fundamental sub-questions that need to be answered first."
2. **Sequential Solving**: "Solve each sub-question one by one, using the answer from the previous step to inform the next search angle."
3. **The 'Reasonable Searchability' Check**: Search for the **atomic ingredients** instead of the **finished meal**.
4. **The Search-to-Fetch Mandate**: For each query fanout, identify the top high-signal URLs and execute `web_fetch`.

---

## 5. PHASE 4: SPECIALIZED TECHNICAL TEARDOWN (ARCHITECTURE AUDITOR)

**CRITICAL DELEGATION**: For this phase, you MUST activate the `architecture-auditor` skill.

1.  **Harvest Ingredients**: Collect real API names, JSON schemas, and method calls to prove the depth of integration.
2.  **Audit Moat**: Use the `architecture-auditor` specialist to perform the "Wrapper vs. Moat" test.
3.  **Feature Teardown**: Draft the detailed component-by-component analysis for the final report.

---

## 6. PHASE 10.5: FORMAL VISUAL DESIGN SPECIFICATION (FACT-DENSE)

Before creating Excalidraw diagrams, you MUST write a **Visual Design Specification** that formalizes the argument. Use the `architecture-auditor` skill to ensure the spec is technical and accurate.

### 10.5.1 The Research Mandate (Visual Ingredients)
For each diagram, you must list the **Evidence Artifacts** discovered in research:
- **Architecture**: List the actual API endpoints, event names, and model names.
- **Market**: List the specific market share percentages and incumbent names.
- **Economic**: List the exact ARR milestones and gross margin percentages.

---

## 7. PHASE 11: SYNTHESIS - THE MASTER DELIVERABLES PROTOCOL

### 7.1 `full_diligence_report.md` (The 30+ Page Master Audit)
- **Header 1: Executive Summary** (3-paragraph distillation).
- **Header 2: Company Profile & Core Product** (Legal names, pivots, exhaustive feature list with sub-bullets).
- **Header 3: The Founder Alpha Audit** (Complete histories, social graphs, citations, and links).
- **Header 4: Financing & Capital Structure** (Round-by-round partners, valuations, board composition).
- **Header 5: Detailed Technical Architecture** (Plumbing, stack choices, bottlenecks, "Wrapper vs. Moat" test).
- **Header 6: Market & Competitive Landscape** (TAM/SAM/SOM synthesis, incumbent weaknesses, displacement economics table).
- **Header 7: Commercials & Unit Economics** (GTM strategy, LTV/CAC modeling, churn analysis).
- **Header 8: Legal, Regulatory & Governance** (IP provenance, compliance status).
- **Header 9: Master Research Appendix** (Categorized links and full source citations).
- **Header 10: Final Investment Verdict** (Detailed rationale explaining the "Why").

---

## 8. PHASE 11.5: THE ITERATIVE MASTER EXPANSION STEP (MANDATORY)

Once the initial draft of the `full_diligence_report.md` is complete, you MUST execute this iterative expansion cycle:
1. **Section Elaborator**: Add at least 3-5 verbose paragraphs per major section.
2. **Structural Depth**: Convert flat lists into hierarchical structures with H3/H4 sub-headings and nested sub-bullets.
3. **Citation Check**: Ensure every factual claim has a corresponding source link (3-5 links per section).

---

## 9. PHASE 12: ADVANCED VISUAL ARGUMENTATION (SKILL DELEGATION)

**CRITICAL MANDATE**: Do NOT attempt to generate Excalidraw JSON manually. Use the `activate_skill` tool to invoke the `excalidraw-diagram` skill.

1. **Invoke the Skill**: Pass your detailed `Visual Design Specification` to the `excalidraw-diagram` skill.
2. **Rendering**: After the skill generates the `.excalidraw` files, use the internal renderer to convert them to PNGs:
   - **Command**: `python3 ~/.agents/skills/excalidraw-diagram/references/render_excalidraw.py diligence_[startup]/diagrams/[filename].excalidraw`

---

## 10. FINAL QUALITY ASSURANCE & HAND-OFF

### 19.1 Hand-off
"Diligence complete. Overview Memo, Deep Dive, and 30+ page Master Audit (with full feature teardowns, iteratively expanded details, and specialized visual diagrams) are in `deliverables/`."

---
*End of VC Diligence Skill Masterclass V21.*
