# Feasibility Study

**Project:** Local Community Skill Exchange and Help Board  
**Group:** Group F — Syed Abdullah Maaz, Fahad Ahmed  
**Assessment:** MSE800 Assessment 2  
**Version:** 1.0 — June 2026

---

## 1. Introduction

This feasibility study evaluates whether the **Local Community Skill Exchange and Help Board** (NeighbourHelp) can be successfully designed, built, and deployed within the MSE800 Assessment 2 timeframe. Four dimensions are assessed:

1. **Technical feasibility** — Can we build it with chosen technology?
2. **Operational feasibility** — Will it work for users and administrators in practice?
3. **Financial feasibility** — Can it be delivered within acceptable cost?
4. **Scheduling feasibility** — Can it be completed in 6 weeks with a 2-person team?

The study concludes with an **overall viability assessment** and recommendation.

---

## 2. Technical Feasibility

### 2.1 Proposed technology

| Component | Technology | Maturity |
|-----------|------------|----------|
| Backend | Python 3.12, Django 5, DRF | Production-proven (15+ years) |
| Database | PostgreSQL | Industry standard |
| Real-time | Django Channels, Redis, ASGI | Official Django extension |
| Containerization | Docker, Docker Compose | Industry standard |
| Deployment | Render / Railway / Fly.io | Established PaaS providers |
| QR codes | Python `qrcode` library | Simple, well-maintained |
| Testing | pytest-django, factory_boy | Standard Django testing stack |

### 2.2 Technical assessment

| Criterion | Finding |
|-----------|---------|
| Skills availability | Team has MSE800 experience in Python, web development, databases, and agile methods |
| Integration complexity | Moderate — Django monolith with Redis for WebSockets; no external payment or OAuth APIs |
| Scalability (prototype) | Stateless ASGI backend can scale horizontally if needed (NFR-08) |
| Security | Django auth, CSRF, PBKDF2 hashing, role permissions — all documented patterns |
| Real-time chat | Django Channels + Redis is a proven architecture; 2-second delivery target achievable (NFR-06) |
| Data model | Relational schema (users, profiles, listings, messages, reviews) suits PostgreSQL |

### 2.3 Technical risks

| Risk | Impact | Mitigation |
|------|--------|------------|
| WebSocket on free-tier cloud | Medium | Select host with WSS; document limitations |
| Email on staging | Low | Mailtrap; pre-verified demo accounts |
| GeoDjango complexity | Low | Default to suburb/postcode; radius as stretch |

### 2.4 Conclusion

**Technical feasibility: FEASIBLE.** No unproven technology; stack matches team capability and assessment scope.

---

## 3. Operational Feasibility

### 3.1 Stakeholders and workflows

| Stakeholder | Primary use | Operational requirement |
|-------------|-------------|-------------------------|
| **Member** | Post/browse help, chat, rate | Simple UI, email verification, mobile-friendly |
| **Moderator** | Review reports, remove content | Moderation dashboard, role permissions |
| **Admin** | Manage categories, roles | Django admin |
| **Assessor** | Demo and UAT | Live URL, Docker, documentation |

### 3.2 Operational assessment

| Criterion | Finding |
|-----------|---------|
| User onboarding | Register → verify → profile → listing in ≤ 5 clicks per journey |
| Community safety | Report, block, moderation queue operational from Sprint 1 |
| Privacy | Suburb/postcode only — protects resident location (NFR-04) |
| Trust | Star ratings and reviews visible on profiles (FR-17, FR-18) |
| In-person connection | QR profile codes for community events (FR-23) |
| Assessor access | `docker compose up` + live URL — no manual dependency install |

### 3.3 Operational risks

| Risk | Mitigation |
|------|------------|
| Low initial user base (pilot) | Seed demo data; recruit classmates/local residents for UAT |
| Moderator availability | Admin role can act as moderator in prototype phase |
| Inappropriate content | Report flow + moderation dashboard from Sprint 1 |

### 3.4 Conclusion

**Operational feasibility: FEASIBLE.** Roles, workflows, and safety mechanisms support assessment demo and limited community pilot.

---

## 4. Financial Feasibility

### 4.1 Cost breakdown (assessment period)

| Item | Cost (NZD) |
|------|------------|
| Software licences | $0 (open source) |
| Development tools | $0 |
| Cloud hosting (free tier) | $0 |
| Email (Mailtrap / console) | $0 |
| Optional custom domain | $0–$25/year |
| **Total** | **$0–$25** |

### 4.2 Cost comparison

