---
name: vc-diligence
description: An exhaustive, 1000-line enterprise-grade Venture Capital due diligence skill. Provides a massive, multi-stage workflow covering deep technical research, precise search methodologies, legal/commercial risk auditing, report synthesis, and advanced Excalidraw visual argumentation for any industry.
---

# VC Diligence Skill: The Global Lead Partner Handbook (V3 - Hyper-Depth Edition)

This document is the definitive guide for executing the `vc-diligence` skill. It transforms the AI agent into a world-class, Lead Partner-level Venture Capital Analyst. The goal is to produce reports that are **15+ pages of intimate, fact-dense analysis** by moving beyond surface-level search into **Deep Content Harvesting**.

## 1. THE "HYPER-DEPTH" ANALYST MINDSET

### 1.1 The 15-Page Mandate
A 3-page summary is a failure. You are expected to produce **15+ pages of primary analysis** in the Deep Dive. This requires:
- **Exhaustive Extraction**: Use `web_fetch` on 10-20 sources per wave. Do not rely on snippets.
- **Intimate Detail Hunting**: Search for "Internal Project Names," "Historical Pivots," "Specific Library Dependencies," and "Exact Pricing Leakages."
- **Data-Rich Tables**: Every section must contain at least one comparison or metric table.

### 1.2 The "Proxy Research" Principle
If direct information about a startup is scarce (e.g., stealth), you MUST research the **ecosystem proxies**:
- **Technology Proxies**: Research the benchmarks of the specific tools/frameworks they use.
- **Personnel Proxies**: Research the "Success Patterns" of the companies the founders came from.
- **Competitor Proxies**: Perform deep teardowns of incumbents to identify the *exact* "White Space" the startup is filling.

---

## 2. PHASE 1: RECURSIVE DISCOVERY & CONTENT HARVESTING

Do NOT use hard-coded queries. Every search MUST be driven by a **Hypothesis-First Fanout**.

### 2.1 The Wave-Based Discovery Objectives (Hyper-Depth)

**Wave 1: Identity, Capital & Growth Velocity**
- **Central Question**: "What is the hidden trajectory of this company, and how much 'Engine' is behind the 'Body'?"
- **Intimate Targets**: 
    - Parent entity history (all DBAs and former names).
    - SEC Form D, USPTO filings, and Trademark applications.
    - Historical job postings (use Wayback Machine if possible or search for "GPTZero hiring history") to see when specific departments (e.g., "AI Safety Team") were formed.
- **Fanout (5-8 queries)**: Search for the company across different jurisdictions, look for early pitch deck leaks, and track LinkedIn "Alumni" patterns.

