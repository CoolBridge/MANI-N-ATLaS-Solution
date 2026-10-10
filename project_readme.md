# MANI (Malaria Atlas Nigeria): AI-Native Public Health Intelligence Platform
Submitted for the **NCAIR National AI Innovation Challenge (NAIC)**.

## 1. Executive Summary & Core Thesis
Malaria control in high-burden sub-Saharan environments suffers from an institutional execution gap: the latency between environmental data generation and grassroots tactical deployment. While massive stores of satellite telemetry, meteorological data, historical case logs, and biological survey records exist, they remain siloed across disparate geographical information systems (GIS), Excel sheets, and academic papers. Public health agencies and implementing partners operate reactively, deploying finite resources after transmission spikes have already saturated local clinics.

**MANI (Malaria Atlas Nigeria)** solves this by engineering an AI-native public health intelligence platform. Moving far beyond generic consumer chatbots, MANI bridges heavy epidemiological data engineering with sovereign AI model adaptation, integrating multi-source geospatial telemetry and **Demographic and Health Survey (DHS) biomarker data** to deliver hyper-localized, actionable intelligence to institutional managers and frontline health workers in native Nigerian languages.

---

## 2. Product Architecture & Technical Stack
MANI’s architecture is structured as a multi-tier, API-first system designed for extreme reliability, low-latency edge deployment, and sovereign data integrity.

```text
┌─────────────────────────────────────────────────────────────────────────┐
│                          DATA INGESTION TIER                            │
│  - CHIRPS (Precipitation)      - NDVI (Vegetation / Vector Habitats)    │
│  - DHS Biomarker Data          - HMIS Surveillance & Vector Records     │
└────────────────────────────────────┬────────────────────────────────────┘
                                     ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                       NORMALIZATION & STORAGE TIER                      │
│  - Normalized Cluster-Year Spatial & Biological Database                │
│  - Automated Geospatial Feature Extraction & Alignment                  │
└────────────────────────────────────┬────────────────────────────────────┘
                                     ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                      INTELLIGENCE & MODEL CORE                          │
│  - N-ATLAS Specialized Derivative (Fine-Tuned for Epidemiological Logic)│
│  - 500+ Example Public-Health Evaluation Benchmark (Hallucination Guard)│
│  - Multilingual & ASR Engine (English, Hausa, Igbo, Yoruba, Pidgin)     │
└────────────────────────────────────┬────────────────────────────────────┘
                                     ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                        DELIVERY & INTERFACE TIER                        │
│  - RESTful API & Institutional Dashboard                                │
│  - Cloudflare Edge Infrastructure (Low-Latency, Secure Access)          │
│  - Voice/USSD/WhatsApp Integration for Frontline Health Workers         │
└─────────────────────────────────────────────────────────────────────────┘
```

- **Data Layer & Normalization**: Ingests real-time CHIRPS rainfall, MODIS/Landsat NDVI vector habitat data, and **DHS biomarker layers** (RDT parasitemia, anemia testing, and ITN usage metrics) into standardized cluster-year grid cells.
- **Model Adaptation (N-ATLAS Derivative)**: Fine-tunes the sovereign N-ATLAS model to comprehend Nigerian administrative hierarchies (LGAs, Wards) and complex epidemiological/biomarker correlation logic.
- **Multilingual & ASR Core**: Supports native processing across Hausa, Igbo, Yoruba, and Nigerian-accented English, complete with voice-note integration for frontline workers.
- **Edge Deployment**: Utilizes Cloudflare edge networks for sub-second, secure access in low-bandwidth regional health offices.

---

## 3. Operational Workflows & Use-Case Matrix

| Stakeholder Segment | Core Operational Pain Point | How MANI Solves It | Measurable Impact |
| :--- | :--- | :--- | :--- |
| **Malaria Program Managers & Partners** | Reactive deployment; lack of predictive visibility at ward level. | Automated hotspot forecasting driven by climatic and DHS biomarker risk models. | Reduction in stock-outs; higher intervention efficacy per naira spent. |
| **State Health Agencies & NMEP** | Fragmented reporting silos, paper-based delays, and inconsistent formats. | Unified API intelligence stack consolidating climate, vector, biomarker, and case data. | Real-time sovereign oversight and auditability across zones. |
| **Community Health Workers (CHEWs)** | Language barriers and cumbersome desktop software unsuited for field use. | Multilingual, voice-first (ASR) mobile and USSD accessibility in local languages. | Immediate adoption at the grassroots level without technical training. |
| **International Donors & NGOs** | Difficulty quantifying program ROI and verifying high-risk target selection. | Rigorously benchmarked risk-reduction models and automated impact reporting. | Transparent justification of funding allocations and institutional confidence. |

---

## 4. Strategic Scalability Roadmap
- **Phase 1 (Nigerian Beachhead):** Anchor within Nigeria—the world's highest burden market—via state health ministries and the NMEP.
- **Phase 2 (Digital Twin Architecture):** Evolve static intelligence into a dynamic national-scale malaria digital twin for multi-variable policy and climate simulations.
- **Phase 3 (Regional Sub-Saharan Replication):** Scale horizontally across West and Central Africa to target broader vector-borne disease landscapes.

## Attribution & License
MANI is built upon **N-ATLaS**, an initiative of the **Federal Ministry of Communications, Innovation and Digital Economy**, powered by **Awarri Technologies**.