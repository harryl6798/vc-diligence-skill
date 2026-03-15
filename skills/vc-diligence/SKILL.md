---
name: vc-diligence
description: An exhaustive, 1000-line enterprise-grade Venture Capital due diligence skill. Provides a massive, multi-stage workflow covering deep technical research, precise search methodologies, legal/commercial risk auditing, report synthesis, and advanced Excalidraw visual argumentation for any industry.
---

# VC Diligence Skill: The Ultimate Lead Partner Framework (V22 - PMF & Multi-Agent Discovery Edition)

This is the definitive handbook for executing the `vc-diligence` skill. It combines **Recursive Hypothesis-Driven Discovery** with **Hyper-Depth Content Harvesting**, **Specialized Architecture Auditing**, **Product-Market Fit (PMF) Leveling**, and **Iterative Report Expansion**. The goal is to produce an **intimate, 30+ page master audit** that identifies the technical plumbing, commercial moats, and legal red-flags of any startup.

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
- **The Isomorphism Principle**: Diagrams must convey business logic through structure, not just labels.
- **The Education Test**: Could someone learn something concrete from the diagram?
- **The Traceability Rule**: Every claim MUST be backed by a link or raw finding file.
- **Fact-Dense Writing**: Omit fluff. Use metrics, specific library names, and exact pricing.
- **The Search-to-Fetch Ratio**: For every Turn that includes a `google_web_search`, you MUST execute a corresponding `web_fetch` Turn for the top 3-5 high-signal results.

---

