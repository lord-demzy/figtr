"""FIG3 Platform.

The FIG3 Platform is a modular, multi-product SaaS platform. It consists of:

- **FIG3 Core** — reusable platform services (identity, tenancy, permissions,
  branding, notifications, storage, configuration, registries, extensions).
- **FIG3 Edu** — the education product built on FIG3 Core.

FIG3 Core must not contain product-specific business logic. Products such as
FIG3 Edu live alongside Core and consume its services.
"""