---
name: vc-diligence
description: An exhaustive, 1000-line enterprise-grade Venture Capital due diligence skill. Provides a massive, multi-stage workflow covering deep technical research, precise search methodologies, legal/commercial risk auditing, report synthesis, and advanced Excalidraw visual argumentation for any industry.
---

# VC Diligence Skill: The Ultimate Lead Partner Framework (V17 - Master Hyper-Depth & Visual Mastery Edition)

This is the definitive handbook for executing the `vc-diligence` skill. It combines **Recursive Hypothesis-Driven Discovery** with **Hyper-Depth Content Harvesting**, **Formal Visual Argumentation**, and **Iterative Report Expansion**. The goal is to produce an **intimate, 30+ page master audit** that identifies the technical plumbing, commercial moats, and legal red-flags of any startup.

## 0. PREREQUISITES & SETUP (CRITICAL)
Before executing this skill, ensure the following dependencies are installed to support diagram rendering:
1. **Python Playwright**: `pip install playwright`
2. **Browser Binaries**: `npx playwright install chromium`
3. **Internal Renderer**: This skill depends on the `excalidraw-diagram` skill's renderer located at `/Users/harrisonluo/.agents/skills/excalidraw-diagram/references/render_excalidraw.py`.

---

## 1. THE "HYPER-DEPTH" ANALYST MINDSET

### 1.1 The 30-Page Master Mandate
A brief summary is a failure. You are building an exhaustive legal and commercial case.
- **The Isomorphism Principle**: Diagrams must convey business logic through structure, not just labels.
- **The Traceability Rule**: Every claim MUST be backed by a link or raw finding file.
- **Fact-Dense Writing**: Omit fluff. Use metrics, specific library names, and exact pricing.
- **Exhaustive Extraction**: Use `web_fetch` on 10-20 sources per wave. **Snippets are insufficient.** You MUST extract full text to construct detailed feature breakdowns.
- **The Search-to-Fetch Ratio**: For every Turn that includes a `google_web_search`, you MUST execute a corresponding `web_fetch` Turn for the top 3-5 high-signal results.

### 1.2 The "Proxy Research" Principle
If direct information about a startup is scarce (e.g., stealth), you MUST research the **ecosystem proxies**:
- **Technology Proxies**: Research the benchmarks of the specific tools/frameworks they use.
- **Personnel Proxies**: Research the "Success Patterns" of the companies the founders came from.
- **Competitor Proxies**: Perform deep teardowns of incumbents to identify the *exact* "White Space" the startup is filling.

---

