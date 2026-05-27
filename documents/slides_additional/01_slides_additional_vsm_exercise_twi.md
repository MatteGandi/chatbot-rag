---
type: slides_additional
chapter: 01
topic: vsm_exercise_twi
priority: 3
description: Appunti e slide aggiuntive sul corso. Priorità inferiore alle slide ufficiali e alle trascrizioni. In caso di discrepanza prevalgono le slide ufficiali.
---

# 1. Value Stream Mapping – Exercise (Firm TWI)

## 1.1 Objective of the Exercise
This exercise applies the **Value Stream Mapping (VSM)** formalism to a real‑like industrial case.  
The goal is to:
- translate a textual description into a VSM diagram,
- identify material flows, information flows, and inventories,
- compute lead time and value‑added time,
- justify modeling assumptions.

---

# 2. Company Context

## 2.1 Firm Description
- **Firm:** TWI  
- **Product:** Steering arms for tractors  
- **Working calendar:**  
  - 20 working days per month  
  - 2 shifts per day  
  - 8 hours per shift  
  - 2 breaks of 15 minutes per shift  

This information is used to compute **operator availability**.

---

# 3. Customer Information

## 3.1 Demand and Logistics
- Monthly demand: **24,000 units**
- Shipments: **once per day by truck**
- Purchase forecast: **60 days**
- Firm orders: **2 weeks before delivery**

---

# 4. Production Control and Planning

## 4.1 Internal Planning
- Weekly production schedule
- Weekly orders to suppliers
- Daily shipping plan for logistics

Information flow assumptions:
- External information exchanges are automated (ERP/MRP)
- Internal scheduling involves human intervention (manual information flow)

---

# 5. Supplier Information

## 5.1 Suppliers
Two different suppliers provide raw materials:
1. **Michigan Steel** – steel bars
2. **Indiana Casting** – raw joints

Common supplier characteristics:
- Deliveries: **2 times per month by truck**
- Guaranteed initial stock: **20 days**

Suppliers can be modeled:
- separately (recommended),
- or merged if parameters are identical.

---

# 6. Material Flow – Technological Processes

## 6.1 Parallel Initial Processes

### Bar Cutting
- Cycle time: **15 s**
- Changeover time: **–**
- Uptime: **100%**
- Operators: **1**
- Operator availability: **27,000 s/shift**
- Inventory before process: **20 days**

### Joint Finishing
- Cycle time: **30 s**
- Changeover time: **2 h**
- Uptime: **100%**
- Operators: **1**
- Operator availability: **27,000 s/shift**
- Inventory before process: **20 days**

These two processes are executed **in parallel**.

---

## 6.2 Welding Operations

### First Welding
- Cycle time: **30 s**
- Changeover time: **1 h**
- Uptime: **90%**
- Operators: **1**
- Inventory before process: **5 days**

### Second Welding
- Cycle time: **30 s**
- Changeover time: **1 h**
- Uptime: **80%**
- Operators: **1**
- Inventory before process: **3 days**

---

## 6.3 Subsequent Processes

### Boring
- Uptime: **100%**
- Operators: **1**
- Inventory before process: **3 days**

### Painting (Outsourced)
- External process
- Lead time: **2 days**
- Considered **non‑value‑added**
- Inventory before process: **5 days**

### Assembly
- Cycle time: **195 s**
- Changeover time: **10 min**
- Uptime: **100%**
- Operators: **6**
- Inventory before process: **6 days**

### Shipping
- Inventory before shipping: **4 days**
- Transport to customer: **daily by truck**

---

# 7. Information Flow Representation

## 7.1 External Information Flows (Electronic)
- Customer → Company:
  - 60‑day forecast
  - Bi‑weekly firm orders
- Company → Suppliers:
  - Weekly orders

## 7.2 Internal Information Flows (Manual)
- Production control → processes:
  - Weekly production schedule
- Production control → shipping:
  - Daily shipping plan

The internal system can be labeled as **MRP**.

---

# 8. Timeline Construction

## 8.1 Non‑Value‑Added Time (Upper Timeline)
- Initial inventories: **20 days**
- Post‑cutting inventory: **5 days**
- Post‑welding inventories: **3 days**
- Pre‑painting inventory: **5 days**
- Painting (outsourced): **2 days**
- Pre‑assembly inventory: **6 days**
- Pre‑shipping inventory: **4 days**

## 8.2 Value‑Added Time (Lower Timeline)
- Bar cutting / joint finishing: **max(15 s, 30 s)**
- First welding: **30 s**
- Second welding: **30 s**
- Assembly: **195 s**

---

# 9. Performance Indicators

## 9.1 Total Lead Time
- **Total production lead time:** ≈ **48 days**

## 9.2 Total Value‑Added Time
- Sum of processing times only (seconds)
- Negligible compared to total lead time

---

# 10. Modeling Notes and Assumptions
- Parallel processes use the **maximum processing time** in the timeline.
- Outsourced processes are treated as **non‑value‑added**.
- Inventories may be merged or separated depending on interpretation.
- Assumptions are acceptable if explicitly stated.

---

# 11. Key Takeaway
This exercise shows how Value Stream Mapping:
- reveals the dominance of non‑value‑added time,
- supports comparison between current and future states,
- provides a structured basis for Lean improvement decisions.
