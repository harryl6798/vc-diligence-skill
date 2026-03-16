---
name: sae-rad-factory
description: Specializes in the "SAE-Rad" pipeline. Analyzes latent disentanglement, Gated SAE math, and monosemantic feature extraction for clinical reporting.
---

# SAE-Rad Factory: The Disentanglement Expert

This agent specializes in the mechanics of Sparse Autoencoders (SAEs) applied to radiology. It focuses on how jumbled "Superposition" is unpacked into discrete, monosemantic features.

## 1. DETAILED OVERVIEW
The SAE-Rad Factory is responsible for the "Forensic Sorting" of neural activations. It takes the dense, uninterpretable cloud of a Vision Transformer (ViT) and passes it through a high-dimensional dictionary layer. This layer identifies specific clinical concepts (features) that are active in the scan, ensuring the final report is a compilation of verified facts rather than a generated narrative.

## 2. IN-DEPTH TECHNICAL ANALYSIS

### 2.1 Gated SAE Mechanics
Standard SAEs suffer from "Feature Shrinkage" where small signals are crushed to zero by the L1 penalty. 
- **The Solution**: Mecha Health uses **Gated SAEs**.
- **The "Gate"**: A separate mathematical path that only asks: "Is this feature present? Yes/No." It uses a hard threshold to ignore background noise.
- **The "Magnitude"**: If the gate is open, a second path estimates the *intensity* of the signal without being penalized by the L1 force.
- **Complexity Explanation**: Think of a noise-canceling microphone. The gate stays closed for background chatter (noise) and only opens when someone speaks (pathology), ensuring the voice is recorded at its full, clear volume.

### 2.2 Automated Labeling (Teacher-Student Distillation)
Mecha does not manually label neurons. It uses a Large Language Model (LLM) to "Student-Audit" the SAE.
- **Process**: The system finds 100 images that strongly activate "Feature #1024." It retrieves the ground-truth reports for those 100 images.
- **Distillation**: The LLM analyzes the commonality across these 100 reports and realizes that every time #1024 is ON, doctors mention "Pleural Effusion." It then hard-codes this label into the feature.

## 3. SUMMARY
The SAE-Rad Factory turns a black-box "guess" into a "fact assembly line." By disentangling the latent space and automating the labeling process, it creates a system that is 100% interpretable and resistant to the hallucination issues of standard LLMs.

---
*End of SAE-Rad Factory Skill.*
