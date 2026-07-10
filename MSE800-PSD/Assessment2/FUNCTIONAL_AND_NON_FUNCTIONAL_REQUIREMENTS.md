# Functional and Non-Functional Requirements

**Project:** Local Community Skill Exchange and Help Board  
**Assessment:** MSE800 Assessment 2  
**Group:** Group F — Syed Abdullah Maaz, Fahad Ahmed  
**Reference:** [Functional and Non Functional Requirements — GeeksforGeeks](https://www.geeksforgeeks.org/software-engineering/functional-vs-non-functional-requirements/)

**Related documents:** [Proposal.rtf](./Proposal.rtf) · [REQUIREMENTS.md](./REQUIREMENTS.md) · [PROJECT_PLAN.md](./PROJECT_PLAN.md)

---

## 1. Requirements Analysis Overview

Requirements analysis identifies what users and stakeholders need before development begins. For this community platform, requirements are classified as follows (per GeeksforGeeks):

| Type | Definition | Question answered |
|------|------------|-------------------|
| **Functional** | What the system **must do** — features and operations | *What features should the system include?* |
| **Non-functional** | How the system **must perform** — quality attributes | *How fast, secure, and reliable should it be?* |
| **Extended** | Additional capabilities beyond core features | *How will the system be monitored, backed up, and protected from overload?* |

> **Example (GeeksforGeeks):** In an online shopping system, functional requirements include login and order placement; non-functional requirements include performance, security, and scalability.  
> **This project:** Functional requirements include user login and help listing posts; non-functional requirements include chat response time, encrypted sessions, and Docker-based portability.

---

## 2. Functional vs Non-Functional — Key Differences

| Functional Requirements | Non-Functional Requirements |
|-------------------------|----------------------------|
| Define **what** the system should do | Define **how** the system should perform |
| Focus on behaviour and operations | Focus on performance, security, usability, reliability |
| Directly visible to users | Indirectly visible; shape user experience |
| Easier to validate (pass/fail on output) | Validated with metrics, SLAs, and benchmarks |
| Documented as use cases / user stories | Documented as technical specs and quality criteria |
| **Examples:** login, post listing, chat, rate user | **Examples:** response time, scalability, maintainability |

---

## 3. Functional Requirements

Functional requirements define specific features the platform must perform. Each item describes **observable behaviour**, the **priority**, the **sprint** when it is implemented, and the **planned code location** under `Assessment2/backend/`.

### 3.1 Authentication and User Management

| ID | Requirement | Description | Priority | Sprint | Implementation Location |
|----|-------------|-------------|----------|--------|-------------------------|
| FR-01 | User registration | New residents create an account with email, password, and display name. Duplicate emails are rejected. | Must | Sprint 1 | `accounts/views.py`, `accounts/models.py`, `templates/accounts/register.html` |
| FR-02 | Email verification | Verification link sent on signup; unverified users cannot post or chat. | Must | Sprint 1 | `accounts/views.py`, `notifications/email.py`, `templates/emails/verify_email.html` |
| FR-03 | Login and logout | Members authenticate with email/password; protected routes require a valid session. | Must | Sprint 1 | `accounts/views.py`, `accounts/urls.py`, `templates/accounts/login.html` |
| FR-04 | Password reset | Users reset password via a time-limited email link. | Should | Sprint 1 | `accounts/views.py`, `templates/emails/password_reset.html` |
| FR-05 | User profile | Members edit skills, bio, suburb/postcode, and optional profile photo. | Must | Sprint 1 | `profiles/models.py`, `profiles/views.py`, `templates/profiles/edit.html` |
| FR-06 | Role-based access | Three roles — Member, Moderator, Admin — with permission checks on sensitive actions. | Must | Sprint 1 | `accounts/models.py`, `accounts/permissions.py` |
| FR-23 | Input validation | Invalid or edge-case input (bad email, weak password, oversized text) returns clear field-level errors. | Must | Sprint 1 | `*/forms.py`, `*/serializers.py`, validation messages in templates |

### 3.2 Listings and Discovery

| ID | Requirement | Description | Priority | Sprint | Implementation Location |
|----|-------------|-------------|----------|--------|-------------------------|
| FR-07 | Create help listing | Post **"I need help"** or **"I can help"** with title, description, category, and suburb. | Must | Sprint 1 | `listings/models.py`, `listings/views.py`, `templates/listings/create.html` |
| FR-08 | Browse listings | Public feed shows active listings with type, category, suburb, author, and date. | Must | Sprint 1 | `listings/views.py`, `templates/listings/list.html` |
| FR-09 | Listing categories | Predefined categories (tutoring, pet sitting, moving, repairs, etc.). | Must | Sprint 1 | `listings/models.py` (Category), `listings/fixtures/categories.json` |
| FR-10 | Edit and close listing | Owners edit or mark listings closed; closed posts leave the public feed. | Must | Sprint 1 | `listings/views.py`, `templates/listings/edit.html` |
| FR-24 | Listing detail view | Single listing page with full description, author summary, and action buttons. | Must | Sprint 1 | `listings/views.py` (ListingDetailView), `templates/listings/detail.html` |
| FR-12 | Nearby search | Filter by suburb, postcode, or radius ("near me"). | Must | Sprint 2 | `listings/filters.py`, `listings/services/location.py`, `templates/listings/search.html` |
| FR-13 | Skill-based matching | Filter by skill keywords or category to find complementary posts. | Should | Sprint 2 | `listings/filters.py`, `templates/listings/search.html` |
| FR-25 | Keyword search | Search listing title and description by text (e.g. "bike repair"). | Must | Sprint 2 | `listings/filters.py`, search bar in `templates/base.html` |

### 3.3 Matching, Communication, and Trust

| ID | Requirement | Description | Priority | Sprint | Implementation Location |
|----|-------------|-------------|----------|--------|-------------------------|
| FR-14 | Express interest / match | Member expresses interest; poster is notified; private chat thread opens. | Must | Sprint 2 | `listings/views.py`, `chat/models.py` (Conversation), `listings/models.py` (MatchRequest) |
| FR-15 | Real-time chat | Matched users send live messages in a conversation window. | Must | Sprint 2 | `chat/consumers.py`, `chat/routing.py`, `config/asgi.py`, `templates/chat/room.html` |
| FR-16 | Chat history | Past messages persist and are scrollable per conversation. | Must | Sprint 2 | `chat/models.py`, `chat/views.py`, `templates/chat/inbox.html` |
| FR-17 | Star ratings | After an exchange, users leave a 1–5 star rating and optional review. | Must | Sprint 2 | `reviews/models.py`, `reviews/views.py`, `templates/reviews/create.html` |
| FR-18 | Aggregate rating display | Profiles show average rating and recent reviews. | Must | Sprint 2 | `profiles/views.py`, `reviews/models.py`, `templates/profiles/detail.html` |
| FR-21 | Email notifications | Email sent on new match or message (configurable). | Should | Sprint 2 | `notifications/tasks.py`, `notifications/email.py` |
| FR-26 | In-app notification centre | Header badge and inbox for unread match/message/rating alerts. | Should | Sprint 2 | `notifications/models.py`, `templates/notifications/inbox.html` |
| FR-27 | Personal dashboard | Member overview of own listings, matches, chats, and pending reviews. | Should | Sprint 2 | `accounts/views.py` (DashboardView), `templates/accounts/dashboard.html` |

### 3.4 Safety, Moderation, and Presentation

| ID | Requirement | Description | Priority | Sprint | Implementation Location |
|----|-------------|-------------|----------|--------|-------------------------|
| FR-11 | Admin moderation panel | Admins/moderators manage users, listings, and reports via admin UI. | Must | Sprint 1 | `moderation/admin.py`, `templates/moderation/dashboard.html` |
| FR-19 | Report user or listing | Members submit reports; items appear in moderation queue. | Must | Sprint 2 | `moderation/models.py` (Report), `moderation/views.py` |
| FR-20 | Block user | Blocked users cannot message or appear in the blocker's feed. | Must | Sprint 2 | `moderation/models.py` (Block), `chat/services.py`, `listings/querysets.py` |
| FR-28 | Moderator report workflow | Moderators set report status (open → resolved/dismissed) with outcome notes. | Must | Sprint 2 | `moderation/views.py`, `templates/moderation/report_detail.html` |
| FR-22 | Responsive web UI | Core flows work on desktop and mobile browsers. | Must | Sprint 1–2 | `templates/base.html`, `static/css/` |

---

## 4. Non-Functional Requirements

Non-functional requirements define **quality attributes**. They are grouped by the categories listed on [GeeksforGeeks](https://www.geeksforgeeks.org/software-engineering/functional-vs-non-functional-requirements/): performance, security, usability, reliability, scalability, maintainability, and portability.

### 4.1 Performance

| ID | Requirement | Description | Priority | Sprint | Implementation Location |
|----|-------------|-------------|----------|--------|-------------------------|
| NFR-05 | Page response time | Listing and search pages load within **3 seconds** on standard broadband. | Should | Sprint 2 | DB indexes in `listings/models.py`, pagination, queryset optimisation |
| NFR-06 | Real-time chat latency | Chat messages delivered within **2 seconds** to connected clients. | Must | Sprint 2 | `chat/consumers.py`, Redis `CHANNEL_LAYERS` in `config/settings.py` |

### 4.2 Security

| ID | Requirement | Description | Priority | Sprint | Implementation Location |
|----|-------------|-------------|----------|--------|-------------------------|
| NFR-01 | Authentication | Protected routes require auth; passwords hashed (PBKDF2). | Must | Sprint 1 | `config/settings.py`, `accounts/authentication.py` |
| NFR-02 | CSRF and XSS protection | CSRF tokens on forms; template auto-escaping for user content. | Must | Sprint 1 | Django middleware, DRF settings |
| NFR-03 | Authorisation | Role and object-level checks on edit, moderation, and admin actions. | Must | Sprint 1 | `accounts/permissions.py`, `listings/permissions.py`, `moderation/permissions.py` |
| NFR-04 | Data privacy | Only suburb/postcode shown; no exact street addresses stored. | Must | Sprint 1 | `profiles/models.py`, `profiles/forms.py` |
| NFR-18 | Rate limiting | Throttle login, registration, report, and chat endpoints against abuse. | Should | Sprint 2 | DRF throttling / `django-ratelimit` in `config/settings.py`, `accounts/throttling.py` |

### 4.3 Usability

| ID | Requirement | Description | Priority | Sprint | Implementation Location |
|----|-------------|-------------|----------|--------|-------------------------|
| NFR-09 | Ease of use | Core journeys (register → post → search → chat → rate) require ≤ **5 clicks** with clear labels. | Must | Sprint 1–2 | Templates, wireframes in `docs/wireframes/`, sprint UX reviews |
| NFR-10 | Accessibility | WCAG 2.1 Level A: semantic HTML, keyboard forms, alt text, colour contrast. | Should | Sprint 2 | `templates/base.html`, `docs/ACCESSIBILITY.md` |

### 4.4 Reliability

| ID | Requirement | Description | Priority | Sprint | Implementation Location |
|----|-------------|-------------|----------|--------|-------------------------|
| NFR-07 | Data persistence | Accounts, listings, messages, and reviews stored in PostgreSQL with ACID transactions. | Must | Sprint 1 | `config/settings.py` (DATABASES), Django migrations |
| NFR-16 | Availability | Prototype targets **≥ 99% uptime** during assessment demos; friendly error pages on failure. | Should | Sprint 2 | `templates/500.html`, `templates/503.html`, health-check in `config/urls.py` |

### 4.5 Scalability

| ID | Requirement | Description | Priority | Sprint | Implementation Location |
|----|-------------|-------------|----------|--------|-------------------------|
| NFR-08 | Horizontal scaling | Stateless REST + ASGI WebSockets allow additional app servers behind a load balancer. | Could | Sprint 2 | `config/asgi.py`, `docs/DEPLOYMENT.md` |

### 4.6 Maintainability

| ID | Requirement | Description | Priority | Sprint | Implementation Location |
|----|-------------|-------------|----------|--------|-------------------------|
| NFR-11 | Modular architecture | Separate Django apps per domain (accounts, listings, chat, reviews, moderation). | Must | Sprint 1 | `backend/` layout, `docs/ARCHITECTURE.md` |
| NFR-12 | Automated testing | ≥ **30 tests** with pytest-django and factory_boy (12 Sprint 1, 18 Sprint 2). | Must | Sprint 1–2 | `tests/`, `conftest.py`, `pytest.ini` |
| NFR-13 | Logging | Errors and key events logged for debugging and audit. | Should | Sprint 2 | `config/settings.py` (LOGGING), views and consumers |
| NFR-14 | Deployability | Staging deploy via Docker Compose and environment variables. | Must | Sprint 2 | `docker-compose.yml`, `.env.example`, `docs/DEPLOYMENT.md` |
| NFR-15 | Email deliverability | Configurable SMTP (staging) or console backend (development). | Should | Sprint 1–2 | `config/settings.py`, `notifications/email.py` |

### 4.7 Portability

| ID | Requirement | Description | Priority | Sprint | Implementation Location |
|----|-------------|-------------|----------|--------|-------------------------|
| NFR-17 | Cross-environment execution | Same codebase runs locally, in Docker, and on staging using env vars only. | Must | Sprint 1–2 | `docker-compose.yml`, `.env.example`, `config/settings.py` |

---

## 5. Extended Requirements

Extended requirements (GeeksforGeeks) improve monitoring, reliability, and future expansion beyond core features.

| ID | Requirement | Description | Priority | Sprint | Implementation Location |
|----|-------------|-------------|----------|--------|-------------------------|
| EXT-01 | Logging | Record failed logins, reports, and chat errors with timestamps for audit. | Must | Sprint 2 | `config/settings.py` (LOGGING) — complements NFR-13 |
| EXT-02 | Monitoring and alerting | Health-check endpoint verifies DB and Redis; deployment docs cover monitoring. | Should | Sprint 2 | `config/views.py` (HealthCheckView), `docker-compose.yml` healthcheck |
| EXT-03 | Usage analytics | Admin view of anonymised counts: registrations, listings, matches, ratings. | Could | Sprint 2 | `analytics/models.py`, `analytics/views.py` |
| EXT-04 | Backup and disaster recovery | PostgreSQL backup script and documented restore procedure. | Should | Sprint 2 | `scripts/backup_db.sh`, `docs/DEPLOYMENT.md` |
| EXT-05 | API rate limiting | Request quotas on public and authenticated APIs during peak load. | Should | Sprint 2 | DRF `AnonRateThrottle` / `UserRateThrottle` — complements NFR-18 |

**Future extended work (out of scope):** feature flags / A-B testing.

---

## 6. Project Example — Help Board Scenario

Following the GeeksforGeeks banking and food-delivery examples, applied to this platform:

**Functional requirements**

- Users log in with email and password (FR-03).
- Users post and browse help listings (FR-07, FR-08).
- Users search nearby and by keyword (FR-12, FR-25).
- Users chat after matching and leave ratings (FR-14 – FR-18).
- Users receive notifications after a match or message (FR-21, FR-26).

**Non-functional requirements**

- Listing pages respond in under 3 seconds (NFR-05).
- Sessions and passwords are protected; only suburb is shown publicly (NFR-01 – NFR-04).
- The prototype stays available during assessment demos (NFR-16).
- The app runs in Docker locally and on staging (NFR-17).

**Extended requirements**

- Failed logins and reports are logged (EXT-01).
- Database backups are documented (EXT-04).
- Auth endpoints are rate-limited (EXT-05).

---

## 7. Sprint Traceability Matrix

| Sprint | Functional | Non-Functional | Extended |
|--------|------------|----------------|----------|
| **Sprint 1** (Weeks 1–2) | FR-01 – FR-11, FR-22 (base), FR-23 – FR-24 | NFR-01 – NFR-04, NFR-07, NFR-09 (partial), NFR-11, NFR-12 (12 tests), NFR-15, NFR-17 | — |
| **Sprint 2** (Weeks 3–4) | FR-12 – FR-28, FR-22 (complete) | NFR-05 – NFR-06, NFR-08 – NFR-10, NFR-12 (+18 tests), NFR-13 – NFR-18 | EXT-01 – EXT-05 |

---

## 8. Acceptance Criteria

The prototype meets requirements analysis goals when:

1. All **Must** functional requirements (FR-01 – FR-11, FR-14 – FR-20, FR-22, FR-24 – FR-25, FR-28) are demonstrable.
2. All **Must** non-functional requirements (NFR-01 – NFR-04, NFR-06 – NFR-07, NFR-09, NFR-11 – NFR-12, NFR-14, NFR-17) are satisfied.
3. Extended requirement **EXT-01** (logging) is configured for the Sprint 2 demo.
4. ≥ 30 automated tests pass (NFR-12).
5. Backup and health-check steps are documented (EXT-02, EXT-04).

---

## 9. Document Export

Generate a Word version of this document:

```bash
cd Assessment2
PYTHONPATH="../Week9/Activity1/.pylibs" python3 generate_requirements_doc.py
```

Output: `Functional_and_NonFunctional_Requirements.docx`