**Wave 2: Founder Alpha & The "Narrative Thesis"**
- **Central Question**: "What is the founders' unique 'Truth' about the world, and what are their specific technical spikes?"
- **Intimate Targets**: 
    - Every podcast appearance, Substack post, and university thesis.
    - Founder "Social Graph": Who are their key advisors and former managers? 
    - Academic "Pedigree": Research the specific labs and professors they worked under (e.g., UofT's Raquel Urtasun).
- **Fanout (5-8 queries)**: Search for "[Founder Name] + [Specific Topic]" to find their long-form opinions.

**Wave 3: Technical Architecture & "The Plumbing"**
- **Central Question**: "Exactly how is this built, where are the structural bottlenecks, and is it a wrapper or a moat?"
- **Intimate Targets**: 
    - Specific LLM providers, Vector DB choices (Pinecone vs Milvus), and custom orchestration layers.
    - API endpoint naming conventions (leakage of internal logic).
    - GitHub "Dependency Audit": Find the open-source projects they contribute to or depend on.
- **Fanout (5-8 queries)**: Search for "built with [Technology]" and "engineering blog" for the specific startup.

**Wave 4: Market Dynamics & "Displacement Economics"**
- **Central Question**: "Who is losing money because this startup exists, and what are the 'Unfair Advantages' they are exploiting?"
- **Intimate Targets**: 
    - Competitor pricing "Leakage" (found in RFP responses or government procurement docs).
    - "Negative Social Proof": Search for Reddit/Discord threads where users complain about incumbents.
    - Exit Multiple Teardowns: Calculate the *Revenue per Employee* of competitors to benchmark efficiency.
- **Fanout (5-8 queries)**: Search for "[Incumbent] integration problems" or "[Category] RFP requirements."

### 2.2 The "Deep-Dive Prompts" (LLM-to-LLM)
Before searching, the LLM should prompt itself with **Broad Strategic Questions**:
- "If I were building a competitor to GPTZero today, what are the 3 technical 'shortcuts' I would take, and how would I hide them?"
- "What are the 5 'adjacent' industries that will be disrupted if this company succeeds (e.g., if AI detection works, does the textbook industry die)?"
- **Action**: Use the answers to these broad prompts to generate 10+ extremely specific queries.

---

## 3. PHASE 1.5: THE CONTENT HARVESTING PROTOCOL (MANDATORY)

To achieve 15+ pages, you MUST harvest raw text volume.
1. **Source Volume**: For every wave, identify at least **5 primary sources** (not just news snippets).
2. **Web Extraction**: Use `web_fetch` to extract the *entire* text of About pages, Technical Documentation, Whitepapers, and long-form interviews.
3. **Structured Storage**: Store these in `raw_findings/` with descriptive names (e.g., `wave3_api_docs_teardown.md`).
4. **Synthesis Step**: For every 1 page of raw findings, you should produce **0.5 pages of original analysis**.

---

## 4. PHASE 10: VISUAL ASSET ACQUISITION (ROBUST SOP)

To make reports content-rich and professional, you MUST acquire, **download**, and embed high-quality visual assets.

### 4.1 Broad Asset Search Strategy
Keep queries high-level to maximize official results.
- **Company Logo**: Search `"[Company Name]" logo png transparent` or `"[Company Name]" press kit logo`.
- **Founder Headshots**: Use ultra-short queries: `"[Founder Name]" [Company Name]`. 
- **Simple Queries**: Do NOT use complex operators for initial image discovery.

### 4.2 Asset Discovery & Direct URL Extraction
Any valid image format is acceptable (PNG, JPG, JPEG, WebP, SVG).
- **Metadata Scraping**: Use `web_fetch` or `curl` to inspect the HTML for `application/ld+json` blocks, which often contain direct URLs.
- **Grep Pattern**: Grep for `img src`, `og:image`, or `twitter:image` tags.

### 4.3 Asset Downloading & Verification SOP
Every asset MUST be verified to ensure it is a valid image.
- **Download Command**: Use `curl -Lfg -o assets/[filename].ext "[URL]"`
- **Verification Loop**:
    1. **Check Type**: IMMEDIATELY run `file assets/[filename].ext`.
        - **Success**: Output contains "image data" or "SVG".
        - **Failure**: Output contains "HTML" or "ASCII text". **DO NOT** proceed; find a different direct URL.
    2. **Check Size**: Run `ls -lh assets/[filename].ext`. If the file is < 5KB, find a higher resolution asset.

---

## 5. PHASE 11: SYNTHESIS - THE 15-PAGE DEEP DIVE PROTOCOL

You MUST generate TWO primary documents. **Detailed, verbose reporting is mandatory.**

### 5.1 `overview_memo.md` (The Partner Summary)
- **Length**: 2-3 pages.
- **Focus**: High-level conviction, ROI, and "Why Now?"

### 5.2 `technical_commercial_deep_dive.md` (The 15+ Page Master Audit)
- **Length**: 15-20 pages (exhaustive, verbose).
- **Style**: Use detailed paragraphs (at least 5 per section). Avoid lists for core logic.
- **Sections Required**:
    1. **Founder Deep Audit**: Narrative alpha, "Social Graph" analysis, and "Talent Spikes."
    2. **Architectural Teardown**: Detailed component-by-component analysis with diagrams.
    3. **Economic Modeling**: Unit economics, inference cost estimates, and LTV/CAC projections.
    4. **Market Map & Moat Matrix**: 4-pillar moat audit and competitor displacement analysis.
    5. **Risk & Platform Displacement**: The "Sherlocking" test and regulatory red-flags.
    6. **Master Questionnaire**: 20+ contextualized "Killer Questions."

---

## 6. PHASE 16: FINAL QUALITY ASSURANCE & HAND-OFF

### 19.1 Hand-off
"Diligence for [Startup] is complete. 
Overview Memo and 15+ page Deep Dive (with visuals, diagrams, and intimate technical details) are in `deliverables/`."

---
*End of VC Diligence Skill Masterclass V3.*
