"""FIG3 Edu — Product Registry Integration.

Provides helpers to register FIG3 Edu with the FIG3 Core Product Registry.
This module ensures the product is discoverable by the platform at startup.
"""

from __future__ import annotations

from fig3.core.registry import ProductRegistry
from fig3.edu.product import EduProductManifest


def register_edu() -> None:
    """Register FIG3 Edu with the global Product Registry."""
    registry = ProductRegistry()
    manifest = EduProductManifest()
    registry.register(manifest)


def unregister_edu() -> None:
    """Unregister FIG3 Edu from the global Product Registry."""
    registry = ProductRegistry()
    try:
        registry.unregister("edu")
    except KeyError:
        pass