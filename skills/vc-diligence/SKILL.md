---
name: vc-diligence
description: An exhaustive, 1000-line enterprise-grade Venture Capital due diligence skill. Provides a massive, multi-stage workflow covering deep technical research, precise search methodologies, legal/commercial risk auditing, report synthesis, and advanced Excalidraw visual argumentation for any industry.
---

# VC Diligence Skill: The Ultimate Lead Partner Framework (V6 - Hyper-Depth & Visual Specification Edition)

This is the definitive handbook for executing the `vc-diligence` skill. It combines **Recursive Hypothesis-Driven Discovery** with **Hyper-Depth Content Harvesting** and **Formal Visual Argumentation**. The goal is to produce an **intimate, 15+ page audit** that identifies the technical plumbing, commercial moats, and legal red-flags of any startup.

## 0. PREREQUISITES & SETUP (CRITICAL)
Before executing this skill, ensure the following dependencies are installed to support diagram rendering:
1. **Python Playwright**: `pip install playwright`
2. **Browser Binaries**: `npx playwright install chromium`
3. **Internal Renderer**: This skill depends on the `excalidraw-diagram` skill's renderer located at `/Users/harrisonluo/.agents/skills/excalidraw-diagram/references/render_excalidraw.py`.

## 1. THE "HYPER-DEPTH" ANALYST MINDSET

