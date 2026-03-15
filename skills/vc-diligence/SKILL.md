---
name: vc-diligence
description: An exhaustive, 1000-line enterprise-grade Venture Capital due diligence skill. Provides a massive, multi-stage workflow covering deep technical research, precise search methodologies, legal/commercial risk auditing, report synthesis, and advanced Excalidraw visual argumentation for any industry.
---

# VC Diligence Skill: The Ultimate Lead Partner Framework (V19 - Full Master Edition)

This is the definitive handbook for executing the `vc-diligence` skill. It combines **Recursive Hypothesis-Driven Discovery** with **Hyper-Depth Content Harvesting**, **Formal Visual Argumentation**, and **Iterative Report Expansion**. The goal is to produce an **intimate, 30+ page master audit** that identifies the technical plumbing, commercial moats, and legal red-flags of any startup.

## 0. PREREQUISITES & SETUP (CRITICAL)
Before executing this skill, ensure the following dependencies are installed to support diagram rendering:
1. **Python Playwright**: `pip install playwright`
2. **Browser Binaries**: `npx playwright install chromium`
3. **Internal Renderer**: This skill depends on the `excalidraw-diagram` skill's renderer located at `/Users/harrisonluo/.agents/skills/excalidraw-diagram/references/render_excalidraw.py`.
4. **Skill Delegation**: You MUST use the `excalidraw-diagram` skill to generate the actual diagrams, passing it your detailed specifications. Do not attempt to write the JSON manually in this workflow.

## 1. THE ANALYST MINDSET & PERSONA

### 1.1 The "Hyper-Depth" Mandate
A brief summary is a failure. You are building an exhaustive legal and commercial case for the deployment of millions of dollars.
- **The 30-Page Master Goal**: The final master audit should aim for 30+ pages of dense, factual analysis.
- **The Isomorphism Principle**: If you remove the text from your diagrams, the shapes must still convey the logic of the business. Diagrams must be fact-dense and follow the design specification strictly.
- **The Traceability Rule**: Every claim in the final memo must be traceable to a specific raw finding file or search result.
- **Fact-Dense Writing**: Omit adjectives like "innovative." Use metrics like "proprietary 16k-feature SAE layer" or "$30M ARR benchmark."
- **Exhaustive Extraction**: Use `web_fetch` on 10-20 sources per wave. **Snippets are insufficient.** You MUST extract the full text of high-signal pages (API docs, About pages, long-form interviews) to construct detailed feature breakdowns.
- **The Search-to-Fetch Ratio**: For every Turn that includes a `google_web_search`, you MUST execute a corresponding `web_fetch` Turn for the top 3-5 high-signal results. Surface-level search results are only the beginning; the actual diligence happens in the full-text analysis.

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

Do NOT use hard-coded queries. Every search MUST be driven by a **Central Question** and an **Internal Hypothesis**. The LLM has full autonomy to craft queries that maximize signal-to-noise for the specific context.

### 4.1 The Wave-Based Discovery Objectives (Hyper-Depth)

**Wave 0: Product DNA & User Persona (The Foundation)**
- **Central Question**: "What exactly is the product, how does it function for the end-user, and who are the core personas it serves?"
- **The Guiding Mandate**: This wave is the most critical as it defines the scope of all subsequent waves. You MUST understand the 'Jobs to be Done' before you can audit the 'Right to Win'.
- **Discovery Specifics**:
    - **Feature Inventory**: List every distinct product feature and its primary utility.
    - **User Personas**: Identify the 'Daily User', the 'Economic Buyer', and the 'Affected Stakeholder'.
    - **UX/Workflow Mapping**: How does the user interact with the product? (e.g., API vs. Web UI vs. Browser Extension).
    - **Value Proposition**: What is the core pain point being solved (e.g., Time savings, Revenue generation, Risk mitigation)?
- **Example Evidence**: A 'How it Works' page; a user manual; onboarding tutorials; detailed customer testimonials describing specific use cases.

