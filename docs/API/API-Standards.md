# FIGTR — API Standards

## Purpose

This document defines the standards and conventions for designing, building, and documenting the FIGTR REST API. Consistency across the API improves developer experience, maintainability, and integration quality.

## General Principles

- **RESTful Design** — Use REST conventions with clear resource-based URLs and HTTP methods.
- **Versioned** — All endpoints are versioned to allow safe evolution.
- **JSON** — All request/response bodies use JSON (UTF-8).
- **Stateless** — The API is stateless; authentication is provided per request.
- **Consistent Errors** — Use a uniform error response format.

## Base URL & Versioning

- Base URL: `/api/v1/` (version 1).
- Future versions increment the path (e.g., `/api/v2/`).
- Versioning is part of the URL path for simplicity and clarity.

## HTTP Methods & Semantics

| Method   | Purpose                          |
|----------|----------------------------------|
| `GET`    | Retrieve a resource or list      |
| `POST`   | Create a new resource            |
| `PUT`    | Replace a resource               |
| `PATCH`  | Partially update a resource      |
| `DELETE` | Delete a resource                |

## URL Conventions

- Use **kebab-case** for URL path segments (e.g., `/api/v1/attendance-records/`).
- Use **plural nouns** for collection resources (e.g., `/students/`, `/classes/`).
- Use the resource ID for individual resources (e.g., `/students/{id}/`).
- Use **snake_case** for query parameters and JSON field names.

## Request Conventions

- **Content-Type:** `application/json` for request bodies.
- **Authentication:** Bearer token in the `Authorization` header: `Authorization: Bearer <token>`.
- **Pagination:** List endpoints support `page` and `page_size` query parameters.
- **Filtering:** Use query parameters for filtering (e.g., `?status=active&class_id=5`).
- **Sorting:** Use `ordering` query parameter (e.g., `?ordering=-created_at`).

## Response Conventions

### Success Responses

- Return the appropriate HTTP status code:
  - `200 OK` — successful `GET`, `PUT`, `PATCH`.
  - `201 Created` — successful `POST`.
  - `204 No Content` — successful `DELETE`.
- Return the resource representation in the response body (except `204`).

### Error Responses

All errors use a consistent format:

```json
{
  "error": {
    "code": "validation_error",
    "message": "A human-readable description of the error.",
    "details": {
      "field_name": ["Specific error message for this field."]
    }
  }
}
```

- `code` — machine-readable error code (e.g., `not_found`, `permission_denied`, `validation_error`).
- `message` — human-readable summary.
- `details` — optional, field-level or additional error details.

### Common Error Status Codes

| Status | Code                | Description                          |
|--------|---------------------|--------------------------------------|
| 400    | `bad_request`       | Malformed request or invalid params  |
| 401    | `unauthenticated`   | Missing or invalid authentication    |
| 403    | `permission_denied` | Authenticated but not authorized     |
| 404    | `not_found`         | Resource does not exist              |
| 409    | `conflict`          | Conflict with current state          |
| 422    | `validation_error`  | Request validation failed            |
| 429    | `rate_limited`      | Too many requests                    |
| 500    | `internal_error`    | Unexpected server error              |

## Authentication & Authorization

- **Authentication:** Token-based (JWT) — to be finalized.
- **Authorization:** Role-based access control (RBAC) with granular permissions.
- All endpoints (except public ones like login) require authentication.
- Tenant context is resolved from the authenticated user; cross-tenant access is forbidden.

## Multi-Tenancy

- Tenant context is derived from the authenticated user's membership.
- All tenant-scoped resources are automatically filtered by the backend.
- Clients do not pass tenant IDs in URLs; the backend resolves the tenant.

## Naming & Field Conventions

- JSON field names use **snake_case**.
- Timestamps use **ISO 8601** format (e.g., `2026-08-01T12:00:00Z`).
- IDs are opaque strings (UUIDs) or integers per project decision.

## Documentation

- The API is documented using **OpenAPI** (Swagger) — to be finalized.
- Interactive docs available at `/api/docs/` (dev/staging).
- All endpoints must be documented before release.

## Versioning & Deprecation

- Deprecated endpoints are marked with a `Deprecation` header and a sunset date.
- Backward-incompatible changes require a new API version.

---

*This document is a living artifact and will be updated as the project evolves.*
</｜DSML｜tool>
<task_progress>
- [x] Create directory structure
- [x] Create docs/Vision/Product-Vision.md
- [x] Create docs/Architecture/System-Architecture.md
- [x] Create docs/Architecture/Development-Standards.md
- [x] Create docs/Database/Database-Conventions.md
- [x] Create docs/API/API-Standards.md
- [ ] Create docs/UI/Design-System.md
- [ ] Create docs/Decisions/ADR-001-project-foundation.md
- [ ] Create .clinerules
- [ ] Create README.md
- [ ] Add .gitkeep files to empty directories
- [ ] Verify structure and present results
</task_progress>
</｜DSML｜tool>