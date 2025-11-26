# Gorgonaut Specifications

This directory contains feature specifications following the Kiro spec-driven development methodology.

## Active Specifications

### 1. Ontology Population (`ontology-population/`)
**Status:** Requirements phase  
**Description:** Populate the Mind Tools ontology with real data from books, modules, tools, meta-skills, and problem-solution mappings.

**Key Requirements:**
- Add Book and Module instances
- Populate 20+ Tool instances (SCAMPER, SWOT, Gantt, etc.)
- Define 8+ MetaSkill instances
- Create 15+ ProblemType instances
- Define 10+ SolutionPattern instances
- Add StakeholderRole and StakeholderNeed data
- Ensure SHACL validation passes
- Organize data in logical .ttl files

### 2. Expert System Implementation (`expert-system/`)
**Status:** Requirements phase  
**Description:** Implement the four-layer expert system architecture for intelligent tool recommendation and workflow generation.

**Key Requirements:**
- Context Engine: Parse signals and frame problems
- Tool Synthesis Engine: Select and compose tools into workflows
- Decision/Action Layer: Generate executable action plans
- Capability Building Layer: Track skills and identify gaps
- SPARQL query integration with ontology
- Clear interfaces between layers
- Error handling and configuration management

### 3. Tool Recommendation API (`tool-recommendation-api/`)
**Status:** Requirements phase  
**Description:** RESTful API exposing expert system capabilities for tool discovery and recommendations.

**Key Requirements:**
- Tool listing and search endpoints
- Meta-skill and problem type browsing
- Recommendation generation endpoint
- Workflow composition endpoint
- User capability tracking endpoints
- Health monitoring and API documentation
- Rate limiting and authentication
- OpenAPI 3.0 specification

### 4. Web UI (`web-ui/`)
**Status:** Requirements phase  
**Description:** React-based web application for tool discovery, recommendations, and capability tracking.

**Key Requirements:**
- Home page with clear value proposition
- Tool browser with search and filtering
- Detailed tool view pages
- Recommendation flow for personalized suggestions
- Workflow generation and visualization
- Capability dashboard for skill tracking
- Responsive design for all devices
- Accessibility compliance (WCAG AA)

## Development Workflow

Each spec follows this progression:

1. **Requirements** - User stories and acceptance criteria (EARS format)
2. **Design** - Architecture, components, and correctness properties
3. **Tasks** - Implementation plan with property-based tests
4. **Implementation** - Coding and validation

## Next Steps

To begin working on a spec:

1. Review the requirements document
2. Run `/kiro/spec-design {feature-name}` to create the design
3. Run `/kiro/spec-tasks {feature-name}` to create the task list
4. Run `/kiro/spec-impl {feature-name}` to begin implementation

## Dependencies

Recommended implementation order:

1. **Ontology Population** (foundation for all other features)
2. **Expert System** (core intelligence layer)
3. **Tool Recommendation API** (integration layer)
4. **Web UI** (user-facing interface)

## Status Tracking

Check progress on any spec:
```
/kiro/spec-status {feature-name}
```

View all specs:
```
/kiro/spec-status
```