**Wave 1: Identity, Trajectory & Capital Structure**
- **Central Question**: "Who is this company at its core, how much capital have they consumed, and what is their growth velocity?"
- **Discovery Specifics**:
    - **Legal Structure**: Identify the parent entity.
    - **Cap Table Proxies**: Hunt for funding announcements. Cross-reference SEC Form D filings.
    - **Hiring Velocity**: Search for "LinkedIn Headcount Growth" patterns or historical job postings.
- **Example Evidence**: A Press Release confirming a $5M Seed round; a Crunchbase entry showing 18 months between rounds.

**Wave 2: Founder Alpha & Talent Density**
- **Central Question**: "Why is this specific team uniquely qualified to win this category, and what are their individual 'superpowers'?"
- **Discovery Specifics**:
    - **The 'Spike'**: Identify the one thing each founder is world-class at.
    - **Social Capital**: Search for testimonials, board seats, or speaking engagements.
    - **Conflict/Cohesion**: Find evidence of past collaboration.
- **Example Evidence**: A Google Scholar profile showing 500+ citations; a LinkedIn recommendation from a former CEO.

**Wave 3: Technical Architecture & Product Moat**
- **Central Question**: "Exactly how is this built, where are the structural bottlenecks, and is it a defensible moat or a thin wrapper?"
- **MANDATORY**: Use `web_fetch` on all technical docs, API references, and engineering blogs found.
- **Discovery Specifics**:
    - **Infrastructure Stack**: Identify the 'Plumbing' (AWS/GCP, DBs, LLMs).
    - **Proprietary IP**: Search for specific internal project names or custom protocols.
    - **Performance Benchmarks**: Hunt for latency, throughput, or accuracy metrics.
- **Example Evidence**: An API reference describing a custom auth layer; a developer's GitHub repo.

**Wave 4: Market Dynamics & Competitive Displacement**
- **Central Question**: "Which $B+ market is being eaten, who are the incumbents being displaced, and what are the exit benchmarks for this category?"
- **The Synthesis Mandate**: Do NOT search for high-level conclusions like `"[Startup] TAM SAM SOM"`. Google does not have these answers. Instead, search for **Atomic Facts**:
    - **Market Size Proxies**: Search for "Total addressable market of [Industry Sector]" or "Total number of [Target User Profile]".
    - **Pricing Proxies**: Search for "[Competitor] pricing" or "[Incumbent] revenue per user".
    - **Adoption Proxies**: Search for "[Competitor] customer count".
- **Hypothesis-First (MANDATORY)**: Based on Waves 1-3, define the *disrupted market* and name the *likely incumbents* and *emerging challengers*.
- **Discovery Specifics**:
    - **Incumbent Vulnerability**: Search for "Negative Reviews" or "Integrations Issues" with incumbents.
    - **Category Pricing**: Hunt for competitor pricing pages or 'Talk to Sales' leakages.
    - **Exit Comps**: Find 3-5 recent M&A deals in the sector.

### 4.2 Query Fanout Mandate
For every Central Question or Hypothesis, you MUST generate a **fanout of 3-5 distinct, multi-angle queries**. Relying on a single search is a failure of diligence.
- **Angle 1: Direct Discovery**: (e.g., `\"[Startup] [Topic]\"`)
- **Angle 2: Proxy Signals**: Search for indirect evidence (e.g., `\"[Topic] reviews\"`, `"hiring for [Topic]"`, or customer complaints).
- **Angle 3: Technical/Source-Specific**: Target deep sources (`site:github.com`, `filetype:pdf`).
- **Angle 4: Competitive/Market Context**: (e.g., `\"[Startup] vs [Competitor]\"`).

