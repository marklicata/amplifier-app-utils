# Amplifier Foundation

Common foundation library for building Amplifier applications.

## Overview

`amplifier-foundation` provides a unified, high-level API for building applications on top of the Amplifier AI development platform. It orchestrates and abstracts the complexity of core Amplifier dependencies:

- **amplifier-core** - Core agent and provider interfaces
- **amplifier-config** - Configuration system
- **amplifier-module-resolution** - Dynamic module loading
- **amplifier-collections** - Tool and capability collections
- **amplifier-profiles** - Agent profiles and presets

## Why Foundation?

Instead of requiring every Amplifier application to integrate 5+ dependencies and manage complex initialization logic, Foundation provides:

- ✅ **Single dependency** - Just add `amplifier-foundation`
- ✅ **Simple API** - High-level abstractions for common tasks
- ✅ **Managed complexity** - Path setup, config resolution, provider management handled for you
- ✅ **Flexibility** - Build CLI, GUI, web API, or embedded applications
- ✅ **Best practices** - Secure defaults, proper error handling, comprehensive logging

## Quick Start

### Installation

```bash
pip install amplifier-foundation
```

### Minimal Application

```python
from amplifier_foundation import AmplifierFoundation

# Initialize foundation with defaults
foundation = AmplifierFoundation()

# Get a configured agent
agent = foundation.create_agent(profile="default")

# Start interacting
response = await agent.run("Hello, world!")
print(response)
```

### With Custom Configuration

```python
from amplifier_foundation import AmplifierFoundation, FoundationConfig

config = FoundationConfig(
    app_name="my-app",
    user_dir="~/.my-app",
    enable_telemetry=False
)

foundation = AmplifierFoundation(config=config)
```

## Core Concepts

### Foundation Instance

The `AmplifierFoundation` class is your entry point. It manages:
- Path resolution (user dir, project dir, bundled data)
- Configuration loading and merging
- Provider registration and lifecycle
- Module system initialization
- Session persistence

### Scopes

Foundation organizes configuration and resources into scopes:
- **User scope** - User-wide settings (~/.amplifier/)
- **Project scope** - Project-specific settings (./amplifier/)
- **Bundled scope** - Read-only defaults shipped with your app

### Providers

Providers are the building blocks of agents (LLM, tools, memory, etc.). Foundation manages:
- Loading provider sources (collections, profiles, modules)
- Instantiating providers with resolved configuration
- Provider lifecycle (init, cleanup, health checks)
- Approval workflows and safety constraints

### Sessions

Foundation includes session management:
- Save/restore conversation history
- Track agent interactions
- Persist state across restarts
- Session metadata and indexing

## API Overview

### Core Classes

```python
from amplifier_foundation import (
    AmplifierFoundation,      # Main entry point
    FoundationConfig,         # Configuration
    PathManager,              # Path resolution
    ProviderManager,          # Provider lifecycle
    SessionStore,             # Session persistence
    SessionSpawner,           # Agent delegation
)
```

### Creating Agents

```python
# From a profile
agent = foundation.create_agent(profile="default")

# From custom config
agent = foundation.create_agent(config={
    "llm": {"provider": "openai", "model": "gpt-4"},
    "tools": ["web_search", "code_execution"]
})

# With session restoration
agent = foundation.create_agent(
    profile="default",
    session_id="previous-session-123"
)
```

### Working with Configuration

```python
# Get merged configuration for current context
config = foundation.get_effective_config()

# Get configuration for specific scope
user_config = foundation.get_config(scope="user")
project_config = foundation.get_config(scope="project")

# Update configuration
foundation.update_config(scope="user", key="llm.model", value="gpt-4")
```

### Managing Providers

```python
# List available providers
providers = foundation.list_providers()

# Get provider instance
llm = foundation.get_provider("openai")

# Check provider health
health = await foundation.check_provider_health("openai")
```

### Session Management

```python
# Save current session
session_id = await foundation.save_session(agent, metadata={"name": "My conversation"})

# List sessions
sessions = foundation.list_sessions()

# Load session
agent = foundation.restore_session(session_id)

# Delete session
foundation.delete_session(session_id)
```

## Architecture

```
┌─────────────────────────────────────────────┐
│          Your Application                   │
│  (CLI, GUI, Web API, Embedded, etc.)       │
└─────────────────┬───────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────┐
│      AmplifierFoundation                    │
│  ┌─────────────────────────────────────┐   │
│  │  PathManager                        │   │
│  │  - User dir, project dir, bundles   │   │
│  └─────────────────────────────────────┘   │
│  ┌─────────────────────────────────────┐   │
│  │  ConfigManager                      │   │
│  │  - Load, merge, resolve config      │   │
│  └─────────────────────────────────────┘   │
│  ┌─────────────────────────────────────┐   │
│  │  ProviderManager                    │   │
│  │  - Register, instantiate, manage    │   │
│  └─────────────────────────────────────┘   │
│  ┌─────────────────────────────────────┐   │
│  │  SessionStore                       │   │
│  │  - Save, load, list sessions        │   │
│  └─────────────────────────────────────┘   │
└─────────────────┬───────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────┐
│         Core Dependencies                   │
│  - amplifier-core                           │
│  - amplifier-config                         │
│  - amplifier-module-resolution              │
│  - amplifier-collections                    │
│  - amplifier-profiles                       │
└─────────────────────────────────────────────┘
```

## Examples

See the [examples](./examples/) directory for complete applications:

- **minimal_app.py** - Simplest possible app (<50 lines)
- **cli_app.py** - Basic command-line interface
- **repl_app.py** - Interactive REPL
- **gui_app.py** - Desktop GUI with Tkinter
- **web_api.py** - REST API with FastAPI
- **multi_agent.py** - Agent delegation and spawning

## Development

### Setup

```bash
git clone https://github.com/microsoft/amplifier-foundation
cd amplifier-foundation
uv venv
uv pip install -e ".[dev]"
```

### Testing

```bash
pytest
```

### Building

```bash
uv build
```

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines.

## License

MIT License - see [LICENSE](./LICENSE) for details.

## Support

- 📚 [Documentation](https://docs.amplifier.dev)
- 💬 [Discussions](https://github.com/microsoft/amplifier-foundation/discussions)
- 🐛 [Issues](https://github.com/microsoft/amplifier-foundation/issues)
- 📧 [Email](mailto:amplifier-support@microsoft.com)
