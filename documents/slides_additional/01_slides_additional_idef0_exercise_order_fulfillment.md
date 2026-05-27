---
type: slides_additional
chapter: 01
topic: idef0_exercise_order_fulfillment
priority: 3
description: Appunti e slide aggiuntive sul corso. Priorità inferiore alle slide ufficiali e alle trascrizioni. In caso di discrepanza prevalgono le slide ufficiali.
---

# 1.3.2 IDEF0 Exercise – Order Fulfillment Process

This exercise shows how to **derive an IDEF0 model step by step** starting from a textual description of a real process.
The example refers to an **order fulfillment process** for the production of a mechanical component.

The goal is to:
- identify activities,
- decompose the process hierarchically,
- correctly classify **Inputs, Controls, Outputs, and Mechanisms (ICOMs)**.

---

## 1.3.2.1 Textual Description of the Process

The process concerns a manufacturing company that:

- receives a **customer request** for a mechanical component,
- prepares an **offer** involving:
  - the technical department,
  - the administrative department,
- receives a **customer order** if the offer is accepted,
- plans and executes production,
- performs **quality control**,
- completes the process with **invoicing and payment**.

The only element physically transformed during the process is the **raw material**, which becomes the **finished product**.

---

## 1.3.2.2 A0 Diagram – Order Fulfillment

### Activity
```
A0 – Order Fulfillment
```

### Inputs
- Raw materials

### Controls
- Customer request
- Customer order

### Outputs
- Finished product
- Invoice

### Mechanisms (Resources)
- Technical department
- Administrative department
- Equipment

---

## 1.3.2.3 Decomposition of A0

The A0 activity is decomposed into two main activities:

```
A1 – Offer Formulation
A2 – Production
```

Logical dependency:
- Production (**A2**) can start only after:
  - the offer is issued,
  - the customer order is received.

---

## 1.3.2.4 A1 – Offer Formulation

### Description
The offer formulation involves cooperation between:
- the **technical department**,
- the **administrative department**.

The offer is based on a preliminary definition of the manufacturing process.

### ICOMs

**Controls**
- Customer request

**Outputs**
- Offer

**Mechanisms**
- Technical department
- Administrative department

There is no physical input transformed in this activity.

---

## 1.3.2.5 Decomposition of A1 – Offer Formulation

A1 is decomposed into three sub-activities:

```
A11 – Process Definition
A12 – Cost Definition
A13 – Offer Formulation
```

---

### A11 – Process Definition

**Controls**
- Customer request

**Outputs**
- Process plan (general description)

**Mechanisms**
- Technical department

---

### A12 – Cost Definition

**Inputs**
- Process plan

**Outputs**
- Cost plan

**Mechanisms**
- Administrative department

---

### A13 – Offer Formulation

**Inputs / Controls**
- Cost plan

**Outputs**
- Offer

**Mechanisms**
- Administrative department

---

## 1.3.2.6 A2 – Production

### Description
Once the offer is accepted and the order is received, the company starts the production process.

### Controls
- Customer order
- Offer

### Inputs
- Raw materials

### Outputs
- Finished product
- Invoice

### Mechanisms
- Technical department
- Administrative department
- Equipment

---

## 1.3.2.7 Decomposition of A2 – Production

A2 is decomposed into the following activities:

```
A21 – Process Plan Definition
A22 – Production Planning
A23 – Raw Material Ordering
A24 – Processing
A25 – Quality Control
A26 – Invoicing
```

---

### A21 – Process Plan Definition

**Controls**
- Offer
- Customer order

**Outputs**
- Detailed process plan

**Mechanisms**
- Technical department

---

### A22 – Production Planning

**Controls**
- Process plan

**Outputs**
- Production plan

**Mechanisms**
- Technical department

---

### A23 – Raw Material Ordering

**Controls**
- Process plan

**Outputs**
- Raw material availability

**Mechanisms**
- Administrative department

---

### A24 – Processing

**Inputs**
- Raw materials

**Controls**
- Production plan

**Outputs**
- Manufactured product

**Mechanisms**
- Technical department
- Equipment

---

### A25 – Quality Control

**Inputs**
- Manufactured product

**Outputs**
- Finished product

**Mechanisms**
- Technical department
- Equipment

---

### A26 – Invoicing

**Controls**
- Finished product

**Outputs**
- Invoice

**Mechanisms**
- Administrative department

---

## 1.3.2.8 Consistency Check

The IDEF0 model is consistent because:
- only **raw materials** are transformed,
- information flows are correctly modeled as controls,
- resources are never transformed,
- outputs of activities are reused coherently as inputs or controls.

---

## 1.3.2.9 Key Takeaways

- IDEF0 starts from a **textual process description**
- Decomposition must preserve:
  - logical precedence,
  - ICOM consistency
- Controls trigger activities but are not transformed
- This exercise illustrates a **complete IDEF0 modeling workflow**