### 4.3 The Search Critic & Intent SOP (Least-to-Most Protocol)
Before executing ANY query, the LLM MUST apply **Least-to-Most Prompting**:
1. **Decomposition**: "Break the Central Question down into the fundamental sub-questions that need to be answered first."
2. **Sequential Solving**: "Solve each sub-question one by one, using the answer from the previous step to inform the next search angle."
3. **The 'Reasonable Searchability' Check**: Search for the **atomic ingredients** instead of the **finished meal**.
4. **The Search-to-Fetch Mandate**: For each query fanout, identify the top high-signal URLs and execute `web_fetch`. Do not proceed to the next sub-question or wave until you have the full-text content of the primary sources.
5. **Synthesis**: Construct a generalized argument that addresses the original Central Question.

### 4.4 The Content Harvesting Protocol (MANDATORY)
To achieve 30+ pages, you MUST harvest raw text volume.
1. **Source Identification**: Identify 5-10 authoritative URLs per wave.
2. **Exhaustive Fetching**: Use `web_fetch` to extract **full text content**. This is critical for detailed product feature breakdowns.
3. **Structured Storage**: Store in `raw_findings/` with descriptive names.
4. **Synthesis Step**: Produce 0.5 pages of original analysis for every 1 page of raw findings.

### 4.5 The Recursive Loop SOP
After each wave, perform an **Evidence Audit**:
1. **Identify Weak Spots**: "I found the product features but I don't know the underlying model provider."
2. **Trigger Wave 5+**: Perform targeted searches for the missing detail.
3. **Exhaustion Rule**: If info is not found after 3 loops, document it as a **🔴 CRITICAL Evidence Gap**.

---

## 5. PHASE 2: MCP SERVICE DISCOVERY & THIRD-PARTY INTELLIGENCE

Before concluding research, check for **MCP** tools (e.g., `crunchbase-tool`).
- **Prompt**: "List all available MCP tools related to company data or financial metrics."
- **Execution**: If found, use them to pull ARR, headcount growth, and cap table data.

---

## 6. PHASE 3: THE FOUNDER ALPHA & TEAM AUDIT

### 6.1 Pedigree & "Right to Win"
- **Talent Spikes**: Identify the one thing each founder is world-class at. Does the team have "Bridge Talent" (experts in two distinct fields)?
- **Grit Signals**: Check for first-gen students, early failures, or competitive history.
- **Audit Step**: Cross-reference LinkedIn tenure with funding milestones.

---

## 7. PHASE 4: TECHNICAL ARCHITECTURE & SYSTEM AUDIT (FEATURE TEARDOWN)

### 7.1 The "Wrapper vs. Moat" Test
- **Engine**: Generic API calls vs. fine-tuned proprietary models.
- **Integration**: Is it a "Bolt-on" or "Embedded Workflow"?
- **Data Provenance**: Who owns the training data? Is it legally defensible?
- **Feature Teardown**: Using the text harvested in Phase 1.5, list every distinct product feature and identify its technical dependency (e.g., "Uses Pinecone for L2 Vector Search").

---

## 8. PHASE 5: COMMERCIAL, FINANCIAL & UNIT ECONOMIC DILIGENCE

Move beyond "searching" into **Economic Modeling**.

### 8.1 The Unit Economic Audit SOP
1. **Inference Cost Modeling**: Estimate the GPU/Token cost of one user interaction vs. subscription price.
2. **GTM Strategy Mapping**: Map out the sales motion (PLG, Enterprise Sales, etc).
3. **LTV/CAC Calculation**: Use industry benchmarks to predict sustainability.
4. **Churn Signal Hunting**: Actively search for "Negative Social Proof" in forums or review sites.

---

## 9. PHASE 6: MARKET DYNAMICS, COMPETITIVE MOATS & EXIT BENCHMARKS

Construct a **Competitive Moat Matrix**.

### 9.1 Market & Benchmarking SOP
1. **The "Slow Giant" Audit**: Identify 3-5 legacy incumbents. Analyze their latest quarterly earnings (10-K/10-Q).
2. **The "Emerging Challenger" Audit**: Find "stealth" or "seed" competitors in niche newsletters.
3. **Exit Multiple Benchmarking**: Find 3-5 recent acquisitions or IPOs. Calculate the Revenue/ARR multiple paid.
4. **The Moat Test**: Rate the startup on 4 pillars: Network Effects, Switching Costs, Cost Advantage, and Intangible Assets.

