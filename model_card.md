# Model Card: MANI-N-ATLaS Epidemiological Intelligence Adapter

## 1. Model Overview
- **Model Name:** MANI (Malaria Atlas Nigeria - N-ATLaS Fine-Tuned Derivative)
- **Base Model:** [NCAIR1/N-ATLaS](https://huggingface.co/NCAIR1/N-ATLaS) (8B Llama-based sovereign architecture)
- **Developed For:** NCAIR National AI Innovation Challenge (NAIC)
- **Task Focus:** Epidemiological reasoning, DHS biomarker risk correlation, resource allocation logic, geospatial analysis, and multilingual public health query resolution.

## 2. Training Methodology & Configuration
- **Fine-Tuning Framework:** Supervised Fine-Tuning (SFT) using `transformers`, `peft`, and `trl`.
- **Quantization:** 4-bit NormalFloat (NF4) via `bitsandbytes`.
- **QLoRA Parameters:**
  - Rank ($r$): 16
  - Alpha ($\alpha$): 32
  - Target Modules: `q_proj`, `k_proj`, `v_proj`, `o_proj`, `gate_proj`, `up_proj`, `down_proj`
  - Dropout: 0.05
- **Infrastructure:** Google Colab (NVIDIA T4 GPU) with automated Google Drive checkpoint synchronization.

## 3. Data Sources & Covariate Ingestion
- **Environmental Covariates:** Real-time satellite telemetry including CHIRPS precipitation grids and NDVI vegetation indices.
- **Biomarker & Household Layers:** Demographic and Health Survey (DHS) biomarker data (parasitemia/RDT prevalence, biological anemia testing indicators, and household ITN usage metrics).
- **Epidemiological Logs:** Normalized cluster-year spatial databases aligning administrative boundaries (LGAs/Wards) with biological infection risks.

## 4. Evaluation & Guardrails
- **Evaluation Benchmark:** Backed by a custom 500+ example public health evaluation benchmark specifically designed to stress-test the model against:
  - Hallucinations in medical dosage or numerical distribution logic.
  - LGA/Ward hierarchical geographical mapping consistency.
  - Multilingual translation and alignment fidelity across Hausa, Igbo, Yoruba, Pidgin, and English.

## 5. Intended Use & Scope
- **Permitted Uses:** Public health forecasting, operational planning for vector control, institutional data synthesis, and localized community health support.
- **Prohibited Uses:** Unverified clinical individual diagnostics, autonomous treatment prescription without human physician/expert oversight, or non-public administrative data scraping.

## 6. Limitations & Attribution
- **Covariate Dependency:** Model outputs depend on the spatial granularity of ingested CHIRPS, NDVI, and DHS biomarker layers; micro-regions outside telemetry tracking require field verification.
- **Attribution Notice:** This model is a specialized derivative of N-ATLaS, an initiative of the Federal Ministry of Communications, Innovation and Digital Economy, powered by Awarri Technologies.
