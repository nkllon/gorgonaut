# Technical Architecture - Gorgonaut

## Technology Stack

### Backend (Python)
- **Language**: Python 3.10+
- **Package Manager**: uv (modern, fast Python package management)
- **Core Libraries**:
  - `rdflib` - RDF graph manipulation and SPARQL queries
  - `pyshacl` - SHACL validation for ontology data
  - `openapi-spec-validator` - API specification validation
  - `python-dotenv` - Environment configuration
  - `graphviz`, `pydot` - Graph visualization

### Frontend (JavaScript/TypeScript)
- **Language**: TypeScript 5.6+
- **Framework**: React 18
- **Build Tool**: Vite 5
- **Package Manager**: npm 10
- **Workspace Structure**: Monorepo with apps/ and packages/

### Semantic Web & Ontology
- **Format**: OWL 2 (Web Ontology Language) in Turtle syntax
- **Validation**: SHACL (Shapes Constraint Language)
- **Query Language**: SPARQL (for graph queries)
- **Namespace**: `http://example.org/gorgonaut#`

### API
- **Specification**: OpenAPI 3.0.3
- **Format**: YAML
- **Validation**: Automated via openapi-spec-validator

### Development Tools
- **Python Linting**: ruff, black
- **Python Type Checking**: mypy (strict mode)
- **Python Testing**: pytest
- **JS Linting**: ESLint
- **JS Formatting**: Prettier
- **Containerization**: Docker, docker-compose
- **Dev Environment**: devcontainer support

## Architecture Patterns

### Monorepo Structure
```
/
├── python/          # Python package (backend, tools, validation)
├── js/              # JavaScript workspace (frontend, shared libs)
├── specs/           # Specifications (ontology, API)
├── docs/            # Documentation
└── .kiro/           # Kiro spec-driven development
```

### Separation of Concerns
1. **Ontology Layer** (`specs/ontology/`) - Pure knowledge representation
2. **Validation Layer** (`python/src/gorgonaut/tools/`) - Data quality enforcement
3. **Business Logic** (to be implemented) - Expert system reasoning
4. **API Layer** (to be implemented) - RESTful interface
5. **Presentation Layer** (`js/apps/web/`) - User interface

### Data Flow
```
User Input → Context Engine → Tool Synthesis → Decision/Action → User Output
                ↓                    ↓              ↓
            Ontology Query ← SPARQL Reasoning → Capability Tracking
```

## Code Quality Standards

### Python
- Line length: 100 characters
- Type hints required (mypy strict mode)
- Docstrings for all public functions/classes
- Test coverage target: 80%+
- No untyped definitions allowed

### TypeScript
- Strict mode enabled
- Explicit return types for functions
- No `any` types without justification
- Component-based architecture for React

### Ontology
- All classes must have `rdfs:label` and `rdfs:comment`
- SHACL shapes for all critical constraints
- Consistent naming conventions (CamelCase for classes, camelCase for properties)
- Disjointness declarations for top-level classes

## Testing Strategy

### Python
- **Unit Tests**: pytest for individual functions/classes
- **Integration Tests**: Validate ontology loading and SPARQL queries
- **Validation Tests**: Ensure SHACL and OpenAPI specs pass
- **Property-Based Tests**: Use Hypothesis for complex logic

### JavaScript
- **Unit Tests**: Vitest for components and utilities
- **Component Tests**: React Testing Library
- **E2E Tests**: Playwright (when UI is mature)

### Ontology
- **SHACL Validation**: Automated via validate_shacl.py
- **Consistency Checks**: OWL reasoning to detect contradictions
- **Example Data**: Maintain examples.ttl with valid instances

## Configuration Management

### Environment Variables
- `APP_ENV` - Environment (development, staging, production)
- `LOG_LEVEL` - Logging verbosity (DEBUG, INFO, WARNING, ERROR)
- `OPENAPI_SPEC_PATH` - Path to OpenAPI specification

### Secrets Management
- 1Password CLI integration for sensitive credentials
- Never commit secrets to repository
- Use `.env` files for local development (gitignored)

## Development Workflow

### Spec-Driven Development
1. Requirements gathering (EARS format)
2. Design with correctness properties
3. Task breakdown with property-based tests
4. Implementation with continuous validation
5. Review and iteration

### Version Control
- Feature branches for new work
- Descriptive commit messages
- Pull requests for review
- Semantic versioning (MAJOR.MINOR.PATCH)

## Performance Considerations

### Ontology Queries
- Index frequently queried properties
- Cache SPARQL query results
- Use inference selectively (RDFS vs OWL)

### API
- Pagination for large result sets
- Response caching for static data
- Rate limiting for public endpoints

### Frontend
- Code splitting for large applications
- Lazy loading for routes
- Memoization for expensive computations

## Security

### API Security
- Authentication required for write operations
- Input validation on all endpoints
- CORS configuration for web clients

### Data Privacy
- No PII in ontology without consent
- Audit logging for sensitive operations
- Secure credential storage

## Deployment (Future)

### Containerization
- Multi-stage Docker builds
- Separate containers for Python backend and web frontend
- docker-compose for local development

### Infrastructure
- Cloud-agnostic design
- Horizontal scaling for API layer
- Graph database for production ontology storage (e.g., GraphDB, Stardog)
