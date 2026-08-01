# ADR-003: Database Design

- **Status:** Accepted
- **Date:** 2026-08-01
- **Deciders:** FIGTR Engineering Team

## Context

FIGTR is a commercial, multi-tenant SaaS platform for school management. ADR-002 established the system architecture and technology stack, including PostgreSQL as the primary database and a membership-based multi-tenancy model. This ADR defines the database architecture, core domain entities, and data model conventions that will guide all database implementation.

## Decision

We will design the FIGTR database using the following architecture:

### Database Architecture

- **PostgreSQL** is the primary database, hosted via **Supabase PostgreSQL**.
- **Every table must have `created_at` and `updated_at` timestamps** (stored in UTC).
- **Naming conventions:** snake_case table/column names; plural table names; PascalCase model names; `is_`/`has_`/`can_` prefix for booleans; foreign keys named after the related model.
- **Foreign key conventions:** explicit `on_delete` behavior; `PROTECT` for critical financial/audit data; junction tables for many-to-many.
- **Indexing principles:** index all foreign keys; index `school_id` on all school-owned tables; composite indexes for common filters.
- **Soft deletes:** not the default; used only where data retention is required (e.g., financial/academic records), with `deleted_at` and ADR documentation.
- **Audit requirements:** audit trail for sensitive data (grades, financial records) via `created_by`/`updated_by` and audit log tables.

### Multi-Tenancy Model

Membership-based multi-tenancy:

```
User
  ↓
Membership
  ↓
School
  ↓
School-owned records
```

- A **User** can belong to **multiple schools**.
- A **User** can have **different roles in different schools**.
- **Every school-owned entity must be linked to a school** via a `school_id` foreign key.
- **Tenant checks happen on the backend** — the Django REST API enforces tenant isolation at the data-access layer.
- **Frontend permissions are not trusted for security** — all authorization is enforced server-side.

### Core Domain Entities

The initial domain model is organized into the following groups:

**Identity:** User, Role, Permission, Membership

**School Management:** School, SchoolProfile, SchoolSettings, AcademicSession, Term, Class, ClassArm, Department, Subject, House, GradingSystem

**People:** Student, ParentGuardian, Teacher, StaffProfile, StudentGuardianRelationship

**Academic:** Attendance, Assessment, Examination, Result, ReportCard, Promotion, AcademicRecord

**Finance:** FeeCategory, FeeStructure, Invoice, Payment, Receipt, FinancialTransaction

**Communication:** Announcement, Notification, Event, Message

**Website Builder:** WebsiteSettings, Page, NewsPost, GalleryItem, ContactSubmission

### Key Relationships

- School has many Students, Teachers, AcademicSessions, Classes, Subjects.
- Student belongs to School; can have many Guardians; has many Results, Invoices.
- Teacher teaches many Subjects.
- Invoice belongs to Student; Payment belongs to Invoice.

## Reason

This database structure supports a scalable multi-tenant SaaS product because:

- **Membership-based multi-tenancy** allows a single user to belong to multiple schools with different roles, which is a core requirement for the platform (e.g., a teacher who is also a parent at another school).
- **School-scoped data** with a `school_id` foreign key on every school-owned entity provides a clear, enforceable tenant isolation boundary.
- **Domain-organized entities** (Identity, School Management, People, Academic, Finance, Communication, Website Builder) map cleanly to Django apps organized by business domain, keeping the codebase maintainable.
- **Standard timestamps and audit fields** provide a consistent foundation for auditing and data integrity.
- **PostgreSQL** provides strong relational integrity, indexing, and JSON support needed for a data-rich school management platform.
- **Backend-enforced tenant isolation** ensures security is not dependent on frontend behavior.

## Consequences

### Benefits

- **Clear tenant isolation** — every school-owned record is scoped by `school_id`, making isolation enforceable and testable.
- **Flexible user model** — users can belong to multiple schools with different roles.
- **Domain-aligned structure** — entities map to Django apps, improving maintainability.
- **Consistent conventions** — timestamps, naming, and indexing reduce ambiguity and errors.
- **Scalable foundation** — the model supports the full MVP roadmap (academics, finance, communication, website builder).
- **Secure by design** — backend-enforced tenant checks protect against unauthorized cross-tenant access.

### Limitations

- **Shared-schema multi-tenancy** — all tenants share the same tables; isolation relies on correct `school_id` scoping in every query. This requires discipline and thorough testing to avoid cross-tenant data leaks.
- **Large tables** — shared tables (e.g., students, results) will grow across all tenants; requires good indexing and pagination.
- **Soft delete complexity** — soft deletes add query complexity where used.

### Future Considerations

- **Schema-per-tenant** — if a tenant requires stronger isolation, this can be revisited (deferred in ADR-002).
- **Partitioning** — large tables (attendance, financial transactions) may require partitioning as data grows.
- **Data warehouse** — advanced analytics may require a separate reporting database.
- **Audit log** — a dedicated audit log table may be introduced for compliance.

## Related

- ADR-001: Project Foundation
- ADR-002: System Architecture
- ADR-004 (planned): Django project structure and app organization.