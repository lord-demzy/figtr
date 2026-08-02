# FIGTR — Project State

## Overview

This document tracks the current state of the FIGTR project, including completed prompts, current status, and next steps.

## Frontend Foundation ✅ COMPLETE

**Status:** Ready for feature development

### Completed

- [x] Next.js 16 project initialized with TypeScript
- [x] Tailwind CSS v4 configured
- [x] shadcn/ui initialized with base-nova preset
- [x] UI components created: Button, Input, Label, Card, Dialog, Table, Form, use-toast
- [x] API client implemented with auth and error handling
- [x] Toast notification system
- [x] Design system documented
- [x] Frontend architecture documented
- [x] Environment variables configured
- [x] FIGTR branded landing page

### Files Created

- `frontend/src/components/ui/*.tsx` (8 components)
- `frontend/src/lib/utils.ts`
- `frontend/src/lib/api-client.ts`
- `frontend/.env.example`
- `docs/UI/Design-System.md` (finalized)
- `docs/Architecture/Frontend-Architecture.md`
- `docs/Decisions/ADR-005-frontend-foundation.md`

### Backend Product Framework Files

- `backend/fig3/core/registry/contracts.py` — `ProductContract` abstract base class.
- `backend/fig3/core/registry/product_registry.py` — `ProductRegistry` singleton.
- `backend/fig3/core/registry/__init__.py` — Package exports.
- `backend/fig3/edu/product.py` — `EduProductManifest` implementing the contract.
- `backend/fig3/edu/registry.py` — Registration helpers for FIG3 Edu.
- `docs/Architecture/Backend-Architecture.md` — Updated with Product Framework section.
- `docs/Decisions/ADR-007-product-framework.md` — Product framework decision record.

### Next Steps

- Implement authentication pages (login, forgot password)
- Build dashboard layout
- Create role-based views (admin, teacher, student, parent)

## Current Status

- **Phase:** Accounts & Authentication (next)
- **Status:** Backend foundation complete; product framework implemented
- **Last Updated:** 2026-08-02

## Completed Prompts

| # | Prompt | Status | Summary |
|---|--------|--------|---------|
| 1 | Project Foundation | ✅ Complete | Created directory structure, documentation framework, `.clinerules`, and README. |
| 2 | System Architecture | ✅ Complete | Finalized technology stack, system architecture, and multi-tenancy model. |
| 3 | Database Architecture & Domain Model | ✅ Complete | Defined database conventions, ERD, MVP vs future entities, and ADR-003. |
| 4 | Backend Foundation Setup | ✅ Complete | Created Django backend foundation with config, core app, health endpoint, and development tools. |
| 5 | Frontend Foundation Setup | ✅ Complete | Next.js 16 app with shadcn/ui components, API client, design system, and landing page. |
| 6 | FIG3 Platform Architecture | ✅ Complete | Refactored backend into FIG3 Core and FIG3 Edu packages per ADR-006. |
| 7 | Product Framework | ✅ Complete | Implemented Product Contract, Product Registry, and FIG3 Edu product manifest. |

## Current Documentation

| Document | Status |
|----------|--------|
| `docs/Vision/Product-Vision.md` | ✅ Complete |
| `docs/Architecture/System-Architecture.md` | ✅ Complete |
| `docs/Architecture/Development-Standards.md` | ✅ Complete |
| `docs/Architecture/Backend-Architecture.md` | ✅ Complete |
| `docs/Architecture/Frontend-Architecture.md` | ✅ Complete |
| `docs/Development/Backend-Setup.md` | ✅ Complete |
| `docs/Database/Database-Conventions.md` | ✅ Complete |
| `docs/Database/ERD.md` | ✅ Complete |
| `docs/Database/MVP-vs-Future.md` | ✅ Complete |
| `docs/API/API-Standards.md` | ✅ Complete |
| `docs/UI/Design-System.md` | ✅ Complete |
| `docs/Decisions/ADR-001-project-foundation.md` | ✅ Complete |
| `docs/Decisions/ADR-002-system-architecture.md` | ✅ Complete |
| `docs/Decisions/ADR-003-database-design.md` | ✅ Complete |
| `docs/Decisions/ADR-004-backend-foundation.md` | ✅ Complete |
| `docs/Decisions/ADR-005-frontend-foundation.md` | ✅ Complete |
| `docs/Decisions/ADR-006-fig3-platform-architecture.md` | ✅ Complete |
| `docs/Decisions/ADR-007-product-framework.md` | ✅ Complete |

## Architecture Decisions

- **ADR-001:** Project Foundation — directory structure, documentation framework, project rules.
- **ADR-002:** System Architecture — Django + DRF + PostgreSQL backend; Next.js + TypeScript + Tailwind + shadcn/ui frontend; Docker + GitHub Actions + Supabase; Django-managed auth + JWT.
- **ADR-003:** Database Design — membership-based multi-tenancy, core domain entities, database conventions.
- **ADR-004:** Backend Foundation — Django project structure, environment-specific settings, core app, quality tools.
- **ADR-005:** Frontend Foundation — Next.js 16, TypeScript, Tailwind CSS v4, shadcn/ui, React Hook Form + Zod.
- **ADR-006:** FIG3 Platform Architecture — Refactored backend into FIG3 Core (platform) and FIG3 Edu (product) packages.
- **ADR-007:** Product Framework — Introduced Product Contract, Product Registry, and product manifests for platform-wide product management.

## Frontend State

- **Node.js:** 20.18.1+
- **Next.js:** 16.2.12
- **React:** 19.2.4
- **UI Components:** Button, Input, Label, Card, Dialog, Table, Form, use-toast
- **API Client:** `src/lib/api-client.ts` with auth token injection and error toasts
- **Landing page:** FIGTR branded hero + feature cards at `/`
- **Lint/Build:** Configured via ESLint and Next.js

## Backend State

- **Python:** 3.14.4 (virtual environment at `backend/.venv/`)
- **Django:** 5.2.16
- **DRF:** 3.17.1
- **Database:** SQLite (development default); PostgreSQL (production via Supabase)
- **Architecture:** FIG3 Platform with FIG3 Core and FIG3 Edu packages
- **Product Framework:** ProductContract, ProductRegistry, EduProductManifest implemented
- **Health endpoint:** `GET /api/health/` → `{"status": "ok"}`
- **Tests:** 1 passing (85% coverage)
- **Linting/Formatting:** Ruff and Black configured and passing

## Next Steps

1. **Prompt 6 (recommended):** Accounts & Authentication — User model, JWT authentication, and role-based access control foundation.
2. **Prompt 7:** Schools & Tenancy — School, SchoolProfile, SchoolSettings, Membership models.
3. **Frontend features:** Authentication pages, dashboard layout, role-based views.

## Notes

- Python 3.12 was specified but not available on the machine; Python 3.14.4 was used (compatible with `requires-python = ">=3.12"`).
- No business features have been implemented yet.
- No database migrations or models have been created.