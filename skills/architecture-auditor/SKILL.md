---
name: architecture-auditor
description: Specialized technical auditor for deep startup architecture teardowns and high-fidelity visual design specifications. Handles component-by-component forensics and maps technical moats for VC diligence.
---

# Architecture Auditor Skill: The CTO's Forensic Handbook

This skill is designed to perform exhaustive technical audits of startup architectures. It moves beyond high-level boxes into "Plumbing Forensics"—identifying specific libraries, API patterns, and infrastructure moats.

## 1. THE RESEARCH MANDATE (EVIDENCE ARTIFACTS)
Before specifying a diagram, you MUST harvest the "Ingredients of Truth":
- **Library Forensics**: Search for specific implementation details (e.g., "Uses LangChain for orchestration with custom Pydantic schemas").
- **API Specifics**: Identify actual endpoint names, event codes (e.g., `DATA_INGESTED`, `INFERENCE_COMPLETE`), and auth protocols.
- **Model Tiering**: Map exactly which models are used for which tasks (e.g., "Llama-3-8b for routing, GPT-4o for final aggregation").

## 2. THE COMPONENT-BY-COMPONENT TEARDOWN
For each technical section of the report:
1.  **Gated Logic**: Describe the "Early Exit" or "Escalation" conditions between model layers.
2.  **Infrastructure Bottlenecks**: Identify exactly where latency or cost issues exist (e.g., "Vector DB query latency at 500ms+ due to high dimensionality").
3.  **Moat Verification**: Prove if a component is proprietary or off-the-shelf by auditing GitHub dependencies or whitepaper citations.

## 3. THE VISUAL DESIGN SPECIFICATION (VDS)
This is the formal prompt passed to the `excalidraw-diagram` skill. Generic specs are failures.

### 3.1 VDS Checklist:
- **Technical Diagram**: Map the data journey from Input to Output. 
    - **Annotations**: Every box must contain its technical purpose + dependency name.
    - **Binding**: Use the Two-Way Binding Protocol (Shape `boundElements` <-> Text `containerId`).
- **Market Diagram**: Use the "Displacement Path" pattern.
    - **Nodes**: Annotate incumbents with their market share % and key technical weakness.
- **Economic Graphs**: Use annotated axes with specific milestones (e.g., "Seed Round Achieved").

## 4. INTEGRATION PROTOCOL
When called by the `vc-diligence` skill:
1.  Read the raw findings in `raw_findings/tech/`.
2.  Perform any missing "Least-to-Most" technical sub-queries.
3.  Draft the `technical_commercial_deep_dive.md` section for Architecture.
4.  Generate the finalized Visual Design Specification for delegation.

---
*End of Architecture Auditor Skill.*
