# Requirements Document - Ontology Population

## Introduction

This specification defines the requirements for populating the Gorgonaut Mind Tools ontology with real-world data. The ontology currently has a comprehensive schema but lacks actual instances of tools, meta-skills, problems, and their relationships. This feature will transform the empty ontology into a rich knowledge graph that can power the expert system.

## Glossary

- **Ontology**: The formal knowledge representation defining classes, properties, and relationships in the Mind Tools domain
- **Mind Tool**: Any cognitive or practical technique for problem-solving, decision-making, or skill development
- **Meta-Skill**: High-level transferable capability (e.g., creativity, decision-making, project management)
- **Problem Type**: Canonical problem statement that users face
- **Solution Pattern**: Abstract approach to solving a problem type
- **Instance**: A specific individual entity in the ontology (e.g., the SCAMPER tool)
- **Turtle Format**: RDF serialization syntax (.ttl files) used for ontology data
- **SHACL**: Shapes Constraint Language for validating ontology data quality

## Requirements

### Requirement 1

**User Story:** As a system architect, I want the ontology populated with Mind Tools book data, so that the knowledge graph reflects the complete corpus of available tools and techniques.

#### Acceptance Criteria

1. WHEN the ontology is loaded THEN the system SHALL include at least one Book instance with name and description
2. WHEN a Book instance is queried THEN the system SHALL return all associated Module instances
3. WHEN the ontology data is validated THEN the system SHALL pass all SHACL constraints for Book and Module entities
4. WHEN a Module is queried THEN the system SHALL return the MetaSkill it implements
5. WHEN multiple books exist THEN the system SHALL maintain distinct namespaces or identifiers for each book

### Requirement 2

**User Story:** As a knowledge worker, I want the ontology to contain specific cognitive tools, so that I can discover and learn about individual techniques.

#### Acceptance Criteria

1. WHEN the ontology is loaded THEN the system SHALL include at least 20 Tool instances covering multiple meta-skills
2. WHEN a Tool instance is queried THEN the system SHALL return its name, description, and associated meta-skill
3. WHEN tools are listed THEN the system SHALL include diverse examples such as SCAMPER, SWOT, Gantt charts, Mind Mapping, and Pareto Analysis
4. WHEN a Tool is validated THEN the system SHALL conform to the :Tool class definition and SHACL shapes
5. WHEN a Tool is queried for relationships THEN the system SHALL return associated ProblemType and SolutionPattern instances

### Requirement 3

**User Story:** As a developer building the expert system, I want meta-skills defined in the ontology, so that tools can be organized by the capabilities they develop.

#### Acceptance Criteria

1. WHEN the ontology is loaded THEN the system SHALL include at least 8 MetaSkill instances
2. WHEN meta-skills are listed THEN the system SHALL include creativity, decision-making, project management, problem-solving, communication, leadership, time management, and strategic thinking
3. WHEN a MetaSkill is queried THEN the system SHALL return all Tools that support that meta-skill
4. WHEN a MetaSkill is queried THEN the system SHALL return Outcomes it contributes to
5. WHEN meta-skill data is validated THEN the system SHALL pass all SHACL constraints

### Requirement 4

**User Story:** As a user seeking help with a problem, I want problem types defined in the ontology, so that the system can match my situation to relevant tools.

#### Acceptance Criteria

1. WHEN the ontology is loaded THEN the system SHALL include at least 15 ProblemType instances
2. WHEN problem types are listed THEN the system SHALL include examples like "need to generate creative ideas", "need to make a decision with multiple criteria", "need to prioritize tasks", and "need to analyze competitive landscape"
3. WHEN a ProblemType is queried THEN the system SHALL return SolutionPattern instances that mitigate it
4. WHEN a ProblemType is queried THEN the system SHALL return Tool instances that address it
5. WHEN problem type data is validated THEN the system SHALL pass all SHACL constraints

### Requirement 5

**User Story:** As a system designer, I want solution patterns defined in the ontology, so that abstract problem-solving approaches can be mapped to concrete tools.

