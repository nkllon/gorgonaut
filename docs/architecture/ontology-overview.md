# Gorgonaut / Mind Tools Ontology — Architectural Interpretation

## Purpose

The ontology formalizes the Mind Tools domain so the expert system can reason over user context, problems, tools, outcomes, and stakeholder needs. It provides a shared vocabulary and graph structure that:
- anchors product features in well-defined concepts,
- enables SPARQL queries and inference,
- supports transparent recommendations and composable workflows,
- and ties decisions to capability-building over time.

Source: `specs/ontology/gorgonaut-mindtools.ttl` (OWL 2, Turtle). Namespace prefix: `:` or `gorgo:` for `http://example.org/gorgonaut#`.

## Core Concepts (Classes)

- MindTool: Root category for the corpus of books, modules, and tools.
- Book: A book or compendium aggregating modules and meta-skills.
- MetaSkill: A transferable capability (creativity, decision-making, project management, …).
- Module: A chapter or logical grouping of tools centered on a meta-skill.
- Tool: An individual technique/framework (e.g., SCAMPER, SWOT, Gantt chart).
- ProblemType: Canonical problem statement users face (e.g., “prioritization under time pressure”).
- SolutionPattern: Abstract solution approach instantiated by specific tools.
- Outcome: Desired result (clarity, alignment, better decision quality, reduced risk, …).
- Stakeholder: Any actor impacted (individual, manager, consultant, student, …).
- StakeholderRole: Role category for a stakeholder (e.g., manager, individual).
- StakeholderNeed: A need or requirement expressed by a stakeholder role.
- ExpertSystem: The intelligent system that operationalizes the ontology.
- SystemLayer: A layer in the expert-system architecture, specialized as:
  - ContextEngine: Ingests signals and frames problems.
  - ToolSynthesisEngine: Selects and composes tools into workflows.
  - DecisionActionLayer: Produces plans, decisions, and communication artifacts.
  - CapabilityBuildingLayer: Tracks skills, gaps, and reinforcement over time.
- ContextSignal: Any signal about the user’s situation (task, constraints, emotion).
- SystemOutput: Structured artifact produced by the system (framed problem, plan, workflow).
- CapabilityMetric: Metric for assessing improvements in capability/performance.
- Evaluation: An assessment instance for tools or the system.
- Risk: A risk or limitation related to tools or system use.
- MythicConcept: Symbolic concept used in branding/metaphor.
- BrandRole: The role a mythic concept plays in branding.

(Top-level classes are declared disjoint to improve consistency.)

## Key Relationships (Object Properties)

- hasModule (MindTool → Module): Books/corpora to their modules.
- implementsMetaSkill (Module → MetaSkill): Module’s primary capability focus.
- groupsTool (Module → Tool): Tools included in a module.
- supportsMetaSkill (Tool → MetaSkill): Meta-skills a tool helps develop.
- addressesProblem (Tool → ProblemType): Problems a tool targets.
- instantiatesPattern (Tool → SolutionPattern): Abstract pattern realized by a tool.
- mitigates / mitigatedBy (SolutionPattern ↔ ProblemType): Pattern–problem linkage (with inverse).
- aimsAtOutcome (Tool → Outcome): Intended outcomes a tool drives.
- contributesToOutcome (MetaSkill → Outcome): Outcomes improved by capability growth.
- hasRole (Stakeholder → StakeholderRole): Stakeholder’s role category.
- hasNeed (Stakeholder → StakeholderNeed): Needs expressed by a stakeholder.
- servesStakeholder / servedBy (ExpertSystem ↔ Stakeholder): Who the system serves.
- hasLayer (ExpertSystem → SystemLayer): Layers in the system architecture.
- ingestsSignal (ContextEngine → ContextSignal): Signals processed for framing.
- producesOutput (SystemLayer → SystemOutput): Outputs produced by each layer.
- improvesMetric (ExpertSystem → CapabilityMetric): Metrics the system targets.
- posesRisk (MindTool → Risk): Risks associated with tools.
- hasMythicConcept (ExpertSystem → MythicConcept): Branding/metaphor linkage.
- assignedBrandRole (MythicConcept → BrandRole): Branding role assignment.
- evaluatesTool (Evaluation → MindTool): Evaluation subject.
- usesFramework (Evaluation → ExpertSystem): Framework/system used for evaluation.

## Datatype Properties (Attributes)

- hasName (Thing → string): Human-readable name.
- hasDescription (Thing → string): Explanatory text.
- hasWeight (SolutionPattern → decimal): Relative importance/weight.
- hasIdentifier (Thing → string): External/system identifier for integration.

## How the Ontology Powers the Expert System

1) Context Understanding (ContextEngine)
- Input: ContextSignal (task, constraints, emotion, role).
- Operation: map signals to candidate ProblemType instances; normalize roles to StakeholderRole.
- Output: SystemOutput (framed problem with candidate problems and rationale).

2) Tool Synthesis (ToolSynthesisEngine)
- Input: Framed problem (ProblemType candidates) and user role/needs.
- Selection: Find Tool where Tool addressesProblem ProblemType, supportsMetaSkill MetaSkill relevant to role/need, and aimsAtOutcome desired Outcome; prefer Tool instantiating suitable SolutionPattern.
- Composition: Build Workflow using compatible tools, ordered by rationale and dependencies.
- Output: SystemOutput (workflow with rationale and required inputs/outputs).

3) Decision/Action (DecisionActionLayer)
- Transform workflow into concrete plans and artifacts for the user/team.
- Preserve traceability to tools, problems, patterns, outcomes.

4) Capability Building (CapabilityBuildingLayer)
- Track capability metrics; connect MetaSkill → Outcome; evaluate improvements over time.
- Feed results back into recommendations and personalization.

## End-to-End Example (Conceptual)

Given: ContextSignal (role=manager, task=“prioritize roadmap”, constraint=“2 days”, emotion=“stressed”)
- ContextEngine: maps to ProblemType “prioritization under time pressure”.
- ToolSynthesisEngine:
  - Candidate Tool A: “Eisenhower Matrix” supportsMetaSkill “decision-making”, addressesProblem “prioritization under time pressure”, aimsAtOutcome “clarity”.
  - Candidate Tool B: “RICE Scoring” supportsMetaSkill “project management”, addressesProblem “feature prioritization”, aimsAtOutcome “alignment”.
  - Choose and compose A → B; both instantiatesPattern “prioritization-by-criteria”.
- DecisionActionLayer: produces a prioritized feature list with communication notes (SystemOutput).
- CapabilityBuildingLayer: logs CapabilityMetric “decision quality” and “cycle time” for follow-up.

## Conventions and Boundaries

- Namespace: `http://example.org/gorgonaut#` with `:` or `gorgo:` prefixes.
- Naming: PascalCase for classes (Tool, MetaSkill), camelCase for properties (addressesProblem), kebab-case for instances.
- Modeled in ontology: concepts, relationships, and evaluation scaffolding.
- Generated artifacts (e.g., step-by-step action plans) live as SystemOutput instances and in application layers, not as ontology schema.

## Next Steps

- Population: Create instances for Books, Modules, Tools, MetaSkills, ProblemTypes, Outcomes, Stakeholders (see `.kiro/specs/ontology-population`).
- Validation: Define and run SHACL shapes for data quality and constraints.
- Query Patterns: Provide SPARQL snippets for common lookups (e.g., “tools for ProblemType X”).
- Integration: Implement graph loading and caching utilities in backend; expose API endpoints; surface results in the web UI.

This interpretation should be used alongside the OWL file for precise semantics and the Kiro specs for implementation details.
