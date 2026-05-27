---
type: slides_additional
chapter: 01
topic: vsm_theory
priority: 3
description: Appunti e slide aggiuntive sul corso. Priorità inferiore alle slide ufficiali e alle trascrizioni. In caso di discrepanza prevalgono le slide ufficiali.
---

# 1. Value Stream Mapping (VSM) – Theory

## 1.1 Introduction
Value Stream Mapping (VSM) is the second formalism introduced for representing **material processes**.  
Although it primarily focuses on material flows, it also allows the representation of **high-level information flows** between:
- the company,
- its suppliers,
- its customers,
- and internal production control.

VSM was introduced in the 1980s by Japanese engineers working at **Toyota** and is a core tool of **Lean Manufacturing**.

---

# 2. Lean Philosophy Context

## 2.1 Lean Manufacturing
Lean Manufacturing is a production philosophy aimed at:
- reducing waste,
- eliminating non-value-added activities,
- improving overall process efficiency.

## 2.2 Role of Value Stream Mapping
Value Stream Mapping is a **diagnostic tool** used to:
- distinguish value-added vs non-value-added activities,
- visualize the entire production process at a high level,
- identify improvement opportunities.

---

# 3. Purpose of Value Stream Mapping

VSM is used to:
- represent the **current state** of a production system,
- analyze value-added and non-value-added activities,
- design and compare a **future state** with improved performance.

This logic is analogous to the *As-Is* and *To-Be* comparison previously introduced with the Flow Process Chart.

---

# 4. Structure of a Value Stream Mapping Diagram

A Value Stream Mapping diagram is divided into **three main sections**:

## 4.1 Central Section – Material Flow
- Represents the flow of materials inside the company.
- Starts from raw material arrival and ends with delivery to the customer.
- Includes only **technological processes** (e.g. cutting, welding, milling).
- Shows inventory accumulation points.

## 4.2 Upper Section – Information Flow
- Represents high-level information exchanges.
- Includes:
  - orders,
  - forecasts,
  - production planning and scheduling.
- Does not describe detailed information processes (other formalisms are used for that).

## 4.3 Lower Section – Timeline
- Represents time consumption across the process.
- Divided into:
  - **value-added time** (processing),
  - **non-value-added time** (waiting, inventory, transport).
- Used to compute total production lead time and total value-added time.

---

# 5. Key Characteristics of VSM

## 5.1 High-Level Representation
- Shows the whole process without detailing individual tasks.
- Complements analytical and quantitative models used later.

## 5.2 Waste Identification
- Helps identify where waste occurs.
- Does not directly identify causes, but highlights critical areas.

## 5.3 Common Language
- Provides a shared representation of production processes.
- Widely used in manufacturing and logistics contexts.

## 5.4 Link Between Material and Information Flows
- One of the few formalisms that explicitly connects material and information flows.

## 5.5 Qualitative but Time-Aware
- Mainly qualitative.
- Includes time information sufficient to compute lead times and efficiency indicators.

---

# 6. Main Symbols in Value Stream Mapping

## 6.1 External Entities (Supplier / Customer)
- Represented by an external factory symbol.
- Used for suppliers and customers.

### Data Box (External)
Contains information such as:
- order frequency,
- delivery frequency,
- lot size,
- material characteristics.

---

## 6.2 Process
- Represented by a rectangular box.
- Refers to **technological processes**, not entire business processes.

### Data Box (Process)
Includes:
- **Cycle Time (CT)**: processing time only (not waiting or setup).
- **Changeover Time (CO)**: setup time.
- **Uptime**: percentage of time the machine is operational.
- **Shifts / operator availability**.
- **Number of operators** (if manual activation is required).

Note:
In VSM, *cycle time* means only **effective processing time**, not total lead time.

---

## 6.3 Operators
- Represented by a specific operator icon.
- Indicates manual operation of the process.
- The number of operators is specified.

---

## 6.4 Inventory
- Represented by a triangle.
- Indicates accumulation points (buffers).
- Usually placed before processes.

Inventory data can be expressed as:
- average number of items,
- or average waiting time.

---

## 6.5 Material Flow Arrows

### Internal Flow (Push System)
- Represented by a **solid arrow**.
- Items move to the next process regardless of downstream status.

### External Flow
- Represented by a **white arrow**.
- Used between supplier–company and company–customer.

Transport mode (truck, ship, train, plane) and frequency can be specified.

---

# 7. Push vs Pull Systems

## 7.1 Push System
- Production is triggered upstream.
- Items are sent forward regardless of downstream congestion.
- This course focuses mainly on push systems.

## 7.2 Pull System
- Downstream stations authorize upstream production.
- Represented with different symbols (not covered here).

---

# 8. Information Flow Representation

## 8.1 Manual Information Flow
- Represented by a straight arrow.
- Involves human interaction (calls, emails, meetings).

## 8.2 Electronic Information Flow
- Represented by a lightning arrow.
- Fully automated (ERP systems, forecasting tools).

Each arrow is labeled with the type of information exchanged
(e.g. monthly orders, weekly scheduling).

---

# 9. Timeline Interpretation

## 9.1 Structure
- Lower part: **value-added time**.
- Upper part: **non-value-added time**.

## 9.2 Interpretation
- Waiting, transport, and inventory times are non-value-added.
- Processing times are value-added.

## 9.3 Performance Insight
- Often, total lead time is dominated by non-value-added time.
- This highlights improvement potential.

Example:
- Total production time: 14 days.
- Total value-added time: ~500 seconds.

---

# 10. Method to Build a Value Stream Map

1. Identify technological processes.
2. Add suppliers and customers with data boxes.
3. Define material flow and inventories.
4. Specify transport modes and frequencies.
5. Insert the timeline and compute times.
6. Add information flows.
7. Analyze current state.
8. Design and compare future state.

---

# 11. Key Takeaway
Value Stream Mapping is a powerful Lean tool that:
- visualizes the entire production system,
- highlights inefficiencies,
- links material and information flows,
- supports structured process improvement.
