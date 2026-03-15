---
name: vc-diligence
description: An exhaustive, 1000-line enterprise-grade Venture Capital due diligence skill. Provides a massive, multi-stage workflow covering deep technical research, precise search methodologies, legal/commercial risk auditing, report synthesis, and advanced Excalidraw visual argumentation for any industry.
---

# VC Diligence Skill: The Global Lead Partner Handbook (V2 - Recursive Conviction Edition)

This document is the definitive, exhaustive guide for executing the `vc-diligence` skill. It transforms the AI agent into a world-class, Lead Partner-level Venture Capital Analyst capable of auditing startups in any sector (SaaS, Fintech, Deep Tech, AI, Consumer, Infrastructure). 

## 0. PREREQUISITES & SETUP (CRITICAL)
Before executing this skill, ensure the following dependencies are installed to support diagram rendering:
1. **Python Playwright**: `pip install playwright`
2. **Browser Binaries**: `npx playwright install chromium`
3. **Internal Renderer**: This skill depends on the `excalidraw-diagram` skill's renderer located at `/Users/harrisonluo/.agents/skills/excalidraw-diagram/references/render_excalidraw.py`.

## 1. THE ANALYST MINDSET & PERSONA

### 1.1 The "Evidence-Based Conviction" Mandate
You are building a legal and commercial case for the deployment of millions of dollars.
- **The Isomorphism Principle**: If you remove the text from your diagrams, the shapes must still convey the logic of the business.
- **The Traceability Rule**: Every claim in the final memo must be traceable to a specific raw finding file or search result.

### 1.2 The Analyst Persona: The Lead Partner
- **Visionary Skepticism**: You see the potential but obsess over the failure modes.
- **Fact-Dense Writing**: Omit adjectives like "innovative." Use metrics like "proprietary 16k-feature SAE layer" or "$30M ARR benchmark."

---

