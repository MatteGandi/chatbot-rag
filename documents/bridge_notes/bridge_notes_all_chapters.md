---
type: bridge_notes
chapter: all
topic: cross_topic_connectors
priority: 1
description: Connettori cross-topic tra i vari moduli del corso. Usare per rispondere a domande che spannano più capitoli. Non introduce fatti nuovi ma riassume relazioni già presenti nel corso.
---

# Bridge-Notes - Version 1

The purpose of this document is to provide short, cross-topic connectors so the chatbot can build coherent answers when a question spans multiple modules. Use with slides (PDF) and glossary (DOCX). These notes do not introduce new facts: they summarize relationships already present in the course.

# 1) CT-WIP-TH: linking factory performance (Little's Law)

· Little's Law connects Work-in-Process(WIP), Throughput (TH) and Cycle Time (CT): WIP = TH × CT (steady state).   
· Station-level decomposition: CT(i) = CTq(i) + E[Ts(i)] → total CT accumulates queueing + service over the routing.   
· The bottleneck (highest utilization u or lowest capacity) caps system TH; reducing WIP without addressing the bottleneck only shortens CT transiently.   
·Raising utilization near 1 causes nonlinear CT growth; managing WIP and variability prevents CT blow-ups at high u.   
· Use VsM timelines to connect step-level processing/waiting with end-to-end CT and inventory positions.

Glossary anchors: Little's Law, Throughput (TH), Work in Process (WIP), Cycle time (CT), Botteneck, Cycle time by station, Timeline & Lead Time (VSM)

# 2) Variability → waiting (CTq) and utilization trade-offs

· Queueing delay depends on arrival and service variability (Ca², Cs2),utilization u,and mean service time E[Ts].   
· As u 个,CTq becomes very sensitive to variability; reducing SCV (CV²) can yield a capacity-equivalent benefit.   
·Natural processing-time variability can be lowered via task decomposition (e.g., Erlang-k phases).   
·Breakdowns/repairs inflate effective service time Te and its variability; availability a impacts E[Te] and thus u and CTq.   
·At line level, departure variability (c_d²) propagates downstream; in serial lines C a²(i)=C d²(i-1).

Glossary anchors: Coefficient of Variation (CV)& SCV, CTq approximation drivers (Ca², Cs², u, E[Ts]), Erlang-k approximation,Availability (a),Flow variability, Serial line (variability propagation)

# 3) Choosing a modeling formalism: Flowchart vs UML vs BPMN vs IDEFO

· Flowchart: simple control-flow with standardized symbols; good for procedures with limited decisions.

· UML: multiple views - Use Case (services), Class(structure), Sequence/Statechart/Activity (behavior).   
· BPMN: process-centric with Activities, Events, Gateways; supports concurrency, pools/lanes, data objects/stores.   
· IDEFO: function-centric (ICOM: Inputs, Controls, Outputs, Mechanisms) with hierarchical decomposition.   
· Practical rule: diagram per purpose 一 requirement capture (Use Case), execution logic (BPMN/Activitv). function decomposition (IDEFO). auick procedures (Flowchart).

Glossary anchors: Flowchart, UML (overview), BPMN (overview), BPMN core elements, Pools & Lanes, IDEFO (overview)

# 4) From Operative Structure to VSM: BOM → operations/resources → lead time

·Product tree/BOM defines components; precedence yields the graph of operations and feasible working seauences.   
· The OP-Resource matrix and resource graph allocate operations to workstations and schedules (Gantt).   
· In VSM, each step becomes a Process box with data (C/T,setup, uptime, VA,scrap); inventories and timelines expose waitina vs processina.   
· Lead time emerges from aggregating process and waiting times across the flow; inventory icons mark WiP and safetv stocks.   
· Use this bridge to translate structural views (BOM/graphs) into flow views (VSM) consistent with CT/WIP/TH metrirs

Glossary anchors: Product tree / Bil of Materials, Graph of operations, Working sequence, Resources & OP-Resource matrix, Factory & Process boxes (VSM), Timeline & Lead Time (VSM)

# 5) Multi-product and re-entrant flows: routing and mixtures at stations

· Re-entrant flows revisit the same workstation; from the station perspective this is equivalent to multiple ‘product tvpes'.   
·At a station,service time is a mixture over products weighted by their arrival shares → use composite mean/SCV.   
· Workload and utilization per station: WL k =∑ iλ i.k E[Tsli.k)l. u k = WL k / c k.   
·Network-level routing matrices (per product) combine into composite routing for shared aueues without brioritv.   
· Per-product mean time in factorv aggregates CTa(k)+E[Tsli.k)l along the visited stations.

Glossary anchors: Re-entrant flow system, Service-time mixture, Workload & utilization with multiple products, Composite routing matrix (P), Mean time in factory by product

# 6) Batch models: transport, setup reduction, k-at-once service

·Transport batching reduces arrival rate by k and changes inter-arrival SCV; batch forming adds (k-1)/2 · E[Td] on average.

· At receiving stations, CTq per item can match single-item flow with same u and individual SCVs.   
· Intra-batch processing adds (k-1)/2 · E[Ts] per item when processed sequentially.   
·Setup-before-batch:amortize setups R over k items (E[R]/k) but batch added formation/processing delays.   
·Batch service (k-at-once) couples batch inter-arrival/service variability with utilization u(B); choose k via CT trade-off.

Glossary anchors: Batch move (transport batching), Batch forming time, Batch queue waiting time (equivalence), Intra-batch processing delay, Batching for setup reduction, Batch service (k-at-once)

# 7) Information systems & Industry 4.O: data to decisions on the shop floor

· ERP integrates cross-functional data; MES provides real-time execution (dispatching, tracking, status) from PLC/SCADA sources.   
· PLM governs product data across lifecycle; horizontal/vertical integration enable end-to-end data flow.   
· loT/lloT and cloud platforms collect/serve data for monitoring,analytics and optimization (e.g., WIP/CT dashboards).   
· Predictive maintenance and condition monitoring reduce effective service time variability (fewer breakdowns → lower CTq).   
· Cyber-security is a prerequisite as connectivity expands the attack surface.

Glossary anchors: ERP, MES, PLM, Horizontal/Vertical integration, loT/IloT, Cloud computing, Predictive maintenance, Condition monitoring & RUL, Cyber security

# 8) Analytical models vs Discrete-Event Simulation (DES): when to use which

·Analytical'factory models'decompose lines/stations and are fast for sensitivity and design rules (u, CT, TH, WIP).   
· DES represents events (arivals, starts/ends, breakdowns) and states (queues, machines, operators) enabling what-if scenarios with complex logic and variability.   
· Verification vs Validation: build the model right vs build the right model; remove initial transient before steady-state statistics.   
· Use DES to validate scheduling rules,batching, re-entrant flows, resource sharing; use analytics for quick back-of-the-envelope checks and parameter sweeps.   
· Triangulate: DES results should be consistent with Litle's Law and queueing approximations at comparable u and variability.

Glossary anchors: Factory model (decomposition), Queueing systems (components), Verification vs Validation, Discrete Event Simulation (DES), Transient vs steady state