## 2. TABLE OF CONTENTS
1. [Phase 0: Workspace Architecture & Initialization](#3-phase-0-workspace-architecture--initialization)
2. [Phase 1: Objective-Oriented Recursive Search & Content Harvesting](#4-phase-1-objective-oriented-recursive-search--content-harvesting)
3. [Phase 2: MCP Service Discovery & Third-Party Intelligence](#5-phase-2-mcp-service-discovery--third-party-intelligence)
4. [Phase 3: The Founder Alpha & Team Audit](#6-phase-3-the-founder-alpha--team-audit)
5. [Phase 4: Specialized Technical Teardown (Architecture Auditor)](#7-phase-4-specialized-technical-teardown-architecture-auditor)
6. [Phase 5: Product-Market Fit (PMF) Audit & Leveling](#8-phase-5-product-market-fit-pmf-audit--leveling)
7. [Phase 6: Commercial, Financial & Unit Economic Diligence](#9-phase-6-commercial-financial--unit-economic-diligence)
8. [Phase 7: Market Dynamics, Competitive Moats & Exit Benchmarks](#10-phase-7-market-dynamics-competitive-moats--exit-benchmarks)
9. [Phase 8: The 2025-2026 AI Impact & Industry Trend Analysis](#11-phase-8-the-2025-2026-ai-impact--industry-trend-analysis)
10. [Phase 9: The Master VC Diligence Questionnaire (Exhaustive)](#12-phase-9-the-master-vc-diligence-questionnaire-exhaustive)
11. [Phase 10: Legal, Regulatory & Governance Risk Auditing](#13-phase-10-legal-regulatory--governance-risk-auditing)
12. [Phase 11: Visual Asset Acquisition & Content Richness](#14-phase-10-visual-asset-acquisition--content-richness)
13. [Phase 11.5: Formal Visual Design Specification](#145-phase-115-formal-visual-design-specification)
14. [Phase 12: Synthesis - Master Deliverables Protocol](#15-phase-12-synthesis---master-deliverables-protocol)
15. [Phase 12.5: The Iterative Master Expansion Step](#155-phase-125-the-iterative-master-expansion-step)
16. [Phase 13: Advanced Visual Argumentation (Skill Delegation)](#16-phase-13-advanced-visual-argumentation-skill-delegation)
17. [Phase 14: Formatting Audit (Tables vs. Bullets)](#17-phase-14-formatting-audit-tables-vs-bullets)
18. [Phase 15: Final Quality Assurance & Hand-off](#18-phase-15-final-quality-assurance--hand-off)

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

**Wave 0.5: Product-Market Fit (PMF) Audit**
- **Central Question**: "At what level of PMF is this startup currently operating (Level 1–4), and what are the signals of satisfaction, demand, and efficiency?"
- **The PMF Method (First Round Framework)**:
    - **Level 1 (Nascent)**: Solving a problem for 3-5 customers. Qualitative: "The Grind."
    - **Level 2 (Developing)**: Scalable sales channel emerging. Qualitative: "Lite PMF."
    - **Level 3 (Strong)**: Floodgates open. Efficiency + GTM refinement. Qualitative: "The Geyser."
    - **Level 4 (Extreme)**: Categorical dominance. Global expansion.
- **Discovery Specifics**: Retention/Usage depth (Satisfaction), Sales velocity/Inbound (Demand), Magic Number/Burn Multiple (Efficiency).

**Wave 1: Identity, Trajectory & Capital Structure**
- **Central Question**: "Who is this company at its core, how much capital have they consumed, and what is their growth velocity?"
- **Discovery Specifics**: Legal Structure, Cap Table Proxies (Form D), Hiring Velocity (LinkedIn).

**Wave 2: Founder Alpha & Talent Density**
- **Central Question**: "Why is this specific team uniquely qualified to win this category, and what are their individual 'superpowers'?"
- **Discovery Specifics**: The 'Spike' (Academic, Serial, BigTech), Social Graph, Conflict/Cohesion history.

**Wave 3: Technical Architecture & Product Moat**
- **Central Question**: "Exactly how is this built, where are the structural bottlenecks, and is it a defensible moat or a thin wrapper?"
- **MANDATORY**: Use `web_fetch` on all technical docs. Build a component-by-component feature teardown.

**Wave 4: Market Dynamics & Competitive Displacement**
- **Central Question**: "Which $B+ market is being eaten, who are the incumbents being displaced, and what are the exit benchmarks?"
- **The Synthesis Mandate**: Do NOT search for "TAM SAM SOM." Search for **Atomic Facts** (user counts, pricing proxies) and synthesize.

### 4.2 Query Fanout Mandate
For every Central Question or Hypothesis, you MUST generate a **fanout of 3-5 distinct, multi-angle queries**.

### 4.3 The Search Critic & Intent SOP (Least-to-Most Protocol)
Before executing ANY query, apply **Least-to-Most Prompting**:
1. **Decomposition**: "Break the Central Question down into the fundamental sub-questions that need to be answered first."
2. **Sequential Solving**: "Solve each sub-question one by one, using the answer from the previous step to inform the next search angle."
3. **The 'Reasonable Searchability' Check**: Search for the **atomic ingredients** instead of the **finished meal**.
4. **The Search-to-Fetch Mandate**: For each query fanout, identify the top high-signal URLs and execute `web_fetch`.

---

## 5. PHASE 4: SPECIALIZED TECHNICAL TEARDOWN (ARCHITECTURE AUDITOR)

**CRITICAL DELEGATION**: For this phase, activate the `architecture-auditor` skill.
1. **Harvest Ingredients**: Collect real API names, JSON schemas, and method calls.
2. **Audit Moat**: Use the `architecture-auditor` to perform the "Wrapper vs. Moat" test.

---

## 6. PHASE 5: PRODUCT-MARKET FIT (PMF) AUDIT & LEVELING

You MUST apply the **First Round Capital PMF Method** to determine the company's trajectory.

### 6.1 The 3 Dimensions of PMF
1. **Satisfaction**: Audit customer reviews, developer forums (Discord/Reddit), and case studies. Are they "Friend-zoned" (like but don't need) or is it a "Painkiller"?
2. **Demand**: Search for inbound interest signals, waiting lists, and pricing power (ability to raise prices without churn).
3. **Efficiency**: Calculate/Model the Magic Number, Burn Multiple, and CAC Payback based on revenue vs. headcount growth.

### 6.2 The 4 Levers (The 4Ps) Evaluation
If the company is stuck between levels, identify which lever they are pulling:
- **Persona**: Moving upmarket or changing the ICP.
- **Problem**: Pivoting to a more urgent/important problem.
- **Promise**: Refining the unique value prop.
- **Product**: Feature iteration to meet the promise.

---

## 7. PHASE 11: SYNTHESIS - THE MASTER DELIVERABLES PROTOCOL

### 7.1 `full_diligence_report.md` (The 30+ Page Master Audit)
- **Header 1: Executive Summary** (3-paragraph distillation).
- **Header 2: Company Profile & Core Product** (Legal names, feature list).
- **Header 3: Product-Market Fit Audit** (Satisfaction/Demand/Efficiency dimensions, PMF Level 1-4 verdict).
- **Header 4: The Founder Alpha Audit** (Histories, social graphs, citations).
- **Header 5: Financing & Capital Structure** (Round-by-round partners, valuations).
- **Header 6: Detailed Technical Architecture** (Plumbing, stack choices, bottlenecks).
- **Header 7: Market & Competitive Landscape** (TAM/SAM/SOM synthesis, incumbent weaknesses).
- **Header 8: Commercials & Unit Economics** (GTM strategy, LTV/CAC modeling).
- **Header 9: Legal, Regulatory & Governance** (IP provenance, compliance).
- **Header 10: Master Research Appendix** (Categorized links).
- **Header 11: Final Investment Verdict** (Detailed rationale explaining the "Why").

---

## 8. PHASE 11.5: THE ITERATIVE MASTER EXPANSION STEP (MANDATORY)

Once the initial draft of the `full_diligence_report.md` is complete, you MUST execute this iterative expansion cycle to reached the **30-page mandate**.

---

## 9. PHASE 12: ADVANCED VISUAL ARGUMENTATION (SKILL DELEGATION)

**CRITICAL MANDATE**: Do NOT attempt to generate Excalidraw JSON manually. Use the `activate_skill` tool to invoke the `excalidraw-diagram` skill.

---

## 10. FINAL QUALITY ASSURANCE & HAND-OFF

### 19.1 Hand-off
"Diligence complete. Overview Memo, Deep Dive, and 30+ page Master Audit (with full PMF Leveling, feature teardowns, and specialized visual diagrams) are in `deliverables/`."

---
*End of VC Diligence Skill Masterclass V22.*
