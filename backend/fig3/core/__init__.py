"""FIG3 Core.

The reusable platform foundation for all FIG3 products. Contains
product-agnostic services organized into the following sub-packages:

- ``identity`` — users, accounts, authentication.
- ``tenancy`` — tenant models, context, isolation.
- ``permissions`` — roles, permissions, access control.
- ``branding`` — tenant theming and visual identity.
- ``notifications`` — email, SMS, in-app, push.
- ``storage`` — file uploads, object storage, media.
- ``configuration`` — settings, feature flags, tenant config.
- ``registry`` — product and module registries.
- ``extensions`` — extension points, hooks, plugins.

FIG3 Core must not contain any product-specific business logic.
"""