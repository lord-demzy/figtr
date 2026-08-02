# FIGTR — System Architecture

## 1. Product Overview

FIGTR is a **commercial, multi-tenant SaaS platform for school management**. It provides a unified digital workspace for schools to manage students, staff, academics, attendance, grades, finance, and communication — all from a single, secure, cloud-based platform.

Each school operates as an isolated **tenant** with its own data, branding, and configuration. The platform serves multiple roles — school administrators, teachers, students, and parents — with role-based access control and strict data isolation between tenants.

## 2. Technology Stack Decisions

The following technology stack has been selected for FIGTR:

### Backend

| Technology | Purpose |
|------------|---------|
| **Django** | Core backend framework — models, ORM, admin, business logic |
| **Django REST Framework (DRF)** | REST API construction, serializers, ViewSets, authentication |
| **PostgreSQL** | Primary relational database |

### Frontend

| Technology | Purpose |
|------------|---------|
| **Next.js** | React framework with server-side rendering and routing |
| **TypeScript** | Type-safe frontend development |
| **Tailwind CSS** | Utility-first styling |
| **shadcn/ui** | Reusable, accessible UI component library |

### Infrastructure

| Technology | Purpose |
|------------|---------|
| **Docker** | Containerization of all services |
| **GitHub Actions** | CI/CD pipeline |
| **Supabase PostgreSQL** | Managed PostgreSQL database |
| **Supabase Storage** | Object storage for file uploads |

### Authentication

| Technology | Purpose |
|------------|---------|
| **Django-managed authentication** | User accounts, sessions, and password management handled by Django |
| **JWT-based API authentication** | Token-based authentication for the REST API |

> **Note:** Supabase Auth will **NOT** be used. Authentication is fully managed by Django, with JWT tokens for API access.

## 3. System Architecture

The system follows a clear, decoupled flow:

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

### Data Flow

1. **Users** interact with the **Next.js frontend** in the browser.
2. The frontend communicates with the **Django REST API** over HTTPS using JSON.
3. The Django REST API enforces authentication, authorization, and multi-tenant data isolation.
4. The API persists and retrieves data from the **PostgreSQL database** (via Supabase).
5. File uploads (documents, images, reports) are stored in **Supabase Storage**.

The frontend never accesses the database directly — all data flows through the Django REST API.

## 4. Backend Architecture Rules

The Django backend follows these architectural rules:

- **Django apps organized by business domain** — Each business domain (e.g., tenants, users, academics, finance) is a separate Django app.
- **Business logic separated from views** — Views/controllers remain thin and delegate to the service layer.
- **Service layer for complex operations** — Complex business operations are implemented in a dedicated service layer, not in views or serializers.
- **DRF ViewSets where appropriate** — Use DRF ViewSets for standard CRUD resources to reduce boilerplate and ensure consistency.
- **Serializers handle validation** — Input validation is performed at the serializer level; business rules are enforced in services.
- **Automated tests required** — All new functionality must include automated tests.

## 5. Frontend Architecture Rules

The Next.js frontend follows these architectural rules:

- **Feature-based folder structure** — Code is organized by feature/domain, not by file type.
- **Reusable components** — Components are small, focused, and reusable across the application.
- **Shared UI components** — Common UI elements are built on the shadcn/ui library and shared across features.
- **API layer separated from components** — All API calls are isolated in a dedicated API layer; components do not make direct HTTP calls.
- **TypeScript required** — All frontend code is written in TypeScript.

## 6. Platform Architecture

FIGTR is built on the **FIG3 Platform**, a modular, multi-product SaaS foundation:

```
FIG3 Platform
├── FIG3 Core
│   ├── Identity (users, accounts, auth)
│   ├── Tenancy (tenant models, context, isolation)
│   ├── Permissions (roles, permissions, access control)
│   ├── Branding (tenant theming, visual identity)
│   ├── Notifications (email, SMS, in-app, push)
│   ├── Storage (file uploads, object storage, media)
│   ├── Configuration (settings, feature flags)
│   ├── Registry (product and module registries)
│   └── Extensions (extension points, hooks, plugins)
└── FIG3 Edu
    └── Education-specific modules
```

### FIG3 Core

- **Product-agnostic** platform foundation used by all FIG3 products.
- Must not contain any product-specific business logic.
- Provides reusable services for identity, tenancy, permissions, branding, notifications, storage, configuration, registry, and extensions.

### FIG3 Edu

- The **education product** built on FIG3 Core.
- Contains all education-specific business logic and modules.
- Consumes services from FIG3 Core.

### Future Products

- FIG3 Legal, FIG3 Commerce, FIG3 HR will live alongside FIG3 Core and FIG3 Edu.
- Each product consumes services from FIG3 Core.
- No code is written for future products now; the architecture allows easy addition.

## 7. Multi-Tenancy Architecture

FIGTR uses a **membership-based multi-tenancy model**:

```
User
  ↓
Membership
  ↓
School
  ↓
School-owned data
```

### Model

- A **User** is a single account that can belong to **multiple schools**.
- A **Membership** links a user to a school and defines the user's **role** within that school (e.g., admin, teacher, student, parent).
- A **School** is the tenant — it owns all school-scoped data (students, classes, grades, finance, etc.).
- **School-owned data** is always scoped to a specific school.

### Key Rules

- One user can belong to multiple schools with **different roles** in each.
- All school-scoped queries must be filtered by the active school context.
- Cross-school data access is strictly prohibited and enforced at the data-access layer.
- The active school context is resolved per request based on the authenticated user's membership.

## 8. External Services

FIGTR plans to integrate with the following external services:

| Service | Purpose |
|---------|---------|
| **Supabase Storage** | File and document storage |
| **Paystack** | Payment processing (fees, invoicing) |
| **Email provider** | Transactional and notification emails (provider to be selected) |
| **SMS provider** | SMS notifications (provider to be selected) |

> These integrations are planned. Each will be documented in detail before implementation.

## 9. Development Principles

FIGTR development follows these principles:

- **Documentation before implementation** — Read and update relevant documentation before writing code. No features without a specification.
- **Small incremental tasks** — Work is broken into small, focused, incremental tasks.
- **AI-assisted development workflow** — AI tools are used to accelerate development while following the project rules in `.clinerules`.
- **Code review before merging** — All changes are reviewed before merging to `main`.

---

*This document is a living artifact and will be refined as the architecture evolves.*