---
type: slides_additional
chapter: 01
topic: idef0_example_breakfast
priority: 3
description: Appunti e slide aggiuntive sul corso. Priorità inferiore alle slide ufficiali e alle trascrizioni. In caso di discrepanza prevalgono le slide ufficiali.
---

# 1. IDEF0 – Example  
## Breakfast Distribution in a Hospital Department

## 1.1 Purpose of the Example
This example illustrates how to model a **real operational process** using the **IDEF0 formalism**, applying:
- functional decomposition,
- hierarchical consistency,
- explicit identification of inputs, outputs, controls, and resources (ICOM).

The process is modeled using **no more than two levels of detail**, to clearly demonstrate the hierarchical logic of IDEF0.

---

# 2. Process Description (Textual Summary)

Breakfast is served every morning in a hospital department.  
Breakfast consists of:
- liquid food (milk, tea, coffee),
- dry food (cookies, croissants),
- jams and sugar.

Breakfast is transported using **wheeled cabinets**:
- In the evening, cabinets are filled with dry food.
- In the morning, liquid food is heated in the kitchen and placed in thermos inside the cabinets.
- Breakfast is delivered to patients by distribution staff.
- Cabinets are transported via elevator.
- After delivery, cabinets are brought back to the kitchen and washed for reuse.

---

# 3. Level 0 Diagram – A0

## 3.1 Activity
**A0 – Breakfast Preparation and Distribution**

This diagram represents the **entire process** as a single macro-activity.

### Inputs
- Dry food  
- Liquid food  
- Jams  
- Sugar  

### Outputs
- Breakfast served to patients  
- Clean cabinets  

### Controls
- Preparation instructions  
- Distribution instructions  
- Washing instructions  

### Resources (Mechanisms)
- Cabinets  
- Hospital staff  
- Elevator  
- Dishwasher  
- Kitchen tools  

> Note: Some controls are not explicitly mentioned in the text but are **reasonably assumed**, as allowed in IDEF0 modeling.

---

# 4. Level 1 Diagram – Decomposition of A0

## 4.1 Expanded Activities
Activity **A0** is decomposed into three sub-activities:

- **A1 – Food Preparation**
- **A2 – Breakfast Distribution**
- **A3 – Cabinet Washing**

---

## 4.2 Activity A1 – Food Preparation

### Inputs
- Dry food  
- Liquid food  
- Jams  
- Sugar  

### Output
- Cabinets filled with breakfast  

### Controls
- Preparation instructions  

### Resources
- Preparation staff  
- Cabinets  
- Kitchen tools  

---

## 4.3 Activity A2 – Breakfast Distribution

### Input
- Cabinets filled with breakfast  

### Outputs
- Breakfast served to patients  
- Cabinets to be cleaned  

### Controls
- Distribution instructions  

### Resources
- Distribution staff  
- Elevator  

---

## 4.4 Activity A3 – Cabinet Washing

### Input
- Cabinets to be cleaned  

### Output
- Clean cabinets  

### Controls
- Washing instructions  

### Resources
- Washing staff  
- Dishwasher  

---

# 5. Level 2 Diagram – Decomposition of A1 (Food Preparation)

## 5.1 Expanded Activities
Activity **A1 – Food Preparation** is further decomposed into:

- **A1.1 – Dry Food Preparation**
- **A1.2 – Liquid Food Preparation**

---

## 5.2 Activity A1.1 – Dry Food Preparation

### Inputs
- Dry food  
- Jams  
- Sugar  

### Output
- Cabinets with dry food  

### Controls
- Dry food preparation instructions  

### Resources
- Preparation staff  
- Cabinets  

---

## 5.3 Activity A1.2 – Liquid Food Preparation

### Inputs
- Liquid food  
- Cabinets with dry food  

### Output
- Cabinets with breakfast  

### Controls
- Liquid food preparation instructions  

### Resources
- Preparation staff  
- Kitchen tools  

---

# 6. Consistency Checks Between Levels

IDEF0 requires **strict consistency** across hierarchical levels:

- All inputs of A0 must appear as inputs in at least one lower-level activity.
- All outputs generated at lower levels must be reflected in higher-level diagrams.
- Resources and controls must remain coherent across decompositions.

Example:
- *Clean cabinets* appear as an output of A3 and must therefore be included as an output of A0.

---

# 7. Modeling Notes

- Temporal order can be represented by:
  - output → input connections, or
  - output → control connections.
- Decisions are **not explicitly modeled** in IDEF0.
- Reasonable assumptions are acceptable if explicitly stated.
- The goal is **functional clarity**, not operational timing.

---

# 8. Key Takeaway
This example demonstrates how IDEF0:
- decomposes a real process hierarchically,
- enforces semantic rigor through ICOM logic,
- ensures coherence across abstraction levels,
- supports clear functional understanding of service processes.
