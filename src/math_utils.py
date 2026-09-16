"""Math utility functions.

Provides simple arithmetic helper functions for addition and multiplication.
"""

from __future__ import annotations

__all__ = ["add", "multiply"]

def add(a: int, b: int) -> int:
    """Return the sum of *a* and *b*.

    Args:
        a: First integer.
        b: Second integer.

    Returns:
        The arithmetic sum of ``a`` and ``b``.
    """
    return a + b

def multiply(a: int, b: int) -> int:
    """Return the product of *a* and *b*.

    Args:
        a: First integer.
        b: Second integer.

    Returns:
        The arithmetic product of ``a`` and ``b``.
    """
    return a * b
