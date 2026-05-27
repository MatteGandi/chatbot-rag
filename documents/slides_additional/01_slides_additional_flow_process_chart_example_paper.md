---
type: slides_additional
chapter: 01
topic: flow_process_chart_example_paper
priority: 3
description: Appunti e slide aggiuntive sul corso. Priorità inferiore alle slide ufficiali e alle trascrizioni. In caso di discrepanza prevalgono le slide ufficiali.
---

# 1. Flow Process Chart – Example (Paper Production)

## 1.1 Purpose of the Example
This example illustrates how to represent a **manufacturing process** using the **Flow Process Chart** formalism.  
The objective is to translate a textual description into standardized symbols, making reasonable assumptions where information is missing.

> Important: when details are not explicitly stated in the text, **assumptions are allowed** and should be clearly documented near the diagram.

---

# 2. General Assumptions
- The process includes both **internal production** (company forest) and **external sourcing** (supplier).
- Transport activities are included when materials move between physically distinct locations.
- When it is unclear whether activities occur in the same location, **either solution is acceptable**.
- Time data are not provided; however, placeholders for time can be added near symbols.

---

# 3. Raw Material Supply

## 3.1 Sources of Wood
Wood is obtained from two sources:
- Company-owned forest
- External supplier

Two valid representations are possible:
1. Represent forest and supplier as **initial warehouses**
2. Start directly with **transport activities**

Both approaches are acceptable.

## 3.2 Initial Activities
- **Operation**: Cutting trees (internal activity)
- **Operation**: Receiving wood from supplier (treated as an activity for clarity)
- **Transport**: Wood conveyed via artificial channel to storage area

---

# 4. Wood Preparation Phase

## 4.1 Storage
- **Inventory**: Wood storage area

## 4.2 Chipping
- **Transport**: Wood to chipper
- **Operation**: Chipping (standard size: 1 × 2 inches)

## 4.3 Dimensional Quality Control
- **Inspection**: Chip size inspection

### 4.3.1 Flow Splitting
- Chips too large → returned to chipper
- Chips too small → removed from the process
- Conforming chips → proceed to silos

This split can be represented by:
- Multiple outgoing arrows
- Or a single inspection followed by branched flows

---

# 5. Chip Storage and Chemical Treatment

## 5.1 Storage
- **Inventory**: Chip silos

## 5.2 Boiling
- **Transport**: Chips from silos to boiling station
- **Operation**: Boiling in caustic soda and sodium sulfide

## 5.3 Fiber Separation
- **Operation**: Low-pressure discharge vat (fiber separation)

Transport between boiling and separation may be omitted if assumed to occur in the same location.

---

# 6. Fiber Processing

## 6.1 Mechanical Treatment
- **Operation**: Centrifugation
- **Operation**: Pressing

## 6.2 Bleaching
- **Operation**: Bleaching of pulp

---

# 7. Resting Phase

## 7.1 Resting Operation
- **Delay / Waiting**: Pulp resting phase

Although physically stored in a warehouse, this phase is modeled as **waiting**, because resting is an intentional process activity.

Optional:
- **Transport** to resting area
- **Inventory** symbol if storage is emphasized

---

# 8. Paper Production

## 8.1 Pulp Processing
- **Transport**: Pulp to paper machine
- **Operation**: Water removal and compression in steam-heated cylinders
- **Operation**: Drying
- **Operation**: Wrapping into large reels

## 8.2 Storage
- **Inventory**: Reel warehouse (waiting for customer orders)

---

# 9. Final Processing and Delivery

## 9.1 Order Fulfillment
- **Transport**: Reels to cutting/rewinding machine
- **Operation**: Cutting and rewinding into smaller reels

## 9.2 Delivery
- **Transport**: Final delivery to customer

The process typically ends with:
- A **transport** (delivery)
- Or a **warehouse** (finished goods storage)

---

# 10. Notes on Diagram Construction

## 10.1 Symbols Used
- Operation: circle
- Transport: arrow
- Inspection: square
- Inventory / Storage: triangle
- Delay / Waiting: delay symbol

## 10.2 Interpretation Flexibility
- Different numbers of transport activities are acceptable.
- The key requirement is **coherence with the text**.
- If the real process is known, representation should reflect physical reality.
- Otherwise, clearly stated assumptions are sufficient.

---

# 11. Key Takeaway
The Flow Process Chart is a flexible but rigorous formalism.  
Correct representation depends less on a single “right” solution and more on:
- Logical consistency
- Clear assumptions
- Proper use of standard symbols
