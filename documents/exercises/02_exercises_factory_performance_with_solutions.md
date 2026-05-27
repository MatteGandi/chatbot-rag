---
type: exercises
chapter: 01
topic: flow_process_chart_vsm_idef0
priority: 2
description: Esercitazione ufficiale con soluzioni complete. FPC (pallet), VSM (DueDi boiler), IDEF0 (technical due diligence).
---

# Process Representation Formalisms (Flow Process Chart, VSM, IDEF0)

---

## Exercise 1 – Pallet Production Process

*Represent the following process with the Flow Process Chart diagram formalism.*

The considered industrial process is the manufacturing and assembly of a transport metal pallet. The pallet is made of three different parts: **metal sheet**, **profile**, and **frame**. Each part of the pallet is manufactured by a sequence of stations.

Particularly:
- Each **sheet** performs the operations of: cutting, corner cutting, and bending.
- Each **profile** performs the operations of: cutting, incision, drilling, and welding.
- Each **frame** performs the operations of: angle cutting and cup welding.

Then, the sheets and the profiles are welded together through **side welding** and **bottom welding** operations. Finally, the frames are welded with the operations of **building up** and **final assembly** to produce the final pallet.

### Table 1 – Manufacturing Tasks

| Task | Task Description     | Time steady-state γ [sec] | Workstation |
|------|----------------------|---------------------------|-------------|
| mt1  | Sheet cutting        | 40                        | s2          |
| mt2  | Sheet corners cutting| 652                       | s3          |
| mt3  | Sheet bending        | 624                       | s4          |
| mt4  | Profile cutting      | 349                       | s5          |
| mt5  | Profile incision     | 504                       | s6          |
| mt6  | Holes drilling       | 1026                      | s7          |
| mt7  | Angles cutting       | 16                        | s8          |
| mt8  | Cup welding          | 192                       | s9          |
| mt9  | Frame welding        | 304                       | s10         |
| mt10 | Sides welding        | 416                       | s11         |
| mt11 | Bottoms welding      | 120                       | —           |
| mt12 | Building-up          | 1187                      | —           |
| mt13 | Assembly             | 1212                      | —           |

### Solution – Flow Process Chart

The Flow Process Chart has **three parallel branches** (one per part type) that converge into a shared assembly sequence.

**Branch 1 – Sheets:**
1. Raw material inventory: Sheets (triangle symbol)
2. Storage S2 (arrow/storage symbol)
3. M1 – Sheet Cutting (40s) → circle operation symbol
4. Storage S3
5. M2 – Corner Cutting (652s)
6. Storage S4
7. M3 – Sheet Bending (624s)
8. → Flow to S11 (side welding station)

**Branch 2 – Profiles:**
1. Raw material inventory: Profiles (triangle symbol)
2. Storage S5
3. M4 – Profile Cutting (349s)
4. Storage S6
5. M5 – Incision (504s)
6. Storage S7
7. M6 – Hole Drilling (1026s)
8. Storage S10
9. M9 – Profile Welding (304s)
10. → Flow to S11

**Branch 3 – Frames:**
1. Raw material inventory: Frames (triangle symbol)
2. Storage S8
3. M7 – Angles Cutting (16s)
4. Storage S9
5. M8 – Cup Welding (192s)
6. → Flow to S11

**Convergence – Assembly:**
1. Storage S11 (sheets + profiles + frames converge here)
2. M10 – Sides Welding (416s)
3. M11 – Bottoms Welding (120s)
4. (Frames join here)
5. M12 – Building-Up (1187s)
6. M13 – Final Assembly (1212s)
7. Final Warehouse (storage symbol)
8. Finished Product (triangle symbol)

**Symbols used in Flow Process Chart:**
- ▽ (inverted triangle) = Inventory / raw material storage
- ▷ (arrow/pentagon) = Storage buffer between stations
- ○ (circle) = Operation / manufacturing task
- → (arrow) = Transport / material flow

---

## Exercise 2 – Assembly Process of the External Body of a Boiler

*Represent the following process with the Value Stream Mapping (VSM) formalism.*

### Process Description

**Company:** DueDi Srl produces the external body of a boiler.

**Information flows:**
- The **Production Controller** manages the production line through **weekly programming**.
- The same office manages **daily orders** from the customer and sends **monthly forecasts** to the supplier.
- **Purchase orders** are sent to the supplier **weekly**.
- A **monthly forecast** is also sent to the supplier.

**Supplier:** Bertero & Partners
- Delivers **every week** the components needed to make **450 boilers** in batches of 50.
- Average wait time in input warehouse before processing: **2 days**.

**Customer:** DueDi Srl (different plant – assembly and final quality control)
- **90 manufactured bodies** delivered every day by trucks.
- Each truck contains **9 pallets**, each pallet contains **10 boxes**, each box contains **1 body**.
- Delivery frequency: **1x per day**.

### Production Process Stages

| Stage            | C/T [s] | C/O [s] | Uptime | Operators | Buffer before |
|------------------|---------|---------|--------|-----------|---------------|
| Assembly         | 60      | 0       | 95%    | 3         | 2 days (input WH) |
| Welding          | 39      | 0       | 100%   | 2         | 1 day         |
| Painting         | 360     | 300     | 100%   | 1         | 5 min (transport) |
| Final Assembly   | 180     | 0       | 95%    | 2         | 3 days        |
| Quality Control  | 340     | 45      | 90%    | 1         | 50s (incl. transport) |
| Shipment/WH      | —       | —       | —      | —         | 2 days        |

