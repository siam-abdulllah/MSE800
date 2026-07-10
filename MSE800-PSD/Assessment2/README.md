# Assessment 2 — Local Community Skill Exchange and Help Board

**Group F:** Syed Abdullah Maaz, Fahad Ahmed  
**Assessment:** MSE800 Assessment 2  
**Methodology:** Agile (Scrum) — 3 sprints × 2 weeks (6 weeks total)

---

## Project Overview

The **Local Community Skill Exchange and Help Board** is a web platform where neighbours post help requests and offers, match by location and skill, chat in real time, and rate each other after completion. The project addresses a common gap in everyday life: residents need small help (tutoring, bike repair, pet sitting, moving boxes) but do not always know who nearby can assist.

**Objectives:**

- Connect neighbours safely for small daily tasks
- Reduce reliance on expensive commercial apps
- Build community trust through profiles, ratings, and moderation

**Expected outcome:** A working Django prototype where users register, post and browse help listings, search nearby, chat in real time, leave ratings, and admins moderate content — suitable for a professional software engineering assessment.

**Technology stack:** Python/Django, PostgreSQL, Django Channels + Redis (real-time chat), GeoDjango or postcode search, responsive web UI, Docker Compose deployment.

---

## Māori Principles and Māori Data Sovereignty

This section explains how Māori principles and **Māori Data Sovereignty** (MDS) will be incorporated throughout the project development lifecycle. Our approach is guided by [Te Mana Raraunga](https://www.temanararaunga.maori.nz/) — the Māori Data Sovereignty Network — and aligns Māori values with responsible software design for a community platform operating in Aotearoa New Zealand.

### Guiding Māori Values

| Principle | Meaning | Application in this project |
|-----------|---------|----------------------------|
| **Rangatiratanga** | Authority and self-determination | Users retain control over their profile, listings, and personal data; they can edit, export, or delete their information without unnecessary barriers. |
| **Whakapapa** | Relationships and context | Data is linked meaningfully (user → profile → listing → conversation) with clear lineage; metadata records who created, modified, and accessed records. |
| **Whanaungatanga** | Relationships and collective responsibility | The platform supports community connection and mutual support — the core purpose of neighbour-to-neighbour exchange — with moderation shaped by community safety needs. |
| **Kaitiakitanga** | Guardianship and stewardship | The development team acts as kaitiaki of stored data: minimising collection, securing storage, and protecting location and identity information (suburb/postcode only, no street addresses). |
| **Manaakitanga** | Care, respect, and hospitality | UX, moderation, and support flows treat users with dignity; reporting and blocking tools protect vulnerable members from harm. |
| **Kotahitanga** | Collective benefit | Features prioritise community wellbeing over commercial extraction — no sale of user data, no hidden profiling for third parties. |

### Embedding Māori Data Sovereignty Across the Lifecycle

#### 1. Planning and Design

During initial planning (documented in [PROJECT_PLAN.md](./PROJECT_PLAN.md), [REQUIREMENTS.md](./REQUIREMENTS.md), and [FEASIBILITY_STUDY.md](./FEASIBILITY_STUDY.md)), MDS is treated as a first-class concern alongside functional and non-functional requirements:

- **Needs analysis** includes Māori and wider community stakeholders (residents, moderators, administrators) to understand expectations for privacy, safety, and cultural respect.
- **Data inventory** identifies what is collected (account details, suburb/postcode, messages, reviews) and what is deliberately excluded (exact addresses, unnecessary demographic fields).
- **Privacy by design** is specified in NFR-04 (suburb/postcode only) and extended with planned user rights: access, correction, deletion, and export of personal data.
- **Cultural safety** is considered in wireframes and category design — avoiding stereotypes, using inclusive language, and planning optional te reo Māori UI labels where practical.
- **Governance model** defines who holds authority over platform data (users for their own data; admins/moderators for community safety within documented policies).

#### 2. Development and Implementation

During sprints (see sprint plan in [REQUIREMENTS.md](./REQUIREMENTS.md)), MDS principles are implemented in code and process:

- **Rangatiratanga in code:** Profile and account modules enforce owner-only edit/delete; account deletion cascades or anonymises related records per a documented retention policy.
- **Kaitiakitanga in security:** Password hashing (NFR-01), CSRF/XSS protection (NFR-02), role-based authorisation (NFR-03), encrypted sessions, and audit logging (NFR-13) for moderation and login events.
- **Whakapapa in data models:** Django models record `created_at`, `updated_at`, and actor references; moderation actions retain an audit trail for accountability.
- **Manaakitanga in safety features:** Report, block, and moderation workflows (FR-19, FR-20, FR-11) protect users from abusive behaviour; email notifications respect user preferences.
- **Data locality:** Staging and production deployment target New Zealand–based or user-approved hosting where feasible, documented in `docs/DEPLOYMENT.md`.
- **Transparency:** A plain-language privacy notice explains what data is collected, why, how long it is kept, and who can access it — linked from registration and profile settings.

#### 3. Testing, Release, and Ongoing Stewardship

In the Release Sprint and beyond:

- **UAT checklist** (FR-29) includes scenarios for privacy controls, data deletion, and moderation — validating that user authority is honoured in practice.
- **Accessibility** (NFR-10) supports equitable access, including keyboard navigation and semantic HTML, aligning with inclusive community values.
- **Review and improvement:** Sprint retrospectives include a standing item on data sovereignty and cultural safety; feedback from Māori students, community advisors, or iwi/hapū representatives (where available) informs backlog prioritisation.
- **Future enhancement:** Te reo Māori localisation, community co-governance of moderation policy, and formal data-sharing agreements if the platform later integrates with council or iwi services.

### Summary

Māori Data Sovereignty is not a single feature but a thread running through planning, design, development, and release. By applying rangatiratanga (user control), kaitiakitanga (responsible stewardship), whanaungatanga (community connection), and manaakitanga (respectful care), this project aims to build technology that strengthens — rather than extracts from — local community relationships in Aotearoa New Zealand.

---

## Documentation

| Document | Description |
|----------|-------------|
| [Proposal.rtf](./Proposal.rtf) | Original project proposal |
| [FUNCTIONAL_AND_NON_FUNCTIONAL_REQUIREMENTS.md](./FUNCTIONAL_AND_NON_FUNCTIONAL_REQUIREMENTS.md) | Standalone FR/NFR document — GeeksforGeeks structure |
| [Functional_and_NonFunctional_Requirements.docx](./Functional_and_NonFunctional_Requirements.docx) | Word export of the standalone FR/NFR document (generated) |
| [REQUIREMENTS.md](./REQUIREMENTS.md) | Sprint traceability specification (IDs, priorities, implementation paths) |
| [PROJECT_PLAN.md](./PROJECT_PLAN.md) | Agile project plan (3 sprints × 2 weeks) |
| [PROJECT_REPORT.md](./PROJECT_REPORT.md) | Full project report including feasibility study |
| [FEASIBILITY_STUDY.md](./FEASIBILITY_STUDY.md) | Detailed feasibility study |
| [Project_Report.docx](./Project_Report.docx) | Word — full project report (generated) |
| [Feasibility_Study.docx](./Feasibility_Study.docx) | Word — standalone feasibility study (generated) |

---

## Generate Word Documents

```bash
# Standalone Functional & Non-Functional Requirements (GeeksforGeeks)
PYTHONPATH="../Week9/Activity1/.pylibs" python3 generate_requirements_doc.py

# Combined project plan + requirements
PYTHONPATH="../Week9/Activity1/.pylibs" python3 generate_documentation.py

# Project report (includes feasibility study section)
PYTHONPATH="../Week9/Activity1/.pylibs" python3 generate_project_report.py

# Standalone feasibility study
PYTHONPATH="../Week9/Activity1/.pylibs" python3 generate_feasibility_doc.py
```

Requires `python-docx` and `matplotlib` (see Week 9 Activity 1 dependencies or install via pip).

---

## Planned Application Structure

```
backend/
├── accounts/       # Registration, login, roles (Sprint 1)
├── profiles/       # User profiles (Sprint 1)
├── listings/       # Help posts and search (Sprint 1–2)
├── chat/           # Real-time messaging (Sprint 2)
├── reviews/        # Ratings (Sprint 2)
├── moderation/     # Report, block, admin (Sprint 1–2)
└── notifications/  # Email (Sprint 1–2)
```

See [REQUIREMENTS.md](./REQUIREMENTS.md) for full traceability from requirement ID to implementation path and sprint.

---

## References

- Te Mana Raraunga — Māori Data Sovereignty Network: https://www.temanararaunga.maori.nz/
- Te Mana Raraunga — Principles: https://www.temanararaunga.maori.nz/single-post/2018/02/09/te-mana-raraunga-principles
