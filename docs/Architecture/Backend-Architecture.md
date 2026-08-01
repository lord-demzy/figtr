# FIGTR — Backend Architecture

## Purpose

This document defines the backend architecture for the FIGTR platform, including the Django project structure, application organization rules, API development approach, testing strategy, and dependency management.

## Django Project Structure

The Django project lives inside `backend/`:

```
backend/
├── config/              # Django project configuration
│   ├── settings/        # Environment-specific settings modules
│   │   ├── base.py      # Common settings (all environments)
│   │   ├── development.py  # Development settings
│   │   └── production.py   # Production settings
│   ├── __init__.py
│   ├── asgi.py          # ASGI entrypoint
│   ├── urls.py          # Root URL configuration
│   └── wsgi.py          # WSGI entrypoint
├── apps/                # Django applications organized by business domain
│   └── __init__.py
├── core/                # Shared functionality application
│   ├── __init__.py
│   ├── apps.py          # App configuration
│   ├── urls.py          # Core URL configuration
│   ├── views.py         # Health check endpoint
│   ├── tests.py         # Core tests
│   ├── utils.py         # Shared utilities (placeholder)
│   └── exceptions.py    # Shared exceptions (placeholder)
├── tests/               # Project-level test utilities
│   └── __init__.py
├── requirements/        # Dependency management
│   ├── base.txt         # Base dependencies (all environments)
│   ├── development.txt  # Development dependencies
│   └── production.txt   # Production dependencies
├── .env.example         # Environment variable template
├── manage.py            # Django management entrypoint
└── pyproject.toml       # Project configuration (Ruff, Black, Pytest)
```

## Application Organization Rules

- **Django apps are organized by business domain** in the `apps/` directory.
- Each business domain (e.g., accounts, schools, students, academics, finance, communication) will be a separate Django app.
- Future apps will be created in `apps/` (e.g., `apps/accounts`, `apps/schools`, `apps/students`).
- The `core` app contains **shared functionality** only — no business features.
- Apps should be small and focused on a single domain responsibility.
- Business logic lives in a **service layer**, not in views or serializers.

## API Development Approach

- **Django REST Framework (DRF)** is used for API construction.
- All API endpoints are under the `/api/` prefix.
- **DRF ViewSets** are used for standard CRUD resources where appropriate.
- **Serializers handle input validation**; business rules are enforced in services.
- API responses follow the standards in `docs/API/API-Standards.md`.
- Authentication and permissions will be implemented in future prompts (JWT-based).

## Testing Strategy

- **Pytest** is the test runner, with `pytest-django` and `pytest-cov`.
- Tests for each app live in the app's `tests.py` or a `tests/` directory.
- The health check endpoint has an automated test.
- All new functionality must include automated tests.
- Coverage is tracked via `pytest-cov`.

## Dependency Management

- Dependencies are organized by environment in `backend/requirements/`:
  - `base.txt` — shared dependencies (Django, DRF, django-environ, django-cors-headers, psycopg2).
  - `development.txt` — includes base + testing and code quality tools (pytest, pytest-django, pytest-cov, ruff, black).
  - `production.txt` — includes base + production server (gunicorn).
- A virtual environment is used for isolation: `backend/.venv/`.
- All configuration uses **environment variables** (via `django-environ`); no hardcoded secrets.

---

*This document is a living artifact and will be updated as the backend evolves.*