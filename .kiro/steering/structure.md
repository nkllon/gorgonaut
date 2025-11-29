# Project Structure - Gorgonaut

## Directory Organization

### Root Level
```
/
├── .cursor/          # Cursor IDE configuration and commands
├── .devcontainer/    # Development container configuration
├── .github/          # GitHub workflows and templates
├── .kiro/            # Kiro spec-driven development
│   ├── specs/        # Feature specifications
│   ├── steering/     # Project-wide guidance
│   └── settings/     # Kiro settings and templates
├── docs/             # Documentation
├── js/               # JavaScript/TypeScript workspace
├── python/           # Python package
├── specs/            # Specifications (ontology, API)
├── .dockerignore     # Docker ignore patterns
├── .gitignore        # Git ignore patterns
├── AGENTS.md         # AI agent development guidelines
├── Makefile          # Common development tasks
└── docker-compose.yml # Container orchestration
```

### Dev Container Conventions
- Configuration lives in `.devcontainer/devcontainer.json`; optional `postCreate.sh` provisions dependencies.
- Features pin: Node 20, Python 3.12, common-utils.
- Post-create: run `make install` (JS npm install; Python `uv sync --extra dev`), fallback to pip if uv unavailable.
- Ports forwarded: 5173 (Vite), 3000 (Web), 8000 (Python); set Codespaces visibility as needed.
- Codespaces defaults: prefer 2-core machine; document idle-stop/retention and stop/delete guidance.
- Secrets: use platform secret stores; never commit `.env` or credentials.
## Python Package (`python/`)

### Structure
```
python/
├── src/
│   └── gorgonaut/
│       ├── __init__.py           # Package initialization
│       ├── config.py             # Configuration management
│       ├── tools/                # CLI tools and utilities
│       │   ├── validate_openapi.py
│       │   └── validate_shacl.py
│       ├── ontology/             # (Future) Ontology loading and querying
│       ├── engine/               # (Future) Expert system engines
│       │   ├── context.py        # Context engine
│       │   ├── synthesis.py     # Tool synthesis engine
│       │   ├── decision.py      # Decision/action layer
│       │   └── capability.py    # Capability building layer
│       └── api/                  # (Future) API implementation
├── tests/                        # Test files (mirror src structure)
├── pyproject.toml                # Package configuration
└── README.md                     # Python package documentation
```

### Naming Conventions
- **Modules**: lowercase with underscores (`context_engine.py`)
- **Classes**: PascalCase (`ContextEngine`, `ToolSynthesizer`)
- **Functions**: lowercase with underscores (`load_ontology`, `query_tools`)
- **Constants**: UPPERCASE with underscores (`DEFAULT_TIMEOUT`, `MAX_RESULTS`)
- **Private**: prefix with underscore (`_internal_helper`)

## JavaScript Workspace (`js/`)

### Structure
```
js/
├── apps/                         # Applications
│   └── web/                      # Web application
│       ├── src/
│       │   ├── main.tsx          # Entry point
│       │   ├── components/       # React components
│       │   ├── pages/            # Page components
│       │   ├── hooks/            # Custom React hooks
│       │   ├── services/         # API clients
│       │   ├── types/            # TypeScript types
│       │   └── utils/            # Utility functions
│       ├── public/               # Static assets
│       ├── package.json
│       └── vite.config.ts
├── packages/                     # Shared libraries
│   └── lib/                      # Shared library
│       ├── src/
│       │   ├── index.ts          # Library entry point
│       │   ├── ontology/         # Ontology client utilities
│       │   ├── types/            # Shared TypeScript types
│       │   └── utils/            # Shared utilities
│       └── package.json
├── .eslintrc.json                # ESLint configuration
├── .prettierrc.json              # Prettier configuration
├── package.json                  # Workspace root package.json
├── tsconfig.base.json            # Base TypeScript configuration
└── README.md                     # JavaScript workspace documentation
```

### Naming Conventions
- **Components**: PascalCase (`ToolCard.tsx`, `SearchBar.tsx`)
- **Hooks**: camelCase with `use` prefix (`useToolSearch.ts`, `useOntology.ts`)
- **Utilities**: camelCase (`formatDate.ts`, `parseQuery.ts`)
- **Types**: PascalCase (`Tool`, `MetaSkill`, `SearchResult`)
- **Constants**: UPPERCASE with underscores (`API_BASE_URL`, `MAX_RESULTS`)

## Specifications (`specs/`)

### Structure
```
specs/
├── api/
│   └── openapi.yaml              # OpenAPI specification
└── ontology/
    ├── gorgonaut-mindtools.ttl   # OWL ontology
    ├── gorgonaut-mindtools-shacl.ttl # SHACL validation shapes
    └── data/
        ├── examples.ttl          # Example instances
        ├── mindtools/            # (Future) Mind Tools data
        │   ├── creativity.ttl    # Creativity tools
        │   ├── decision-making.ttl
        │   └── project-management.ttl
        └── stakeholders/         # (Future) Stakeholder data
```