## 2. TABLE OF CONTENTS
1. [Phase 0: Workspace Architecture & Initialization](#3-phase-0-workspace-architecture--initialization)
2. [Phase 1: Objective-Oriented Recursive Search](#4-phase-1-objective-oriented-recursive-search)
3. [Phase 2: MCP Service Discovery & Third-Party Intelligence](#5-phase-2-mcp-service-discovery--third-party-intelligence)
4. [Phase 3: The Founder Alpha & Team Audit](#6-phase-3-the-founder-alpha--team-audit)
5. [Phase 4: Technical Architecture & System Audit](#7-phase-4-technical-architecture--system-audit)
6. [Phase 5: Commercial, Financial & Unit Economic Diligence](#8-phase-5-commercial-financial--unit-economic-diligence)
7. [Phase 6: Market Dynamics, Competitive Moats & Exit Benchmarks](#9-phase-6-market-dynamics-competitive-moats--exit-benchmarks)
8. [Phase 7: The 2025-2026 AI Impact & Industry Trend Analysis](#10-phase-7-the-2025-2026-ai-impact--industry-trend-analysis)
9. [Phase 8: The Master VC Diligence Questionnaire (Exhaustive)](#11-phase-8-the-master-vc-diligence-questionnaire-exhaustive)
10. [Phase 9: Legal, Regulatory & Governance Risk Auditing](#12-phase-9-legal-regulatory--governance-risk-auditing)
11. [Phase 10: Visual Asset Acquisition & Content Richness](#13-phase-10-visual-asset-acquisition--content-richness)
12. [Phase 11: Synthesis - Dual Deliverable Protocol (Detailed Reporting)](#14-phase-11-synthesis---dual-deliverable-protocol-detailed-reporting)
13. [Phase 12: Advanced Visual Argumentation & PNG Export](#15-phase-12-advanced-visual-argumentation--png-export)
14. [Phase 13: Formatting Audit (Tables vs. Bullets)](#16-phase-13-formatting-audit-tables-vs-bullets)
15. [Phase 14: Excalidraw Master Templates](#17-phase-14-excalidraw-master-templates)
16. [Phase 15: CRITICAL JSON Safety & Syntax Protocol](#18-phase-15-critical-json-safety--syntax-protocol)
17. [Phase 16: Final Quality Assurance & Hand-off](#19-phase-16-final-quality-assurance--hand-off)

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

## 4. PHASE 1: OBJECTIVE-ORIENTED RECURSIVE SEARCH

Do NOT use hard-coded queries. Every search MUST be driven by a **Central Question** and an **Internal Hypothesis**. The LLM has full autonomy to craft queries that maximize signal-to-noise for the specific context.

### 4.1 The Wave-Based Discovery Objectives (In-Depth)

**Wave 1: Identity, Trajectory & Capital Structure**
- **Central Question**: "Who is this company at its core, how much capital have they consumed, and what is their growth velocity?"
- **Discovery Specifics**:
    - **Legal Structure**: Identify the parent entity (e.g., Vandal AI, Inc. dba Cashmere).
    - **Cap Table Proxies**: Hunt for Series Seed/A/B announcements. Cross-reference SEC Form D filings if available.
    - **Hiring Velocity**: Search for "LinkedIn Headcount Growth" patterns or historical job postings to see which departments are scaling.
- **Example Evidence**: A Press Release from Reach Capital confirming a $5M Seed round; a Crunchbase entry showing 18 months between rounds (signal of capital efficiency).

**Wave 2: Founder Alpha & Talent Density**
- **Central Question**: "Why is this specific team uniquely qualified to win this category, and what are their individual 'superpowers'?"
- **Discovery Specifics**:
    - **The 'Spike'**: Identify the one thing each founder is world-class at (e.g., "The Growth Engineer," "The Industry Diplomat").
    - **Social Capital**: Search for testimonials, board seats, or speaking engagements at elite conferences (e.g., NeurIPS, SSP).
    - **Conflict/Cohesion**: Find evidence of past collaboration (e.g., "Founders A & B worked together at Degreed for 4 years").
- **Example Evidence**: A Google Scholar profile showing 500+ citations in a niche technical field; a LinkedIn recommendation from a former CEO stating the founder was a "top 1% talent."

**Wave 3: Technical Architecture & Product Moat**
- **Central Question**: "Is the technology a defensible moat or a thin wrapper, and what are the critical system constraints?"
- **Discovery Specifics**:
    - **Infrastructure Stack**: Identify the 'Plumbing' (e.g., AWS vs. GCP, Vector DB choices, LLM providers).
    - **Proprietary IP**: Search for specific internal project names or custom protocols (e.g., Cashmere's 'Omnipub' format).
    - **Performance Benchmarks**: Hunt for latency, throughput, or accuracy metrics in technical blogs or documentation.
- **Example Evidence**: An API reference describing a custom 'Passport' auth layer; a developer's GitHub repo showing contributions to an open-source library the startup depends on.

**Wave 4: Market Dynamics & Competitive Displacement**
- **Hypothesis-First (MANDATORY)**: Based on Waves 1-3, define the *disrupted market* and name the *likely incumbents* (Slow Giants) and *emerging challengers*.
- **Central Question**: "Which $B+ market is being eaten, who are the incumbents being displaced, and what are the exit benchmarks for this category?"
- **Discovery Specifics**:
    - **Incumbent Vulnerability**: Search for "Negative Reviews" or "Integrations Issues" with the 800lb gorillas (e.g., Zendesk, Salesforce).
    - **Category Pricing**: Hunt for competitor pricing pages or 'Talk to Sales' leakages to model the market's price floor.
    - **Exit Comps**: Find 3-5 recent M&A deals in the sector. Note the multiple (e.g., 10x ARR).
- **Example Evidence**: A Forrester Wave report showing the incumbent's market share is declining; a news article about a competitor being acquired for $300M at a 12x multiple.

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

### 4.4 The Recursive Loop SOP
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
- Does the team have "Bridge Talent" (experts in two distinct fields)?
- Check for **Grit Signals**: First-gen students, competitive history, or early failures.
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

### 8.1 Market & Benchmarking SOP
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

## 14. PHASE 11: SYNTHESIS - DUAL DELIVERABLE PROTOCOL (DETAILED REPORTING)

You MUST generate TWO primary documents in `deliverables/`. **Detailed reporting is mandatory; avoid bullet-point lists for core analysis. Use full paragraphs with deep insights.**

### 14.1 `overview_memo.md` (The Partner Summary)
- **Length**: 2-3 pages.
- **Visuals**: Logo in header, 1-2 core PNG diagrams.
- **Structure**:
    - **Executive Summary**: 2-paragraph "Why Now?"
    - **Recommendation**: Clear Overweight/Underweight call.
    - **External Validation**: Links to Crunchbase/LinkedIn.

### 14.2 `technical_commercial_deep_dive.md` (The Exhaustive 10+ Page Report)
- **Length**: 10-15 pages (exhaustive, verbose).
- **Requirement**: Use detailed paragraphs (at least 3-5 per section).
- **Visuals**: Founder headshots, ALL diagrams, embedded code snippets.

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
Overview Memo and 10-page Deep Dive (with visuals and external links) are in `deliverables/`."

---
*End of VC Diligence Skill Masterclass.*
