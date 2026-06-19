# Requirements Specification

**Project:** Local Community Skill Exchange and Help Board  
**Assessment:** MSE800 Assessment 2  
**Group:** Group F — Syed Abdullah Maaz, Fahad Ahmed  
**Methodology:** Agile (Scrum) — 2 sprints × 2 weeks

---

## 1. Purpose

This document defines the functional and non-functional requirements for the Local Community Skill Exchange and Help Board platform. Each requirement includes a brief description, priority, target sprint, and the planned implementation location within the Django project.

Implementation paths use the planned repository layout under `Assessment2/backend/` unless noted otherwise.

---

## 2. Functional Requirements

| ID | Requirement | Description | Priority | Sprint | Implementation Location |
|----|-------------|-------------|----------|--------|-------------------------|
| FR-01 | User registration | New residents can create a member account with email, password, and display name. Duplicate emails are rejected with a clear validation message. | Must | Sprint 1 | `backend/accounts/views.py` (RegisterView), `backend/accounts/serializers.py`, `backend/accounts/models.py` (CustomUser), `backend/templates/accounts/register.html` |
| FR-02 | Email verification | After registration, the system sends a verification link. Unverified accounts cannot post listings or send messages. | Must | Sprint 1 | `backend/accounts/views.py` (VerifyEmailView), `backend/notifications/email.py`, `backend/config/settings.py` (EMAIL_*), `backend/templates/emails/verify_email.html` |
| FR-03 | User login and logout | Registered members can log in with email/password and log out securely. Session or token auth is enforced on protected routes. | Must | Sprint 1 | `backend/accounts/views.py` (LoginView, LogoutView), `backend/accounts/urls.py`, `backend/templates/accounts/login.html` |
| FR-04 | Password reset | Users can request a password-reset email and set a new password via a time-limited token link. | Should | Sprint 1 | `backend/accounts/views.py` (PasswordResetView), `backend/templates/emails/password_reset.html` |
| FR-05 | User profile | Members maintain a profile with skills, short bio, suburb/postcode, and optional profile photo. Profile data is editable by the owner only. | Must | Sprint 1 | `backend/profiles/models.py` (Profile), `backend/profiles/views.py`, `backend/profiles/forms.py`, `backend/templates/profiles/edit.html`, `backend/media/profiles/` |
| FR-06 | Role-based access | The platform supports three roles: **Member**, **Moderator**, and **Admin**. Permissions restrict moderation and admin actions to authorised roles. | Must | Sprint 1 | `backend/accounts/models.py` (role field), `backend/accounts/permissions.py`, `backend/config/settings.py` (AUTH_USER_MODEL, groups) |
| FR-07 | Create help listing | Authenticated members can post listings labelled **"I need help"** or **"I can help"** with title, description, category, and suburb. | Must | Sprint 1 | `backend/listings/models.py` (Listing), `backend/listings/views.py` (CreateListingView), `backend/listings/forms.py`, `backend/templates/listings/create.html` |
| FR-08 | Browse listings | All visitors can browse active listings on a home/feed page with title, type, category, suburb, author, and date posted. | Must | Sprint 1 | `backend/listings/views.py` (ListingListView), `backend/templates/listings/list.html`, `backend/listings/urls.py` |
| FR-09 | Listing categories | Listings are organised by predefined categories (e.g. tutoring, pet sitting, moving, repairs) to simplify discovery. | Must | Sprint 1 | `backend/listings/models.py` (Category), `backend/listings/fixtures/categories.json`, Django admin category management |
| FR-10 | Edit and close listing | Listing owners can edit or mark their own listings as closed/completed. Closed listings no longer appear in the public feed. | Must | Sprint 1 | `backend/listings/views.py` (UpdateListingView, CloseListingView), `backend/templates/listings/edit.html` |
| FR-11 | Admin moderation panel | Admins and moderators can view reported content, suspend users, and remove inappropriate listings via Django admin and a moderation dashboard. | Must | Sprint 1 | `backend/moderation/admin.py`, `backend/listings/admin.py`, `backend/accounts/admin.py`, `backend/templates/moderation/dashboard.html` |
| FR-12 | Nearby search | Users can filter listings by suburb, postcode, or radius ("near me") so they only see relevant local offers and requests. | Must | Sprint 2 | `backend/listings/filters.py`, `backend/listings/views.py` (NearbySearchView), `backend/profiles/models.py` (location fields), GeoDjango or postcode lookup in `backend/listings/services/location.py`, `backend/templates/listings/search.html` |
| FR-13 | Skill-based matching | Users can filter listings by skill keywords or category to match complementary "need help" and "can help" posts. | Should | Sprint 2 | `backend/listings/filters.py` (skill/category query params), `backend/listings/views.py`, search UI in `backend/templates/listings/search.html` |
| FR-14 | Express interest / match | A member can express interest in a listing; the poster is notified and a private chat thread is opened between the two users. | Must | Sprint 2 | `backend/listings/views.py` (ExpressInterestView), `backend/chat/models.py` (Conversation), `backend/listings/models.py` (MatchRequest), `backend/templates/listings/detail.html` |
| FR-15 | Real-time chat | Matched users exchange messages in real time through a per-conversation chat window with message history. | Must | Sprint 2 | `backend/chat/consumers.py` (WebSocket), `backend/chat/models.py` (Message), `backend/chat/routing.py`, Redis channel layer in `backend/config/asgi.py`, `backend/templates/chat/room.html` |
| FR-16 | Chat history | Users can scroll through past messages in each conversation. Messages are persisted in PostgreSQL. | Must | Sprint 2 | `backend/chat/models.py`, `backend/chat/views.py` (ConversationListView), `backend/chat/serializers.py`, `backend/templates/chat/inbox.html` |
| FR-17 | Star ratings | After a completed exchange, either party can leave a 1–5 star rating and optional short review for the other user. | Must | Sprint 2 | `backend/reviews/models.py` (Review), `backend/reviews/views.py`, `backend/reviews/forms.py`, `backend/templates/reviews/create.html` |
| FR-18 | Display aggregate rating | User profiles show average star rating and recent reviews to build community trust. | Must | Sprint 2 | `backend/profiles/views.py` (ProfileDetailView), `backend/reviews/models.py` (aggregate property), `backend/templates/profiles/detail.html` |
| FR-19 | Report user or listing | Members can report abusive behaviour or inappropriate listings. Reports appear in the moderation queue. | Must | Sprint 2 | `backend/moderation/models.py` (Report), `backend/moderation/views.py` (CreateReportView), `backend/templates/moderation/report_form.html` |
| FR-20 | Block user | Members can block another user to prevent further messages and hide that user's listings from their view. | Must | Sprint 2 | `backend/moderation/models.py` (Block), `backend/moderation/views.py`, chat/listing query filters in `backend/chat/services.py` and `backend/listings/querysets.py` |
| FR-21 | Match notifications | When another user expresses interest or sends a chat message, the recipient receives an email notification (configurable). | Should | Sprint 2 | `backend/notifications/tasks.py`, `backend/notifications/email.py`, `backend/templates/emails/new_match.html`, `backend/templates/emails/new_message.html` |
| FR-22 | Responsive web UI | All core flows (register, browse, search, chat, rate) work on desktop and mobile browsers through a responsive layout. | Must | Sprint 1–2 | `backend/templates/base.html`, CSS in `backend/static/css/`, optional React/HTMX components in `backend/frontend/` |

