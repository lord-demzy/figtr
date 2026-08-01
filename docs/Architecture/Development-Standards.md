# FIGTR — Development Standards

## Purpose

This document defines the engineering standards and conventions that all FIGTR development must follow. These standards ensure consistency, maintainability, and quality across the codebase.

## General Principles

1. **Documentation First** — Read relevant documentation before writing code. Do not create features without a specification.
2. **Follow Existing Patterns** — Match the architecture and conventions already established in the codebase.
3. **Minimal Dependencies** — Do not introduce unnecessary dependencies. Every new dependency must be justified.
4. **Configuration via Environment** — Use environment variables for all configuration. Never hardcode secrets or environment-specific values.
5. **Separation of Concerns** — Keep backend business logic separated from views/controllers. Keep frontend components reusable.
6. **Test Everything** — Write tests for all new functionality.
7. **Focused Changes** — Do not modify unrelated files. Keep changes scoped to the task at hand.

## Code Style & Formatting

- Follow the language-specific style guides:
  - **Python (Django):** PEP 8, with Black for formatting and isort for import ordering.
  - **TypeScript/JavaScript (Next.js):** ESLint + Prettier with the project's shared config.
- Use meaningful, descriptive names for variables, functions, and classes.
- Keep functions small and focused on a single responsibility.

## Git Workflow

- **Branching:** Use feature branches off `main` (e.g., `feature/tenant-management`, `fix/attendance-bug`).
- **Commit Messages:** Use conventional commits format:
  - `feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `chore:`, `style:`.
- **Pull Requests:** Each PR must:
  - Reference the related issue/specification.
  - Include a clear description of changes.
  - Pass all CI checks (lint, tests, build).
  - Be reviewed before merging.

## Backend Standards (Django)

- **Project Structure:** Follow the modular app structure defined in the architecture docs.
- **Business Logic:** Place business logic in service/domain layer, not in views or serializers.
- **Views/Controllers:** Keep thin — delegate to services.
- **Models:** Define clear relationships, constraints, and indexes. Use migrations for schema changes.
- **API:** Follow the API standards in `docs/API/API-Standards.md`.
- **Validation:** Validate input at the serializer level; enforce business rules in services.

## Frontend Standards (Next.js)

- **Component Structure:** Reusable, composable components. Keep components small and focused.
- **State Management:** Use the project's chosen state management approach consistently.
- **Styling:** Follow the design system in `docs/UI/Design-System.md`.
- **Data Fetching:** All data via the API layer; no direct database access.
- **Accessibility:** Ensure components are accessible (semantic HTML, ARIA where needed).

## Database Standards

- Follow the conventions in `docs/Database/Database-Conventions.md`.
- All schema changes via migrations.
- Never write raw SQL unless necessary and approved.

## API Standards

- Follow the conventions in `docs/API/API-Standards.md`.
- All endpoints must be versioned.
- Consistent error handling and response formats.

## Security Standards

- Never hardcode secrets, API keys, or credentials.
- Use environment variables or a secret manager.
- Validate and sanitize all user input.
- Enforce tenant isolation at the data-access layer.
- Use parameterized queries / ORM to prevent SQL injection.

## Documentation Standards

- Update relevant documentation when behavior changes.
- New features must be documented before or alongside implementation.
- Use ADRs (`docs/Decisions/`) to record significant architectural decisions.

## Definition of Done

A task is considered complete when:

- [ ] Code is implemented per the specification.
- [ ] Tests are written and passing.
- [ ] Code follows the project's style and conventions.
- [ ] Documentation is updated if needed.
- [ ] No unrelated files were modified.
- [ ] Changes are explained to the team.

---

*This document is a living artifact and will be updated as the project evolves.*