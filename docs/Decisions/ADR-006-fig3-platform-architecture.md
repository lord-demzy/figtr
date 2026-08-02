# ADR-006: FIG3 Platform Architecture

- **Status:** Accepted
- **Date:** 2026-08-02
- **Deciders:** FIGTR Engineering Team

## Context

FIGTR was initially architected as a single-application Django project with a `core` app for shared functionality and an `apps/` directory for future business domains. While this structure served the initial foundation, it does not support FIGTR's long-term vision of becoming a multi-product SaaS platform.

The product vision requires:
- A reusable platform foundation (FIG3 Core) that serves all FIG3 products.
- Clear separation between platform services and product-specific business logic.
- Support for future products (FIG3 Legal, FIG3 Commerce, FIG3 HR) without architectural changes.
- FIG3 Edu as the first product built on top of the FIG3 Platform.

## Decision

We will refactor the backend architecture to establish the FIG3 Platform with the following structure:

### Package Structure

```
backend/
├── config/              # Django project configuration
├── fig3/                # FIG3 Platform root package
│   ├── __init__.py
│   ├── core/            # FIG3 Core — reusable platform foundation
│   │   ├── __init__.py
│   │   ├── apps.py
│   │   ├── urls.py
│   │   ├── views.py     # Health check
│   │   ├── tests.py
│   │   ├── utils.py
│   │   ├── exceptions.py
│   │   ├── identity/    # Users, accounts, auth
│   │   ├── tenancy/     # Tenant models, context, isolation
│   │   ├── permissions/ # Roles, permissions, access control
│   │   ├── branding/    # Tenant theming, visual identity
│   │   ├── notifications/ # Email, SMS, in-app, push
│   │   ├── storage/     # File uploads, object storage, media
│   │   ├── configuration/ # Settings, feature flags
│   │   ├── registry/    # Product and module registries
│   │   └── extensions/  # Extension points, hooks, plugins
│   └── edu/             # FIG3 Edu — education product
│       ├── __init__.py
│       ├── apps.py
│       ├── urls.py      # Future
│       ├── views.py     # Future
│       ├── tests.py     # Future
│       └── ...          # Education-specific modules
├── tests/
└── requirements/
```

### Key Architectural Principles

1. **FIG3 Core** — Product-agnostic platform foundation:
   - Contains reusable services used by all FIG3 products.
   - Must not contain school-specific, legal-specific, or any product-specific business logic.
   - Organized into 10 sub-packages covering identity, tenancy, permissions, branding, notifications, storage, configuration, registry, and extensions.

2. **FIG3 Edu** — Education product:
   - Contains all education-specific business logic and modules.
   - Consumes services from FIG3 Core.
   - Lives alongside FIG3 Core in the `fig3/` package.

3. **Future Products** — FIG3 Legal, FIG3 Commerce, FIG3 HR:
   - Will live alongside FIG3 Core and FIG3 Edu in the `fig3/` package.
   - Will consume services from FIG3 Core.
   - No code written for them now; architecture allows easy addition.

4. **Existing Functionality**:
   - Health check endpoint (`GET /api/health/`) preserved.
   - Shared utilities and exceptions preserved.
   - Existing tests preserved.
   - All existing APIs and behavior maintained.

## Reason

This architecture supports FIGTR's long-term goals because:

- **Modular platform design** — FIG3 Core provides a reusable foundation that all products share, reducing duplication and ensuring consistency.
- **Clear separation of concerns** — Platform services (FIG3 Core) are strictly separated from product logic (FIG3 Edu), making the codebase easier to maintain and test.
- **Scalability** — New products can be added to the `fig3/` package without modifying FIG3 Core. Each product is self-contained but shares platform services.
- **Preservation of existing functionality** — No breaking changes to existing APIs or behavior. The health check, utilities, and exceptions remain functional.
- **Alignment with product vision** — The architecture directly supports the goal of FIGTR as a multi-product SaaS platform.

## Consequences

### Benefits

