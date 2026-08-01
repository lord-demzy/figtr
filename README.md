# FIGTR

**FIGTR** is a commercial, multi-tenant SaaS platform for school management. It provides a unified digital workspace for schools to manage students, staff, academics, attendance, grades, finance, and communication — all from a single, secure, cloud-based platform.

## Project Overview

FIGTR is built as a decoupled, scalable platform:

- **Backend API** (`backend/`) — business logic, authentication, multi-tenancy, and data persistence.
- **Frontend Web Application** (`frontend/`) — the user interface for all roles (admin, teacher, student, parent).
- **Documentation** (`docs/`) — the single source of truth for vision, architecture, standards, and decisions.

## Development Philosophy

FIGTR follows a **documentation-first** development philosophy:

1. **Read before you write** — Always consult the relevant documentation before writing code.
2. **Specification before implementation** — Features are not built without a specification.
3. **Consistency** — Follow existing architecture patterns and conventions.
4. **Minimalism** — No unnecessary dependencies; every dependency must be justified.
5. **Security by default** — Environment-based configuration, no hardcoded secrets, strict tenant isolation.
6. **Quality** — Tests for all new functionality, and a clear Definition of Done.

All development — including AI-assisted development — must follow the rules in [`.clinerules`](.clinerules).

## Technology Stack

> **Placeholder** — The final technology stack will be finalized and recorded in the Architecture Decision Records (`docs/Decisions/`).

| Layer      | Technology (placeholder)          |
|------------|-----------------------------------|
| Backend    | Django + Django REST Framework    |
| Frontend   | Next.js (React)                   |
| Database   | PostgreSQL                        |
| Cache/Queue| Redis                             |
| Container  | Docker                            |
| CI/CD      | GitHub Actions                    |

## Setup Instructions

> **Placeholder** — Setup instructions will be added once the backend and frontend projects are scaffolded.

### Prerequisites

- (To be defined)

### Backend Setup

1. (To be defined)

### Frontend Setup

1. (To be defined)

### Running with Docker

1. (To be defined)

## Documentation Guide

The `docs/` directory is the single source of truth for the project:

| Directory       | Purpose                                              |
|-----------------|------------------------------------------------------|
| `docs/Vision/`  | Product vision and strategy                          |
| `docs/PRD/`     | Product requirements                                 |
| `docs/Architecture/` | System architecture and development standards    |
| `docs/Database/`| Database conventions                                 |
| `docs/API/`     | API standards                                        |
| `docs/UI/`      | Design system                                        |
| `docs/Prompts/` | AI-assisted development prompts                      |
| `docs/Decisions/` | Architecture Decision Records (ADRs)               |

### Key Documents

- [Product Vision](docs/Vision/Product-Vision.md)
- [System Architecture](docs/Architecture/System-Architecture.md)
- [Development Standards](docs/Architecture/Development-Standards.md)
- [Database Conventions](docs/Database/Database-Conventions.md)
- [API Standards](docs/API/API-Standards.md)
- [Design System](docs/UI/Design-System.md)
- [ADR-001: Project Foundation](docs/Decisions/ADR-001-project-foundation.md)

## Project Structure

```
figtr/
├── backend/          # Backend API
├── frontend/         # Frontend web application
├── docs/             # Project documentation
├── .github/          # GitHub configuration (CI/CD, templates)
├── docker/           # Docker configuration
├── scripts/          # Utility scripts
└── .clinerules       # Project development rules
```

## License

> To be determined.

---

*FIGTR is a commercial product. All rights reserved.*