---

## 3. Non-Functional Requirements

| ID | Requirement | Description | Priority | Sprint | Implementation / Addressed In |
|----|-------------|-------------|----------|--------|-------------------------------|
| NFR-01 | Security — authentication | All protected API endpoints and views require authenticated sessions or JWT tokens. Passwords are hashed with Django's default hasher (PBKDF2). | Must | Sprint 1 | `backend/config/settings.py` (AUTH, PASSWORD_HASHERS), `backend/accounts/authentication.py`, DRF permission classes in `backend/*/permissions.py` |
| NFR-02 | Security — CSRF and XSS | Forms and API mutations use CSRF protection; user-generated content is escaped in templates to reduce XSS risk. | Must | Sprint 1 | Django middleware in `backend/config/settings.py`, template auto-escaping, DRF renderer settings |
| NFR-03 | Security — authorisation | Role checks enforce that only listing owners edit their posts and only moderators/admins access moderation actions. | Must | Sprint 1 | `backend/accounts/permissions.py`, object-level permissions in `backend/listings/permissions.py`, `backend/moderation/permissions.py` |
| NFR-04 | Data privacy | Exact street addresses are not stored or displayed; only suburb/postcode and optional approximate location are shown to protect resident privacy. | Must | Sprint 1 | `backend/profiles/models.py` (suburb/postcode fields only), validation in `backend/profiles/forms.py`, listing display templates |
| NFR-05 | Performance — page response | Public listing pages and search results load within 3 seconds on a standard broadband connection under normal demo load. | Should | Sprint 2 | Database indexes on `backend/listings/models.py`, `select_related`/`prefetch_related` in querysets, pagination in list views |
| NFR-06 | Performance — real-time chat | Chat messages are delivered to connected clients within 2 seconds via Django Channels and Redis. | Must | Sprint 2 | `backend/chat/consumers.py`, Redis channel layer in `backend/config/settings.py` (CHANNEL_LAYERS), load testing in `backend/tests/test_chat.py` |
| NFR-07 | Reliability — data persistence | User accounts, listings, messages, and reviews are stored in PostgreSQL with transactional integrity. | Must | Sprint 1 | `backend/config/settings.py` (DATABASES), Django ORM migrations in each app |
| NFR-08 | Scalability | Backend is stateless (REST + WebSockets via ASGI) so additional app servers can be added behind a load balancer for future growth. | Could | Sprint 2 | `backend/config/asgi.py`, `backend/config/wsgi.py`, deployment notes in `Assessment2/docs/DEPLOYMENT.md` |
| NFR-09 | Usability | Primary user journeys (register → post → search → chat → rate) require no more than 5 clicks each, with clear labels and error messages. | Must | Sprint 1–2 | UX review during Sprint 1/2 reviews; wireframes in `Assessment2/docs/wireframes/`, form validation messages in templates |
| NFR-10 | Accessibility | UI meets basic WCAG 2.1 Level A: semantic HTML, keyboard-navigable forms, alt text on profile photos, sufficient colour contrast. | Should | Sprint 2 | `backend/templates/base.html`, `backend/static/css/main.css`, accessibility checklist in `Assessment2/docs/ACCESSIBILITY.md` |
| NFR-11 | Maintainability | Code follows Django app structure with separate modules per domain (accounts, listings, chat, reviews, moderation). | Must | Sprint 1 | Repository layout under `backend/`, README in `Assessment2/README.md`, coding conventions in `Assessment2/docs/ARCHITECTURE.md` |
| NFR-12 | Testability | Automated tests cover critical paths using pytest-django and factory_boy; target ≥ 30 tests with CI-friendly execution. | Must | Sprint 1–2 | `backend/tests/` (12 unit tests Sprint 1, 18 integration tests Sprint 2), `backend/conftest.py`, `pytest.ini` |
| NFR-13 | Observability | Application errors and key events (failed login, report submitted) are logged for debugging and audit during assessment demos. | Should | Sprint 2 | `backend/config/settings.py` (LOGGING), structured logs in views/consumers |
| NFR-14 | Deployability | Prototype can be deployed to a staging server with PostgreSQL, Redis, and media storage configured via environment variables. | Must | Sprint 2 | `Assessment2/docker-compose.yml`, `Assessment2/.env.example`, `Assessment2/docs/DEPLOYMENT.md`, deployment task in Sprint 2 backlog |
| NFR-15 | Email deliverability | Outbound email (verification, notifications) uses configurable SMTP settings suitable for development (console backend) and staging (SMTP). | Should | Sprint 1–2 | `backend/config/settings.py` (EMAIL_BACKEND, EMAIL_HOST), `backend/notifications/email.py` |

