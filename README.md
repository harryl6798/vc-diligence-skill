# VC Diligence Skill Framework

A high-performance framework for AI-driven Venture Capital due diligence. This repository contains a suite of specialized skills designed to automate deep-dive audits of startups, focusing on technical moats, commercial viability, and product-market fit.

## 🚀 Overview

The `vc-diligence` framework transforms an AI agent into a world-class Lead Partner-level analyst. It moves beyond basic search to perform **Recursive Discovery** and **Hyper-Depth Content Harvesting**, culminating in 30+ page master audits.

### Key Capabilities

*   **Recursive Wave Discovery**: Multi-stage research (Waves 0-4) covering Product DNA, Founder Alpha, Technical Architecture, and Market Dynamics.
*   **PMF Leveling**: Formal audit of Product-Market Fit (Levels 1-4) based on the **First Round Capital PMF Method** (Satisfaction, Demand, and Efficiency).
*   **Architecture Auditing**: Specialized "Plumbing Forensics" using the `architecture-auditor` to identify real API patterns, library dependencies, and model tiering.
*   **Visual Mastery**: Automated generation of fact-dense Excalidraw diagrams (Architecture, Market Displacement, Growth Curves) with a strict Two-Way Binding Protocol.
*   **Hyper-Depth Mandate**: Enforces a 1:1 Search-to-Fetch ratio, ensuring the agent analyzes full-text documents rather than just search snippets.

## 📂 Repository Structure

*   **/skills/vc-diligence**: The master framework governing the end-to-end diligence workflow and iterative report expansion.
*   **/skills/architecture-auditor**: A specialist sub-agent for deep technical teardowns and generating visual design specifications.
*   **/deliverables**: Standards for generating the **Partner Overview Memo**, **Technical Deep Dive**, and the **30-Page Master Audit**.

## 🛠️ Methodology (V24 Master Edition)

1.  **Phase 1 (Decomposition)**: Use Least-to-Most prompting to break down the investment thesis into atomic sub-questions.
2.  **Phase 2 (Harvesting)**: Execute 3-5 multi-angle query fanouts per wave, followed by exhaustive full-text extraction via `web_fetch`.
3.  **Phase 3 (Synthesis)**: Build TAM/SAM/SOM models from atomic facts (Synthesis Mandate) rather than searching for high-level conclusions.
4.  **Phase 4 (Expansion)**: Iteratively expand initial drafts into dense, research-grade "Truth Files" with sub-bullets and verified citations.

---
*Developed for high-conviction investment decision-making.*
