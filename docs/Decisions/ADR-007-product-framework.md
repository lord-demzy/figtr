# ADR-007: FIG3 Product Framework

- **Status:** Accepted
- **Date:** 2026-08-02
- **Deciders:** FIGTR Engineering Team

## Context

FIGTR needs a standardized way to represent, discover, and manage its products
(FIG3 Edu, FIG3 Legal, FIG3 Commerce, FIG3 HR) within the FIG3 Core platform.
Without a formal product framework, each product would define its own metadata,
navigation, permissions, and modules ad-hoc, leading to inconsistency and
platform integration bugs.

## Decision

We will introduce a **Product Framework** consisting of:

1. **Product Contract** — an abstract interface (`ProductContract`) that every
   product must implement.
2. **Product Registry** — a singleton registry (`ProductRegistry`) that
   discovers and manages installed products.
3. **Product Manifest** — per-product implementation of the contract (e.g.,
   `EduProductManifest`).
4. **Registration helpers** — convenience functions to register/unregister a
   product at startup.

## Rationale

- **Consistency** — All products declare identity, navigation, permissions,
  modules, and features through the same interface.
- **Discoverability** — The registry provides a single source of truth for
  installed products, enabling the platform to build dynamic navigation,
  permissions, and module toggles.
- **Extensibility** — New products can be added by implementing the contract
  and registering the manifest; no changes to FIG3 Core are required.
- **Separation of concerns** — Product-specific metadata lives in the product
  package, not in FIG3 Core.

## Architecture

### Files Created

- `backend/fig3/core/registry/contracts.py` — `ProductContract` abstract base class.
- `backend/fig3/core/registry/product_registry.py` — `ProductRegistry` singleton.
- `backend/fig3/edu/product.py` — `EduProductManifest` implementing the contract.
- `backend/fig3/edu/registry.py` — `register_edu()` / `unregister_edu()` helpers.

### Product Contract Methods

- `get_identity()` — code, name, version, description.
- `get_metadata()` — tenant type, branding, settings.
- `get_navigation()` — top-level navigation items and routes.
- `get_permissions()` — product-specific permissions.
- `get_modules()` — feature modules (enable/disable per tenant).
- `get_features()` — feature flags and capabilities.
- `validate()` — optional validation hook.

### Product Registry API

- `register(product)` — register a product implementing `ProductContract`.
- `unregister(code)` — remove a product by code.
- `get(code)` — retrieve a product by code.
- `all()` — return all registered products.
- `is_registered(code)` — check registration status.
- `clear()` — remove all products (testing).

## Consequences

### Benefits

- **Standardized product declarations** — Core and frontend can rely on a
  consistent shape for product metadata.
- **Runtime product discovery** — The platform can enumerate installed products
  without hardcoding.
- **Per-tenant module toggles** — Modules declared by a product can be
  enabled/disabled per tenant via configuration.
- **Feature flagging** — Products expose capabilities the platform can query.

### Trade-offs

- **Additional abstraction layer** — Products must implement the contract,
  adding a small amount of boilerplate. This is acceptable for the
  standardization benefits.
- **Registry as singleton** — Simplifies access but can complicate testing.
  A `clear()` method is provided for test cleanup.

### Risks

- **Contract drift** — Products may diverge from the contract over time.
  Mitigated by:
  - Clear docstrings and examples.
  - Type checking and tests.
  - Code reviews enforcing the boundary.

## Alternatives Considered

- **Per-product Django app configurations** — Rejected; Python packages with
  explicit manifests provide clearer boundaries.
- **Database-backed product registry** — Rejected; registry is platform-level
  and does not need persistence. It is populated at startup.
- **Decorator-based registration** — Rejected; explicit registration is simpler
  and more testable.

## Related

- ADR-006: FIG3 Platform Architecture
- ADR-004: Backend Foundation

## Extension Points for Future Products

To add a new product (e.g., FIG3 Legal):

1. Create `backend/fig3/legal/` package.
2. Implement `LegalProductManifest(ProductContract)` in `product.py`.
3. Call `ProductRegistry().register(LegalProductManifest())` at startup.
4. Declare modules and features as needed.

No changes to FIG3 Core are required.