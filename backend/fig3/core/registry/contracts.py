"""FIG3 Core — Product Contract.

Defines the interface that every FIG3 product must implement.
This contract ensures consistency across all products (FIG3 Edu, FIG3 Legal, etc.)
and enables the Product Registry to discover and manage products uniformly.

No product-specific logic is allowed here.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class ProductContract(ABC):
    """Abstract base class that all FIG3 products must implement.

    A 'product' in FIG3 terminology is a self-contained business domain
    (e.g., Education, Legal, Commerce, HR) that plugs into the FIG3 Core
    platform. Each product declares its identity, metadata, navigation,
    permissions, modules, and features through this contract.
    """

    @abstractmethod
    def get_identity(self) -> dict[str, Any]:
        """Return the product's core identity.

        Example:
            {
                "code": "edu",
                "name": "FIG3 Edu",
                "version": "1.0.0",
                "description": "Education management platform",
            }
        """
        raise NotImplementedError

    @abstractmethod
    def get_metadata(self) -> dict[str, Any]:
        """Return extended product metadata.

        Should include tenant type, branding references, and any
        platform-level configuration the product requires.
        """
        raise NotImplementedError

    @abstractmethod
    def get_navigation(self) -> list[dict[str, Any]]:
        """Return navigation items exposed by this product.

        Each item should include at least a label and a URL or route name.
        Example:
            [
                {"label": "Dashboard", "route": "edu:dashboard"},
                {"label": "Students", "route": "edu:student-list"},
            ]
        """
        raise NotImplementedError

    @abstractmethod
    def get_permissions(self) -> list[dict[str, Any]]:
        """Return permissions defined by this product.

        Each permission entry should include a codename and human-readable name.
        Example:
            [
                {"codename": "view_student", "name": "Can view student"},
                {"codename": "add_student", "name": "Can add student"},
            ]
        """
        raise NotImplementedError

    @abstractmethod
    def get_modules(self) -> list[dict[str, Any]]:
        """Return sub-modules or feature modules declared by this product.

        Example:
            [
                {"code": "students", "name": "Student Management", "enabled": True},
                {"code": "admissions", "name": "Admissions", "enabled": False},
            ]
        """
        raise NotImplementedError

    @abstractmethod
    def get_features(self) -> list[dict[str, Any]]:
        """Return feature flags or capabilities exposed by this product.

        Example:
            [
                {"code": "online_exams", "name": "Online Exams", "enabled": True},
            ]
        """
        raise NotImplementedError

    def validate(self) -> bool:
        """Optional validation hook called during registration.

        Return True if the product is valid and ready to be registered.
        Raise ValueError with a descriptive message if invalid.
        """
        return True