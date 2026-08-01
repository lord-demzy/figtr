# ADR-004: Backend Foundation

- **Status:** Accepted
- **Date:** 2026-08-01
- **Deciders:** FIGTR Engineering Team

## Context

FIGTR is a commercial, multi-tenant SaaS platform for school management. ADR-002 established the system architecture with Django + Django REST Framework + PostgreSQL as the backend stack. ADR-003 defined the database design and domain model. Before any business features can be built, a solid Django backend foundation is required — project structure, configuration, shared core functionality, and development quality tools.

## Decision

We will establish the initial Django backend foundation with the following structure and configuration:

### Project Structure

```
backend/
├── config/              # Django project configuration (settings, urls, wsgi, asgi)
├── apps/                # Django applications organized by business domain
├── core/                # Shared functionality application (health check, utils, exceptions)
├── tests/               # Project-level test utilities
├── requirements/        # Environment-specific dependency files
├── .env.example         # Environment variable template
├── manage.py            # Django management entrypoint
└── pyproject.toml       # Project configuration (Ruff, Black, Pytest)
```

### Technology Configuration

- **Python 3.12+** (tested on Python 3.14.4).
- **Django 5.2** with environment-specific settings modules:
  - `config/settings/base.py` — common settings.
  - `config/settings/development.py` — development settings (SQLite default).
  - `config/settings/production.py` — production settings (PostgreSQL, security hardening).
- **Django REST Framework** configured with pagination, JSON rendering, and placeholder authentication/permissions.
- **PostgreSQL** as the production database (via Supabase), with SQLite for easy local development.
- **Environment variables** for all configuration via `django-environ` — no hardcoded secrets.

### Core Application

- A `core` Django app provides shared functionality:
  - Health check endpoint: `GET /api/health/` → `{"status": "ok"}`.
  - Placeholder for shared utilities.
  - Placeholder for shared exceptions.
  - Automated test for the health endpoint.

### Development Quality Tools

- **Pytest** with `pytest-django` and `pytest-cov` for testing and coverage.
- **Ruff** for linting.
- **Black** for code formatting.
- Configuration in `backend/pyproject.toml`.

### Dependency Management

- `requirements/base.txt` — Django, DRF, django-environ, django-cors-headers, psycopg2-binary.
- `requirements/development.txt` — base + pytest, pytest-django, pytest-cov, ruff, black.
- `requirements/production.txt` — base + gunicorn.

## Reason

This structure supports FIGTR development because:

- **Clean separation** — the `config/` package (configuration), `apps/` (future business domains), and `core/` (shared functionality) are clearly separated.
- **Scalable app organization** — future apps (accounts, schools, students, academics, finance, communication) will be added to `apps/` by business domain, following ADR-003's domain model.
- **Environment-aware configuration** — separate settings modules and environment variables allow safe development, staging, and production configurations without hardcoded secrets.
- **Quality-first development** — Pytest, Ruff, and Black are configured upfront, ensuring all future code follows project standards (per `.clinerules`).
- **Immediate verifiability** — the health check endpoint and its test verify the foundation works before any business features are built.

## Consequences

### Benefits

- **Ready-to-develop foundation** — new apps can be added without additional setup.
- **Consistent configuration** — all environments use the same base settings pattern.
- **Automated quality gates** — linting, formatting, and tests are available immediately.
- **No hardcoded secrets** — environment variables are the standard from day one.
- **Testable health endpoint** — validates the deployment is functional.

### Trade-offs

- **Python 3.14 used instead of 3.12** — the task specified Python 3.12, but only Python 3.14 was available on the development machine. The code is compatible with 3.12+ (`requires-python = ">=3.12"`), so this is forward-compatible.
- **SQLite for development by default** — PostgreSQL is the production database, but SQLite is the development default for simplicity. This may mask PostgreSQL-specific behaviors.
- **Placeholder authentication/permissions** — DRF is configured, but authentication is not yet implemented (per scope restrictions).

### Risks

- **Settings drift** — environment-specific settings could diverge; mitigated by keeping shared settings in `base.py`.
- **SQLite/PostgreSQL differences** — mitigated by supporting `USE_SQLITE=False` for PostgreSQL development.

## Related

- ADR-001: Project Foundation
- ADR-002: System Architecture
- ADR-003: Database Design