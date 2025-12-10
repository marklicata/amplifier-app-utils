"""Amplifier Foundation - Common library for building Amplifier applications.

This package provides a unified, high-level API for building applications on top
of the Amplifier AI development platform.
"""

from .paths import PathManager, ScopeNotAvailableError, ScopeType, get_effective_scope, validate_scope_for_write

__version__ = "0.1.0"

__all__ = [
    "PathManager",
    "ScopeType",
    "ScopeNotAvailableError",
    "validate_scope_for_write",
    "get_effective_scope",
    "__version__",
]
