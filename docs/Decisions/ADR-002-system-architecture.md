# ADR-002: System Architecture

- **Status:** Accepted
- **Date:** 2026-08-01
- **Deciders:** FIGTR Engineering Team

## Context

FIGTR is a commercial, multi-tenant SaaS platform for school management. The project foundation (ADR-001) established the directory structure and documentation framework, but left the technology stack and system architecture as placeholders. This ADR finalizes the system architecture, technology stack, and architectural patterns that will guide all future development.

## Decision

We will build FIGTR using the following architecture and technology stack:

### Technology Stack

**Backend:**
- **Django** — core backend framework (models, ORM, admin, business logic).
- **Django REST Framework (DRF)** — REST API construction, serializers, ViewSets, authentication.
- **PostgreSQL** — primary relational database.

**Frontend:**
- **Next.js** — React framework with server-side rendering and routing.
- **TypeScript** — type-safe frontend development.
- **Tailwind CSS** — utility-first styling.
- **shadcn/ui** — reusable, accessible UI component library.

**Infrastructure:**
- **Docker** — containerization of all services.
- **GitHub Actions** — CI/CD pipeline.
- **Supabase PostgreSQL** — managed PostgreSQL database.
- **Supabase Storage** — object storage for file uploads.

**Authentication:**
- **Django-managed authentication** — user accounts, sessions, and password management handled by Django.
- **JWT-based API authentication** — token-based authentication for the REST API.
- **Supabase Auth will NOT be used.**

### System Architecture

```
Users
  ↓
Next.js Frontend
  ↓
Django REST API
  ↓
PostgreSQL Database
  ↓
Supabase Storage
```

### Backend Architecture Patterns

- Django apps organized by **business domain**.
- **Business logic separated from views** — thin views delegating to a service layer.
- **Service layer** for complex operations.
- **DRF ViewSets** where appropriate for standard CRUD.
- **Serializers handle validation**; business rules enforced in services.
- **Automated tests** required for all new functionality.

### Frontend Architecture Patterns

- **Feature-based folder structure**.
- **Reusable components**.
- **Shared UI components** built on shadcn/ui.
- **API layer separated from components**.
- **TypeScript required**.

### Multi-Tenancy Model

Membership-based multi-tenancy:

```
User
  ↓
Membership
  ↓
School
  ↓
School-owned data
```

- One user can belong to **multiple schools** with **different roles** in each.
- All school-scoped data is filtered by the active school context.
- Cross-school data access is strictly prohibited.

### External Services (Planned)

- **Supabase Storage** — file/document storage.
- **Paystack** — payment processing.
- **Email provider** — transactional/notification emails (provider to be selected).
- **SMS provider** — SMS notifications (provider to be selected).

## Reason

These technologies and patterns were selected for the following reasons:

- **Django + DRF** — mature, battle-tested framework with a rich ecosystem, strong ORM, built-in admin, and excellent support for REST APIs and multi-tenancy patterns. Python's readability and the framework's "batteries included" philosophy accelerate development while maintaining quality.
- **PostgreSQL** — robust, feature-rich relational database with strong data integrity, JSON support, and scalability. Supabase provides a managed, cost-effective hosting option.
- **Next.js + TypeScript** — industry-standard React framework with SSR/SSG, excellent developer experience, and TypeScript for type safety across the frontend.
- **Tailwind CSS + shadcn/ui** — modern, utility-first styling with a reusable, accessible component library that accelerates UI development while keeping components customizable.
- **Django-managed authentication + JWT** — keeps authentication fully under our control (no third-party auth dependency), while JWT provides stateless, scalable API authentication.
- **Docker + GitHub Actions** — containerization for consistent environments and automated CI/CD for quality and speed.
- **Membership-based multi-tenancy** — flexible model allowing users to belong to multiple schools with different roles, which is a core requirement for the platform.
- **Service layer pattern** — keeps business logic testable, maintainable, and separated from the HTTP layer.

## Consequences

### Benefits

- **Mature, well-supported stack** — reduces risk and accelerates development.
- **Clear separation of concerns** — backend/frontend decoupling, service layer, and feature-based frontend structure improve maintainability.
- **Type safety** — TypeScript on the frontend and Django's strong typing reduce bugs.
- **Scalable multi-tenancy** — membership model supports users across multiple schools.
- **Full control over authentication** — no dependency on a third-party auth provider.
- **Reproducible environments** — Docker and CI/CD ensure consistency.

### Trade-offs

- **Django + DRF** — heavier than lighter frameworks; requires disciplined structure to avoid "fat views."
- **Supabase** — managed service introduces a dependency on a third-party platform for database and storage.
- **JWT** — requires careful token management (expiry, refresh, revocation).
- **Service layer** — adds a layer of abstraction that must be consistently applied to avoid inconsistency.
- **Multi-tenancy complexity** — membership model requires careful enforcement of tenant isolation in every query.

### Risks

- **Tenant isolation bugs** — mitigated by enforcing school scoping at the data-access layer and thorough testing.
- **Provider lock-in** — Supabase is used for managed PostgreSQL and storage; mitigated by using standard PostgreSQL and S3-compatible storage interfaces.
- **JWT security** — mitigated by following JWT best practices (short-lived tokens, refresh tokens, secure storage).

## Alternatives Considered

- **Supabase Auth** — rejected; we want full control over authentication and user management within Django.
- **MongoDB / NoSQL** — rejected; relational data (students, classes, grades, finance) benefits from PostgreSQL's integrity and relationships.
- **Vue.js / Svelte** — rejected; Next.js/React is the industry standard with a larger ecosystem and better SSR support.
- **Schema-per-tenant multi-tenancy** — deferred; the membership-based model (shared schema with school scoping) is simpler and sufficient for the initial phase. This may be revisited in a future ADR.

## Related

- ADR-001: Project Foundation
- ADR-003 (planned): Database schema and multi-tenancy implementation details.