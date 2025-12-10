# Amplifier Foundation

**Common library for building Amplifier applications**

A unified, high-level API that abstracts the complexity of the Amplifier AI platform. Build CLI, GUI, web APIs, and other applications with minimal boilerplate.

## 🎯 Purpose

Amplifier Foundation extracts the common infrastructure needed by all Amplifier applications:

- **Path Management** - Consistent directory structure and configuration paths
- **Provider Sources** - Canonical provider module sources and resolution
- **Session Management** - Persistence and recovery for conversational sessions
- **Key Management** - Secure API key storage
- **Mention Loading** - @mention system for referencing files/collections
- **Project Utilities** - Project detection and workspace management

Instead of:
```python
# 500+ lines of boilerplate across 5 dependencies...
```

You get:
```python
from amplifier_foundation import PathManager

pm = PathManager(app_name="my-app")
config = pm.create_config_manager()
# Done! Ready to build.
```

## 🚀 Quick Start

### Installation

```bash
pip install amplifier-foundation
```

### Build a Minimal App

```python
from amplifier_foundation import PathManager, SessionStore, KeyManager

# Setup
pm = PathManager(app_name="my-cool-app")
config = pm.create_config_manager()
profile_loader = pm.create_profile_loader()
session_store = SessionStore()
key_manager = KeyManager()

# Load a profile and run a session
profile = profile_loader.load("default")
session = AmplifierSession(config=config, profile=profile)
await session.initialize()

response = await session.execute("Hello!")
print(response)

# Save session for later
session_store.save(session.session_id, transcript, metadata)
```

## 📦 What's Included

### Core Components

| Component | Purpose | LOC |
|-----------|---------|-----|
| **PathManager** | Path resolution with dependency injection | 430 |
| **Mention Loading** | @mention system (models, resolver, loader, utils) | 220 |
| **Provider Sources** | Canonical provider sources & installation | 180 |
| **Session Store** | Atomic persistence with backup/recovery | 420 |
| **Key Manager** | Secure API key storage | 90 |
| **Project Utils** | Project slug generation | 30 |

**Total:** ~1,370 LOC + comprehensive tests

### Features

✅ **Zero Boilerplate** - One import, 5 lines to get started  
✅ **Dependency Injection** - PathManager provides factories for all core objects  
✅ **Battle-Tested** - Extracted from production CLI with 41 passing tests  
✅ **Type-Safe** - Full type hints with mypy compatibility  
✅ **Well-Documented** - Every module has comprehensive docstrings  
✅ **Cross-Platform** - Windows, macOS, Linux support

## 🏗️ Architecture

```
Your Application (CLI, GUI, API, etc.)
         ↓ uses
Amplifier Foundation (this library)
         ↓ orchestrates
Core Dependencies (abstracted)
  ├─ amplifier-core
  ├─ amplifier-config
  ├─ amplifier-module-resolution
  ├─ amplifier-collections
  └─ amplifier-profiles
```

The foundation handles all the complexity of coordinating these dependencies, providing a clean, stable API.

## 📚 Usage Examples

### Path Management

```python
from amplifier_foundation import PathManager

# Create with custom app name
pm = PathManager(app_name="my-app")

# Get configuration manager
config = pm.create_config_manager()

# Get profile loader
profile_loader = pm.create_profile_loader()

# Access paths directly
print(pm.workspace_dir)  # ~/.amplifier/
print(pm.config_paths.user)  # ~/.amplifier/settings.yaml
print(pm.session_dir)  # ~/.amplifier/projects/<slug>/sessions/
```

### Session Persistence

```python
from amplifier_foundation import SessionStore

store = SessionStore()

# Save a session
store.save(
    session_id="my-session",
    transcript=[{"role": "user", "content": "Hello"}],
    metadata={"created": "2024-01-01T00:00:00Z"}
)

# Load it back
transcript, metadata = store.load("my-session")

# List all sessions (sorted by mtime)
sessions = store.list_sessions()

# Cleanup old sessions
removed = store.cleanup_old_sessions(days=30)
```

### Provider Sources

```python
from amplifier_foundation import (
    DEFAULT_PROVIDER_SOURCES,
    get_effective_provider_sources,
    install_known_providers,
    source_from_uri,
)

# Get canonical sources
print(DEFAULT_PROVIDER_SOURCES["provider-anthropic"])
# => "git+https://github.com/microsoft/amplifier-module-provider-anthropic@main"

# Install all known providers
installed = install_known_providers(config_manager=config)

# Resolve a source (handles both git and local paths)
source = source_from_uri("git+https://github.com/user/repo@main")
module_path = source.resolve()
```

### Key Management

```python
from amplifier_foundation import KeyManager

km = KeyManager()

# Save API key (creates ~/.amplifier/keys.env)
km.save_key("ANTHROPIC_API_KEY", "sk-ant-...")

# Check if key exists
if km.has_key("ANTHROPIC_API_KEY"):
    print("Anthropic configured!")

# Auto-detect configured provider
provider = km.get_configured_provider()  # => "anthropic"
```

### Mention Loading

```python
from amplifier_foundation.mention_loading import (
    MentionResolver,
    ContentLoader,
    parse_mentions,
)

# Parse @mentions from text
mentions = parse_mentions("Check @README.md and @src/main.py")
# => ["README.md", "src/main.py"]

# Resolve paths
resolver = MentionResolver()
resolved = await resolver.resolve_path("README.md")

# Load content recursively
loader = ContentLoader(resolver=resolver)
content = await loader.load_mentions(mentions, max_depth=3)
```

## 🧪 Testing

Run the test suite:

```bash
git clone https://github.com/microsoft/amplifier-foundation
cd amplifier-foundation
uv sync
uv run pytest tests/ -v
```

**Current status:** 41 tests passing ✅

## 📖 Documentation

- **[IMPLEMENTATION_STATUS.md](IMPLEMENTATION_STATUS.md)** - Detailed implementation progress
- **[examples/](examples/)** - Working example applications
- **[docs/](docs/)** - Architecture diagrams and guides

## 🤝 Contributing

Contributions welcome! This library is extracted from production CLI code, so changes should maintain backward compatibility and high test coverage (>90%).

### Development Setup

```bash
git clone https://github.com/microsoft/amplifier-foundation
cd amplifier-foundation
uv sync --dev
uv run pytest tests/ -v
```

## 📋 Roadmap

**Phase 2 (Current):**
- [x] Provider sources
- [x] Session store  
- [x] Key manager
- [x] Project utils
- [ ] Provider manager (in progress)
- [ ] App settings helpers

**Phase 3:**
- [ ] Module manager
- [ ] Agent configuration
- [ ] Session spawner (agent delegation)

**Phase 4:**
- [ ] PyPI publication
- [ ] CI/CD pipeline
- [ ] Example applications

## 📄 License

MIT License - see [LICENSE](LICENSE)

## 🙏 Credits

Extracted from [amplifier-app-cli](https://github.com/microsoft/amplifier-app-cli) with contributions from the Amplifier team.

---

**Status:** Alpha - Active Development  
**Test Coverage:** 41 tests passing  
**Python:** 3.11+  
**Platform:** Windows, macOS, Linux
