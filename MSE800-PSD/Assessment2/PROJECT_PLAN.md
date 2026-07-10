# Agile Project Plan

**Project:** Local Community Skill Exchange and Help Board  
**Assessment:** MSE800 Assessment 2  
**Group:** Group F — Syed Abdullah Maaz, Fahad Ahmed  
**Duration:** 4 weeks (2 sprints × 2 weeks)  
**Related documents:** [Proposal.rtf](./Proposal.rtf), [REQUIREMENTS.md](./REQUIREMENTS.md), [FUNCTIONAL_AND_NON_FUNCTIONAL_REQUIREMENTS.md](./FUNCTIONAL_AND_NON_FUNCTIONAL_REQUIREMENTS.md)

---

## 1. Project Overview

In everyday life, residents often need small help (tutoring, bike repair, pet sitting, moving boxes) but do not know who nearby can assist. This project delivers a community platform where neighbors post requests and offers, match by location and skill, chat to arrange details, and rate each other after completion.

**Objectives:** connect neighbors safely, reduce the cost of small services, and build trust through profiles and reviews.

**Expected outcome:** A working prototype where users register, post and browse help listings, search nearby, chat in real time, leave ratings, and admins moderate content — suitable for a professional software engineering assessment.

---

## 2. Technology Stack

| Layer | Technology | Purpose |
|-------|------------|---------|
| Backend | Python, Django, Django REST Framework | Users, listings, messaging, ratings APIs |
| Database | PostgreSQL | Persistent storage for users, posts, messages, reviews |
| Location | GeoDjango or postcode/suburb search | "Near me" listing filter |
| Real-time | Django Channels + Redis | Live chat between matched users |
| Media | Django file storage (local / S3) | Profile photos |
| Safety | Django permissions, report/block, admin panel | Community moderation |
| Frontend | Responsive web UI (Django templates + HTMX or React) | Member-facing pages |
| Email | Django email backend | Signup verification and match notifications |
| Testing | pytest-django, factory_boy | Automated unit and integration tests |

---

## 3. Sprint Summary

| Sprint | Duration | Objective | Key Requirements | Outcome |
|--------|----------|-----------|------------------|---------|
| Sprint 1 | Week 1–2 | Project setup, user accounts, profiles, listings, admin | FR-01 – FR-11, FR-23 – FR-24; NFR-01 – NFR-04, NFR-07, NFR-11, NFR-12 (partial), NFR-17 | Users register, create profiles, post/browse listings; 12 unit tests pass |
| Sprint 2 | Week 3–4 | Search, chat, ratings, safety, deployment | FR-12 – FR-28; NFR-05 – NFR-06, NFR-09 – NFR-18; EXT-01 – EXT-05 | Full prototype with chat, ratings, moderation; 18 integration tests pass; deployed |

---

## 4. Sprint 1 — User Accounts & Listings

**Goal:** Establish the foundation — authentication, profiles, listings, and moderation.

### 4.1 Backlog

| Task | Deliverable | Requirements |
|------|-------------|--------------|
| Set up Django + PostgreSQL project structure | Working dev environment, `docker-compose.yml` | NFR-07, NFR-11 |
| Implement user registration and email verification | Members can sign up and verify email | FR-01, FR-02, NFR-01, NFR-15 |
| Implement login, logout, password reset | Secure session management | FR-03, FR-04, NFR-01, NFR-02 |
| Build profile page (skills, suburb, photo) | Editable user profiles | FR-05, NFR-04 |
| Define roles: Member, Moderator, Admin | Permission classes and admin groups | FR-06, NFR-03 |
| Create listing model, categories, CRUD views | Post "I need help" / "I can help" listings | FR-07, FR-09, FR-10 |
| Build listing browse/home page | Public feed of active listings | FR-08 |
| Configure Django admin and moderation dashboard | Admins manage users and posts | FR-11 |
| Input validation and listing detail pages | Clear errors; full listing view | FR-23, FR-24 |
| Responsive base templates and static assets | Mobile-friendly UI shell | FR-22, NFR-09 |
| Environment-based configuration (Docker) | Portable dev/staging setup | NFR-17 |
| Write unit tests (pytest-django) | 12 tests passing | NFR-12 |

### 4.2 Planned Repository Layout (Sprint 1)

```
Assessment2/
├── backend/
│   ├── config/           # settings, urls, asgi, wsgi
│   ├── accounts/         # FR-01 – FR-04, FR-06
│   ├── profiles/         # FR-05
│   ├── listings/         # FR-07 – FR-10
│   ├── moderation/       # FR-11 (admin views)
│   ├── notifications/    # FR-02 email
│   ├── templates/
│   ├── static/
│   └── tests/            # Sprint 1 unit tests
├── docker-compose.yml
├── REQUIREMENTS.md
└── PROJECT_PLAN.md
```

### 4.3 Sprint 1 Review Demo

- Register a new user and verify email
- Log in and complete profile (skills, suburb, photo)
- Create a help listing and browse the home feed
- Admin removes an inappropriate listing via moderation panel

