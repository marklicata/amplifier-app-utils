"""Amplifier Foundation - Common library for building Amplifier applications.

This package provides a unified, high-level API for building applications on top
of the Amplifier AI development platform.
"""

from .key_manager import KeyManager
from .paths import PathManager, ScopeNotAvailableError, ScopeType, get_effective_scope, validate_scope_for_write
from .project_utils import get_project_slug
from .provider_sources import (
    DEFAULT_PROVIDER_SOURCES,
    get_effective_provider_sources,
    install_known_providers,
    is_local_path,
    source_from_uri,
)
from .session_store import SessionStore

__version__ = "0.1.0"

__all__ = [
    # Core path management
    "PathManager",
    "ScopeType",
    "ScopeNotAvailableError",
    "validate_scope_for_write",
    "get_effective_scope",
    # Provider sources
    "DEFAULT_PROVIDER_SOURCES",
    "get_effective_provider_sources",
    "install_known_providers",
    "is_local_path",
    "source_from_uri",
    # Session management
    "SessionStore",
    # Project utilities
    "get_project_slug",
    # Key management
    "KeyManager",
    # Version
    "__version__",
]
