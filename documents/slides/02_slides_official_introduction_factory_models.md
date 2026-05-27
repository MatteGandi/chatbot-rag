---
type: exercises
chapter: 02
topic: factory_performance_littles_law_bottleneck
priority: 2
description: Esercitazione ufficiale con soluzioni complete. Little's Law, bottleneck analysis, WIP/TH/CT, simulazione.
---

# Factory Analysis

## Key Formulas

**Little's Law:**
```
WIP = TH × CT
```

**Queue time:**
```
CTq = CT - E[Ts]
```

**Throughput (arrival rate):**
```
TH = λ = 1 / E[Ta]
```

**Cycle Time from WIP and TH:**
```
CT = WIP / λ
```

**Station capacity (single machine):**
```
capacity [jobs/min] = 1 / process_time [min]
```

**Station capacity (m identical machines in parallel):**
```
capacity [jobs/min] = m / process_time [min]
```

**Bottleneck rate:**
```
rb = min(station capacities)
```

**Raw process time:**
```
T0 = sum of process times of all workstations (one machine each)
```

**Critical WIP:**
```
W0 = rb × T0
```

**Best-case Throughput (TH_BEST):**
```
TH_BEST(w) = w / T0      if w ≤ W0
TH_BEST(w) = rb           if w > W0
```

**Best-case Cycle Time (CT_BEST):**
```
CT_BEST(w) = T0           if w ≤ W0
CT_BEST(w) = w / rb       if w > W0
```

---

## Exercise 1

**Problem:** A workstation with a single machine has a long-run average WIP of 20 jobs. The average inter-arrival time is 19 minutes, and the average queue time is 6 hours. Find the average processing time per job.

**Given:**
- WIP = 20 jobs
- E[Ta] = 19 minutes = 0.3167 hours → rounded to **0.3 hours** in solution
- CTq = 6 hours

**Solution:**

| Variable | Value | Unit |
|----------|-------|------|
| WIP | 20 | jobs |
| E[Ta] | 19 | minutes |
| E[Ta] | 0.3 | hours |
| CTq | 6 | hours |
| λ = TH = 1/E[Ta] | 3.2 | jobs/hour |
| CT = WIP / TH | 6.33 | hours |
| E[Ts] = CT – CTq | 0.33 | hours |
| E[Ts] | **20** | **min** |

**Answer:** The average processing time per job is **20 minutes**.

---

## Exercise 2

**Problem:** A bakery has WIP = 15 cakes, arrival rate = 3 cakes/hour, and average baking time = 18 minutes. Find the average time a cake spends in the queue.

**Given:**
- WIP = 15 cakes
- λ = 3 cakes/hour
- E[Ts] = 18 minutes = 0.3 hours

**Solution:**
```
CT  = WIP / λ = 15 / 3 = 5 hours
CTq = CT – E[Ts] = 5 – 0.3 = 4.7 hours
```

**Answer:** The average queue time is **4.7 hours**.

---

## Exercise 3

**Problem:** A tech support center has WIP = 10 calls, average processing time = 4 minutes, and average time in system (CT) = 1 hour. Find the average arrival rate.

**Given:**
- WIP = 10 calls
- E[Ts] = 4 minutes = 0.0667 hours
- CT = 1 hour

**Solution:**
```
λ = WIP / CT = 10 / 1 = 10 calls/hour
```

**Answer:** The average arrival rate is **10 calls/hour**.

---

## Exercise 4

**Problem:** Serial production system with 3 workstations and constant WIP = 5 jobs. Processing times (hours): W1 = 2h, W2 = 3h, W3 = 1h. Initial state: (5, 0, 0). Simulate 15 hours and compute cycle times for first 4 completed jobs.

**System layout:**
```
→ [W1: 2h] → [W2: 3h] → [W3: 1h] → out
         ↑ new jobs enter
```

**Notation (a, b):**
- **a** = total number of jobs in workstation (queue + being processed)
- **b** = elapsed processing time for the job currently being processed

### Simulation Table – Detailed State (a,b) format

