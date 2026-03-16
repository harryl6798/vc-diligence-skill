---
name: tech-brief-orchestrator
description: High-level technical "Editor-in-Chief" that coordinates specialized sub-agents to produce exhaustive, research-grade technical briefs.
---

# Technical Brief Orchestrator: The Master System Architect

This skill is designed to coordinate the hyper-depth technical audit process. It sequences the research and synthesis activities of specialized technical sub-agents to produce a 15+ page Master Technical Research Paper.

## 1. THE ORCHESTRATION WORKFLOW
The Orchestrator follows a strictly sequential, additive process to ensure no technical detail is missed.

### 1.1 Phase 1: Context Harvesting (Full-Text)
For every technical pillar (Superposition, SAE-Rad, Causal Probing, Trajectory Forecasting, Infrastructure), the Orchestrator MUST:
1.  **Identify Primary Sources**: Find at least 3-5 authoritative technical URLs (Arxiv, Engineering Blogs, API Docs).
2.  **Exhaustive Fetching**: Use `web_fetch` to extract the full text. **Search snippets are forbidden.**
3.  **Raw Ingredient Storage**: Save the extracted text in `raw_findings/tech/harvest_[pillar_name].md`.

### 1.2 Phase 2: Initial Specialized Analysis
The Orchestrator activates the specialized sub-agents one by one to produce the first technical draft:
1.  **Superposition Auditor**: Audits latent overlap risks.
2.  **SAE-Rad Factory**: Analyzes the disentanglement pipeline.
3.  **Causal Probe Specialist**: Audits the verification loop.
4.  **LookOut Trajectory Analyst**: Analyzes the path forecasting transfer.
5.  **Mecha Infrastructure Expert**: Audits efficiency and security moats.

### 1.3 Phase 3: Technical Context Expansion (The Second Phase)
After the initial analysis, the Orchestrator MUST perform a **Context Gap Audit**:
1.  **Identify "Thin" Logic**: Scan the generated teardowns for generic terms (e.g., "They use high-performance compute").
2.  **Deep-Dive Re-Searching**: Execute 3-5 high-resolution queries targeting missing primitives:
    - **Specific Versions**: "What version of [X] library is used?"
    - **Hyper-parameters**: "What are the expansion factors for the SAE layer?"
    - **Edge Cases**: "How does the system handle [Specific Failure Mode Y]?"
3.  **Synthesis Injection**: Re-activate the relevant sub-agent with this new context to expand the section by 2-3 detailed paragraphs.

### 1.4 Phase 4: Visual Design Specification & Rendering
The Orchestrator generates the finalized VDS for the `excalidraw-diagram` skill.

### 1.5 Phase 5: Visual Refinement Loop (The Second Phase)
Once diagrams are rendered, the Orchestrator MUST:
1.  **Inspect PNG Quality**: Check for text legibility and binding compliance.
2.  **Educational Audit**: Does the diagram explain a specific technical concept or is it just generic boxes?
3.  **Refinement Round**: If the diagram is insufficient, update the VDS with specific technical labels (e.g., actual API endpoint names) and re-delegate to `excalidraw-diagram`.

### 1.6 Phase 6: Final Master Synthesis
Assemble the final `master_technical_brief.md` with:
1.  **Component-by-Component Teardown**.
2.  **Technical Diligence Roadmap** (suggesting specific codebases or logs for future auditors).
3.  **Hyper-Linked Bibliography**.

## 2. THE HYPER-DEPTH STANDARDS
- **No Deletions**: Every iteration MUST be strictly additive.
- **Fact Density**: Every paragraph must contain at least one technical "Ingredient of Truth".
- **Traceability**: Every section must include links to the harvested sources.

---
*End of Technical Brief Orchestrator Skill.*