### Ontology Conventions
- **Prefix**: `gorgo:` or `:` for `http://example.org/gorgonaut#`
- **Classes**: PascalCase (`:Tool`, `:MetaSkill`)
- **Properties**: camelCase (`:hasName`, `:addressesProblem`)
- **Instances**: kebab-case (`:scamper-technique`, `:swot-analysis`)
- **Files**: kebab-case with `.ttl` extension

## Documentation (`docs/`)

### Structure
```
docs/
├── architecture/                 # Architecture documentation
│   ├── ontology-overview.md
│   ├── expert-system.md
│   └── api-design.md
├── guides/                       # User and developer guides
│   ├── getting-started.md
│   ├── ontology-guide.md
│   └── api-guide.md
└── research/                     # Research and references
    ├── mind-tools-analysis.md
    └── related-systems.md
```

## Kiro Specs (`.kiro/specs/`)

### Structure
```
.kiro/specs/
├── ontology-population/          # Spec for populating ontology data
│   ├── requirements.md
│   ├── design.md
│   ├── tasks.md
│   └── spec.json
├── expert-system/                # Spec for expert system implementation
│   ├── requirements.md
│   ├── design.md
│   ├── tasks.md
│   └── spec.json
├── tool-recommendation-api/      # Spec for recommendation API
│   ├── requirements.md
│   ├── design.md
│   ├── tasks.md
│   └── spec.json
└── web-ui/                       # Spec for web interface
    ├── requirements.md
    ├── design.md
    ├── tasks.md
    └── spec.json
```

### Spec Naming
- Use kebab-case for spec directories
- Keep names concise but descriptive
- Align with feature/component names

## File Naming Patterns

### Python
- Test files: `test_<module>.py` (e.g., `test_context_engine.py`)
- Config files: `<name>_config.py` or `config.py`
- CLI tools: `<action>_<target>.py` (e.g., `validate_shacl.py`)

### TypeScript/React
- Components: `<ComponentName>.tsx`
- Hooks: `use<HookName>.ts`
- Types: `<name>.types.ts` or `types.ts`
- Tests: `<name>.test.ts` or `<name>.test.tsx`
- Styles: `<name>.module.css` (CSS modules)

### Configuration
- Python: `pyproject.toml` (modern standard)
- JavaScript: `package.json`, `tsconfig.json`, `vite.config.ts`
- Docker: `Dockerfile`, `docker-compose.yml`, `.dockerignore`
- Git: `.gitignore`, `.gitattributes`

## Import Organization

### Python
```python
# Standard library
import os
from pathlib import Path

# Third-party
from rdflib import Graph
import pytest

# Local
from gorgonaut.config import AppConfig
from gorgonaut.ontology import load_graph
```

### TypeScript
```typescript
// React and external libraries
import React from 'react';
import { useQuery } from '@tanstack/react-query';

// Internal packages
import { Tool, MetaSkill } from '@gorgonaut/lib';

// Local imports
import { ToolCard } from './components/ToolCard';
import { useToolSearch } from './hooks/useToolSearch';
```

## Code Organization Principles

1. **Separation of Concerns** - Each module has a single, well-defined responsibility
2. **Dependency Direction** - Dependencies flow inward (UI → Services → Core)
3. **Testability** - Code structured to facilitate unit and integration testing
4. **Discoverability** - Logical grouping and consistent naming for easy navigation
5. **Scalability** - Structure supports growth without major refactoring

## Common Patterns

### Python Module Structure
```python
"""Module docstring explaining purpose."""

# Imports
from typing import Optional

# Constants
DEFAULT_VALUE = 42

# Type definitions
class MyClass:
    """Class docstring."""
    pass

# Functions
def my_function() -> None:
    """Function docstring."""
    pass

# Main execution
if __name__ == "__main__":
    pass
```

### React Component Structure
```typescript
// Imports
import React from 'react';

// Types
interface Props {
  title: string;
}

// Component
export function MyComponent({ title }: Props) {
  // Hooks
  // Event handlers
  // Render
  return <div>{title}</div>;
}
```

## Build Artifacts

### Ignored Patterns
- Python: `__pycache__/`, `*.pyc`, `.pytest_cache/`, `dist/`, `*.egg-info/`
- JavaScript: `node_modules/`, `dist/`, `build/`, `.vite/`
- IDE: `.vscode/`, `.idea/`, `*.swp`
- Environment: `.env`, `.env.local`
- OS: `.DS_Store`, `Thumbs.db`

### Generated Files
- Python: `dist/` (built packages)
- JavaScript: `dist/`, `build/` (compiled output)
- Documentation: `docs/_build/` (generated docs)
