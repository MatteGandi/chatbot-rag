---
type: glossary
chapter: all
topic: glossary_and_routing
priority: 1
description: Glossario completo del corso con mapping concetti-file. Usare per espandere query e collegare termini sinonimi ai file corretti. Fonte autorevole per la definizione dei termini.
---

# AI‑Friendly Glossary for AMPS Chatbot

This glossary maps **concepts, keywords, formulas, and use‑cases** to the **exact files** where they are explained. It is designed to help a chatbot reliably retrieve answers by associating user intents with the correct source file.

---

## 01_slides_official_fpc_vsm_idef0.md

**Scope**: Formalisms for manufacturing process modeling and process representation.

**Key concepts**:
- Process definition (input–output transformation, sequence of activities)
- Product lifecycle perspective (plan, design, implement, support, disposal)
- Communication problems in process description
- Importance of formalism in heterogeneous teams

**Modeling formalisms**:
- Flow Process Chart (symbols, operations, transport, inspection, storage)
- Value Stream Mapping (VSM): material flow, information flow, lead time, value‑added vs non‑value‑added time
- IDEF0 diagrams: functions, inputs, controls, outputs, mechanisms

**Typical questions routed here**:
- “How can I represent a production process graphically?”
- “Difference between VSM and flow chart”
- “What is IDEF0 used for?”

---

## 02_slides_official_introduction_factory_models.md

**Scope**: Foundations of analytical factory modeling.

**Key concepts**:
- Factory as a network of workstations
- Jobs, routings, job types
- Decomposition approach (model → analyze → reintegrate)
- Steady‑state analysis

**Performance measures**:
- Cycle Time (CT, CTs, CT(i))
- Work‑In‑Process (WIP)
- Throughput (TH)
- Relationship between CT, WIP, and TH (Little’s Law)

**Typical questions routed here**:
- “What is cycle time vs lead time?”
- “What is WIP?”
- “What are the main factory performance indicators?”

---

## 03_slides_official_single_workstation_analysis.md

**Scope**: Queueing analysis of a single workstation.

**Key concepts**:
- Deterministic vs stochastic models
- Variability sources (machines, operators, materials, arrivals)
- Random variables and distributions

**Metrics and formulas**:
- Coefficient of Variation (CV)
- Squared Coefficient of Variation (SCV)
- Utilization factor (u)
- Waiting time vs utilization trade‑off

**Models**:
- M/M/1, M/M/c queue intuition
- State‑diagram approach
- Finite capacity systems

**Typical questions routed here**:
- “How does variability affect waiting time?”
- “What is SCV?”
- “How does utilization influence queues?”

---

## 04_slides_official_process_variability.md

**Scope**: Impact and decomposition of processing time variability.

**Key concepts**:
- Natural processing time variability
- Arrival variability vs service variability
- Variability as a hidden capacity loss

**Analytical tools**:
- G/G/1 cycle time approximation
- Role of Ca², Cs², utilization, mean service time

**Operational insights**:
- Variability reduction vs capacity increase
- Decomposition of tasks to reduce variance

**Typical questions routed here**:
- “How can reducing variability reduce cycle time?”
- “What are Ca² and Cs²?”
- “Why variability is equivalent to utilization?”

---

## 05_slides_official_multiple_stage_factory_models.md

**Scope**: Serial production systems and flow variability.

**Key concepts**:
- Flow variability propagation
- Conservation of flow
- Arrival, service, and departure variability

**Formulas and approximations**:
- Whitt approximation for Cd²
- Effect of utilization on departure variability

**Systems**:
- Serial lines as G/G/c networks
- Decomposition of multi‑stage systems

**Typical questions routed here**:
- “How does variability propagate downstream?”
- “What determines departure variability?”
- “How to model a serial production line?”

---

## 06_slides_official_multiple_product_factory_models.md

**Scope**: Factories producing multiple products.

**Key concepts**:
- Product types and routing matrices
- Re‑entrant flows
- Flow conservation by product

**Analytical structure**:
- Product‑specific arrival rates (λᵢ,k)
- Routing probability matrices
- Workstation workload calculation

**Service time modeling**:
- Mixture distributions
- Product‑weighted mean and SCV

**Typical questions routed here**:
- “How do multiple products affect workload?”
- “How is service time computed with different products?”
- “What is a re‑entrant flow?”

---

## 07_slides_official_batch_models.md

**Scope**: Modeling batch production and batch transport.

**Key concepts**:
- Batch size (k)
- Batch forming delay
- Trade‑off between setup savings and cycle time

**Batch types**:
- Batch for transport
- Batch for setup sharing

**Formulas**:
- Batch inter‑arrival time
- Batch SCV reduction
- Individual item delay due to batching

**Typical questions routed here**:
- “How does batch size affect cycle time?”
- “What is batch forming time?”
- “Why batching increases WIP?”

---

## 08_slides_official_information_systems.md

**Scope**: Information systems in manufacturing organizations.

**Key concepts**:
- Data vs information
- Information as an intangible asset
- Strategic vs operational benefits

**System components**:
- Enterprise system
- Organizational system
- Information system
- IT system

**Design perspectives**:
- Functional view
- Activity‑level view (Anthony’s pyramid)
- Process‑oriented view

**Typical questions routed here**:
- “What is an information system?”
- “Difference between IS and IT system?”
- “How are information systems classified?”

---

## 09_slides_official_industry_4_0.md

**Scope**: Digital transformation of manufacturing.

**Key concepts**:
- Industrial revolutions (1.0 → 5.0)
- Cyber‑physical systems
- Digitalization and automation

**Enabling technologies**:
- Simulation and Digital Twin
- Industrial IoT
- Augmented Reality
- Collaborative robots (cobots)

**Group Technology**:
- Group Technology (GT): grouping parts and machines based on similarities
- Cellular manufacturing
- Role of GT in Industry 4.0 for flexibility and efficiency

**Typical questions routed here**:
- “What is Industry 4.0?”
- “What is a digital twin?”
- “What is group technology and where is it used?”

---

## Usage note for chatbot

When a user query involves:
- **Variability, queues, utilization** → files 03, 04, 05
- **Multiple products or routings** → file 06
- **Batching** → file 07
- **Process representation** → file 01
- **Digital manufacturing / Industry 4.0 / Group Technology** → file 09

This mapping should be used as the primary routing logic for retrieval‑augmented generation.

