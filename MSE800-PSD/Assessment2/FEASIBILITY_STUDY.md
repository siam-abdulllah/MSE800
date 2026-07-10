# Feasibility Study

**Project:** Local Community Skill Exchange and Help Board  
**Assessment:** MSE800 Assessment 2  
**Group:** Group F — Syed Abdullah Maaz, Fahad Ahmed  
**Date:** June 2026

**Reference:** [Types of Feasibility Study in Software Project Development — GeeksforGeeks](https://www.geeksforgeeks.org/software-engineering/types-of-feasibility-study-in-software-project-development/)

**Related documents:** [Proposal.rtf](./Proposal.rtf) · [REQUIREMENTS.md](./REQUIREMENTS.md) · [PROJECT_PLAN.md](./PROJECT_PLAN.md) · [PROJECT_REPORT.md](./PROJECT_REPORT.md)

---

## 1. Introduction

A **feasibility study** evaluates whether a proposed software project is practical and beneficial before development begins. It is a key stage in the Software Project Management Process (SDLC) and helps decide whether to proceed, stop, or revise the project plan.

This study analyses the Local Community Skill Exchange and Help Board — a web platform where neighbours post help requests and offers, match by location and skill, chat in real time, and rate each other — across the **eight feasibility types** defined by [GeeksforGeeks](https://www.geeksforgeeks.org/software-engineering/types-of-feasibility-study-in-software-project-development/).

---

## 2. Need of Feasibility Study

A feasibility study is required before committing development effort because it:

- Determines whether the proposed project is **practically feasible** or should be stopped or revised
- **Identifies risk factors** in development and deployment (e.g. WebSocket complexity, scope creep)
- **Narrows business alternatives** — confirms a community help board is preferable to building unrelated systems
- **Enhances success rate** by analysing technical, economic, schedule, and resource parameters before coding begins
- Provides a **go / no-go conclusion** for Group F and the MSE800 Assessment 2 timeline

Without this study, the team could invest six weeks in a solution that exceeds available skills, budget, or schedule.

---

## 3. Aim of Feasibility Study

Per GeeksforGeeks, the feasibility study aims to answer:

| Aim | Assessment for this project |
|-----|----------------------------|
| Does the system **contribute to overall objectives**? | Yes — connects neighbours, reduces cost of small tasks, builds community trust (see [Proposal.rtf](./Proposal.rtf)) |
| Can the system be **implemented using current technology**? | Yes — Django, PostgreSQL, Redis, Channels are mature and course-aligned |
| Can the system **integrate with existing systems**? | Yes — REST APIs and standard email (SMTP) allow future integration with council portals or community groups; prototype stands alone for assessment |

---

## 4. Feasibility Study Process

This report follows the four-step feasibility analysis process:

| Step | Activity | How it was applied |
|------|----------|-------------------|
| 1. Information assessment | Define project concept, aims, and objectives | Reviewed [Proposal.rtf](./Proposal.rtf), [REQUIREMENTS.md](./REQUIREMENTS.md), and stakeholder needs |
| 2. Information collection | Gather data on technology, cost, schedule, legal, and market context | Analysed tech stack, sprint plan, NZD cost estimates, Privacy Act considerations, and competitor landscape |
| 3. Report writing | Document analysis and findings for each feasibility type | This document — Sections 5–12 |
| 4. General information | Summarise conclusions and recommendation | Section 13 — Executive Summary and Decision |

---

## 5. Types of Feasibility Study — Summary

| # | Type | Verdict | Priority (GeeksforGeeks) |
|---|------|---------|--------------------------|
| 5.1 | Technical Feasibility | **Feasible** | High |
| 5.2 | Operational Feasibility | **Feasible** | High |
| 5.3 | Economic Feasibility | **Feasible** | **Most important** |
| 5.4 | Legal Feasibility | **Feasible** | Moderate |
| 5.5 | Schedule Feasibility | **Feasible** | High |
| 5.6 | Cultural and Political Feasibility | **Feasible** | Moderate |
| 5.7 | Market Feasibility | **Feasible** | Moderate |
| 5.8 | Resource Feasibility | **Feasible** | High |
| | **Overall** | **Proceed with development** | |

---

## 5.1 Technical Feasibility

**Definition (GeeksforGeeks):** Analyses whether current hardware, software, and required technology can support project development; assesses technical team skills, whether existing technology can be used, and ease of maintenance and upgrade.

**Analysis:**

| Factor | Assessment |
|--------|------------|
| Hardware | Standard developer laptops sufficient; staging VM for deployment |
| Software | Python, Django, DRF, PostgreSQL, Redis — all open source and well documented |
| Team technical skills | Group F has MSE800 course experience in Python, web development, and software engineering practices |
| Existing technology reuse | Django auth, admin, ORM, and CSRF reduce custom development |
| Maintenance & upgrade | Modular Django apps (accounts, listings, chat, reviews, moderation); migrations support schema changes |

| Component | Technology | Feasibility rationale |
|-----------|------------|----------------------|
| Backend & API | Python, Django, DRF | Industry-standard; extensive documentation |
| Database | PostgreSQL | Reliable storage for users, listings, messages, reviews |
| Real-time chat | Django Channels + Redis | Established WebSocket pattern for Django |
| Location search | GeoDjango or postcode/suburb filter | Text filter fallback if GeoDjango is complex (FR-12) |
| Testing | pytest-django, factory_boy | Supports ≥ 30 automated tests (NFR-12) |
| Deployment | Docker Compose | Reproducible staging environment (NFR-14) |

| Risk | Mitigation |
|------|------------|
| GeoDjango complexity | Suburb/postcode text search as primary filter |
| WebSocket deployment | Test Channels + Redis early in Sprint 2 |
| Scope exceeds capacity | Must/Should prioritisation in [REQUIREMENTS.md](./REQUIREMENTS.md) |

**Verdict: Technically feasible** — no unproven technology required; team skills match the stack.

---

## 5.2 Operational Feasibility

**Definition (GeeksforGeeks):** Analyses the degree to which the product can provide required services; ease of operation and maintenance after deployment; usability; and whether the proposed solution is acceptable to users and operators.

**Analysis:**

| Factor | Assessment |
|--------|------------|
| Service to requirements | All Must functional requirements (FR-01 – FR-21) map to clear user journeys |
| Ease of operation | Responsive UI (FR-22); ≤ 5-click core journeys (NFR-09) |
| Maintenance after deployment | Django admin for user/listing management; logging for audit (NFR-13) |
| Usability | Categories, validation messages, and UAT checklist (FR-29) in Release Sprint |
| Acceptability of solution | Email verification, ratings, report/block, and moderation build user trust |

| Stakeholder | Operational need | How addressed |
|-------------|------------------|---------------|
| Community member | Post, browse, chat, rate | FR-07 – FR-08, FR-15 – FR-18 |
| Moderator | Review reports | FR-11, FR-19 |
| Admin | Manage platform | Django admin (FR-11) |

**Verdict: Operationally feasible** — workflows match real community use; maintenance manageable by the team.

---

## 5.3 Economic Feasibility

**Definition (GeeksforGeeks):** Analyses project **cost vs benefit** — development cost (hardware, software, design, operations) against financial and practical benefits. This is the **most important** feasibility type.

**Analysis — Costs:**

| Cost item | Amount (NZD) | Notes |
|-----------|--------------|-------|
| Development labour | $0 | Group F — assessment project |
| Software licences | $0 | Open-source stack |
| Hardware (dev machines) | $0 | Already owned |
| Design & development | $0 | In-house |
| Staging infrastructure | $0 – $15/month | Free tiers / student cloud credits |
| Operational cost (demo) | $0 – $5/month | Minimal for prototype |
| **Total direct cost** | **~$0 – $20/month** | |

**Analysis — Benefits:**

| Benefit | Value |
|---------|-------|
| Community connection | Stronger local networks; informal help formalised |
| Cost savings vs commercial apps | Avoids 10–20% platform fees (Airtasker, etc.) |
| Trust building | Profiles and ratings reduce risk of unknown helpers |
| Assessment / learning outcome | Demonstrates full-stack software engineering skills |
| Future production potential | Low incremental cost to scale beyond prototype |

**Cost–benefit conclusion:** Benefits significantly outweigh costs. Economic feasibility is strongly positive for an academic prototype with near-zero direct expenditure.

**Verdict: Economically feasible** — highest-priority feasibility type; project is financially justified.

---

## 5.4 Legal Feasibility

**Definition (GeeksforGeeks):** Analyses legality of the project — data protection, social media/community platform obligations, licences, copyright, and ethical requirements.

**Analysis:**

| Legal area | Assessment | Mitigation |
|------------|------------|------------|
| Privacy & data protection | User emails, profiles, messages, and photos stored | Collect minimum data; suburb/postcode only (NFR-04); Privacy Policy in Release Sprint docs |
| New Zealand Privacy Act 2020 | Personal information handled | Secure storage (PostgreSQL); hashed passwords (NFR-01); user can edit/delete own profile |
| User-generated content | Listings, chat, reviews posted by members | Terms of use; report/block (FR-19, FR-20); moderator review (FR-11) |
| Open-source licences | Django (BSD), PostgreSQL, Redis | Compliant use; no licence conflict for assessment prototype |
| Copyright | Profile photos and listing content uploaded by users | Users retain ownership; platform displays with permission implied by posting |
| Payment / financial regulation | No payments in prototype | Out of scope — avoids PCI-DSS and financial services regulation |
| Age / consent | Community platform for general residents | Terms note users must be 18+ or have guardian consent for assessment scope |

**Verdict: Legally feasible** — no legal barriers identified; standard privacy and moderation controls address main risks.

---

## 5.5 Schedule Feasibility

**Definition (GeeksforGeeks):** Analyses whether the project can be **completed on time**; deadlines and timelines impact organisational goals if missed.

**Analysis:**

| Sprint | Duration | Deliverables |
|--------|----------|--------------|
| Sprint 1 | Weeks 1–2 | Auth, profiles, listings, admin; 12 unit tests |
| Sprint 2 | Weeks 3–4 | Search, chat, ratings, safety; +18 integration tests |
| Release Sprint | Weeks 5–6 | Staging deploy, UAT, regression, release notes |
| **Total** | **6 weeks** | Assessment deadline met |

| Factor | Assessment |
|--------|------------|
| Team capacity | 2 developers × ~20 hrs/week × 6 weeks ≈ 240 person-hours |
| Must requirements scoped | FR-01 – FR-21 + FR-29 fit within Sprints 1–2 + Release |
| Buffer | Dedicated Release Sprint — no new major features in Weeks 5–6 |
| Assessment deadline | 6-week plan aligned to MSE800 Assessment 2 window |

| Schedule risk | Mitigation |
|---------------|------------|
| Sprint 2 overload | Parallel task split; start Channels in Week 3 |
| Integration delays | Automated tests from Sprint 1; regression in Release Sprint |

**Verdict: Schedule feasible** — 3-sprint plan with Release Sprint meets assessment timeline.

---

## 5.6 Cultural and Political Feasibility

**Definition (GeeksforGeeks):** Assesses how the project affects organisational culture and political environment; considers acceptance of change and potential internal or community opposition.

**Analysis:**

| Factor | Assessment |
|--------|------------|
| Community culture fit | Platform supports **neighbourhood cooperation** — aligns with community values of mutual aid |
| Acceptance of technology | Web-based; no app store install required — low barrier for diverse age groups |
| Trust in strangers | Cultural hesitation to ask neighbours for help | Mitigated by profiles, ratings, suburb-only display, and moderation |
| Political / organisational barriers | Academic assessment — no external political opposition | Group F and course tutors support the project scope |
| Moderation sensitivity | Diverse community backgrounds | Report/block and moderator workflow (FR-19, FR-11) handle inappropriate content |
| Change management | New platform replaces informal word-of-mouth | Simple onboarding (register → post) reduces adoption friction |

**Verdict: Culturally and politically feasible** — solution aligns with community cooperation values; moderation addresses cultural sensitivity.

---

## 5.7 Market Feasibility

**Definition (GeeksforGeeks):** Evaluates whether the market is willing and able to accept the proposed system; analyses target market, user needs, and competitors.

**Analysis:**

| Factor | Assessment |
|--------|------------|
| Target market | Local residents needing or offering small daily help (tutoring, repairs, pet sitting, moving) |
| User need | Strong — informal help is common but hard to discover nearby |
| Market willingness | Residents prefer free/low-cost community exchange over paid commercial apps for simple tasks |
| Competitors | Airtasker, TaskRabbit — fee-based, commercial focus | This platform: **free community exchange**, local trust focus |
| Differentiation | Suburb-based matching, ratings, moderation, no platform fees |
| Market size (prototype) | Single community / campus demo scope — sufficient for assessment |
| Future market potential | Scalable to suburbs, community groups, or housing associations |

**Verdict: Market feasible** — clear user need; differentiated from commercial competitors; viable for prototype and future community rollout.

---

## 5.8 Resource Feasibility

**Definition (GeeksforGeeks):** Evaluates whether adequate **human, financial, technological, and hardware** resources are available to complete the project successfully.

**Analysis:**

| Resource type | Required | Available | Gap |
|---------------|----------|-----------|-----|
| Human — developers | 2 full-stack developers | Group F (2 members) | None |
| Human — moderators | Admin/moderator for demo | Group F acts as admin | None for prototype |
| Financial | $0 – $20/month staging | Student budget / free tiers | None |
| Technology — software | Django, PostgreSQL, Redis, Git, Docker | Open source; course-provided tools | None |
| Technology — hardware | Dev laptops, staging VM | Owned / free cloud tier | None |
| Knowledge | Python, Django, agile practices | MSE800 course + documentation | None critical |
| Time | ~240 person-hours over 6 weeks | 3-sprint plan | Managed via Must-first scope |

**Verdict: Resource feasible** — all required resources are available or obtainable at negligible cost.

---

## 6. Integration Feasibility (Supplementary)

Although not a separate GeeksforGeeks type, integration is part of the **aim** of feasibility study:

| Integration point | Feasibility |
|-------------------|-------------|
| Email (SMTP) for verification and notifications | Standard Django email backend — feasible |
| Future council or community group portals | REST API (DRF) allows future integration |
| Mobile apps (future) | Out of scope; API-ready backend supports future apps |

---

## 7. Feasibility Decision Matrix

| Feasibility type | Weight | Score (1–5) | Weighted | Comments |
|------------------|--------|-------------|----------|----------|
| Technical | 15% | 5 | 0.75 | Proven stack; defined fallbacks |
| Operational | 12% | 4 | 0.48 | Clear roles; demo seeding needed |
| **Economic** | **20%** | **5** | **1.00** | **Most important — near-zero cost, high benefit** |
| Legal | 8% | 4 | 0.32 | Privacy and moderation addressed |
| Schedule | 15% | 4 | 0.60 | Realistic 3-sprint plan |
| Cultural & Political | 8% | 4 | 0.32 | Aligns with community values |
| Market | 10% | 4 | 0.40 | Clear need; differentiated offering |
| Resource | 12% | 5 | 0.60 | Team, tools, and time available |
| **Total** | **100%** | | **4.47 / 5.00** | **Viable — proceed** |

*Scoring: 1 = not feasible, 5 = highly feasible*

---

## 8. Overall Viability and Recommendation

### 8.1 Justification of the Proposed Solution

The Local Community Skill Exchange and Help Board is **viable** because:

1. **Technical:** Django ecosystem covers all Must requirements without experimental technology.
2. **Operational:** User journeys are practical; moderation and privacy support daily community use.
3. **Economic:** Near-zero cost with significant community and learning benefits — strongest feasibility factor.
4. **Legal:** Privacy, content moderation, and open-source compliance are addressable within prototype scope.
5. **Schedule:** 6-week, 3-sprint plan with Release Sprint meets the assessment deadline.
6. **Cultural/Political:** Platform supports mutual aid — aligned with community cooperation values.
7. **Market:** Underserved niche between informal help and expensive commercial apps.
8. **Resource:** Two developers, open-source tools, and course support are sufficient.

### 8.2 Recommendation

**Proceed with development** according to [REQUIREMENTS.md](./REQUIREMENTS.md) and [PROJECT_PLAN.md](./PROJECT_PLAN.md).

- **Go:** All eight GeeksforGeeks feasibility types assessed as feasible
- **Do not stop:** No feasibility type indicates the project should be abandoned
- **Do not majorly revise:** Scope is appropriate; defer out-of-scope items (native apps, payments, OAuth) only

---

## 9. Executive Summary (General Information)

| Item | Conclusion |
|------|------------|
| Project | Local Community Skill Exchange and Help Board |
| Feasibility framework | [GeeksforGeeks — 8 types](https://www.geeksforgeeks.org/software-engineering/types-of-feasibility-study-in-software-project-development/) |
| Overall score | **4.47 / 5.00** |
| Decision | **Approved to proceed** |
| Next step | Sprint 1 — foundation (Weeks 1–2) |

---

## 10. Related Documents

| Document | Purpose |
|----------|---------|
| [PROJECT_REPORT.md](./PROJECT_REPORT.md) | Full project report including feasibility study (Section 7) |
| [REQUIREMENTS.md](./REQUIREMENTS.md) | Functional and non-functional requirements |
| [PROJECT_PLAN.md](./PROJECT_PLAN.md) | 3-sprint agile plan |
| [Proposal.rtf](./Proposal.rtf) | Original project proposal |

**Generate Word version:**

```bash
PYTHONPATH="../Week9/Activity1/.pylibs" python3 generate_feasibility_doc.py
```

Output: `Feasibility_Study.docx`
