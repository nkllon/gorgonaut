# Requirements Document - Ontology Overview

## Introduction

This specification defines the requirements for an architectural document that interprets the Gorgonaut / Mind Tools ontology in clear, human-readable terms. The goal is to connect ontology classes and properties to product behavior and expert-system architecture so contributors can understand how the knowledge graph drives recommendations, workflows, and capability building.

## Scope

- Target document: `docs/architecture/ontology-overview.md`
- Audience: engineers, knowledge engineers, product stakeholders
- Inputs: OWL ontology (`specs/ontology/gorgonaut-mindtools.ttl`), Kiro steering docs
- Out of scope: full ontology population, SHACL definitions, implementation specifics

## Glossary

- Ontology: Formal model of domain concepts and relationships
- Object property: Relationship between two entities
- Datatype property: Attribute whose value is a literal (string, number)
- Meta-skill: High-level, transferable capability (e.g., creativity)
- Problem type: Canonical problem the user faces
- Solution pattern: Abstract approach a tool instantiates

## Requirements

### Requirement 1 — Purpose and Scope
The document SHALL state the purpose of the ontology and how it supports the product and expert system.

### Requirement 2 — Core Concepts
The document SHALL enumerate core classes in plain English, including but not limited to:
- MindTool, Book, Module, Tool, MetaSkill
- ProblemType, SolutionPattern, Outcome
- Stakeholder, StakeholderRole, StakeholderNeed
- ExpertSystem, SystemLayer (ContextEngine, ToolSynthesisEngine, DecisionActionLayer, CapabilityBuildingLayer)
- ContextSignal, SystemOutput, CapabilityMetric, Evaluation, Risk, MythicConcept, BrandRole

### Requirement 3 — Key Relationships
The document SHALL describe key object properties and how they interconnect concepts, including:
- hasModule, implementsMetaSkill, groupsTool
- supportsMetaSkill, addressesProblem, instantiatesPattern
- mitigates / mitigatedBy, aimsAtOutcome, contributesToOutcome
- hasRole, hasNeed, servesStakeholder / servedBy, hasLayer
- ingestsSignal, producesOutput, improvesMetric
- posesRisk, hasMythicConcept, assignedBrandRole, evaluatesTool, usesFramework

### Requirement 4 — Data Properties
The document SHALL list primary datatype properties and intended usage:
- hasName, hasDescription, hasWeight, hasIdentifier

### Requirement 5 — Architectural Mapping
The document SHALL map ontology concepts to the expert-system layers and end-to-end data flow (signals → framing → synthesis → outputs → capability tracking).

### Requirement 6 — Example Path
The document SHALL include at least one end-to-end example that traces:
ContextSignal → ProblemType → Tool (supportsMetaSkill, addressesProblem, aimsAtOutcome) → SystemOutput.

### Requirement 7 — Conventions and Boundaries
The document SHALL document namespace and naming conventions and clarify modeling boundaries (what is in the ontology vs. generated artifacts).

### Requirement 8 — Next Steps
The document SHALL outline next steps for ontology population, SHACL validation, and typical query patterns.

## Acceptance Criteria

1. WHEN a reader opens `docs/architecture/ontology-overview.md` THEN they SHALL find a clear explanation of ontology purpose and scope.
2. WHEN a reader scans the document THEN they SHALL find plain-English descriptions of all listed core classes and key properties.
3. WHEN a reader looks for relationships THEN they SHALL find how tools, problems, meta-skills, outcomes, and stakeholders connect.
4. WHEN a reader wants system context THEN they SHALL see how the ontology maps to expert-system layers and data flow.
5. WHEN a reader needs a concrete illustration THEN the document SHALL include at least one end-to-end example path.
6. WHEN a contributor follows conventions THEN they SHALL find namespace and naming guidelines consistent with the repository.
7. WHEN planning future work THEN the document SHALL point to population, validation, and query next steps.