**Legend:**
- C/T = Cycle Time
- C/O = Changeover / Setup Time
- Uptime = Machine availability

### VSM Key Metrics

- **Production Lead Time** = 2 days + 1 day + 5 min + 3 days + 50s + 2 days ≈ **8 days + ~22 min**
- **Value Added Lead Time** = 60s + 39s + 300s + 180s + 340s + 0s = **979s**

### VSM Structure (described)

**Top row (information flow):**
- Bertero & Partners ←→ Production Controller ←→ DueDi Srl (customer)
- Weekly production – monthly forecast (left arrow)
- Daily production – monthly forecast (right arrow)
- Weekly Production Plan (push scheduling box)

**Bottom row (material flow, left to right):**
1. Supplier icon → Input Inventory (450 pcs) → [2 days buffer]
2. **Assembly** (C/T=60s, C/O=0s, Uptime=95%, 3 operators) → [1 day buffer, 90 pcs]
3. **Welding** (C/T=39s, C/O=0s, Uptime=100%, 2 operators) → [5 min transport, push arrow]
4. **Painting** (C/T=360s, C/O=300s, Uptime=100%, 1 operator) → [3 days buffer, 270 pcs]
5. **Final Assembly** (C/T=180s, C/O=0s, Uptime=95%, 2 operators) → [50s buffer, 180 pcs]
6. **Quality Control** (C/T=340s, C/O=45s, Uptime=90%, 1 operator) → [2 days buffer]
7. **Shipment** → Customer icon (DueDi Srl, 1x/day, 9 pallets/truck, 10 items/pallet)

**Timeline (bottom):**
```
[2d] [60s] [1d] [39s] [5min] [300s] [3d] [180s] [50s] [340s] [2d] [0s]
```

---

## Exercise 3 – Realization of a Technical Due Diligence

*Represent the following process with the IDEF0 formalism.*

### Color Legend used in the exercise:
- 🟩 **Green** = Activity
- 🟪 **Pink/Magenta** = Resources
- 🟦 **Blue** = Controls
- 🟨 **Yellow** = Input
- 🟧 **Orange** = Output

### Process Description

**Introduction (Node 0 – Context):**
The drafting of a **technical due diligence** is requested by a **client** (buyer or seller of a building/property) to a consulting company, in order to evaluate the regulatory and maintenance status of a property.

The consulting firm uses:
- A **Transferability Team**: deals with structural and urban issues.
- A **Facilities Team**: deals with plant and environmental issues.

The output of the process is a **report** to be delivered within a **deadline set by the client**. Before drafting the report, a property assessment must be carried out.

---

### Node 0 – Technical Due Diligence Redaction

| IDEF0 Element | Content |
|---------------|---------|
| **Controls** (top) | Customer Request, Deadline, Plans, Document List |
| **Inputs** (left) | Documentation |
| **Outputs** (right) | List of Missing Documentation, Questions, CapEx Hypothesis, Conformity Opinion List |
| **Resources/Mechanisms** (bottom) | Transferability Team, Facility Team |
| **Activity box** | Technical Due Diligence Redaction |

---

### Node A0 – Technical Due Diligence Redaction (Level 2 decomposition)

This node decomposes the main activity into two sub-activities:

**Sub-activity A1 – Facility Analysis:**
- Inputs: Documentation
- Controls: Customer Request, Plans, Document List
- Mechanisms: Transferability Team, Facility Team
- Outputs: Photos, Technical Observations, Selected Documentation → feed into A2

**Sub-activity A2 – Report Redaction:**
- Inputs: Photos, Technical Observations, Selected Documentation (from A1)
- Controls: Deadline
- Mechanisms: Facility Team
- Outputs: CapEx Hypothesis, Conformity Opinion List
- Also outputs: List of Missing Documentation, Questions

---

### Node A1 – Facility Analysis (Level 3 decomposition)

**Level 3 description:** An on-site visit is organized to evaluate the property. The visit requires participation of both expert teams. Detailed notes are taken using property plans, and photographs are taken. The visit produces:
- **Observations** to be reported
- **Questions** to be posed to the client about unclear aspects

In parallel, the property owner provides **documentation**. The teams analyze it to identify **missing documentation** based on a required documentation list.

This node decomposes into two sub-activities:

**Sub-activity A11 – Facility Inspection:**
- Controls: Customer Request, Plans
- Mechanisms: Transferability Team, Facility Team
- Outputs: Photos, Questions, Observations

**Sub-activity A12 – Document Analysis:**
- Inputs: Documentation
- Controls: Document List
- Mechanisms: Facility Team
- Outputs: Selected Documentation, List of Missing Documentation

---

### Node A2 – Report Redaction (Level 2 detail)

**Level 2 description:** Based on available documentation and on-site visit results (observations and photographs), assessments are made in three areas:
1. **Transferability**
2. **Facilities**
3. **Environment**

For each area:
- **CapEx (Capital Expenditure)** is hypothesized
- A **conformity opinion** is formulated

The conformity opinions of all three areas are consolidated into the **final report**.

---

### IDEF0 Diagram Summary Table

| Node | Title | Diagram N° |
|------|-------|------------|
| Node 0 | Technical Due Diligence Redaction (context) | N.1 |
| Node A0 | Technical Due Diligence Redaction (decomposed) | N.2 |
| Node A1 | Facility Analysis | N.3 |

---

*End of document – Process Representation Formalisms exercises (Flow Process Chart, VSM, IDEF0)*
