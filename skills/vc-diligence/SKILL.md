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
2. [Phase 1: Advanced Recursive Search Methodology](#4-phase-1-advanced-recursive-search-methodology)
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

## 4. PHASE 1: ADVANCED RECURSIVE SEARCH METHODOLOGY

### 4.1 The Wave-Based Approach & Hypothesis Generation
For each wave, the LLM MUST first generate **Internal Hypotheses** to guide the search. Do not search blindly; predict what the evidence will look like.

**Wave 1: Identity & Early History (Hypothesis-First)**
- **Hypothesis**: "Based on the startup name and brief, they likely participated in [Accelerator] or were founded by [Ex-BigTech] alum. They are likely solving [Specific Problem]."
- **Queries**:
  - `"[Startup Name]" launch OR Y Combinator OR TechCrunch`
  - `"[Startup Name]" "series A" funding date 2024 2025`
  - `site:crunchbase.com "[Startup Name]" funding history`

**Wave 2: Founder Alpha (Technical & Academic Hypothesis)**
- **Hypothesis**: "Founder A likely has a background in [Field] from [University]. Founder B likely managed [Product/Team] at [Previous Startup]."
- **Queries**:
  - `"[Founder Name]" research OR thesis OR patents OR publications`
  - `"[Founder Name]" "github" OR "open-source" contributions`
  - `site:linkedin.com "[Founder Name]" "former" OR "founder"`

**Wave 3: Technical Architecture (Structural Hypothesis)**
- **Hypothesis**: "The system likely uses a [Tech Stack/Pattern] (e.g., RAG, SAE, Vector DB) and depends on [Third-Party API] for core logic. Scalability is likely limited by [Constraint]."
- **Queries**:
  - `"[Startup Name]" architecture OR system diagram OR tech stack`
  - `"[Startup Name]" "API docs" OR "developer guide" filetype:pdf`
  - `"[Startup Name]" "benchmark" OR "latency" OR "throughput"`

**Wave 4: Market & Exit Benchmarks (Strategic Hypothesis)**
- **Hypothesis**: "This startup is disrupting [Market Segment]. Likely incumbents are [Slow Giants]. Exit multiples for this category are likely [X-Y] based on [Recent Deal]."
- **Queries**:
  - `"[Proposed Category]" market size bottom-up analysis 2025`
  - `"[Hypothesized Competitor]" ARR 2024 2025 OR acquisition price`
  - `"[Industry]" M&A multiples 2025 "ARR"`

### 4.2 The Search Critic & Step-Back SOP
Before executing any query:
1. **Mental Model Check**: Does this query align with my internal hypothesis?
2. **Critic Loop**: Is the query too conversational? Strip it down to high-signal keywords.
3. **Step-Back**: If a specific technical query (e.g., a specific patch version) fails, step back to the broader product's compatibility or changelog.
4. **Keyword Transformation**: Use operators like `filetype:pdf` or `site:github.com` to target primary sources.

### 4.3 The Recursive Loop SOP
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
2. **GTM Strategy Mapping**: Map out the sales motion. Is it PLG (Product-Led Growth), Enterprise Sales, or Channel-Partnership based?
3. **LTV/CAC Calculation**: Use industry benchmarks for the category (e.g., SaaS, Fintech) to predict if the current GTM is sustainable.
4. **Churn Signal Hunting**: Actively search for "Negative Social Proof" in developer forums, Reddit, or review sites to identify retention risks.

---

## 9. PHASE 6: MARKET DYNAMICS, COMPETITIVE MOATS & EXIT BENCHMARKS

You MUST construct a **Competitive Moat Matrix** that goes beyond simple feature lists.

### 8.1 Market & Benchmarking SOP
1. **The "Slow Giant" Audit**: Identify 3-5 legacy incumbents. Analyze their latest quarterly earnings (10-K/10-Q) to see if they are building competing AI capabilities.
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

---

## 11. PHASE 8: THE MASTER VC DILIGENCE QUESTIONNAIRE (EXHAUSTIVE)

Generate a custom list of **25-50 High-Conviction Questions** for the founders based on your findings.

### 11.1 Questionnaire Generation SOP
1. **Contextualize**: Do not use generic templates. Every question must reference a finding (e.g., "Given your reliance on [Provider X], how do you mitigate...")
2. **The "Killer" Questions**: Focus on the 3 biggest risks identified in your research.
3. **Evidence Validation**: Formulate questions that require the founder to provide data (e.g., "Show us the retention cohort data for Segment Y").

---

## 12. PHASE 9: LEGAL, REGULATORY & GOVERNANCE RISK AUDITING

Conduct a **Legal & Regulatory Red-Flag Audit**.

### 12.1 Legal Diligence SOP
1. **IP Provenance Audit**: Search for patent filings or university IP agreements. Identify if the tech was developed during a PhD or at a previous employer.
2. **Data Privacy Posture**: Check for GDPR/CCPA compliance in the privacy policy. Search for SOC 2 or ISO 27001 certifications.
3. **Compliance Risk**: In regulated industries (Fintech/Health), audit their licensing status (e.g., "Do they have a money transmitter license?").
4. **Governance Review**: Check for Board composition and 83(b) election mentions in early legal docs if available.

---

## 13. PHASE 10: VISUAL ASSET ACQUISITION & CONTENT RICHNESS

To make reports content-rich and professional, you MUST acquire, **download**, and embed high-quality visual assets.

### 13.1 Broad Asset Search Strategy
Do NOT use overly specific queries for images. Use broad "Name + Company" patterns to find official bios and logos first.
- **Company Logo**: Search `"[Company Name]" logo png transparent`
- **Founder Headshots**: Search `"[Founder Name]" [Company Name]`
- **Simple Queries**: Keep search queries simple to maximize the chance of finding official pages (e.g., Team, About, or Press pages).

### 13.2 Asset Discovery & Direct URL Extraction
Finding the direct image URL is critical to avoid downloading HTML pages.
- **Metadata Scraping**: Use `web_fetch` or `curl` to inspect the HTML for `application/ld+json` blocks, which often contain direct URLs for logos and person headshots.
- **Grep Pattern**: Grep for `img src` or `og:image` tags in the source code to find high-resolution assets.
- **Absolute URLs**: Ensure the URL is absolute (starting with `http`) before attempting to download.

### 13.3 Asset Downloading & Verification SOP
Every asset found MUST be downloaded to the `assets/` directory and **verified** to ensure it is a valid image and not an HTML error page.
- **Download Command**: Use `curl -L -o assets/[filename].ext [URL]` to follow redirects.
- **Verification**: IMMEDIATELY run `file assets/[filename].ext` after downloading.
  - **Success**: Output identifies it as "PNG image data" or "JPEG image data".
  - **Failure**: Output identifies it as "HTML document text". If this happens, the URL was likely a webpage, not a direct image link. Re-examine the source for the `src` attribute.
- **Naming**: Use descriptive names (e.g., `logo.png`, `munk_headshot.jpg`).

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