---

## 10. PHASE 7: THE 2025-2026 AI IMPACT & INDUSTRY TREND ANALYSIS

Analyze the startup's survival through the **"AI Platform Shift."**

### 10.1 Trend Analysis SOP
1. **Agentic Readiness**: Does the API allow for autonomous agents to interact (MCP readiness)?
2. **Sovereignty Check**: Can it be deployed on-premise or in sovereign cloud regions?
3. **Efficiency Frontier**: Are they using "Small Models" (SLMs) or distillation?
4. **Platform Risk**: The "Sherlocking" Test (OpenAI/Microsoft risk).

---

## 11. PHASE 8: THE MASTER VC DILIGENCE QUESTIONNAIRE (EXHAUSTIVE)

Generate a custom list of **25-50 High-Conviction Questions**.

### 11.1 Master Question Pool by Category (Selection)
- **Technology**: Hallucination management, model-agnosticism, fine-tuning vs. wrappers.
- **Product**: Economic Buyer vs. Daily User, Time to Value (TTV), integration depth.
- **Commercial**: Marginal cost per query, GTM wedge, NRR targets.
- **Team**: Bridge talent, conflict resolution history, biggest technical failure.
- **Legal**: IP ownership, Fair Use posture, jurisdictional compliance.

---

## 12. PHASE 9: LEGAL, REGULATORY & GOVERNANCE RISK AUDITING

Conduct a **Legal & Regulatory Red-Flag Audit**.

### 12.1 Legal Diligence SOP
1. **IP Provenance Audit**: Search for patent filings or university IP agreements.
2. **Data Privacy Posture**: Check GDPR/CCPA compliance and SOC 2/ISO certifications.
3. **Compliance Risk**: In regulated industries, audit licensing status.
4. **Governance Review**: Check Board composition and 83(b) election mentions.

---

## 13. PHASE 10: VISUAL ASSET ACQUISITION & CONTENT RICHNESS

Acquire, **download**, and embed high-quality visual assets.

### 13.1 Asset Acquisition SOP
- **Download Command**: Use `curl -Lfg -o assets/[filename].ext "[URL]"`
- **Verification Loop**: 
    1. **Check Type**: Run `file assets/[filename].ext`. Success = "image data". Failure = "HTML".
    2. **Check Size**: Run `ls -lh`. If < 5KB, find a higher resolution asset.

---

## 13.5 PHASE 10.5: FORMAL VISUAL DESIGN SPECIFICATION (RICH VISUALS)

Before creating Excalidraw diagrams, write a **Visual Design Specification** that formalizes the "Visual Argument." **Empty or generic diagrams are a failure.**

### 13.5.1 The Market Diagram Spec
- **Rich Nodes**: List incumbents and challengers. Annotate with market share or key weakness.
- **Segments**: Categorize into logical layers (e.g., "Legacy," "Real-time," "Data Licensing").
- **Arrows**: Describe the "Displacement Path."

### 13.5.2 The Technical Architecture Spec
- **Detailed Flow**: Map the data journey through every hierarchical layer.
- **Annotated Components**: Every box must contain technical purpose and dependency name.
- **Gated Logic**: Describe "Early Exit" or "Escalation" conditions.

### 13.5.3 Relevant Graphs & Data Visuals
- **Data Points**: List exact metrics found (ARR, headcount).
- **Annotated Axes**: Define axes and include labels for specific milestones.

---

## 14. PHASE 11: SYNTHESIS - THE MASTER DELIVERABLES PROTOCOL

You MUST generate THREE primary documents. **Detailed, verbose reporting is mandatory.**

### 14.1 `overview_memo.md` (The Partner Summary)
- **Length**: 2-3 pages.
- **Visuals**: Logo in header, 1-2 core PNG diagrams.