| Alternative | Typical cost | This project |
|-------------|--------------|--------------|
| Commercial gig apps (Airtasker, TaskRabbit) | 10–20% service fee per job | No payment — $0 fees |
| Custom agency development | $10,000+ | Student project — $0 labour cost |
| Paid cloud (production scale) | $50–200/month | Not required for assessment; free tier sufficient |

### 4.3 Financial benefits

- Residents coordinate help **without platform fees**
- **Zero infrastructure cost** for assessment prototype
- Clear upgrade path to paid hosting only if pilot expands

### 4.4 Conclusion

**Financial feasibility: HIGHLY FEASIBLE.** Minimal to zero cost for assessment delivery.

---

## 5. Scheduling Feasibility

### 5.1 Project schedule

| Sprint | Weeks | Hours | Focus |
|--------|-------|-------|-------|
| Sprint 1 | 1–2 | 59 | Foundation (auth, profiles, listings, moderation) |
| Sprint 2 | 3–4 | 69 | Core (search, chat, ratings, QR, safety) |
| Release | 5–6 | 66 | Deploy, UAT, regression, handover |
| **Total** | **6** | **~194** | |

**Per developer:** ~97 hours over 6 weeks ≈ **16 hours/week** — achievable alongside MSE800 coursework.

### 5.2 Requirements coverage

| Sprint | Functional requirements | Non-functional |
|--------|-------------------------|----------------|
| Sprint 1 | FR-01 – FR-11 | NFR-01 – NFR-04, NFR-07, NFR-11, NFR-12 (12 tests) |
| Sprint 2 | FR-12 – FR-23 | NFR-05, NFR-06, NFR-12 (+18 tests) |
| Release | FR-29 | NFR-09, NFR-10, NFR-12, NFR-13, **NFR-14** |

### 5.3 Milestones

| Week | Milestone |
|------|-----------|
| 2 | Sprint 1 review — auth, profiles, listings |
| 4 | Sprint 2 review — search, chat, ratings, QR |
| 5 | Staging deployment live |
| 6 | UAT sign-off + production demo URL |

### 5.4 Schedule risks

| Risk | Mitigation |
|------|------------|
| Sprint 2 overload | Defer FR-04 (password reset) or GeoDjango if needed |
| Deployment slip | Provision cloud in Week 5 Day 1 |
| UAT failures | Dedicated Release Sprint; Must items fixed before sign-off |

### 5.5 Conclusion

**Scheduling feasibility: FEASIBLE.** All Must requirements mapped to sprints with contingency in Release Sprint.

---

## 6. Overall Viability Assessment

### 6.1 Summary matrix

| Dimension | Rating | Confidence |
|-----------|--------|------------|
| Technical | ✅ Feasible | High |
| Operational | ✅ Feasible | High |
| Financial | ✅ Highly feasible | High |
| Scheduling | ✅ Feasible | Medium–High |

### 6.2 Viability justification

The **Local Community Skill Exchange and Help Board** is a **viable and justified** solution because:

1. It solves a **real community problem** — neighbours lack a free, trusted way to offer and find local help.
2. The **technology stack is proven** and aligned with course learning outcomes.
3. The **6-week agile plan** is realistic for a 2-developer team with ~194 estimated hours.
4. **Cost is negligible** ($0–$25) using open-source tools and free-tier cloud hosting.
5. **Lecturer approval** confirms scope appropriateness; enhancements (Docker, QR, live deploy) are scheduled without overloading sprints.
6. **Safety and privacy** are designed in from Sprint 1 — essential for a community platform.

### 6.3 Recommendation

| Decision | **PROCEED with implementation** |
|----------|-----------------------------------|
| Rationale | All four feasibility dimensions are positive; no blocking issues identified |
| Conditions | Meet Release Sprint go/no-go criteria: live URL, UAT pass, ≥ 30 tests, Docker works |
| Review point | End of Sprint 2 — confirm chat and QR on track before Release Sprint |

### 6.4 Go / No-Go criteria (Release Sprint)

| # | Criterion | Required |
|---|-----------|----------|
| 1 | Live public URL accessible | Yes |
| 2 | `docker compose up` works from README | Yes |
| 3 | All Must functional requirements demonstrated | Yes |
| 4 | ≥ 30 automated tests pass | Yes |
| 5 | UAT checklist ≥ 95% Must items pass | Yes |
| 6 | QR code flow works on mobile scan | Yes |

---

## 7. References

- `PROJECT_PROPOSAL.md` — full project proposal (Section 9)
- `PROJECT_PLAN.md` — sprint schedule and effort estimates
- `REQUIREMENTS.md` — functional and non-functional requirements
- Lecturer approval feedback — June 2026