#### Acceptance Criteria

1. WHEN the ontology is loaded THEN the system SHALL include at least 10 SolutionPattern instances
2. WHEN solution patterns are listed THEN the system SHALL include examples like "structured brainstorming", "multi-criteria evaluation", "visual organization", and "systematic analysis"
3. WHEN a SolutionPattern is queried THEN the system SHALL return ProblemType instances it mitigates
4. WHEN a SolutionPattern is queried THEN the system SHALL return Tool instances that instantiate it
5. WHERE a SolutionPattern has a weight property THEN the system SHALL store it as a decimal value

### Requirement 6

**User Story:** As a product manager, I want stakeholder roles and needs defined in the ontology, so that the system can provide role-appropriate recommendations.

#### Acceptance Criteria

1. WHEN the ontology is loaded THEN the system SHALL include at least 5 StakeholderRole instances
2. WHEN stakeholder roles are listed THEN the system SHALL include individual knowledge worker, manager, consultant, team lead, and student
3. WHEN a StakeholderRole is queried THEN the system SHALL return associated StakeholderNeed instances
4. WHEN stakeholder needs are listed THEN the system SHALL include examples like "quick decision-making", "team coordination", "client problem-solving", and "skill development"
5. WHEN stakeholder data is validated THEN the system SHALL pass all SHACL constraints

### Requirement 7

**User Story:** As a quality assurance engineer, I want all ontology data to be valid, so that the system operates reliably without data integrity issues.

#### Acceptance Criteria

1. WHEN ontology data files are created THEN the system SHALL use valid Turtle syntax
2. WHEN SHACL validation is executed THEN the system SHALL report zero violations
3. WHEN ontology data is loaded THEN the system SHALL successfully parse without errors
4. WHEN entities are created THEN the system SHALL include required properties (hasName for all named entities)
5. WHEN relationships are defined THEN the system SHALL reference only existing entity instances

### Requirement 8

**User Story:** As a developer, I want ontology data organized in logical files, so that the knowledge graph is maintainable and extensible.

#### Acceptance Criteria

1. WHEN ontology data is stored THEN the system SHALL organize instances into separate files by domain (e.g., creativity.ttl, decision-making.ttl)
2. WHEN a new meta-skill domain is added THEN the system SHALL create a new .ttl file without modifying existing files
3. WHEN data files are loaded THEN the system SHALL merge all instances into a single coherent graph
4. WHEN file organization is reviewed THEN the system SHALL follow the structure defined in structure.md
5. WHEN example data exists THEN the system SHALL maintain it in specs/ontology/data/examples.ttl separate from production data

### Requirement 9

**User Story:** As a content curator, I want tool descriptions to be informative, so that users can understand when and how to apply each technique.

#### Acceptance Criteria

1. WHEN a Tool instance is created THEN the system SHALL include a description of at least 50 characters
2. WHEN a Tool description is written THEN the system SHALL explain what the tool does and when to use it
3. WHEN tool data is reviewed THEN the system SHALL use clear, jargon-free language
4. WHEN multiple tools are compared THEN the system SHALL maintain consistent description structure and detail level
5. WHEN a Tool is queried THEN the system SHALL return both name and description properties

### Requirement 10

**User Story:** As a system integrator, I want tools linked to their outcomes, so that the system can explain the benefits of using specific techniques.

#### Acceptance Criteria

1. WHEN the ontology is loaded THEN the system SHALL include at least 10 Outcome instances
2. WHEN outcomes are listed THEN the system SHALL include examples like "better decisions", "increased creativity", "improved time management", and "clearer communication"
3. WHEN a Tool is queried THEN the system SHALL return Outcome instances it aims to achieve
4. WHEN a MetaSkill is queried THEN the system SHALL return Outcome instances it contributes to
5. WHEN outcome relationships are validated THEN the system SHALL confirm proper use of aimsAtOutcome and contributesToOutcome properties
