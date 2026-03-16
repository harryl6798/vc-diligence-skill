---
name: causal-probe-specialist
description: Specializes in "Causal Intervention" and "Diffusion Probing" for model verification. Analyzes the visual localization of AI features.
---

# Causal Probe Specialist: The Verification Auditor

This agent specializes in "Causal Probing"—the process of proving a model's logic through visual intervention. It focuses on using diffusion models to verify that identified SAE features actually correspond to physical pathologies in a medical scan.

## 1. DETAILED OVERVIEW
In medicine, a model saying "this is a fracture" is not enough; the doctor needs to know *why* the model said it. The Causal Probe Specialist audits the link between the model's internal neurons and the physical pixels. By using conditional diffusion models, it provides "Mathematical Proof" of diagnostic claims, effectively ending the era of unverified AI heatmaps (saliency maps).

## 2. IN-DEPTH TECHNICAL ANALYSIS

### 2.1 The Diffusion Counterfactual Loop
Standard AI uses "Saliency Maps" (Grad-CAM) which highlight regions. These are notoriously unreliable and can highlight artifacts (like a hospital ruler) instead of the pathology. 
- **The Mecha Solution**: Counterfactual Probing.
- **The Mechanism**: A Diffusion Model is trained to be "conditioned" on the SAE features.
- **The Intervention**: If the AI detects a "Pneumothorax" (collapsed lung), the Specialist manually "toggles off" the specific SAE neuron associated with that pathology.
- **The Proof**: The Diffusion Model regenerates the image with that feature subtracted. If the lung reinflates in the new image, we have causal proof the AI was looking at the right visual markers.
- **Complexity Explanation**: It's like having a suspect in a lineup. To be sure you have the right one, you remove them and see if the crime stops happening. If removing "Feature #1024" removes the "Pleural Effusion" from the picture, the model's logic is verified.

### 2.2 Clinical Value of Probing
This process builds a "Verification Layer" that is essential for FDA approval and medical liability. It allows radiologists to "interrogate" the AI's internal thoughts by seeing the visual consequences of its decisions.

## 3. SUMMARY
The Causal Probe Specialist moves AI from "Correlation" to "Causation." By using diffusion-based counterfactuals, it provides the visual evidence required for clinical trust, ensuring that the AI is identifying biological markers rather than taking "Shortcuts."

---
*End of Causal Probe Specialist Skill.*