## 2. TABLE OF CONTENTS
1. [Phase 0: Workspace Architecture & Initialization](#3-phase-0-workspace-architecture--initialization)
2. [Phase 1: Objective-Oriented Recursive Search & Content Harvesting](#4-phase-1-objective-oriented-recursive-search--content-harvesting)
3. [Phase 2: MCP Service Discovery & Third-Party Intelligence](#5-phase-2-mcp-service-discovery--third-party-intelligence)
4. [Phase 3: The Founder Alpha & Team Audit](#6-phase-3-the-founder-alpha--team-audit)
5. [Phase 4: Technical Architecture & System Audit](#7-phase-4-technical-architecture--system-audit)
6. [Phase 5: Commercial, Financial & Unit Economic Diligence](#8-phase-5-commercial-financial--unit-economic-diligence)
7. [Phase 6: Market Dynamics, Competitive Moats & Exit Benchmarks](#9-phase-6-market-dynamics-competitive-moats--exit-benchmarks)
8. [Phase 7: The 2025-2026 AI Impact & Industry Trend Analysis](#10-phase-7-the-2025-2026-ai-impact--industry-trend-analysis)
9. [Phase 8: The Master VC Diligence Questionnaire (Exhaustive)](#11-phase-8-the-master-vc-diligence-questionnaire-exhaustive)
10. [Phase 9: Legal, Regulatory & Governance Risk Auditing](#12-phase-9-legal-regulatory--governance-risk-auditing)
11. [Phase 10: Visual Asset Acquisition & Content Richness](#13-phase-10-visual-asset-acquisition--content-richness)
12. [Phase 10.5: Formal Visual Design Specification](#135-phase-105-formal-visual-design-specification)
13. [Phase 11: Synthesis - Master Deliverables Protocol](#14-phase-11-synthesis---master-deliverables-protocol)
14. [Phase 11.5: The Iterative Master Expansion Step](#145-phase-115-the-iterative-master-expansion-step)
15. [Phase 12: Advanced Visual Argumentation & PNG Export](#15-phase-12-advanced-visual-argumentation--png-export)
16. [Phase 13: Formatting Audit (Tables vs. Bullets)](#16-phase-13-formatting-audit-tables-vs-bullets)
17. [Phase 14: Excalidraw JSON Protocol (The Two-Way Binding Rule)](#17-phase-14-excalidraw-json-protocol-the-two-way-binding-rule)
18. [Phase 15: CRITICAL JSON Safety & Syntax Protocol](#18-phase-15-critical-json-safety--syntax-protocol)
19. [Phase 16: Final Quality Assurance & Hand-off](#19-phase-16-final-quality-assurance--hand-off)

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
- **Discovery Specifics**: Feature inventory, user personas (Economic Buyer vs. Daily User), UX/Workflow mapping.

**Wave 1: Identity, Trajectory & Capital Structure**
- **Central Question**: "Who is this company, how much capital have they consumed, and what is their growth velocity?"
- **Targets**: SEC Form D, USPTO filings, historical job postings, and parent entity history.

**Wave 2: Founder Alpha & The "Narrative Thesis"**
- **Central Question**: "Why is this specific team uniquely qualified to win, and what is their unique 'Truth' about the world?"
- **Targets**: Every podcast, Substack post, university thesis, and "Social Graph" (advisors/former managers).

**Wave 3: Technical Architecture & Product Moat**
- **Central Question**: "Exactly how is this built, and is it a defensible moat or a thin wrapper?"
- **MANDATORY**: Use `web_fetch` on all technical docs found. Build a component-by-component feature teardown.

**Wave 4: Market Dynamics & Displacement Economics**
- **Central Question**: "Who is losing money because this startup exists, and what are the exit benchmarks?"
- **Synthesis Mandate**: Do NOT search for "TAM SAM SOM." Search for **Atomic Facts** (user counts, pricing proxies) and synthesize the conclusion.

### 4.2 The Search Critic & Intent SOP (Least-to-Most Protocol)
Before executing ANY query, the LLM MUST apply **Least-to-Most Prompting**:
1. **Decomposition**: "Break the Central Question down into the fundamental sub-questions that need to be answered first."
2. **Sequential Solving**: "Solve each sub-question one by one, using the answer from the previous step to inform the next search angle."
3. **The 'Reasonable Searchability' Check**: Search for the **atomic ingredients** instead of the **finished meal**.
4. **The Search-to-Fetch Mandate**: For every search, execute `web_fetch` on the top 3 high-signal results.

---

## 5. PHASE 1.5: THE CONTENT HARVESTING PROTOCOL (MANDATORY)

To achieve 30+ pages, you MUST harvest raw text volume.
1. **Source Volume**: Identify at least **5 primary sources** per wave.
2. **Exhaustive Fetching**: Use `web_fetch` to extract the *entire* text of high-signal pages.
3. **Structured Storage**: Store in `raw_findings/` with descriptive names.
4. **Synthesis Step**: Produce 0.5 pages of original analysis for every 1 page of raw findings.

---

## 6. PHASE 10.5: FORMAL VISUAL DESIGN SPECIFICATION (FACT-DENSE)

**Generic diagrams are a failure.** Before creating Excalidraw files, write a detailed spec.
- **Technical Diagram**: Map the data journey. Annotate boxes with technical purposes and dependency names. Show gated logic.
- **Market Diagram**: List incumbents/challengers. Annotate with market share/weakness. Show "Displacement Paths."
- **Growth Graphs**: Define X/Y axes. List exact metrics (ARR, Headcount) and annotate milestones.

---

## 7. PHASE 11: SYNTHESIS - THE MASTER DELIVERABLES PROTOCOL

### 7.1 `full_diligence_report.md` (The 30+ Page Truth File)
- **Header 1: Executive Summary** (3-paragraph distillation).
- **Header 2: Company Profile & Core Product** (Legal names, pivots, exhaustive feature list with sub-bullets).
- **Header 3: The Founder Alpha Audit** (Complete histories, social graphs, citations, and links).
- **Header 4: Financing & Capital Structure** (Round-by-round partners, valuations, board composition).
- **Header 5: Detailed Technical Architecture** (Plumbing, stack choices, bottlenecks).
- **Header 6: Market & Competitive Landscape** (TAM/SAM/SOM synthesis, incumbent weaknesses).
- **Header 7: Commercials & Unit Economics** (GTM strategy, LTV/CAC modeling, churn analysis).
- **Header 8: Legal, Regulatory & Governance** (IP provenance, compliance status).
- **Header 9: Master Research Appendix** (Categorized links and full source citations).
- **Header 10: Final Investment Verdict** (Detailed rationale explaining the "Why").

---

## 8. PHASE 11.5: THE ITERATIVE MASTER EXPANSION STEP (MANDATORY)

Once the initial draft of the `full_diligence_report.md` is complete, you MUST execute this iterative expansion cycle:

1.  **Phase 11.5.1: The Section-by-Section Elaborator**
    - Identify intimate details (specific quotes, internal project names, library versions) that were missed and inject them.
    - **Requirement**: Add at least 3-5 verbose paragraphs per major section.
2.  **Phase 11.5.2: Structural Depth & Nested Sub-Bulleting**
    - Convert flat lists into hierarchical structures with H3 and H4 sub-headings.
    - **Requirement**: Every high-level point must have at least 2 nested sub-bullets of detail.
3.  **Phase 11.5.3: The Global Citation Audit & Link Injection**
    - Every factual claim MUST be followed by a source link. 
    - **Requirement**: At least 3-5 external links per major section.
4.  **Phase 11.5.4: Research Density Check**
    - Tone must feel like a "Legal Brief." Replace all vague adjectives with specific metrics or technical reasons.

---

## 9. PHASE 14: EXCALIDRAW JSON PROTOCOL (THE TWO-WAY BINDING RULE)

To prevent "empty" diagrams, all text inside shapes MUST use the **Two-Way Binding Protocol**:

1.  **The Shape (Container)**: Must have a `boundElements` array listing the text element's ID.
2.  **The Text (Label)**: Must have a `containerId` pointing to the shape's ID.
3.  **Template Structure**:
```json
{
  "elements": [
    {
      "id": "rect-01",
      "type": "rectangle",
      "x": 100, "y": 100, "width": 250, "height": 100,
      "boundElements": [{ "id": "text-01", "type": "text" }]
    },
    {
      "id": "text-01",
      "type": "text",
      "containerId": "rect-01",
      "text": "Fact-Dense Description\nwith Metrics",
      "textAlign": "center", "verticalAlign": "middle",
      "x": 110, "y": 125, "width": 230, "height": 50
    }
  ]
}
```

---

## 10. FINAL QUALITY ASSURANCE & HAND-OFF

### 19.1 Hand-off
"Diligence for [Startup] is complete. Overview Memo, Deep Dive, and 30+ page Master Audit (with full feature teardowns and iterative expansion) are in `deliverables/`."

---
*End of VC Diligence Skill Masterclass V17.*