---

## 4. Requirements Traceability Matrix

| Sprint | Functional Requirements | Non-Functional Requirements |
|--------|-------------------------|-----------------------------|
| **Sprint 1** (Weeks 1–2) | FR-01 – FR-11, FR-22 (base UI) | NFR-01 – NFR-04, NFR-07, NFR-09 (partial), NFR-11, NFR-12 (12 unit tests), NFR-15 (verification email) |
| **Sprint 2** (Weeks 3–4) | FR-12 – FR-21, FR-22 (complete) | NFR-05 – NFR-06, NFR-08 – NFR-10, NFR-12 (18 integration tests), NFR-13 – NFR-15 |

---

## 5. Out of Scope (Assessment Prototype)

The following items are explicitly excluded from the Assessment 2 prototype but may be noted as future work:

- Native mobile apps (iOS/Android)
- Payment processing or escrow for paid services
- Third-party OAuth login (Google, Facebook)
- Multi-language / i18n support
- Automated background job matching beyond suburb/skill filters

---

## 6. Acceptance Criteria Summary

The prototype is considered complete when:

1. A new user can register, verify email, log in, and create a profile (FR-01 – FR-05).
2. The user can post and browse help listings with categories (FR-07 – FR-09).
3. Nearby search returns locally relevant listings (FR-12).
4. Two matched users can chat in real time and leave ratings (FR-14 – FR-18).
5. Report, block, and admin moderation flows function correctly (FR-11, FR-19 – FR-20).
6. All **Must** non-functional requirements are demonstrated in the Sprint 2 review demo.
7. Automated test suite passes with ≥ 30 tests (NFR-12).