| Time  | W1     | W2     | W3     | WIP |
|-------|--------|--------|--------|-----|
| 00:00 | (5,0)  | (0,0)  | (0,0)  | 5   |
| 01:00 | (5,1)  | (0,0)  | (0,0)  | 5   |
| 02:00 | (4,0)  | (1,0)  | (0,0)  | 5   |
| 03:00 | (4,1)  | (1,1)  | (0,0)  | 5   |
| 04:00 | (3,0)  | (2,2)  | (0,0)  | 5   |
| 05:00 | (3,1)  | (1,0)  | (1,0)  | 5   |
| 06:00 | (3,0)  | (2,1)  | (0,0)  | 5   |
| 07:00 | (3,1)  | (2,2)  | (0,0)  | 5   |
| 08:00 | (2,0)  | (2,0)  | (1,0)  | 5   |
| 09:00 | (3,1)  | (2,1)  | (0,0)  | 5   |
| 10:00 | (2,0)  | (3,2)  | (0,0)  | 5   |
| 11:00 | (2,1)  | (2,0)  | (1,0)  | 5   |
| 12:00 | (2,0)  | (3,1)  | (0,0)  | 5   |
| 13:00 | (2,1)  | (3,2)  | (0,0)  | 5   |
| 14:00 | (1,0)  | (3,0)  | (1,0)  | 5   |
| 15:00 | (1,1)  | (3,1)  | (0,0)  | 5   |

### Simulation Table – Simplified (jobs count) format

| Time  | W1 | W2 | W3 | WIP | Control |
|-------|----|----|----|-----|---------|
| 00:00 | 5  | 0  | 0  | 5   | 0       |
| 01:00 | 5  | 0  | 0  | 5   | 0       |
| 02:00 | 4  | 1  | 0  | 5   | 0       |
| 03:00 | 4  | 1  | 0  | 5   | 0       |
| 04:00 | 3  | 2  | 0  | 5   | 0       |
| 05:00 | 3  | 1  | 1  | 5   | 0       |
| 06:00 | 3  | 2  | 0  | 5   | 0       |
| 07:00 | 3  | 2  | 0  | 5   | 0       |
| 08:00 | 2  | 2  | 1  | 5   | 0       |
| 09:00 | 3  | 2  | 0  | 5   | 0       |
| 10:00 | 2  | 3  | 0  | 5   | 0       |
| 11:00 | 2  | 2  | 1  | 5   | 0       |
| 12:00 | 2  | 3  | 0  | 5   | 0       |
| 13:00 | 2  | 3  | 0  | 5   | 0       |
| 14:00 | 1  | 3  | 1  | 5   | 0       |
| 15:00 | 2  | 3  | 0  | 5   | 0       |

### Buffer-based Table (alternative representation)

| Time  | Buffer W1 | W1 | Buffer W2 | W2 | Buffer W3 | W3 |
|-------|-----------|----|-----------|----|-----------|-----|
| 00:00 | 5 4 3 2   | 1  | 0         | 0  | 0         | 0  |
| 01:00 | 5 4 3 2   | 1  | 0         | 0  | 0         | 0  |
| 02:00 | 5 4 3     | 2  | 0         | 1  | 0         | 0  |
| 03:00 | 5 4 3     | 2  | 0         | 1  | 0         | 0  |
| 04:00 | 5 4       | 3  | 2         | 1  | 0         | 0  |
| 05:00 | 5 4       | 3  | 0         | 2  | 0         | 1  |
| 06:00 | 6 5       | 4  | 3         | 2  | 0         | 0  |
| 07:00 | 6 5       | 4  | 3         | 2  | 0         | 0  |
| 08:00 | 6         | 5  | 4         | 3  | 0         | 2  |
| 09:00 | 7 6       | 5  | 4         | 3  | 0         | 0  |
| 10:00 | 7         | 6  | 5 4       | 3  | 0         | 0  |
| 11:00 | 7         | 6  | 5         | 4  | 0         | 3  |
| 12:00 | 8         | 7  | 6 5       | 4  | 0         | 0  |
| 13:00 | 8         | 7  | 6 5       | 4  | 0         | 0  |
| 14:00 | 0         | 8  | 7 6       | 5  | 0         | 4  |
| 15:00 | 9         | 8  | 7 6       | 5  | 0         | 0  |

