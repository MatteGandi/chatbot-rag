---
type: slides_additional
chapter: 02
topic: penny_fab_model
priority: 3
description: Appunti aggiuntivi sul corso. In caso di discrepanza prevalgono le slide ufficiali.
---

# 2.2 Penny Fab Model  
## Single Workstation and Factory-Level Analysis

## 2.2.1 Purpose of the Model
The **Penny Fab Model** is a didactic example used to introduce:
- analytical modeling of production systems,
- performance evaluation using **Little’s Law**,
- the impact of variability and system boundaries.

---

# 2.2.2 Modeling Philosophy
The analytical approach:
- decomposes the factory into simple components,
- models each component separately,
- recomposes the system to analyze global behavior.

This is an approximation of reality and abstracts from operators and transport systems.

---

# 2.2.3 System Boundaries
The analysis focuses only on the factory:
- jobs arrive with known parameters,
- jobs follow a routing,
- completed jobs exit the system.

---

# 2.2.4 Core Definitions

## Workstation
A workstation is a set of identical machines or operators working in parallel.

## Queue
Jobs wait in a queue when machines are busy.

## Routing
The ordered sequence of workstations visited by a job.

---

# 2.2.5 Arrival Process
Jobs may arrive individually or in batches.
Arrival is characterized by the arrival rate λ and its distribution.

---

# 2.2.6 Processing Times
Processing times are random variables with known mean and variability.

---

# 2.2.7 Performance Measures

### Cycle Time (CT)
```
CT = CTQ + E[TS]
```

### Work In Process (WIP)
Average number of jobs inside the system.

### Throughput (TH)
Completed jobs per unit of time.
In steady state:
```
TH = λ
```

---

# 2.2.8 Little’s Law
```
WIP = TH · CT
```

---

# 2.2.9 Key Insights
- Variability generates waiting.
- Waiting dominates cycle time.
- Little’s Law links all KPIs.

---

# 2.2.10 Key Takeaway
The Penny Fab Model shows how simplified analytical models provide deep insight into production system behavior.
