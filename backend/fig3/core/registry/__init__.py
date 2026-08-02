"""FIG3 Core — Registry.

Platform-level registry services: product registry and module registry.
This package is product-agnostic and must not contain school-specific logic.
"""

from fig3.core.registry.contracts import ProductContract
from fig3.core.registry.product_registry import ProductRegistry

__all__ = ["ProductContract", "ProductRegistry"]