### 1.1 The 15-Page Mandate
A 3-page summary is a failure. You are building a legal and commercial case for the deployment of millions of dollars.
- **The Isomorphism Principle**: If you remove the text from your diagrams, the shapes must still convey the logic of the business.
- **The Traceability Rule**: Every claim in the final memo must be traceable to a specific raw finding file or search result.
- **Fact-Dense Writing**: Omit adjectives like "innovative." Use metrics like "proprietary 16k-feature SAE layer" or "$30M ARR benchmark."
- **Exhaustive Extraction**: Use `web_fetch` on 10-20 sources per wave. Do not rely on snippets.

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
13. [Phase 11: Synthesis - Dual Deliverable Protocol (Detailed Reporting)](#14-phase-11-synthesis---dual-deliverable-protocol-detailed-reporting)
14. [Phase 12: Advanced Visual Argumentation & PNG Export](#15-phase-12-advanced-visual-argumentation--png-export)
15. [Phase 13: Formatting Audit (Tables vs. Bullets)](#16-phase-13-formatting-audit-tables-vs-bullets)
16. [Phase 14: Excalidraw Master Templates](#17-phase-14-excalidraw-master-templates)
17. [Phase 15: CRITICAL JSON Safety & Syntax Protocol](#18-phase-15-critical-json-safety--syntax-protocol)
18. [Phase 16: Final Quality Assurance & Hand-off](#19-phase-16-final-quality-assurance--hand-off)

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

Do NOT use hard-coded queries. Every search MUST be driven by a **Hypothesis-First Fanout**. You must generate 3-5 multi-angle queries for every objective.

### 4.1 The Wave-Based Discovery Objectives (Hyper-Depth)

**Wave 1: Identity, Trajectory & Capital Structure**
- **Central Question**: "Who is this company at its core, how much capital have they consumed, and what is their growth velocity?"
- **Hypothesis**: Predict funding stage, lead investors, and parent entity history.
- **Intimate Targets**: 
    - Parent entity history (all DBAs and former names).
    - SEC Form D, USPTO filings, and Trademark applications.
    - Historical job postings (use Wayback Machine if possible) to see when specific departments (e.g., "AI Safety Team") were formed.
- **Example Evidence**: A Press Release confirming a $5M Seed round; a Crunchbase entry showing 18 months between rounds (signal of capital efficiency).

**Wave 2: Founder Alpha & The "Narrative Thesis"**
- **Central Question**: "Why is this specific team uniquely qualified to win this category, and what are their individual 'superpowers'?"
- **Hypothesis**: Predict founder backgrounds, academic pedigree, and former professional "Success Patterns."
- **Intimate Targets**: 
    - Every podcast appearance, Substack post, and university thesis.
    - Founder "Social Graph": Who are their key advisors and former managers?
    - Academic "Pedigree": Research the specific labs and professors they worked under.
- **Example Evidence**: A Google Scholar profile showing 500+ citations; a LinkedIn recommendation from a former CEO stating the founder was a "top 1% talent."

**Wave 3: Technical Architecture & Product Moat**
- **Central Question**: "Exactly how is this built, where are the structural bottlenecks, and is it a defensible moat or a thin wrapper?"
- **Hypothesis**: Predict the tech stack (RAG, SAE, Vector DB), data provenance, and critical system constraints.
- **Intimate Targets**: 
    - Specific LLM providers, Vector DB choices, and custom orchestration layers.
    - API endpoint naming conventions (leakage of internal logic).
    - GitHub "Dependency Audit": Find the open-source projects they contribute to or depend on.
- **Example Evidence**: An API reference describing a custom auth layer; a developer's GitHub repo showing contributions to an open-source library.

**Wave 4: Market Dynamics & Competitive Displacement**
- **Hypothesis-First (MANDATORY)**: Based on Waves 1-3, define the *disrupted market* and name the *likely incumbents* (Slow Giants) and *emerging challengers*.
- **Central Question**: "Which $B+ market is being eaten, who are the incumbents being displaced, and what are the exit benchmarks for this category?"
- **Intimate Targets**: 
    - Competitor pricing "Leakage" (found in RFP responses or government procurement docs).
    - "Negative Social Proof": Search for Reddit/Discord threads where users complain about incumbents.
    - Exit Multiple Teardowns: Calculate the *Revenue per Employee* of competitors to benchmark efficiency.
- **Example Evidence**: A Forrester Wave report showing the incumbent's market share is declining; an M&A deal at a 12x revenue multiple.

### 4.2 Query Fanout Mandate
For every Central Question or Hypothesis, you MUST generate a **fanout of 3-5 distinct, multi-angle queries**. Relying on a single search is a failure of diligence.
- **Angle 1: Direct Discovery**: (e.g., `"[Startup] [Topic]"`)
- **Angle 2: Proxy Signals**: Search for indirect evidence (e.g., `"[Topic] reviews"`, `"hiring for [Topic]"`, or customer complaints).
- **Angle 3: Technical/Source-Specific**: Target deep sources (e.g., `site:github.com`, `filetype:pdf`, or `site:docs.[startup].io`).
- **Angle 4: Competitive/Market Context**: (e.g., `"[Startup] vs [Competitor]"`, or incumbent quarterly reports).

### 4.3 The Search Critic & Intent SOP
Before executing ANY query, the LLM MUST think:
1. **The Objective**: "What specific piece of evidence am I missing to answer the Central Question of this wave?"
2. **The Fanout Plan**: "What are my 3-5 distinct angles for this objective?"
3. **The Query Selection**: "Does each query use high-signal keywords and operators (site:, filetype:, -inurl:)?"
4. **The 'Google Assumption' Check**: "Am I assuming Google has a direct answer? If not, how do I search for 'proxies' of this info?"

### 4.4 The Content Harvesting Protocol (MANDATORY)
To achieve 15+ pages, you MUST harvest raw text volume.
1. **Source Volume**: For every wave, identify at least **5 primary sources** (not just news snippets).
2. **Web Extraction**: Use `web_fetch` to extract the *entire* text of About pages, Technical Documentation, Whitepapers, and long-form interviews.
3. **Structured Storage**: Store these in `raw_findings/` with descriptive names (e.g., `wave3_api_docs_teardown.md`).
4. **Synthesis Step**: For every 1 page of raw findings, you should produce **0.5 pages of original analysis**.

### 4.5 The Recursive Loop SOP
After each wave, you MUST perform an **Evidence Audit**:
1. **Identify Weak Spots**: "I found the product features but I don't know the underlying model provider."
2. **Trigger Wave 5+**: Perform 3-5 more targeted searches specifically for the missing detail using Query Expansion.
3. **Exhaustion Rule**: If information cannot be found after 3 recursive loops, document it as a **🔴 CRITICAL Evidence Gap**.

---

## 5. PHASE 2: MCP SERVICE DISCOVERY & THIRD-PARTY INTELLIGENCE

Before concluding research, check if any **Model Context Protocol (MCP)** tools are available that provide specialized startup data (e.g., `crunchbase-tool`, `startup-intel-api`).
- **Prompt**: "List all available MCP tools related to company data or financial metrics."
- **Execution**: If found, use these tools to pull ARR, headcount growth, and cap table data.

---

## 6. PHASE 3: THE FOUNDER ALPHA & TEAM AUDIT

### 6.1 Pedigree & "Right to Win"
- **Talent Spikes**: Identify the one thing each founder is world-class at. Does the team have "Bridge Talent" (experts in two distinct fields)?
- **Grit Signals**: Check for first-gen students, competitive history, or early failures.
- **Audit Step**: Cross-reference LinkedIn tenure with funding milestones. Did the founders stay through the hard times?

---

## 7. PHASE 4: TECHNICAL ARCHITECTURE & SYSTEM AUDIT

### 7.1 The "Wrapper vs. Moat" Test
- **Engine**: Generic API calls vs. fine-tuned proprietary models.
- **Integration**: Is it a "Bolt-on" or "Embedded Workflow"?
- **Data Provenance**: Who owns the training data? Is it legally defensible?
- **SOP**: Use `read_file` on API docs or whitepapers to identify proprietary logic vs. standard libraries.

---

## 8. PHASE 5: COMMERCIAL, FINANCIAL & UNIT ECONOMIC DILIGENCE

You MUST move beyond "searching" for metrics and move into **Economic Modeling**.

### 8.1 The Unit Economic Audit SOP
1. **Inference Cost Modeling**: Based on the technical architecture (Phase 4), estimate the cost of one user interaction (GPU/Token cost).
    - *Example*: For a Gen-AI video startup, model the cost per minute of video generated against the subscription price ($29/mo). If GPU cost is $2/min and average user generates 20 mins, unit economics are negative ($40 cost vs $29 revenue).
2. **GTM Strategy Mapping**: Map out the sales motion. Is it PLG (Product-Led Growth), Enterprise Sales, or Channel-Partnership based?
3. **LTV/CAC Calculation**: Use industry benchmarks for the category (e.g., SaaS, Fintech) to predict if the current GTM is sustainable.
4. **Churn Signal Hunting**: Actively search for "Negative Social Proof" in developer forums, Reddit, or review sites to identify retention risks.

---

## 9. PHASE 6: MARKET DYNAMICS, COMPETITIVE MOATS & EXIT BENCHMARKS

You MUST construct a **Competitive Moat Matrix** that goes beyond simple feature lists.

### 9.1 Market & Benchmarking SOP
1. **The "Slow Giant" Audit**: Identify 3-5 legacy incumbents. Analyze their latest quarterly earnings (10-K/10-Q) to see if they are building competing AI capabilities.
    - *Example*: In 'AI for Customer Support', identify Zendesk and Salesforce as 'Slow Giants'. Search their recent acquisitions (e.g., Zendesk acquiring Klaus) to set exit benchmarks.
2. **The "Emerging Challenger" Audit**: Use `google_web_search` to find "stealth" or "seed" competitors mentioned in niche newsletters (e.g., The Information, Axios Pro).
3. **Exit Multiple Benchmarking**: Find 3-5 recent acquisitions or IPOs in the sector. Calculate the Revenue/ARR multiple paid.
4. **The Moat Test**: Rate the startup on 4 pillars: Network Effects, Switching Costs, Cost Advantage, and Intangible Assets (Patents/Brand).

---

## 10. PHASE 7: THE 2025-2026 AI IMPACT & INDUSTRY TREND ANALYSIS

Analyze the startup's survival through the **"AI Platform Shift."**

### 10.1 Trend Analysis SOP
1. **Agentic Readiness**: Does the startup's API allow for autonomous agents to interact with it (MCP readiness)?
2. **Sovereignty Check**: Can the product be deployed on-premise or in sovereign cloud regions (e.g., for EU/Healthcare)?
3. **Efficiency Frontier**: Are they using "Small Models" (SLMs) or distillation to improve margins vs. competitors using large LLMs?
4. **Platform Risk**: If OpenAI/Microsoft added this feature today, would the startup die? (The "Sherlocking" Test).
    - *Example*: For a medical coding startup, evaluate if Epic (EHR giant) is releasing an internal medical coding agent. If Epic's 'Ambient AI' covers 80% of features, risk is 🔴 CRITICAL.

---

## 11. PHASE 8: THE MASTER VC DILIGENCE QUESTIONNAIRE (EXHAUSTIVE)

Generate a custom list of **25-50 High-Conviction Questions** for the founders. The LLM MUST select the most relevant questions from the pools below based on the startup's specific industry and stage.

### 11.1 Master Question Pool by Category

**Category A: Technology & AI Moat**
1. "What is your proprietary data advantage? Is the data unique, or is it public data with a unique cleaning/labeling process?"
2. "How do you handle 'hallucinations' in a production environment where accuracy is 🔴 CRITICAL (e.g., legal, medical)?"
3. "Are you fine-tuning your own models, or are you essentially a sophisticated wrapper around OpenAI/Anthropic?"
4. "What is your strategy for model-agnosticism? How easily can you switch providers if pricing or performance changes?"
5. "Do you have token-level or query-level usage tracking for attribution and monetization?"

**Category B: Product & Market Fit**
1. "Who is the 'Economic Buyer' vs. the 'Daily User'? How do you bridge the gap between user delight and buyer ROI?"
2. "What is the 'Time to Value' (TTV) for a new enterprise customer? How much manual 'implementation' or 'consulting' is required?"
3. "Is this a 'Nice to Have' (efficiency gain) or a 'Must Have' (revenue generation or compliance necessity)?"
4. "How does your product integrate with existing legacy workflows (e.g., SAP, Salesforce, Epic)?"
5. "What is the 'Magic Moment' for a user where they realize this product is indispensable?"

**Category C: Commercial & Unit Economics**
1. "Walk us through the marginal cost of one user query. What is the GPU/Token burn as you scale?"
2. "What is your GTM 'Wedge'? How do you get into an organization, and what is the 'Expansion' path?"
3. "What are your net revenue retention (NRR) targets? How do you defend against churn from 'AI experimentation' budgets?"
4. "Is your pricing model aligned with user value (e.g., per-outcome) or just seat-based (per-user)?"
5. "Who are your top 3 'Loss-Leader' competitors who might use predatory pricing to gain market share?"

**Category D: Team & Culture**
1. "What is the 'Bridge Talent' in this team? (e.g., 10 years in Publishing + 5 years in AI)."
2. "How did the founders meet, and what is the 'Conflict Resolution' history?"
3. "What is the single biggest technical or commercial failure the team has navigated in the last 12 months?"
4. "How do you attract 'A-tier' AI talent in a market where BigTech can pay $500k+ salaries?"
5. "Who is the 'Philosophical Anchor' on the team ensuring the product remains ethical/compliant?"

**Category E: Legal, Regulatory & IP**
1. "Do you have clear ownership of all IP developed during the pre-seed/academic phase?"
2. "What is your posture on 'Fair Use' vs. 'Licensed Access' for your training/inference data?"
3. "In which jurisdictions are you currently compliant (GDPR, CCPA, HIPAA)?"
4. "Are there any 'Hidden Liens' or 'University IP Overhangs' from previous research work?"
5. "What happens to the user's data? Is it used to train your models, or is it kept in a sovereign silo?"

### 11.2 Questionnaire Generation SOP
1. **Selection**: Pick 15-20 questions from the pool above that match the startup's current wave findings.
2. **Contextualize**: Reference specific findings (e.g., "Given your reliance on [Provider X], how do you mitigate...").
3. **The "Killer" Questions**: Focus on the 3 biggest risks identified in your research.

---

## 12. PHASE 9: LEGAL, REGULATORY & GOVERNANCE RISK AUDITING

Conduct a **Legal & Regulatory Red-Flag Audit**.

### 12.1 Legal Diligence SOP
1. **IP Provenance Audit**: Search for patent filings or university IP agreements. Identify if the tech was developed during a PhD or at a previous employer.
2. **Data Privacy Posture**: Check for GDPR/CCPA compliance in the privacy policy. Search for SOC 2 or ISO 27001 certifications.
3. **Compliance Risk**: In regulated industries (Fintech/Health), audit their licensing status.
    - *Example*: For a UK Fintech, verify if they hold an EMI license or rely on a third-party 'BaaS' provider. If the provider is Railsr (known issues), risk is 🟠 MATERIAL.
4. **Governance Review**: Check for Board composition and 83(b) election mentions.

---

## 13. PHASE 10: VISUAL ASSET ACQUISITION & CONTENT RICHNESS

To make reports content-rich and professional, you MUST acquire, **download**, and embed high-quality visual assets.

### 13.1 Broad Asset Search Strategy
Keep queries high-level to maximize official results.
- **Company Logo**: Search `"[Company Name]" logo png transparent` or `"[Company Name]" press kit logo`.
- **Founder Headshots**: Use ultra-short queries: `"[Founder Name]" [Company Name]`. This is usually sufficient to yield direct bios or LinkedIn-anchored images.
- **Simple Queries**: Do NOT use complex operators for initial image discovery. Focus on finding official "About" or "Press" pages.

### 13.2 Asset Discovery & Direct URL Extraction
Any valid image format is acceptable (PNG, JPG, JPEG, WebP, SVG).
- **Metadata Scraping**: Use `web_fetch` or `curl` to inspect the HTML for `application/ld+json` blocks, which often contain direct URLs for logos and person headshots.
- **Grep Pattern**: Grep for `img src`, `og:image`, or `twitter:image` tags.
- **Absolute URLs**: Ensure the URL is absolute. If relative, prepend the base domain.

### 13.3 Asset Downloading & Verification SOP
Every asset MUST be verified to ensure it is a valid image and NOT an HTML "Not Found" or "Redirect" page.
- **Download Command**: Use `curl -Lfg -o assets/[filename].ext "[URL]"`
    - `-L`: Follow redirects.
    - `-f`: Fail silently on server errors (HTTP 4xx/5xx).
    - `-g`: Disable globbing for URLs with brackets.
- **Verification Loop**:
    1. **Check Type**: IMMEDIATELY run `file assets/[filename].ext`.
        - **Success**: Output contains "image data" or "SVG".
        - **Failure**: Output contains "HTML" or "ASCII text". This indicates the URL was a webpage or a failed redirect. **DO NOT** proceed with this file; find a different direct URL.
    2. **Check Size**: Run `ls -lh assets/[filename].ext`. If the file is < 5KB, it is likely a tracking pixel or placeholder. Seek a higher resolution asset.
- **Naming**: Use descriptive names (e.g., `logo.png`, `tian_headshot.jpg`).

### 13.4 Richness Mandate
- **Logos**: Embed the local logo at the top of every primary deliverable.
- **Team Photos**: Embed local headshots in the "Founder Alpha" section.
- **Hyperlinks**: Use descriptive hyperlinks for all external sources.

---

## 13.5 PHASE 10.5: FORMAL VISUAL DESIGN SPECIFICATION

Before creating Excalidraw diagrams, the LLM MUST write a **Visual Design Specification** that formalizes the "Visual Argument." This ensures that the diagrams are not generic but are built using the intimate details harvested in earlier phases.

### 13.5.1 The Market Diagram Spec
Define exactly what the market map looks like:
- **Nodes**: List every incumbent (Slow Giant) and emerging challenger found in research.
- **Segments**: Categorize the market into logical layers (e.g., "Legacy Verification," "Real-time Authorship," "Data Licensing").
- **Moats**: Specify which moat pillars (4 Pillars) apply to each segment.
- **Arrows**: Describe the "Displacement Path"—how the startup is eating the incumbent's market share.

### 13.5.2 The Technical Architecture Spec
Define the "Component-by-Component" teardown:
- **Flow**: Map the data journey from "Input Content" through every hierarchical layer found in research.
- **Gated Logic**: Describe the "Early Exit" or "Escalation" conditions between model layers (e.g., statistical vs. transformer).
- **Constraints**: Annotate where the bottlenecks (latency, cost) exist based on documentation.
- **Proprietary Moats**: Bold the components that are custom-built vs. off-the-shelf.

### 13.5.3 Relevant Graphs & Data Visuals
Specify any remaining relevant graphs that would make good diagrams (e.g., Growth Trajectories, Unit Economic Comparisons):
- **Data Points**: List the exact metrics found (ARR, headcount, cost per scan).
- **Axis Logic**: Define what the X and Y axes represent to prove the "Viral Growth" or "Inference Flip" thesis.

---

## 14. PHASE 11: SYNTHESIS - THE MASTER DELIVERABLES PROTOCOL

You MUST generate THREE primary documents. **Detailed, verbose reporting is mandatory.**

### 14.1 `overview_memo.md` (The Partner Summary)
- **Length**: 2-3 pages.
- **Visuals**: Logo in header, 1-2 core PNG diagrams.
- **Structure**:
    - **Executive Summary**: 2-paragraph "Why Now?"
    - **Recommendation**: Clear Overweight/Underweight call.
    - **External Validation**: Links to Crunchbase/LinkedIn.

### 14.2 `technical_commercial_deep_dive.md` (The 15+ Page Master Audit)
- **Length**: 15-20 pages (exhaustive, verbose).
- **Requirement**: Use detailed paragraphs (at least 5 per section). Avoid lists for core logic.
- **Visuals**: Founder headshots, ALL diagrams, embedded code snippets.
- **Sections Required**:
    1. **Founder Deep Audit**: Narrative alpha, "Social Graph" analysis, and "Talent Spikes."
    2. **Architectural Teardown**: Detailed component-by-component analysis with diagrams.
    3. **Visual Design Specification**: Detailed textual plan written *after* the teardown, explaining exactly what the Market Diagram, Technical Architecture Diagram, and any other relevant data graphs (e.g., Growth Trajectories) look like with all details.
    4. **Economic Modeling**: Unit economics, inference cost estimates, and LTV/CAC projections.
    5. **Market Map & Moat Matrix**: 4-pillar moat audit and competitor displacement analysis.
    6. **Risk & Platform Displacement**: The "Sherlocking" test and regulatory red-flags.
    7. **Master Questionnaire**: 20+ contextualized "Killer Questions."

### 14.3 `full_diligence_report.md` (The Comprehensive Master Audit)
- **Length**: Highly exhaustive (30+ pages of raw and synthesized data).
- **Purpose**: A complete "Truth File" containing every piece of evidence, data point, and analytical thought generated during the process.
- **Detailed Sections Required**:
    1.  **Executive Summary**: A 3-paragraph distillation of the entire 30-page document.
    2.  **Company Profile & Identity**: Mission, legal structure, historical pivots, and current core product offering.
    3.  **The "Founder Alpha" Audit**: Exhaustive bios, academic publication history, patent audits, and "Social Graph" (who they know and who they've worked for).
    4.  **Financing & Capital Structure**: Complete history of rounds, specific lead partners, board composition, and valuation growth velocity.
    5.  **Product & Technical Architecture**: Component-by-component teardown of the "Plumbing," tech stack choices, and identified infrastructure bottlenecks.
    6.  **Market Dynamics & Industry Trends**: Detailed TAM/SAM/SOM modeling, 2025-2026 platform shift analysis, and regulatory tailwinds.
    7.  **Competitive Landscape Matrix**: Feature-by-feature comparison with incumbents (Slow Giants) and stealth challengers, including Displacement Economics.
    8.  **Commercials & Unit Economics**: GTM strategy mapping, LTV/CAC projections, inference cost modeling, and churn signal analysis.
    9.  **Legal, Regulatory & Governance**: IP provenance audit, data privacy posture (GDPR/CCPA/FERPA), and material risk assessment.
    10. **The Master Research Appendix**: A structured compilation of ALL raw text and sources harvested during the Content Harvesting Protocol (Phase 1.5).
    11. **The Investment Thesis (Detail)**: 5-7 specific points of conviction and 3-5 specific "Risks to Monitor."
    12. **The Final Verdict**: A definitive "Invest / No Invest" call with a detailed rationale explaining the "Why" behind the decision.

---

## 15. PHASE 12: ADVANCED VISUAL ARGUMENTATION & PNG EXPORT

### 15.1 PNG Export Protocol (High-Resolution)
Once diagrams are finalized in `.excalidraw` format, you MUST convert them to `.png` to allow embedding in markdown. 
**Method**: This skill uses a Python wrapper `scripts/export_diagrams.py` which calls the `excalidraw-diagram` skill's internal renderer for maximum fidelity.
- **Command**: `python3 scripts/export_diagrams.py [diligence_folder]`
- **Requirement**: Must have `playwright` (Python) and `chromium` (npx) installed.
- **Embedding Syntax**: `![Architecture Diagram](../diagrams/architecture.png)`

---

## 16. PHASE 13: FORMATTING AUDIT (TABLES VS. BULLETS)

Before finalizing, perform a structural audit to maximize readability:
1. **The Table Test**: If comparing 3+ items across 2+ attributes (e.g., Competitors, Unit Economics), use a **Table**.
2. **The Bullet Test**: Use bullets ONLY for chronological events or simple lists.
3. **Richness Check**: Ensure at least 40% of the report is paragraph-driven analysis.

---

## 17. PHASE 14: EXCALIDRAW MASTER TEMPLATES

*(Refer to previous detailed JSON templates for Rectangles, Arrows, and Code Snippets.)*

---

## 18. PHASE 15: CRITICAL JSON SAFETY & SYNTAX PROTOCOL

**NO LITERAL NEWLINES**: Escape every newline as `\n` in strings. 

---

## 19. PHASE 16: FINAL QUALITY ASSURANCE & HAND-OFF

### 19.1 Hand-off
"Diligence for [Startup] is complete. 
Overview Memo and 15+ page Deep Dive (with visuals, diagrams, and intimate technical details) are in `deliverables/`."

---
*End of VC Diligence Skill Masterclass V6.*
