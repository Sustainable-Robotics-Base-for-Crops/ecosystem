# SMOR: towards a diffusible standard for agricultural robotics in the service of agroecology

### Sustainable Robotics Base for Crops

Author: Alexandre Prévault-Osmani — CTO and co-founder of SABI AGRI

*White paper · short version · September 2026 · CC BY 4.0 licence*

---

## Contents

1. [Summary](#summary)
2. [Key notions](#key-notions)
3. [Thesis and positioning](#thesis-and-positioning)
4. [What holds diffusion back](#what-holds-diffusion-back)
5. [The SMOR vision](#the-smor-vision)
6. [A reference architecture and an open chain of evidence](#a-reference-architecture-and-an-open-chain-of-evidence)
7. [The SRBC robot, a first embodiment](#the-srbc-robot-a-first-embodiment)
8. [Evaluating what matters to the farm](#evaluating-what-matters-to-the-farm)
9. [A commons that belongs to the farming world](#a-commons-that-belongs-to-the-farming-world)
10. [Safety, compliance and co-responsibility](#safety-compliance-and-co-responsibility)
11. [From code to commons: the roadmap](#from-code-to-commons-the-roadmap)
12. [Limits and call to action](#limits-and-call-to-action)
13. [References](#references)
14. [About the author](#about-the-author)

---

## Summary

Agricultural robotics promises to reduce arduous work, to respond to recruitment difficulties and to make more precise interventions possible. Ten years after the first robots arrived in the fields, its diffusion nevertheless remains marginal. A successful demonstration says little about a machine’s availability over a season, the agronomic quality of its work or its viability in the daily life of a farm. The challenge is shifting: making a robot work now matters less than creating the conditions for its lasting adoption.

We argue that robotics should first benefit small and medium-sized diversified farms engaged in an agroecological transition. To this end, we propose the SMOR vision — *Small, Modular, Open & Responsible* — expressed as a reference architecture, an open documentary chain linking what the robot was meant to do with what it actually did, an evaluation method, a model of commons belonging to the farming world and an explicit allocation of responsibilities. The SRBC robot is its first industrial embodiment. SMOR is a framework to be put to the test: this text sets out its thesis and proposals, and the full version will provide the evidence.

---

## Key notions

- **ODD** (operational design domain): the conditions under which an autonomous function was designed and validated — field, soil, weather, slope, localisation quality, presence of people.
- **Mission order**: a file describing what the robot must do, within which limits and with which authorised reactions.
- **Work performed**: a file describing what the robot did, under which encountered conditions, and how the farm assesses the service delivered.
- **Open Core**: a model in which interfaces and generic building blocks are open, while hardware realisation, calibration and services remain the manufacturer’s responsibility.

---

## Thesis and positioning

Since the mid-2010s, agricultural robotics has moved from laboratories to fields. Progress in perception, navigation and automation is real; commercial diffusion remains modest given the diversity of production and the number of farms [1, 2]. This gap calls for another definition of maturity.

Our approach is simple: the maturity of an agricultural robot is measured by its **diffusibility**, that is, its capacity to be used, maintained, repaired and improved over the long time of agriculture. It requires a fit with a clearly identified agronomic and human need, an accessible cost, safety demonstrated within an explicit domain, maintenance available nearby and genuine ownership by the people who use it.

We make an explicit positioning choice: agricultural robotics should first benefit small and medium-sized farms, particularly when they are diversified and engaged in an agroecological transition. We define them first as human-scale agricultural businesses, where the person who farms retains a direct capacity for observation and decision over crops and soils; the French agricultural census classification by standard output provides a statistical benchmark [3]. These farms carry the diversity of production, the stewardship of territories, rural employment and context-specific know-how. They are also the most exposed to labour costs, arduous work and investment barriers.

Agroecological practices call for more observation, more precision and more differentiated interventions [4]. This agronomic intensity becomes hard to sustain when human work is counted as a mere cost against economies of scale. Robotics can rebalance this situation by reducing arduous work and making feasible operations that benefit soils and ecosystems: precise sowing that prepares early mechanical weeding, repeated passes of a light tool within a short window, a light machine wherever soil bearing capacity demands it.

The same technology can also serve the concentration of the means of production, dependency on proprietary suppliers and the rapid obsolescence of equipment [5, 6]. The trajectory depends on choices of architecture, business model and governance. The mismatch between the short cycles of digital technology and the long timescales of agriculture makes this a structural issue: a machine that people can no longer understand, maintain or adapt becomes a constraint, even when it performed well at the outset.

We distinguish three levels: the robot’s **technical capability** (moving, following a row, operating a tool safely), the **agronomic service** obtained within a given window (regular sowing, effective hoeing) and the **agroecological impact**, observed over time at the scale of the cropping system (inputs avoided, soil condition, biodiversity, working conditions, farm autonomy, full cost). Existing evaluation schemes mostly document the first level; the other two determine a robot’s value for a farm.

> **Thesis**  
> Agricultural robotics will become a lever for the diffusion of agroecology provided it is designed to be useful, accessible, maintainable, safe, interoperable and appropriable, and can demonstrate its performance under real conditions.

We add a methodological conviction: diffusion is as much a problem of **representation** as of measurement. As long as agronomic intent and the result obtained are described in different vocabularies, field feedback stays isolated, the results of two manufacturers stay incomparable and responsibilities stay impossible to examine. A shared, versioned vocabulary is the first condition for cumulative knowledge.

---

## What holds diffusion back

An agricultural robot works in contact with living systems: soil, vegetation, weather and work organisation change over a single season. Every performance must therefore be related to a use, a configuration and an explicit operating domain.

The barriers are known and interdependent [1, 7]: **robustness** over a whole season; **safety**, which requires detecting dangerous situations and reaching a safe state; **agronomic performance**, judged by the quality of the tool’s work more than by the precision of the trajectory; **economic viability**, which depends on supervision time, maintenance and downtime far more than on purchase price; **interoperability**, weak as long as formats, interfaces and logs remain specific to each manufacturer, and the resulting **technological dependency**. Recent work shows that the human time spent on logistics and supervision is the real issue to solve for small-scale robotics [7].

Precision agriculture already has valuable standards, such as ISOXML or ADAPT, to describe a task and the work applied [8, 9]. They were designed for a person at the controls who guarantees the domain of use. With a robot, part of the observation and decision moves to the machine, and the chain linking intent to execution must become explicit: what the robot must do, under which conditions it is authorised to do so, how it reacts to the unexpected, what it encountered and what it achieved. Industry recognises this need, with the AEF work stream on autonomous machines [10], as does research on the agricultural operational design domain [11]. We see this work as convergent and wish to contribute an open proposal already used in the field.

The literature that examines robotics from an agroecological perspective converges on one point: the trajectory remains open. The same technology can lead to fleets of small machines serving diversified systems or to large machines consolidating monocultures [6]. Bringing autonomous functions into agroecological systems requires designing with a diversity of stakeholders, moving beyond a “monocultural mindset” [5], and farmers rank responsibility, safety and data control among their first concerns [12]. These conclusions ground our choice to entrust farmers with deciding on and guaranteeing the uses of the technology they work with.

---

## The SMOR vision

SMOR is a design and evaluation framework that links the characteristics of a robot to its agronomic, economic, ecological and social effects. At this stage, it has the status of a proposal submitted to the test of the field and of discussion.

We choose mainly electric traction and actuators. Electric motors and actuators can be controlled finely, report their state and integrate directly with diagnostic systems. Electricity can come from the grid or be produced on the farm, opening the way to full or partial energy autonomy; batteries and motors must nonetheless be assessed over their life cycle.

**Small: a proportionate scale.** We favour machines whose mass, power and footprint remain proportionate to the operations. Our dimensional target lies between a human and a draught horse: roughly 80 to 1,200 kg, under 10 km/h, a few kilowatts, half a day to a full day of autonomy, very low voltage and, for light carriers, an investment below 40,000 euros. Beyond that, mass brings the machine back into the world of the tractor, with its motorisation, logistics and price. These values are design targets. Limited mass reduces the energy involved and eases transport and maintenance; the effect on soil also depends on contact pressure, slip, number of passes and moisture [13]. This scale allows several specialised robots, or robots shared between farms, rather than a single machine sized for the heaviest operation. It becomes a lasting economic advantage when human time per hectare actually falls, which requires reliable missions without continuous monitoring and, in time, supervision of several robots by a single person.

**Modular: adapt, repair, share.** We separate a stable base (structure, energy, control, interfaces, safety) from modules adapted to crops, tools and contexts: changing a tool, running gear or sensor without replacing the carrier, evolving a software function without rebuilding the whole, retrofitting a machine within the crop calendar. This modularity rests on documented dimensions, connectors, protocols and formats; without them, it would remain at the mercy of the original supplier.

**Open: sovereignty over time.** We open first the interfaces, mission and data formats, documentation and generic software building blocks, then the designs when their publication strengthens repairability. The Open Source we stand for is an industrial method: explicit licences, versioned contracts, tests, documentation, governance and stable releases. It guarantees farms sovereignty of use (diagnosing, repairing, adapting, having the machine maintained by another provider), shifts manufacturers’ differentiation towards integration, safety and service, and enables lasting competence in local workshops.

**Responsible: accountable innovation.** A technology becomes responsible when its effects are anticipated, discussed, measured and corrected with the people it concerns [14]. This principle commits us to involving farmers in defining needs and in evaluation, designing safety from the outset, documenting the limits of use, measuring the consumption of materials, energy and digital resources, preserving farmers’ decision-making, guaranteeing the farm’s control over its data and making the allocation of responsibilities verifiable.

These four principles form a whole. A small closed robot remains captive and ages quickly; an open platform without governance fragments; a modular machine that is too expensive has no effect on diffusion. **SMOR proposes overall coherence: a robotics whose performance is measured by its capacity to make agroecology practicable, economically viable and durably appropriable by the farming world.**

---

## A reference architecture and an open chain of evidence

A reference architecture provides a common language: it separates functions and defines the interfaces that allow a component to be replaced without rebuilding the system. Each manufacturer remains free in its hardware choices, provided it respects the common contracts and safety requirements. We propose six layers: energy and actuators, vehicle control, documented field buses, onboard computing (ROS 2 is a relevant foundation today), perception and localisation, mission and user interface. One principle runs through them: **safety-related functions remain independent of the general-purpose computer and of any remote connection.** Essential functions remain available offline, and the interface makes visible the robot’s state, its limits and the cause of every stop.

The most structuring contract is the **vehicle interface**, which describes commands, states, tool capabilities and faults. It allows the same navigation function to adapt to several carriers, and thus turns a product into a platform.

The second contract concerns the mission. We propose **JSON Agri**, an open format published under the CC BY 4.0 licence [15], readable without IT training and verifiable by a machine. It organises a chain of two documents. The **mission order** describes the agronomic objective and its acceptance criteria, the carrier–tool pair, the authorised operating domain, the trajectory, the permitted zones and the planned reactions to events: a low battery, for example, triggers a return to the charging area along authorised paths. The **work performed** links this intent to the conditions encountered, the events, human interventions, service indicators and the farm’s agronomic assessment. A digital fingerprint of the order, copied into the work performed, guarantees that execution is compared with the exact version of the mission.

Three choices give this chain its reach. The authorised domain and the encountered conditions share the same vocabulary, so that any deviation can be linked to a detection, a decision, a responsibility and a piece of evidence. Reactions to events form a closed vocabulary: the machine refuses any instruction that is unknown or absent from the catalogue validated by its manufacturer, and its safety floor remains beyond the reach of any file. The attestation produced in simulation proves that a file has passed defined checks under identified assumptions; it stands as evidence of verification, distinct from a certificate.

The chain thus separates three validations: **preparation**, in the mission editor; **operational** validation, on board, where the robot checks the mission against its configuration and the conditions confirmed on site, and keeps the freedom to refuse; **service** validation, after the mission, through the farm’s agronomic assessment. This separation guards against two costly confusions: taking a simulation for an authorisation, or a completed mission for a successful service. Public specification rules (a small and stable core, missing data declared as such, guaranteed compatibility, offline validation), conformance levels and a validator allow any third party to verify its implementation independently. JSON Agri thus complements existing standards by describing the autonomy chain they leave implicit.

---

## The SRBC robot, a first embodiment

The SRBC robot, designed by SABI AGRI, tests these principles on a machine that is sold and used in the field. This compact electric carrier, on wheels or tracks, weighs around 250 kg in its tracked configuration, in the lower part of the SMOR envelope. It carries tools for light soil preparation, sowing, crop care and transport. Its hardware safety chain operates independently of the computer, and high-level protection functions (geofencing, safety vision) impose their command on navigation through priority arbitration. **The trained person operating the robot defines and respects the domain of use; high-level software helps prevent incidents; low-level control guarantees the return to a safe state.**

Navigation, localisation, geofencing, safety perception, simulation, the JSON Agri format and the mission editors are published on the GitHub organisation [Sustainable-Robotics-Base-for-Crops](https://github.com/Sustainable-Robotics-Base-for-Crops), under the Apache 2.0 licence for code and CC BY 4.0 for specifications. The robot working in the field runs this public code. The controller software, vehicle driver, command contracts, calibrations and remote services remain the manufacturer’s responsibility: SRBC is an **industrial Open Core**, and we describe its openness as it stands.

Any external organisation can thus run a simulated robot end to end, prepare and validate a mission, observe a real robot through a published interface, check the conformance of its files and reuse every navigation building block. The next opening steps will make it possible to command the robot, port the software stack to other vehicles and assemble a machine from public code.

---

## Evaluating what matters to the farm

An isolated demonstration produces an example; a documented, repeated and comparable protocol produces evidence. Our method links each result to an agronomic operation, a reference situation (manual work, tractor, previous practice), an operating domain, a configuration and a versioned catalogue of indicators, all set before the trial. Carried by the mission order – work performed chain, this relationship allows a third party to recalculate what we publish. Indicators cover agronomic service, availability, energy, safety, human time, full cost and effects on soil; they are published with their calculation convention, dispersion and coverage. A missing value is declared as such: absence is information.

The machine can measure its durations, trajectory, energy and localisation quality. The quantities that determine the benefit for the farm often depend on a person: conditions actually encountered, agronomic satisfaction, supervision time, need for a second pass. We propose to collect them at three moments, where the person actually is: during preparation, when loading the mission onto the robot and at the end of the mission, with a tool that pre-fills what it can and asks few questions. Likewise, a measured quantity becomes a criterion when someone sets its threshold in the mission order and the machine knows how to react when it is crossed.

Our first instrumented campaigns confirm the feasibility of this chain across different robots, farms and tools. The body of evidence will grow with its successes as well as its failures, to establish where, when and under which conditions robotics brings a real agroecological benefit.

---

## A commons that belongs to the farming world

We argue that the software ecosystem of agricultural robotics — file formats, trajectory-tracking code, decision algorithms, mission and traceability tools — should become a **commons that belongs to the farming world and that the farming world takes up**.

This commons is first of all a vocabulary. A farm describes its expectations in agronomic terms, a dealer in terms of service, a manufacturer in terms of functions. The primary role of the commons is to allow these stakeholders to **describe, exchange and contest facts** in the same terms. Open code makes this vocabulary usable and proves in production that it works; the vocabulary makes the code substitutable, and therefore the commons governable. A format that several implementations can read escapes any confiscation, including by the company that launched it.

By the farming world, we mean farmers and the workshops, dealers, cooperatives, institutes and manufacturers who work in their service. This ownership is built through five verifiable properties:

- **it stays open**: licences guarantee free use over time, and the trademark protects the meaning of words;
- **it outlives the company that launched it**: public repositories, history and documentation allow others to take it over; in time, its ownership will be entrusted to a non-profit organisation, independent of any manufacturer, whose members by right will include farmers and their organisations;
- **it is governed with the people it serves**: farmers sit in the decisions that concern its purpose and hold a right to contest;
- **it returns data to the farm**: the work performed belongs to the farm, which can read it, keep it, pass it on or keep it to itself without going through a supplier [12];
- **it can be learned**: readable tools, peer training and local workshops place it in the tradition of popular technical education.

The components of a robot call for different degrees of openness. **Common contracts** (formats, indicators, interfaces, conformance criteria) open first; **generic building blocks** (navigation, simulation, diagnostics, editors) develop as software commons; **industrial integration** and the safety chain belong to the manufacturer; **sensitive services and data** keep controlled access. The rule that makes an Open Core defensible fits in one sentence: **open the contracts and the generic logic; keep the hardware realisation, calibration and fleet services.** A manufacturer’s advantage lies in its machine, its safety chain, its service network and its capacity to honour its commitments over time.

Openness shifts value and costs. It reduces the reimplementation of the same foundations and creates maintenance and governance needs that must be funded. Selling and leasing machines, local adaptation, service contracts, maintained releases, training and compliance support sustain companies, provided they forgo captivity through withheld data, subscriptions required for basic operation or artificially closed interfaces. We apply Apache 2.0 to code and CC BY 4.0 to specifications and texts; the question of reciprocity for certain assets will be settled collectively.

Governance follows use. Decisions on the format are already recorded publicly, and a written procedure allows them to be contested. Several stages, triggered by observable facts, organise what comes next, starting with a release committee from the first third-party implementation, then a users’ college with a right to contest as soon as a farmers’ collective, a cooperative or a dealer depends on the format. The final stage transfers ownership of the format and trademark to the non-profit organisation described above; it makes the commons independent of the company that launched it, and we regard it as a condition for the credibility of the whole.

---

## Safety, compliance and co-responsibility

The compliance of an autonomous machine shapes its design, testing and monitoring throughout its life. The Machinery Directive 2006/42/EC applies until 19 January 2027, after which Regulation (EU) 2023/1230 takes over [16]; the ISO 18497:2024 series covers autonomous agricultural machinery [17]. Open code facilitates audit, traceability and maintenance. Safety and compliance, for their part, remain attached to each machine placed on the market or put into service, to its risk analysis, its tests and its validated configuration. A repair that preserves compliance remains a repair, and openness should precisely make it easier; a modification that creates a new hazard engages the person or entity that carries it out. The teams maintaining the commons answer for the quality of contributions; validation of the integration rests with the entity that puts the machine into service.

We propose to complement this regulatory allocation with an **operational co-responsibility**, which specifies for each step who decides, who validates and which evidence is kept.

| Step | Decides | Validates | Evidence kept |
|---|---|---|---|
| Agronomic choice and work window | Farmer | Farmer | intent and criteria in the mission order |
| Field map and known obstacles | Farmer | Farmer | referenced field map |
| Authorised domain and reactions to events | Farmer or operator | Manufacturer’s safety floor | domain and strategies in the order |
| Tool mounting and pre-start check | Operator | Operator | planned and actual configuration |
| Execution | Machine, free to refuse | Manufacturer’s limits, emergency stop | events, requested and applied actions |
| Assessment of the service delivered | Farmer | Farmer | assessment recorded in the work performed |

A cell without an owner is a result: it signals a gap to address. A responsibility understood differently by two parties is also a result, to be discussed openly. This co-responsibility organises day-to-day cooperation and leaves the regulatory responsibility of the manufacturer or integrator fully intact. **The aim is to make knowledge shareable while maintaining explicit responsibility for every machine put into service.**

---

## From code to commons: the roadmap

The diffusion of SMOR will be measured by the capacity of external organisations to understand the interfaces, reproduce a trial, adapt a building block, read a work-performed file and maintain a machine independently of its designer. We proceed in four levels: **make visible** what exists, with its status and limits; **make reproducible** the installation and simulation of a mission; **make interoperable** by publishing contracts and tests; **make diffusible** by building the evidence, skills and field services.

Five work streams follow: consolidating the open base; publishing the command contracts and the vehicle interface, then obtaining a second implementation of the format by an external organisation, the condition for speaking of a standard; building a body of evidence reviewed by an independent institute, with full cost and human time measured over several campaigns; organising the safety of each commercial configuration; developing territorial skills, so that farms, workshops and dealers can diagnose, repair and train others in turn, since people govern what they understand. Deployment proceeds in circles, from internal use to trusted partners, then to third-party integrations and broader diffusion, each step depending on observable criteria. Download counts signal interest; agricultural diffusion is proven in the field.

---

## Limits and call to action

This text proposes a conceptual and technical framework; demonstrating its agronomic and economic benefits requires repeated campaigns and multi-year monitoring, which the full version will document. We know its limits: the SMOR envelope is a design target; SRBC is a first case study, carried by a team engaged in its development; the adoption of JSON Agri by other manufacturers and the publication of the vehicle interface are the next steps; effects on soils and on the farming profession take time to observe. This is the situation of an emerging commons. We publish it to bring together the implementations, skills and uses that will allow it to grow.

Nothing prevents us from innovating quickly and well; everything invites us to do it together [18]. Everyone can take a first step, at their own scale:

- **farmers and collectives**: host an instrumented mission, demand access to the mission orders and work performed on their fields, say at the end of a mission what the machine cannot know;
- **dealers, workshops, integrators**: learn to read a mission file, document a tool mounting, report an incident with its configuration, train a neighbour;
- **robot and tool manufacturers**: implement a reader for the format, publish an interface, however modest, with its limits;
- **institutes, laboratories, educational institutions**: run a protocol, audit a calculation convention, propose a threshold based on observations;
- **cooperatives, local authorities, public funders**: support common infrastructure (test sites, training, documentation, maintenance of standards) on a par with machine purchases;
- **development communities**: improve a building block, write a test, maintain a stable release, take part in governance.

> **Technology becomes agricultural progress when it durably increases farmers’ capacity to understand, decide and act.**  
> Opening robotics means giving the farming world the means to take part in its design, to master its uses and to transmit its knowledge.

**Join the ecosystem**  
[github.com/Sustainable-Robotics-Base-for-Crops](https://github.com/Sustainable-Robotics-Base-for-Crops)

---

## References

[1] Bechar, A., & Vigneault, C. (2016). Agricultural robots for field operations: Concepts and components. *Biosystems Engineering*, 149, 94–111. [https://doi.org/10.1016/j.biosystemseng.2016.06.014](https://doi.org/10.1016/j.biosystemseng.2016.06.014)

[2] Lowenberg-DeBoer, J., Huang, I. Y., Grigoriadis, V., & Blackmore, S. (2020). Economics of robots and automation in field crop production. *Precision Agriculture*, 21, 278–299. [https://doi.org/10.1007/s11119-019-09667-5](https://doi.org/10.1007/s11119-019-09667-5)

[3] Agreste. (2022). *Recensement agricole 2020 — Typologie des exploitations selon leur dimension économique* [2020 agricultural census — farm typology by economic size]. French Ministry of Agriculture. [https://agreste.agriculture.gouv.fr/agreste-web/disaron/RA2020_001/detail/](https://agreste.agriculture.gouv.fr/agreste-web/disaron/RA2020_001/detail/)

[4] Wezel, A., Bellon, S., Doré, T., Francis, C., Vallod, D., & David, C. (2009). Agroecology as a science, a movement and a practice. A review. *Agronomy for Sustainable Development*, 29(4), 503–515. [https://doi.org/10.1051/agro/2009004](https://doi.org/10.1051/agro/2009004)

[5] Ditzler, L., & Driessen, C. (2022). Automating Agroecology: How to Design a Farming Robot Without a Monocultural Mindset? *Journal of Agricultural and Environmental Ethics*, 35, 2. [https://doi.org/10.1007/s10806-021-09876-x](https://doi.org/10.1007/s10806-021-09876-x)

[6] Daum, T. (2021). Farm robots: ecological utopia or dystopia? *Trends in Ecology & Evolution*, 36(9), 774–777. [https://doi.org/10.1016/j.tree.2021.06.002](https://doi.org/10.1016/j.tree.2021.06.002)

[7] Spykman, O., Lowenberg-DeBoer, J., & Gandorfer, M. (2026). Crop robots as potential enablers of economical and biodiversity-smart small-scale farming. *Precision Agriculture*. [https://doi.org/10.1007/s11119-026-10367-0](https://doi.org/10.1007/s11119-026-10367-0)

[8] ISO. (2015). *ISO 11783-10:2015 — Tractors and machinery for agriculture and forestry — Serial control and communications data network — Part 10: Task controller and management information system data interchange*. [https://www.iso.org/standard/61581.html](https://www.iso.org/standard/61581.html)

[9] AgGateway. (2025). *ADAPT Standard 2.0 — Documentation*. [https://adaptstandard.org/docs/](https://adaptstandard.org/docs/)

[10] Agricultural Industry Electronics Foundation (AEF). (n.d.). *Autonomy in Agriculture (AUT) — project team, use cases and work items*. [https://www.aef-online.org/aef-aut/](https://www.aef-online.org/aef-aut/)

[11] Felske, M., Redenius, J., Happich, G., & Schöning, J. (2026). Towards an Agricultural Operational Design Domain: A Framework. *Smart Agricultural Technology*. [https://doi.org/10.1016/j.atech.2026.102246](https://doi.org/10.1016/j.atech.2026.102246)

[12] Holm, S., Pedersen, S. M., & Tamirat, T. W. (2024). Robots in agriculture — A case-based discussion of ethical concerns on job loss, responsibility, and data control. *Smart Agricultural Technology*, 9, 100633. [https://doi.org/10.1016/j.atech.2024.100633](https://doi.org/10.1016/j.atech.2024.100633)

[13] Batey, T. (2009). Soil compaction and soil management — a review. *Soil Use and Management*, 25(4), 335–345. [https://doi.org/10.1111/j.1475-2743.2009.00236.x](https://doi.org/10.1111/j.1475-2743.2009.00236.x)

[14] Stilgoe, J., Owen, R., & Macnaghten, P. (2013). Developing a framework for responsible innovation. *Research Policy*, 42(9), 1568–1580. [https://doi.org/10.1016/j.respol.2013.05.008](https://doi.org/10.1016/j.respol.2013.05.008)

[15] Sustainable Robotics Base for Crops. (2026). *Agri JSON format, version 3 — schema, profiles, vocabularies, indicator registry and documentation*. CC BY 4.0 licence. [https://github.com/Sustainable-Robotics-Base-for-Crops/json_agri_format](https://github.com/Sustainable-Robotics-Base-for-Crops/json_agri_format)

[16] European Parliament & Council of the European Union. (2023). *Regulation (EU) 2023/1230 of 14 June 2023 on machinery*. [https://eur-lex.europa.eu/eli/reg/2023/1230/oj](https://eur-lex.europa.eu/eli/reg/2023/1230/oj)

[17] ISO. (2024). *ISO 18497, parts 1 to 4 — Agricultural machinery and tractors — Safety of partially automated, semi-autonomous and autonomous machinery*. [https://www.iso.org/standard/82684.html](https://www.iso.org/standard/82684.html)

[18] Prévault-Osmani, A. (2026). *Manifesto for open agricultural robotics*. Sustainable Robotics Base for Crops. CC BY 4.0 licence. [https://github.com/Sustainable-Robotics-Base-for-Crops/ecosystem/blob/main/manifesto/MANIFESTO.en.md](https://github.com/Sustainable-Robotics-Base-for-Crops/ecosystem/blob/main/manifesto/MANIFESTO.en.md)

---

## About the author

**Alexandre Prévault-Osmani**  
CTO and co-founder of SABI AGRI

An engineer by profession and a farmer by background, Alexandre Prévault-Osmani has worked since 2015 at the intersection of electrification, agricultural robotics, Open Source and agroecology. He takes part in the development of the SRBC robot, presented in this text as a case study.

**Contact**

- GitHub: [Alexandre-PO](https://github.com/Alexandre-PO)
- LinkedIn: [alexandre-po](https://www.linkedin.com/in/alexandre-po)
