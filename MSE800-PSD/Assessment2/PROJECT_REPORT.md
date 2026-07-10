# Project Report

**Project:** Local Community Skill Exchange and Help Board  
**Assessment:** MSE800 Assessment 2  
**Group:** Group F — Syed Abdullah Maaz, Fahad Ahmed  
**Methodology:** Agile (Scrum) — 3 sprints × 2 weeks  
**Duration:** 6 weeks

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Introduction and Project Background](#2-introduction-and-project-background)
3. [Objectives and Expected Outcomes](#3-objectives-and-expected-outcomes)
4. [Technology Stack](#4-technology-stack)
5. [Requirements Overview](#5-requirements-overview)
6. [Agile Project Plan Summary](#6-agile-project-plan-summary)
7. [Feasibility Study](#7-feasibility-study)
8. [Conclusion and Recommendation](#8-conclusion-and-recommendation)
9. [References and Related Documents](#9-references-and-related-documents)

---

## 1. Executive Summary

This report documents the planning and feasibility analysis for the **Local Community Skill Exchange and Help Board** — a web platform where neighbours post help requests and offers, match by location and skill, chat in real time, and rate each other after completion.

The project uses an agile 3-sprint plan (6 weeks) with a dedicated Release Sprint. Requirements are defined in [REQUIREMENTS.md](./REQUIREMENTS.md). A feasibility study (Section 7) confirms the solution is **technically, operationally, financially, and schedule feasible**. The team recommends proceeding with development.

---

## 2. Introduction and Project Background

In everyday life, residents often need small help — tutoring, bike repair, pet sitting, moving boxes — but do not know who nearby can assist. Commercial platforms charge fees and are not always suited to casual community exchange.

This project builds a community platform to connect neighbours safely, reduce the cost of small services, and build trust through profiles and reviews. The deliverable is a working prototype suitable for a professional software engineering assessment.

---

## 3. Objectives and Expected Outcomes

**Objectives:**

- Connect neighbours safely for small daily tasks
- Reduce reliance on expensive commercial apps
- Build community trust through profiles, ratings, and moderation

**Expected outcome:** A working prototype where users register, post and browse help listings, search nearby, chat in real time, leave ratings, and admins moderate content.

---

## 4. Technology Stack

| Layer | Technology |
|-------|------------|
| Backend | Python, Django, Django REST Framework |
| Database | PostgreSQL |
| Real-time | Django Channels + Redis |
| Location | GeoDjango or postcode/suburb search |
| Frontend | Responsive web UI (Django templates) |
| Testing | pytest-django, factory_boy |
| Deployment | Docker Compose, staging server |

---

## 5. Requirements Overview

Requirements are documented in [REQUIREMENTS.md](./REQUIREMENTS.md) and [FUNCTIONAL_AND_NON_FUNCTIONAL_REQUIREMENTS.md](./FUNCTIONAL_AND_NON_FUNCTIONAL_REQUIREMENTS.md).

| Type | Count | Examples |
|------|-------|----------|
| Functional (FR) | 23 | Registration, listings, chat, ratings, UAT |
| Non-functional (NFR) | 15 | Security, performance, deployability, testing |
| Sprints | 3 | Sprint 1 (foundation), Sprint 2 (features), Release Sprint |

---

## 6. Agile Project Plan Summary

| Sprint | Weeks | Focus |
|--------|-------|-------|
| Sprint 1 | 1–2 | User accounts, profiles, listings, admin |
| Sprint 2 | 3–4 | Search, chat, ratings, safety features |
| Release Sprint | 5–6 | UAT, deployment, regression, release notes |

Full backlog and activity log: [PROJECT_PLAN.md](./PROJECT_PLAN.md).

---

## 7. Feasibility Study

This section follows the [GeeksforGeeks eight-type feasibility framework](https://www.geeksforgeeks.org/software-engineering/types-of-feasibility-study-in-software-project-development/). Full analysis: [FEASIBILITY_STUDY.md](./FEASIBILITY_STUDY.md).

### 7.1 Need and Aim

**Need:** Determine whether the project is practically feasible before committing six weeks of development; identify risks; provide a go/no-go decision.

**Aim:** Confirm the system contributes to project objectives (community connection), can be built with current technology (Django stack), and can integrate with standard services (email, future APIs).

### 7.2 Feasibility Study Process

1. **Information assessment** — reviewed proposal and requirements  
2. **Information collection** — gathered data on technology, cost, schedule, legal, market, and resources  
3. **Report writing** — documented eight feasibility types (this section)  
4. **General information** — summary and recommendation (Section 7.10)

### 7.3 Summary of Findings — Eight Feasibility Types

| Type | Verdict | Key finding |
|------|---------|-------------|
| **Technical** | Feasible | Django, PostgreSQL, Redis, Channels — mature stack; team skills sufficient |
| **Operational** | Feasible | Clear user journeys; moderation and maintenance via Django admin |
| **Economic** | Feasible | **Most important** — ~$0 cost; high community and learning benefit |
| **Legal** | Feasible | Privacy Act considerations addressed; moderation and open-source compliance |
| **Schedule** | Feasible | 6-week / 3-sprint plan meets assessment deadline |
| **Cultural & Political** | Feasible | Aligns with community mutual-aid values; moderation handles sensitivity |
| **Market** | Feasible | Clear local need; differentiated from fee-based commercial apps |
| **Resource** | Feasible | 2 developers, open-source tools, ~240 person-hours available |
| **Overall** | **Proceed** | Weighted score: **4.47 / 5.00** |

### 7.4 Technical Feasibility

Analyses hardware, software, team skills, and technology maintainability. Django provides auth, ORM, admin, and REST APIs. Channels + Redis supports chat. Suburb/postcode search avoids GeoDjango risk. **Verdict: Feasible.**

### 7.5 Operational Feasibility

Analyses service delivery, usability, and post-deployment maintenance. Members, moderators, and admins have defined workflows. Responsive UI and ≤ 5-click journeys (NFR-09). **Verdict: Feasible.**

### 7.6 Economic Feasibility

Analyses cost vs benefit — the **most important** feasibility type per GeeksforGeeks. Direct cost ~$0–$20/month; benefits include community connection, cost savings vs commercial apps, and assessment learning outcomes. **Verdict: Feasible.**

### 7.7 Legal Feasibility

Analyses Privacy Act compliance, user-generated content, open-source licences, and moderation obligations. No payment processing avoids financial regulation. Privacy policy and suburb-only display planned. **Verdict: Feasible.**

### 7.8 Schedule Feasibility

Analyses timelines and deadlines. Sprint 1 (foundation), Sprint 2 (features), Release Sprint (UAT/deploy) over 6 weeks. ~240 person-hours for 2 developers. **Verdict: Feasible.**

### 7.9 Cultural, Political, Market, and Resource Feasibility

- **Cultural & Political:** Platform supports neighbourhood cooperation; report/block and moderation address community sensitivity. **Feasible.**
- **Market:** Strong need for local help; differentiated from Airtasker-style fee platforms. **Feasible.**
- **Resource:** Human, financial, technology, and hardware resources all available. **Feasible.**

### 7.10 Feasibility Decision and Recommendation

| Type | Weight | Score | Weighted |
|------|--------|-------|----------|
| Technical | 15% | 5 | 0.75 |
| Operational | 12% | 4 | 0.48 |
| Economic | 20% | 5 | 1.00 |
| Legal | 8% | 4 | 0.32 |
| Schedule | 15% | 4 | 0.60 |
| Cultural & Political | 8% | 4 | 0.32 |
| Market | 10% | 4 | 0.40 |
| Resource | 12% | 5 | 0.60 |
| **Total** | 100% | | **4.47 / 5.00** |

**Recommendation: Proceed with development** — all eight feasibility types assessed as feasible.

---

## 8. Conclusion and Recommendation

The Local Community Skill Exchange and Help Board is a viable, feasible project for MSE800 Assessment 2. Requirements are defined, the agile plan is structured across three sprints, and the feasibility study confirms the solution can be built, operated, and delivered within budget and schedule.

**Next steps:**

1. Execute Sprint 1 — foundation (Weeks 1–2)
2. Execute Sprint 2 — core features (Weeks 3–4)
3. Execute Release Sprint — UAT and deployment (Weeks 5–6)

---

## 9. References and Related Documents

| Document | Location |
|----------|----------|
| Project proposal | [Proposal.rtf](./Proposal.rtf) |
| Requirements specification | [REQUIREMENTS.md](./REQUIREMENTS.md) |
| Functional & non-functional requirements | [FUNCTIONAL_AND_NON_FUNCTIONAL_REQUIREMENTS.md](./FUNCTIONAL_AND_NON_FUNCTIONAL_REQUIREMENTS.md) |
| Feasibility study (full) | [FEASIBILITY_STUDY.md](./FEASIBILITY_STUDY.md) |
| Agile project plan | [PROJECT_PLAN.md](./PROJECT_PLAN.md) |
| Word — project report | `Project_Report.docx` (generated) |
| Word — feasibility study | `Feasibility_Study.docx` (generated) |

**Generate Word reports:**

```bash
PYTHONPATH="../Week9/Activity1/.pylibs" python3 generate_project_report.py
PYTHONPATH="../Week9/Activity1/.pylibs" python3 generate_feasibility_doc.py
```