### 14.2 `technical_commercial_deep_dive.md` (The 15+ Page Master Audit)
- **Length**: 15-20 pages (exhaustive).
- **Sections Required**: Founder Deep Audit, Architectural Teardown, Visual Design Spec (Annotated), Economic Modeling, Market Map, Risk Assessment, Master Questionnaire.

### 14.3 `full_diligence_report.md` (The Comprehensive Master Audit)
- **Length**: 30+ pages.
- **Purpose**: A complete "Truth File" dump and synthesis of everything retrieved.
- **Structure Requirements**:
    - **Header 1: Executive Summary** (3-paragraph distillation).
    - **Header 2: Company Profile & Core Product** (Legal names, pivots, exhaustive feature list with sub-bullets).
    - **Header 3: The Founder Alpha Audit** (Complete histories, social graphs, citations, and links).
    - **Header 4: Financing & Capital Structure** (Round-by-round partners, valuations, board composition).
    - **Header 5: Detailed Technical Architecture** (Plumbing, stack choices, bottlenecks, "Wrapper vs. Moat" test).
    - **Header 6: Market & Competitive Landscape** (TAM/SAM/SOM synthesis, incumbent weaknesses, displacement economics table).
    - **Header 7: Commercials & Unit Economics** (GTM strategy, LTV/CAC modeling, churn analysis).
    - **Header 8: Legal, Regulatory & Governance** (IP provenance, GDPR/FERPA status, material risk assessment).
    - **Header 9: Master Research Appendix** (Categorized links and full source citations).
    - **Header 10: Final Investment Verdict** (Detailed rationale explaining the "Why").

---

## 14.5 PHASE 11.5: THE ITERATIVE MASTER EXPANSION STEP (MANDATORY)

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

## 15. PHASE 12: ADVANCED VISUAL ARGUMENTATION (SKILL DELEGATION)

**CRITICAL MANDATE**: Do NOT attempt to generate Excalidraw JSON manually. The syntax for nested binding and routing is highly complex and error-prone. 

You MUST use the `activate_skill` tool to invoke the `excalidraw-diagram` skill. 

### 15.1 The Delegation Protocol
1. **Compile the Context**: Take the detailed `Visual Design Specification` you generated in Phase 10.5.
2. **Invoke the Skill**: Inform the user you are generating the diagrams using the `excalidraw-diagram` skill, and ask the user to provide the `Visual Design Specification` to that skill as its prompt. 
    - *Example Prompt to User*: "I have completed the Visual Design Specification. I will now use the `excalidraw-diagram` skill to generate the actual visual assets. Here is the specification I will pass to it..."
3. **Execution**: The `excalidraw-diagram` skill has specific logic for two-way container binding, arrow routing, and color themes that will ensure the diagrams are fact-dense and visually appealing.
4. **Rendering**: After the `excalidraw-diagram` skill generates the `.excalidraw` files in the `diagrams/` folder, use the internal renderer to convert them to PNGs:
   - **Command**: `python3 ~/.agents/skills/excalidraw-diagram/references/render_excalidraw.py diligence_[startup_name]/diagrams/[filename].excalidraw`

---

## 16. PHASE 13: FORMATTING AUDIT (TABLES VS. BULLETS)

Before finalizing, perform a structural audit to maximize readability:
1. **The Table Test**: If comparing 3+ items across 2+ attributes (e.g., Competitors, Unit Economics), use a **Table**.
2. **The Bullet Test**: Use bullets ONLY for chronological events or simple lists.
3. **Richness Check**: Ensure at least 40% of the report is paragraph-driven analysis.

---

## 17. PHASE 14: FINAL QUALITY ASSURANCE & HAND-OFF

### 19.1 Hand-off
"Diligence for [Startup] is complete. 
Overview Memo, Deep Dive, and 30+ page Master Audit (with full feature teardowns, iteratively expanded details, and specialized visual diagrams) are in `deliverables/`."

---
*End of VC Diligence Skill Masterclass V19.*