---

## Exercise 5

**Problem:** Using the production line from Exercise 4 (W1=2h, W2=3h, W3=1h):
1. Compute rb, T0, and W0 with original configuration (1 machine each).
2. Assume W2 has **2 identical machines** (same process time). Recompute rb, T0, W0.

### Solution 1 – Original (1 machine per workstation)

| Workstation | Process time [min] | Station capacity [jobs/min] |
|-------------|--------------------|-----------------------------|
| 1           | 2                  | 0.50                        |
| 2           | 3                  | **0.33** ← bottleneck       |
| 3           | 1                  | 1.00                        |

```
rb = 0.33 jobs/min   (bottleneck = W2)
T0 = 2 + 3 + 1 = 6 min
W0 = rb × T0 = 0.33 × 6 = 2.00 jobs
```

**TH_BEST and CT_BEST table (w = 1 to 7):**

| w | TH   | CT   |
|---|------|------|
| 1 | 0.17 | 6.0  |
| 2 | 0.33 | 6.0  ← W0 |
| 3 | 0.33 | 9.0  |
| 4 | 0.33 | 12.0 |
| 5 | 0.33 | 15.0 |
| 6 | 0.33 | 18.0 |
| 7 | 0.33 | 21.0 |

### Solution 2 – W2 with 2 machines

| Workstation | Process time [min] | Machines | Station capacity [jobs/min] |
|-------------|--------------------|-----------|-----------------------------|
| 1           | 2                  | 1         | 0.50 ← bottleneck           |
| 2           | 3                  | 2         | 0.67                        |
| 3           | 1                  | 1         | 1.00                        |

```
rb = 0.50 jobs/min   (bottleneck = W1)
T0 = 2 + 3 + 1 = 6 min   (raw process time unchanged)
W0 = rb × T0 = 0.50 × 6 = 3.00 jobs
```

---

## Exercise 6

**Problem:** Automobile assembly line with 5 workstations:

| Workstation | Machines | Process time [h/job] | Station capacity [jobs/h] |
|-------------|----------|----------------------|---------------------------|
| 1           | 3        | 1.5                  | 3/1.5 = **2.00**          |
| 2           | 2        | 2.0                  | 2/2.0 = **1.00**          |
| 3           | 1        | 2.5                  | 1/2.5 = **0.40** ← bottleneck |
| 4           | 4        | 1.0                  | 4/1.0 = **4.00**          |
| 5           | 2        | 2.0                  | 2/2.0 = **1.00**          |

**Questions:**
1. Identify the bottleneck workstation and its bottleneck rate.
2. Calculate the raw process time T0.
3. Compute the critical WIP W0.
4. Given TH = 1 job/4 hours = 0.25 jobs/h and WIP = 9 jobs (constant), find CT – T0.

**Solutions:**

**1. Bottleneck:**
```
Bottleneck = Workstation 3 (single machine, 2.5h process time)
rb = 0.40 jobs/hour
```

**2. Raw process time:**
```
T0 = 1.5 + 2.0 + 2.5 + 1.0 + 2.0 = 9 hours
```

**3. Critical WIP:**
```
W0 = rb × T0 = 0.40 × 9 = 3.6 jobs
```

**4. Difference CT – T0:**
```
TH = 1/4 = 0.25 jobs/hour
CT = WIP / TH = 9 / 0.25 = 36 hours
CT – T0 = 36 – 9 = 27 hours
```

**Answers:**
1. WS3, rb = 0.40 jobs/hour
2. T0 = 9 hours
3. W0 = 3.6 jobs
4. CT – T0 = **27 hours**

---

*End of document – Factory Analysis exercises (Little's Law, Bottleneck analysis, WIP/TH/CT)*
