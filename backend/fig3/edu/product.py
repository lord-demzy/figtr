"""FIG3 Edu — Product Manifest.

Implements the ProductContract to declare FIG3 Edu's identity, metadata,
navigation, permissions, modules, and features to the FIG3 Core platform.
"""

from __future__ import annotations

from typing import Any

from fig3.core.registry.contracts import ProductContract


class EduProductManifest(ProductContract):
    """Product manifest for FIG3 Edu.

    This class is the single source of truth for FIG3 Edu's platform-level
    declarations. Core and other platform services consume this manifest
    to discover and integrate with the product.
    """

    def get_identity(self) -> dict[str, Any]:
        """Return FIG3 Edu's core identity."""
        return {
            "code": "edu",
            "name": "FIG3 Edu",
            "version": "1.0.0",
            "description": "Education management platform for schools",
        }

    def get_metadata(self) -> dict[str, Any]:
        """Return FIG3 Edu's extended metadata."""
        return {
            "tenant_type": "school",
            "branding": {
                "logo": "fig3/edu/branding/logo.png",
                "primary_color": "#2563eb",
                "accent_color": "#0ea5e9",
            },
            "settings": {
                "max_students_per_tenant": 5000,
                "supports_multi_campus": True,
            },
        }

    def get_navigation(self) -> list[dict[str, Any]]:
        """Return top-level navigation items for FIG3 Edu.

        Actual routes will be implemented in future prompts.
        """
        return [
            {"label": "Dashboard", "route": "edu:dashboard", "icon": "layout-dashboard"},
            {"label": "Students", "route": "edu:student-list", "icon": "users"},
            {"label": "Academics", "route": "edu:academics", "icon": "book-open"},
            {"label": "Finance", "route": "edu:finance", "icon": "credit-card"},
            {"label": "Settings", "route": "edu:settings", "icon": "settings"},
        ]

    def get_permissions(self) -> list[dict[str, Any]]:
        """Return permissions defined by FIG3 Edu.

        These are education-specific permissions managed by FIG3 Core's
        permission system.
        """
        return [
            {"codename": "view_student", "name": "Can view student"},
            {"codename": "add_student", "name": "Can add student"},
            {"codename": "change_student", "name": "Can change student"},
            {"codename": "delete_student", "name": "Can delete student"},
            {"codename": "view_teacher", "name": "Can view teacher"},
            {"codename": "manage_admissions", "name": "Can manage admissions"},
            {"codename": "manage_finance", "name": "Can manage finance"},
            {"codename": "view_reports", "name": "Can view reports"},
            {"codename": "manage_timetable", "name": "Can manage timetable"},
            {"codename": "manage_examinations", "name": "Can manage examinations"},
        ]

    def get_modules(self) -> list[dict[str, Any]]:
        """Return feature modules declared by FIG3 Edu.

        Modules are top-level feature domains. They can be enabled/disabled
        per tenant via configuration.
        """
        return [
            {"code": "students", "name": "Student Management", "enabled": True},
            {"code": "teachers", "name": "Teacher Management", "enabled": True},
            {"code": "academics", "name": "Academics", "enabled": True},
            {"code": "admissions", "name": "Admissions", "enabled": False},
            {"code": "finance", "name": "Finance & Billing", "enabled": False},
            {"code": "examinations", "name": "Examinations", "enabled": False},
            {"code": "timetable", "name": "Timetable", "enabled": False},
            {"code": "reports", "name": "Reports & Analytics", "enabled": False},
            {"code": "communication", "name": "Communication", "enabled": False},
            {"code": "library", "name": "Library", "enabled": False},
        ]

    def get_features(self) -> list[dict[str, Any]]:
        """Return feature flags or capabilities exposed by FIG3 Edu."""
        return [
            {
                "code": "multi_campus",
                "name": "Multi-Campus Support",
                "enabled": True,
                "description": "Allow a single tenant to manage multiple campuses",
            },
            {
                "code": "online_admissions",
                "name": "Online Admissions",
                "enabled": False,
                "description": "Enable online student application and admission workflow",
            },
            {
                "code": "parent_portal",
                "name": "Parent Portal",
                "enabled": False,
                "description": "Self-service portal for parents",
            },
            {
                "code": "mobile_app",
                "name": "Mobile App Integration",
                "enabled": False,
                "description": "Support for native mobile applications",
            },
        ]

    def validate(self) -> bool:
        """Validate that the manifest is well-formed."""
        identity = self.get_identity()
        required_fields = ["code", "name", "version", "description"]
        for field in required_fields:
            if field not in identity or not identity[field]:
                raise ValueError(
                    f"Product identity missing required field: {field}"
                )
        return True