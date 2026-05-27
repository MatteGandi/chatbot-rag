---
type: slides_additional
chapter: 02
topic: introduction_littles_law_exercises
priority: 3
description: Appunti aggiuntivi sul corso. In caso di discrepanza prevalgono le slide ufficiali.
---

# 2.1 Introduction to Production System Modeling  
## Little’s Law and Exercises

## 2.1.1 Course Context and Objectives
This section introduces the **analysis and modeling of production systems**.  
It corresponds to **Chapter 2** of the reference textbook and defines the analytical framework used throughout the course.

The adopted approach is **analytical and hierarchical**:
- start from simple systems,
- derive fundamental relationships between KPIs,
- progressively extend the models to more complex systems.

---

# 2.1.2 Modeling Approach

The course follows a **bottom-up strategy**:
1. Single workstation (single machine)
2. Production line (series of workstations)
3. Networks with merging and splitting flows
4. Multiple product types
5. Batch arrivals

Each model is an **approximation** of reality:
- not all real-world elements are modeled,
- operators, transport systems, and detailed behaviors may be abstracted,
- assumptions must be justified by the analysis objectives.

---

# 2.1.3 System Boundaries

The analysis focuses on the **factory system only**:
- jobs arrive at the factory with given parameters,
- jobs follow a routing inside the factory,
- completed jobs exit the system (delivery or storage not analyzed further).

---

# 2.1.4 Basic Definitions

## Jobs
The terms *job*, *item*, and *order* are used interchangeably to indicate a physical entity entering the production system.

## Factory
A factory is composed of multiple **workstations**.

## Workstation
A workstation is a set of **identical machines or operators**:
- same processing parameters,
- parallel operation,
- identical processing time distributions.

## Queue
A physical or logical place where jobs wait when machines are busy.

## Routing
The ordered sequence of workstations visited by a job.

Different product types may follow **different routings** within the same factory.

---

# 2.1.5 Arrival Process

Jobs may arrive:
- individually,
- in batches.

Arrival is characterized by:
- average arrival rate,
- average inter-arrival time,
- probability distribution (often exponential).

These are **input parameters** of the model.

---

# 2.1.6 Processing Times

Processing times:
- are not deterministic,
- follow probability distributions,
- are characterized by mean value and variability.

---

# 2.1.7 Key Performance Indicators (KPIs)

## Cycle Time (CT)
The **cycle time** is the time a job spends inside the system.

Terminology note:
- in Value Stream Mapping this quantity is often called *lead time*,
- in queueing theory and analytical models it is called *cycle time*.

Two notions:
- real cycle time: directly measured in the plant,
- planned cycle time: conservative estimate used for planning and scheduling.

### System vs Workstation Cycle Time
- CTᵢ: cycle time at workstation *i*
- CTₛ: total cycle time of the system

At workstation level:
```
CTᵢ = CTQᵢ + E[TSᵢ]
```

---

## Work In Process (WIP)
WIP is the **average number of jobs inside the system**:
- jobs being processed,
- jobs waiting in queues.

---

## Throughput (TH)
Throughput is the **rate of completed jobs** leaving the system:
- jobs per hour,
- jobs per day.

In steady state:
```
TH = arrival rate
```

---

# 2.1.8 Steady-State Assumption

Performance measures are evaluated in **steady state**:
- after initial transient effects disappear,
- independent of initial system conditions.

Instantaneous values fluctuate due to variability,  
but **average values converge** to steady-state limits.

---

# 2.1.9 Arrival and Departure Functions

Define for job *i*:
- arrival time: aᵢ
- departure time: dᵢ

Define:
- A(t): cumulative arrival function
- D(t): cumulative departure function

The number of jobs in the system at time *t* is:
```
N(t) = A(t) − D(t)
```

---

# 2.1.10 Average Cycle Time

For a time interval [a, b]:

```
CT = (1 / Nₐᵦ) · Σ (dᵢ − aᵢ)
```

---

# 2.1.11 Average WIP

Average WIP over [a, b]:

```
WIP = (1 / (b − a)) · ∫ N(t) dt
```

---

# 2.1.12 Little’s Law

```
WIP = TH · CT
```

Equivalent form:
```
WIP = λ · CT
```

---

# 2.1.13 Exercise 1

**Given:**
- WIP = 25 jobs  
- λ = 4 jobs/hour  
- E[TS] = 14.5 minutes  

**Solution:**
- CT = 25 / 4 = 6.25 hours  
- E[TS] = 0.24 hours  
- CTQ = 6.01 hours  

---

# 2.1.14 Exercise 2

**Given:**
- λ = 10 jobs/day = 0.417 jobs/hour  
- CT₁ = 4.2 hours  
- CT₂ = 5.3 hours  

**Solution:**
- WIP = λ · (CT₁ + CT₂) = 3.96 jobs  

---

# 2.1.15 Key Takeaways
- Steady-state averages are central.
- Little’s Law links WIP, CT, and TH.
- Valid at all system levels.
