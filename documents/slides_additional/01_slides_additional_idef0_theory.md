---
type: slides_additional
chapter: 01
topic: idef0_theory
priority: 3
description: Appunti e slide aggiuntive sul corso. Priorità inferiore alle slide ufficiali e alle trascrizioni. In caso di discrepanza prevalgono le slide ufficiali.
---

# 1. IDEF0 – Theory

## 1.1 Introduction
IDEF0 is the last formalism introduced in this course.  
It belongs to the **IDEF family** of diagrams, developed within the **ICAM (Integrated Computer Aided Manufacturing)** project.

Different IDEF formalisms exist (IDEF0, IDEF1, IDEF1X, IDEF2, etc.), each designed for specific purposes.  
This section focuses exclusively on **IDEF0**, which is used to build **functional models** of organizations or systems.

---

# 2. Purpose of IDEF0

IDEF0 is used to:
- represent **activities/functions** of a system,
- specify **constraints and controls** between activities,
- describe systems through a **hierarchical decomposition**,
- support functional understanding rather than detailed sequencing.

Compared to previous formalisms, IDEF0 introduces new conceptual elements:
- **controls**
- **resources (mechanisms)**

---

# 3. Key Characteristics

## 3.1 Simple Graphical Language
IDEF0 uses only:
- **boxes** → activities
- **arrows** → relationships

The expressive power comes from the **position** of arrows, not from different symbols.

## 3.2 Textual Emphasis
Each diagram includes:
- a title,
- an identification code (node),
- labeled activities and flows.

## 3.3 Hierarchical Structure
IDEF0 models are **multi-level**:
- high-level diagrams show general functions,
- lower-level diagrams refine activities into more detailed sub-functions.

The model is not a single diagram, but a **set of interconnected diagrams**.

---

# 4. Hierarchical Decomposition Logic

## 4.1 Top-Level Diagram (A0)
- Represents the entire system as **one single activity**.
- This activity is labeled **A0**.

## 4.2 Lower-Level Diagrams
- The activity A0 is decomposed into activities A1, A2, A3, …
- Each of these activities can be further decomposed:
  - A1 → A11, A12, A13
  - A4 → A41, A42, A43

Each diagram explicitly references its **parent activity**, ensuring traceability.

---

# 5. Activity Representation

## 5.1 Activity Box
- Represents a function or activity.
- Labeled with a verb or short description.
- Identified by a unique number in the lower-right corner.

### Constraint
- A maximum of **six activities per diagram** is allowed.
- If more are needed, further decomposition is required.

---

# 6. Arrow Semantics (ICOM Framework)

Each activity is connected by **four types of arrows**, depending on their position.

## 6.1 Input (Left)
- Enters from the **left side**.
- Represents what is **consumed or transformed** by the activity.
- Inputs are modified by the activity.

## 6.2 Output (Right)
- Exits from the **right side**.
- Represents the **result** produced by the activity.

## 6.3 Control (Top)
- Enters from the **top**.
- Represents constraints, rules, or documents.
- Controls are **not consumed**.
- Examples:
  - manuals,
  - production plans,
  - customer requirements.

## 6.4 Resource / Mechanism (Bottom)
- Enters from the **bottom**.
- Represents resources that enable the activity:
  - machines,
  - tools,
  - people,
  - departments.
- Resources are not consumed, only their **time** is used.

---

# 7. Input vs Control: Key Concept

- **Input**: transformed by the activity and becomes part of the output.
- **Control**: consulted but not modified.

Example:
- A work plan:
  - input for a *design* activity (it is modified),
  - control for a *production* activity (it is only consulted).

---

# 8. Parallel Activities

Parallel execution can be represented by:
- connecting the **output** of one activity to the **controls** of multiple activities,
- or by splitting outputs into multiple flows.

This indicates that activities can start independently once a prerequisite output is available.

---

# 9. Examples of Activity Relationships

## 9.1 Sequential Physical Processing
- Drilling → Polishing
- Output of drilling (drilled plate) becomes input of polishing.
- Same control (work cycle) can apply to both activities.

## 9.2 Design vs Production
- Design activity outputs a **work plan**.
- Production activity uses:
  - raw materials as input,
  - work plan as control,
  - machines and operators as resources.

---

# 10. Representing Alternatives (No Decision Symbol)

IDEF0 does **not** include explicit decision symbols.

Alternative outcomes are represented by:
- multiple outputs exiting the same activity.

Example:
- Book received:
  - correct → cataloging activity,
  - incorrect → return to vendor.

The branching is implicit in the outputs.

---

# 11. Modeling Complex Systems

IDEF0 diagrams can include:
- multiple activities,
- several interacting documents,
- departments modeled as resources,
- documents flowing as inputs, outputs, or controls.

The decomposition logic keeps diagrams readable despite complexity.

---

# 12. Advantages of IDEF0

- Clear functional representation.
- Easy to understand even for non-experts.
- Strong support for hierarchical reasoning.
- Useful for:
  - system understanding,
  - responsibility allocation,
  - cost analysis (costs can be aggregated bottom-up).

---

# 13. Key Takeaway
IDEF0 is a **functional modeling formalism** focused on:
- what activities do,
- what they need,
- what constrains them,
- and what they produce.

Its hierarchical nature makes it especially effective for analyzing complex systems at multiple levels of abstraction.