---

## 5. Sprint 2 — Matching, Chat & Ratings

**Goal:** Complete the community loop — discover nearby help, communicate, rate, and deploy safely.

### 5.1 Backlog

| Task | Deliverable | Requirements |
|------|-------------|--------------|
| Nearby search by suburb/postcode/radius | Location-based listing filter | FR-12, FR-13, NFR-05 |
| Keyword search and personal dashboard | Text search; member overview page | FR-25, FR-27 |
| Express interest and open conversation | Match request workflow | FR-14 |
| Real-time chat (Django Channels + Redis) | Live messaging between matched users | FR-15, FR-16, NFR-06 |
| In-app notification centre | Unread alerts for matches and messages | FR-26 |
| Rating and review system | Star ratings on profiles | FR-17, FR-18 |
| Report, block, and moderator workflow | Safety controls and report resolution | FR-19, FR-20, FR-28, NFR-03 |
| Email match and message notifications | Users notified of activity | FR-21, NFR-15 |
| Rate limiting on auth and API endpoints | Brute-force and abuse protection | NFR-18, EXT-05 |
| Logging, health check, backup scripts | Observability and disaster recovery | EXT-01 – EXT-04, NFR-13, NFR-16 |
| Integration tests and bug fixes | 18 tests passing (30 total) | NFR-12 |
| Accessibility and UX polish | WCAG Level A checklist | NFR-09, NFR-10 |
| Deploy prototype to staging | Live demo URL | NFR-14, NFR-13 |
| Logging and error handling | Audit trail for moderation events | NFR-13 |

### 5.2 Planned Repository Additions (Sprint 2)

```
Assessment2/backend/
├── chat/                 # FR-14 – FR-16
├── reviews/              # FR-17 – FR-18
├── moderation/           # FR-19 – FR-20 (reports, blocks)
├── listings/services/    # location.py — FR-12
└── tests/                # integration tests (chat, ratings, search)
Assessment2/docs/
├── DEPLOYMENT.md
├── ARCHITECTURE.md
└── ACCESSIBILITY.md
```

### 5.3 Sprint 2 Review Demo

- Search listings near a suburb/postcode
- Express interest, open chat, send real-time messages
- Leave a star rating after completed help
- Report and block a user; moderator resolves report
- Show deployed prototype and passing test suite

---

## 6. Activity Log & Progress Updates

| Week | Sprint | Activity | Status |
|------|--------|----------|--------|
| Week 1 | Sprint 1 | Sprint planning, project setup, user auth (FR-01 – FR-04) | Planned |
| Week 2 | Sprint 1 | Profiles, listings, admin panel, unit tests (FR-05 – FR-11) | Planned |
| Week 2 | Sprint 1 | Sprint 1 review & retrospective | Planned |
| Week 3 | Sprint 2 | Sprint planning, nearby search, chat setup (FR-12 – FR-16) | Planned |
| Week 4 | Sprint 2 | Ratings, report/block, testing, deployment (FR-17 – FR-21) | Planned |
| Week 4 | Sprint 2 | Sprint 2 review & retrospective | Planned |

---

## 7. Sprint Reviews & Retrospectives

| Sprint | Review (Demo) | Retrospective |
|--------|---------------|---------------|
| Sprint 1 | Register user, create profile, post listing, browse home page, admin moderation | *To be completed at end of Sprint 1* |
| Sprint 2 | Search nearby, chat live, leave rating, report user, deploy prototype | *To be completed at end of Sprint 2* |

---

## 8. Risk Register

| Risk | Impact | Mitigation | Sprint |
|------|--------|------------|--------|
| GeoDjango setup complexity | Delays nearby search | Fallback to suburb/postcode text filter (FR-12) | Sprint 2 |
| WebSocket deployment issues | Chat unavailable in demo | Test Channels + Redis early in Week 3; provide HTTP polling fallback | Sprint 2 |
| Email not delivered in dev | Verification blocked | Use console email backend locally; document SMTP for staging | Sprint 1 |
| Scope creep | Miss sprint goals | Strict Must/Should prioritisation in REQUIREMENTS.md | Both |

---

## 9. Definition of Done

A backlog item is **Done** when:

1. Code is merged to the main branch with passing tests for the affected requirements.
2. Relevant functional and non-functional requirements are traceable in [REQUIREMENTS.md](./REQUIREMENTS.md).
3. UI changes are responsive and manually verified on desktop and mobile widths.
4. New models have migrations; new endpoints/views have pytest coverage.
5. Feature is demonstrable in the sprint review.

---

## 10. Final Deliverables

| Deliverable | Location |
|-------------|----------|
| Project proposal | `Proposal.rtf` |
| Requirements specification | `REQUIREMENTS.md` |
| Agile project plan | `PROJECT_PLAN.md` |
| Generated Word documentation | `Local_Community_Skill_Exchange_Project_Documentation.docx` |
| Working Django prototype | `backend/` |
| Test suite (≥ 30 tests) | `backend/tests/` |
| Deployment guide | `docs/DEPLOYMENT.md` |
