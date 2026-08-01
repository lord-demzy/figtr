# FIGTR — Database Conventions

## Purpose

This document defines the conventions for database design, naming, and management within the FIGTR platform. Following these conventions ensures consistency, maintainability, and data integrity across all modules.

## Database Principles

### Primary Database

- **PostgreSQL** is the primary database for FIGTR, hosted via **Supabase PostgreSQL**.
- All persistent application data is stored in PostgreSQL.
- The Django ORM is used for all database access; raw SQL is avoided unless necessary and approved.

### Naming Conventions

- **Tables / Models:** Use **snake_case** for table names. Table names are **plural** and descriptive (e.g., `students`, `classes`, `attendance_records`). Model class names use **PascalCase** (e.g., `Student`, `ClassRoom`, `AttendanceRecord`).
- **Columns / Fields:** Use **snake_case**. Use descriptive, unambiguous names (e.g., `first_name`, `enrollment_date`, `is_active`).
- **Boolean fields:** Prefix with `is_`, `has_`, or `can_` (e.g., `is_active`, `has_graduated`).
- **Foreign keys:** Name the field after the related model (e.g., `student_id`, `class_id`).

### Table Naming Rules

- Table names are **plural** and descriptive.
- Use the domain prefix where helpful to group related tables (e.g., `academic_*`, `finance_*`).
- Avoid SQL reserved words as table/column names (e.g., `order`, `group`, `user`). If unavoidable, rename or quote consistently.

### Foreign Key Conventions

- **One-to-Many:** Use a foreign key on the "many" side.
- **Many-to-Many:** Use a junction/through table with explicit naming (e.g., `student_classes`).
- **One-to-One:** Use a unique foreign key.
- Always define `on_delete` behavior explicitly (e.g., `CASCADE`, `SET_NULL`, `PROTECT`).
- Use `PROTECT` for critical financial or audit data to prevent accidental deletion.

### Timestamp Requirements

- **Every table must have `created_at` and `updated_at` timestamps.**
- `created_at` — timestamp of record creation (set automatically).
- `updated_at` — timestamp of last update (updated automatically on change).
- Timestamps are stored in **UTC**.

### Indexing Guidelines

- Add indexes on columns used frequently in `WHERE`, `JOIN`, and `ORDER BY` clauses.
- Use composite indexes where multiple columns are commonly filtered together.
- Name indexes descriptively (e.g., `idx_students_class_id`).
- **Every foreign key should be indexed** to support efficient joins.
- **Index the `school_id` column on all school-owned tables** — critical for tenant isolation queries.

### Audit Logging Considerations

- For sensitive data (e.g., grades, financial records), maintain an audit trail:
  - `created_by`, `updated_by` fields where relevant.
  - A separate audit log table for significant changes.
- Audit requirements are enforced at the application/service layer.
- Audit logs are immutable — they are append-only records.

### Soft Deletion Policy

- Soft deletes are **not the default**; hard deletes are preferred for most records.
- Soft deletes may be used for specific entities where data retention is required (e.g., financial records, academic records).
- If soft deletes are used, include `deleted_at` (nullable) and filter it in all queries.
- The decision to use soft deletes for a specific entity must be recorded in an ADR.

## Multi-Tenancy Design

FIGTR uses a **membership-based multi-tenancy model**:

```
User
  ↓
Membership
  ↓
School
  ↓
School-owned records
```

### Architecture

- A **User** is a single platform account that can belong to **multiple schools**.
- A **Membership** links a user to a school and defines the user's **role** within that school (e.g., admin, teacher, student, parent).
- A **School** is the tenant — it owns all school-scoped data.
- **School-owned records** are always linked to a specific school via a `school_id` foreign key.

### Rules

- **Users can belong to multiple schools.**
- **Users can have different roles per school.**
- **All school data must be isolated** — every school-owned entity is scoped by `school_id`.
- **Tenant checks happen on the backend** — the Django REST API enforces tenant isolation at the data-access layer.
- **Frontend permissions are not trusted for security** — the frontend only controls UI visibility; all authorization is enforced server-side.

---

*This document is a living artifact and will be updated as the project evolves.*