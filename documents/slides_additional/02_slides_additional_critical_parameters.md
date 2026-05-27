---
type: slides_additional
chapter: 02
topic: critical_parameters
priority: 3
description: Appunti aggiuntivi sul corso. In caso di discrepanza prevalgono le slide ufficiali.
---

# 2.3 Critical Parameters of Production Lines

## 2.3.1 Introduction
This section introduces the **critical parameters** used to analyze the performance of production lines.
These parameters allow us to:
- determine the **best achievable performance** of a system,
- compare optimal conditions with actual factory behavior,
- identify inefficiencies and improvement potential.

The analysis builds on the relationships between **WIP, throughput, and cycle time**.

---

# 2.3.2 Definition of Critical Parameters

Three critical parameters characterize a production line:

## Bottleneck Rate (Rᵦ)
- Defined as the **throughput of the bottleneck workstation**.
- The bottleneck is the workstation with the **lowest capacity**.
- Rᵦ represents the **maximum achievable throughput** of the line.

---

## Raw Process Time (T₀)
- Defined as the **sum of the average processing times** of all workstations.
- Represents the **minimum possible cycle time**.
- No job can exit the system faster than T₀.

---

## Critical WIP (W₀)
- Defined as:
```
W₀ = Rᵦ · T₀
```
- Represents the minimum WIP level required to achieve:
  - maximum throughput,
  - minimum cycle time.

---

# 2.3.3 Example 1 – Balanced Production Line

### System Description
- 4 machines in series
- Each machine has:
  - processing time = 2 hours
  - capacity = 1 / 2 = 0.5 jobs/hour
- No failures, no scrap, immediate transfer

### Critical Parameters
- Bottleneck rate:
```
Rᵦ = 0.5 jobs/hour
```
- Raw process time:
```
T₀ = 2 + 2 + 2 + 2 = 8 hours
```
- Critical WIP:
```
W₀ = 0.5 · 8 = 4 jobs
```

This is a **balanced line**, since all machines have the same capacity.

---

# 2.3.4 Example 2 – Unbalanced Line with Parallel Machines

### System Description
Four workstations in series:
- WS1: 1 machine, 2 h
- WS2: 2 machines, 5 h
- WS3: 6 machines, 10 h
- WS4: 2 machines, 3 h

### Workstation Capacities
Capacity of each workstation is the **sum of machine capacities**:
- WS1: 0.5 jobs/h
- WS2: 0.4 jobs/h
- WS3: 0.6 jobs/h
- WS4: 0.67 jobs/h

### Critical Parameters
- Bottleneck: WS2
```
Rᵦ = 0.4 jobs/hour
```
- Raw process time:
```
T₀ = 2 + 5 + 10 + 3 = 20 hours
```
- Critical WIP:
```
W₀ = 0.4 · 20 = 8 jobs
```

---

# 2.3.5 Industrial Example – Performance Comparison

Given:
- Bottleneck rate: 114 parts/hour
- Raw process time: 33.9 hours
- Critical WIP:
```
W₀ ≈ 3869 units
```

Actual performance:
- Throughput: 71.8 parts/hour
- WIP: 47,600 units
- Cycle time: 663 hours

### Interpretation
- Throughput ≈ 63% of maximum
- WIP ≈ 12 × critical WIP
- Cycle time ≈ 24 × raw process time

The system performs **far from optimal conditions**.

---

# 2.3.6 Relationship Between WIP, CT, and TH

Let:
- W = WIP level

Then:

### Cycle Time
```
CT(W) = T₀            if W ≤ W₀
CT(W) = W / Rᵦ        if W > W₀
```

### Throughput
```
TH(W) = W / T₀        if W ≤ W₀
TH(W) = Rᵦ            if W > W₀
```

---

# 2.3.7 Interpretation of the Curves

- For W ≤ W₀:
  - Throughput increases linearly
  - Cycle time remains minimal

- For W > W₀:
  - Throughput saturates at Rᵦ
  - Cycle time increases linearly with W

This region corresponds to **congestion**.

---

# 2.3.8 Exam-Style Exercise (Solved)

### Given
Three workstations in series with processing times:
- 3 min
- 2 min
- 4 min

### Solution
- Capacities:
  - WS1: 0.33 jobs/min
  - WS2: 0.5 jobs/min
  - WS3: 0.25 jobs/min
- Bottleneck:
```
Rᵦ = 0.25 jobs/min
```
- Raw process time:
```
T₀ = 3 + 2 + 4 = 9 min
```
- Critical WIP:
```
W₀ = 0.25 · 9 = 4.5 jobs
```

### Behavior for W > W₀
- Throughput remains constant at Rᵦ
- Cycle time increases as W / Rᵦ

---

# 2.3.9 Key Takeaways
- Critical parameters define **optimal system performance**.
- Bottleneck determines maximum throughput.
- Excess WIP increases cycle time without increasing throughput.
- Comparing actual vs critical values reveals inefficiencies.