- **Reusable platform** — FIG3 Core services (identity, tenancy, permissions, etc.) can be reused across all FIG3 products.
- **Clean separation** — Product-specific logic is isolated in product packages (e.g., `fig3.edu`), making it easier to understand, test, and evolve.
- **Future-proof** — Adding FIG3 Legal, FIG3 Commerce, or FIG3 HR requires only creating a new product package alongside FIG3 Core.
- **Maintainable** — Platform concerns are centralized in FIG3 Core, reducing duplication and ensuring consistent behavior across products.
- **No functional changes** — Existing functionality (health check, tests, settings) continues to work without modification.

### Trade-offs

- **Increased package depth** — The new structure introduces more nested directories, which may feel verbose for small projects. This is acceptable because FIGTR is expected to grow significantly.
- **Migration overhead** — Moving files from `core/` to `fig3/core/` requires updating imports and settings. This is a one-time cost with long-term benefits.
- **Learning curve** — New developers must understand the FIG3 Core / FIG3 Edu split. This is mitigated by clear documentation and docstrings in each package.

### Risks

- **Import errors during migration** — Mitigated by carefully updating all import paths in views, urls, and settings, and verifying with tests.
- **Breaking changes to external references** — Mitigated by preserving all existing API endpoints and behavior. The health check remains at `/api/health/`.
- **FIG3 Core contamination** — Risk of product-specific logic creeping into FIG3 Core. Mitigated by:
  - Clear docstrings in each sub-package stating "must not contain school-specific logic."
  - Code reviews enforcing the boundary.
  - Architectural tests verifying no product-specific imports in FIG3 Core.

## Alternatives Considered

- **Keep existing `core/` app structure** — Rejected; does not support multi-product vision and mixes platform and product concerns.
- **Use Django app configurations to simulate products** — Rejected; Python packages provide clearer boundaries and are more scalable.
- **Create FIG3 Core as a separate Django project** — Rejected; FIG3 Core and FIG3 Edu must share the same database and settings, so a single project with packages is more appropriate.
- **Implement all 10 sub-packages now** — Rejected; sub-packages are created as placeholders with clear docstrings. Actual implementation will happen in future prompts when needed.

## Related

- ADR-001: Project Foundation
- ADR-002: System Architecture
- ADR-003: Database Design
- ADR-004: Backend Foundation
- ADR-005: Frontend Foundation

## Migration Notes

### Files Moved

- `backend/core/__init__.py` → `backend/fig3/core/__init__.py`
- `backend/core/apps.py` → `backend/fig3/core/apps.py`
- `backend/core/views.py` → `backend/fig3/core/views.py`
- `backend/core/urls.py` → `backend/fig3/core/urls.py`
- `backend/core/tests.py` → `backend/fig3/core/tests.py`
- `backend/core/utils.py` → `backend/fig3/core/utils.py`
- `backend/core/exceptions.py` → `backend/fig3/core/exceptions.py`
- `backend/apps/` (directory) → removed (empty)

### Files Created

- `backend/fig3/__init__.py`
- `backend/fig3/edu/__init__.py`
- `backend/fig3/edu/apps.py`
- `backend/fig3/core/identity/__init__.py`
- `backend/fig3/core/tenancy/__init__.py`
- `backend/fig3/core/permissions/__init__.py`
- `backend/fig3/core/branding/__init__.py`
- `backend/fig3/core/notifications/__init__.py`
- `backend/fig3/core/storage/__init__.py`
- `backend/fig3/core/configuration/__init__.py`
- `backend/fig3/core/registry/__init__.py`
- `backend/fig3/core/extensions/__init__.py`

### Configuration Changes

- `backend/config/settings/base.py` — Updated `LOCAL_APPS` to reference `fig3.core` and `fig3.edu`.
- `backend/config/urls.py` — Updated to include `fig3.core.urls`.
- `backend/pyproject.toml` — Updated pytest coverage path to `fig3/core`.
- `backend/fig3/core/apps.py` — Updated `name` to `fig3.core` and `label` to `fig3_core`.
- `backend/fig3/core/urls.py` — Updated import from `core.views` to `fig3.core.views`.