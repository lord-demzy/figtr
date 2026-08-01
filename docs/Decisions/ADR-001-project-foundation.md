# ADR-001: Project Foundation

- **Status:** Accepted
- **Date:** 2026-08-01
- **Deciders:** FIGTR Engineering Team

## Context

FIGTR is a commercial, multi-tenant SaaS school management platform. The project is starting from an empty repository. Before any feature development begins, we need to establish a solid project foundation: a clear directory structure, documentation framework, and development rules that will guide all future work.

## Decision

We will establish the following project foundation:

### 1. Directory Structure

```
figtr/
├── backend/          # Backend API (Django, to be finalized)
├── frontend/         # Frontend web app (Next.js, to be finalized)
├── docs/             # All project documentation
│   ├── Vision/       # Product vision and strategy
│   ├── PRD/          # Product requirements
│   ├── Architecture/ # System architecture & dev standards
│   ├── Database/     # Database conventions
│   ├── API/          # API standards
│   ├── UI/           # Design system
│   ├── Prompts/      # AI-assisted development prompts
│   └── Decisions/    # Architecture Decision Records (ADRs)
├── .github/          # GitHub configuration (CI/CD, templates)
├── docker/           # Docker configuration files
└── scripts/          # Utility scripts
```

### 2. Documentation Framework

- A set of living documentation files establish the product vision, system architecture, development standards, database conventions, API standards, and design system.
- Architecture Decision Records (ADRs) in `docs/Decisions/` record significant decisions and their rationale.

### 3. Project Rules

- A `.clinerules` file at the repository root defines the rules that all development (including AI-assisted development) must follow.

### 4. Technology Stack (Placeholders)

- **Backend:** Django + Django REST Framework (placeholder, to be finalized).
- **Frontend:** Next.js (React) (placeholder, to be finalized).
- **Database:** PostgreSQL (placeholder, to be finalized).
- **Containerization:** Docker.
- **CI/CD:** GitHub Actions.

> These are placeholders. Final technology choices will be recorded in dedicated ADRs.

## Consequences

### Positive

- Clear, predictable project structure that scales with the codebase.
- Documentation-first culture reduces ambiguity and onboarding time.
- ADRs provide a historical record of architectural decisions.
- Project rules ensure consistent, high-quality development.

### Negative

- Initial setup time before feature work begins.
- Documentation must be maintained to stay accurate.

### Risks

- Documentation could become stale if not updated. Mitigated by the "documentation first" rule in `.clinerules`.
- Placeholder technology choices could change, requiring updates to docs. Mitigated by recording final choices in dedicated ADRs.

## Alternatives Considered

- **No documentation / minimal structure:** Rejected — would lead to inconsistency and poor maintainability for a commercial product.
- **Monolithic single-folder structure:** Rejected — the separation of backend/frontend is essential for a decoupled, scalable SaaS platform.

## Related

- ADR-002 (planned): Multi-tenancy strategy.
- ADR-003 (planned): Technology stack finalization.