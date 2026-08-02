"""FIG3 Core — Product Registry.

Central registry for discovering, registering, and managing FIG3 products.
The registry is product-agnostic and enforces the Product Contract.
"""

from __future__ import annotations

from typing import Any

from fig3.core.registry.contracts import ProductContract


class ProductRegistry:
    """Singleton registry that holds all registered FIG3 products.

    Usage:
        registry = ProductRegistry()
        registry.register(my_product)  # ProductContract instance
        product = registry.get("edu")
        all_products = registry.all()
    """

    _instance: ProductRegistry | None = None

    def __new__(cls) -> ProductRegistry:
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._products: dict[str, ProductContract] = {}
            cls._instance._initialized = False
        return cls._instance

    def register(self, product: ProductContract) -> None:
        """Register a product with the registry.

        Args:
            product: An instance implementing ProductContract.

        Raises:
            TypeError: If product does not implement ProductContract.
            ValueError: If a product with the same code is already registered.
        """
        if not isinstance(product, ProductContract):
            raise TypeError(
                f"Product must implement ProductContract. Got {type(product).__name__}"
            )

        identity = product.get_identity()
        code = identity.get("code")

        if not code:
            raise ValueError("Product identity must include a 'code' field.")

        if code in self._products:
            raise ValueError(
                f"Product with code '{code}' is already registered."
            )

        if not product.validate():
            raise ValueError(
                f"Product '{code}' failed validation and was not registered."
            )

        self._products[code] = product

    def unregister(self, code: str) -> None:
        """Remove a product from the registry.

        Args:
            code: Product code to remove.

        Raises:
            KeyError: If product is not registered.
        """
        if code not in self._products:
            raise KeyError(f"Product '{code}' is not registered.")
        del self._products[code]

    def get(self, code: str) -> ProductContract:
        """Retrieve a registered product by code.

        Args:
            code: Product code.

        Returns:
            The registered ProductContract instance.

        Raises:
            KeyError: If product is not registered.
        """
        if code not in self._products:
            raise KeyError(f"Product '{code}' is not registered.")
        return self._products[code]

    def all(self) -> dict[str, ProductContract]:
        """Return all registered products as a dict keyed by code."""
        return dict(self._products)

    def is_registered(self, code: str) -> bool:
        """Check whether a product is registered."""
        return code in self._products

    def clear(self) -> None:
        """Remove all registered products (useful for testing)."""
        self._products.clear()