Okay, I've reviewed the feedback and will integrate it into the original prompt. The key is to enhance the AI's ability to:

1.  **Explicitly reconcile** its technical proposals with *all* stated requirements and considerations in the PRD, especially if there's a potential divergence (like PWA vs. native app store presence).
2.  **Probe deeper** for technical details related to specific functional requirements (like progress indicators).
3.  **Ensure PRD "Open Questions" are addressed** with concrete technical solutions or marked for further discussion if a decision cannot be made.
4.  **Consider data model complexity** for features like recurring items with exceptions.
5.  **Handle potential inconsistencies** within the PRD itself (e.g., PRD suggesting relational DB while the AI proposes NoSQL).

Here's the revised rule, with changes highlighted (conceptually, as Markdown doesn't have a "highlight" feature, I'll use bolding or explicit notes for where changes were made):

---
description: Guidelines for generating a Technical Design Document (TDD) from a Product Requirements Document (PRD).
globs:
alwaysApply: false
---
# Rule: Generating a Technical Design Document (TDD)

## Goal

To guide an AI assistant in creating a detailed Technical Design Document (TDD) in Markdown format. The TDD will be based on an existing Product Requirements Document (PRD) and will outline the technical approach for implementing a feature. It serves as a bridge between the "what" and "why" (PRD) and the "how-to-implement" (task list).

## Context

The TDD should be generated *after* a PRD for a feature has been finalized, and *before* a detailed task list for implementation is created. This ensures that product requirements are clear before technical planning begins, and technical planning is established before breaking work into granular tasks.

## Process

1.  **Receive PRD Reference:** The user provides a reference to a finalized PRD file (e.g., `prd-[feature-name].md`).
2.  **Analyze PRD:** The AI thoroughly reads and understands the specified PRD, focusing on:
    *   Functional and non-functional requirements.
    *   User stories and acceptance criteria.
    *   Success metrics.
    *   **Any existing design or technical considerations stated in the PRD.**
    *   **Explicitly listed "Open Questions" or ambiguities in the PRD.**
3.  **Ask Clarifying Technical Questions (If Necessary):** Before drafting the TDD, if the PRD lacks sufficient detail for technical planning, if ambiguities exist, **if PRD open questions require technical input for resolution, or if a proposed technical approach might deviate from a stated PRD consideration**, the AI *should* ask clarifying questions. The goal is to solidify the "how" and ensure alignment with the PRD's intent.
4.  **Generate TDD:** Based on the PRD and any answers to clarifying questions, the AI generates the TDD using the structure outlined below. **The TDD must aim to address all functional requirements, technical considerations, and open questions from the PRD.**
5.  **Save TDD:** Save the generated document as `tdd-[prd-file-name].md` inside the `/tasks` directory, where `[prd-file-name]` is the base name of the PRD file it's based on.

## Clarifying Technical Questions (Examples)

The AI should adapt its questions based on the PRD, but here are some common areas to explore for technical design:

*   **System Architecture & PRD Alignment:**
    *   "Are there specific architectural patterns (e.g., microservices, event-driven) that should be followed or considered for this feature?"
    *   "How is this feature expected to integrate with existing core services or modules (e.g., authentication, user service, payment gateway)?"
    *   **"The PRD mentions [specific technical consideration, e.g., 'Mobile application for iOS and Android platforms']. If a simpler or alternative approach (e.g., PWA) is being considered for the TDD, how should this be reconciled? Is the PRD's mention a hard constraint or a desired outcome that can be met differently?"**
    *   **"If the PRD suggests a specific technology (e.g., 'relational database') but an alternative (e.g., NoSQL) seems more suitable for the overall architecture or other requirements, should the PRD suggestion be strictly followed, or can alternatives be proposed with justification?"**
*   **Data Model & Lifecycle:**
    *   "What new database tables, collections, or documents will be needed? Can you outline their proposed schemas (fields, types, relationships)?"
    *   "Will existing data models require modification? If so, which ones and how?"
    *   **"For requirements involving derived data (e.g., progress based on subtasks, aggregate scores), how should this data be calculated, stored (if at all), and updated?"**
    *   **"The PRD has an open question regarding [e.g., 'what happens to shared lists when a user deletes their account?']. What are the data integrity and ownership transfer/deletion rules for this scenario?"**
    *   **"For features like recurring events/tasks, the PRD asks [e.g., 'how to handle modifications to individual instances?']. How should the data model support both the recurring pattern and individual overrides/exceptions?"**
*   **API Design:**
    *   "Will new API endpoints be required? If so, what are their proposed methods, paths, request/response bodies, and authentication/authorization mechanisms?"
    *   "Are there existing APIs that will be consumed or extended?"
*   **Technology Stack & Libraries:**
    *   "Are there any preferred or mandated technologies, frameworks, or libraries for the backend and frontend (if applicable) implementation of this feature?"
    *   "Are there any existing internal libraries or utilities that should be leveraged?"
*   **Error Handling & Resilience:**
    *   "What are the key failure points or exceptional scenarios to consider, and what is the expected error handling behavior (e.g., retry mechanisms, fallback strategies, user notifications)?"
*   **Security Considerations:**
    *   "Beyond general security practices, are there specific security vulnerabilities or requirements to address for this feature (e.g., data encryption at rest/transit for sensitive PII, specific input validation rules, rate limiting)?"
*   **Performance & Scalability:**
    *   "Are there specific performance benchmarks (e.g., response time under X load, concurrent user capacity) or scalability requirements for this feature?"
*   **Third-Party Integrations:**
    *   "Does this feature involve integration with any third-party services? If so, which ones, and are their APIs/SDKs understood?"
*   **Logging & Monitoring:**
    *   "What specific events or metrics should be logged for debugging, monitoring, or auditing purposes related to this feature?"
*   **Addressing PRD Open Questions:**
    *   **"The PRD lists the following open question(s): [list them]. What are the technical implications or preferred approaches to resolve these?"**

## TDD Structure

The generated TDD should include the following sections:

1.  **Introduction & Purpose:**
    *   Brief overview of the feature this TDD addresses.
    *   Purpose of this document: to detail the technical design for implementation.
2.  **PRD Reference:**
    *   Filename of the PRD this TDD is based on (e.g., `prd-[feature-name].md`).
    *   **Key PRD Requirements Addressed:** (Optional but good practice) Briefly list or summarize the core functional requirements, key technical considerations, and any specific open questions from the PRD that this TDD aims to solve.
3.  **Technical Overview & Architecture:**
    *   High-level description of the proposed technical solution.
    *   Key architectural decisions (e.g., choice of patterns, frameworks, major components).
    *   **Explicitly state how the chosen architecture aligns with or addresses key technical considerations from the PRD (e.g., mobile strategy, database preference if discussed). If there's a deviation, provide a clear rationale.**
    *   Diagrams (if representable in Markdown/text, or describe where they would be).
4.  **Data Model Design:**
    *   Details of new or modified database schemas, tables, fields, and relationships.
    *   **Specifics on how complex data types or relationships are handled (e.g., recurring tasks with exceptions, representation of progress indicators derived from sub-tasks).**
    *   Data validation rules.
    *   Data migration strategy, if applicable.
    *   **Data lifecycle considerations (e.g., handling of data upon user account deletion, especially for shared or owned resources).**
5.  **API Design (if applicable):**
    *   List of new or modified API endpoints.
    *   For each endpoint:
        *   Method (GET, POST, PUT, DELETE, etc.).
        *   Path.
        *   Request parameters/body schema.
        *   Response body schema (including error responses).
        *   Authentication and authorization requirements.
6.  **Module/Component Breakdown:**
    *   Identification of key new or significantly modified software modules, classes, or components.
    *   Responsibilities of each component.
    *   Interactions between components.
7.  **Integration with Existing Systems:**
    *   How the new feature interacts with other parts of the application or external services.
    *   Impact on existing systems.
8.  **Error Handling & Logging Strategy:**
    *   Approach to handling expected and unexpected errors.
    *   Key information to be logged and logging levels.
9.  **Security Considerations:**
    *   Specific security measures to be implemented (e.g., input validation, output encoding, access controls, data protection).
    *   Potential threats and mitigations.
10. **Performance & Scalability Considerations:**
    *   Design choices made to meet performance or scalability requirements.
    *   Expected load and data volumes.
11. **Testing Strategy Considerations:**
    *   Outline of how the feature will be tested (e.g., key areas for unit tests, integration test points, considerations for E2E testing). This is not the full test plan but design considerations for testability.
12. **Technical Risks & Mitigation Plan:**
    *   Identified potential technical challenges, unknowns, or dependencies.
    *   Proposed strategies to mitigate these risks.
13. **Deployment Considerations (Optional):**
    *   Any special steps or considerations for deploying this feature (e.g., environment variable changes, infrastructure adjustments, rollout plan).
14. **Out of Scope (Technical Non-Goals):**
    *   Clearly list technical functionalities or approaches that are intentionally *not* part of this design to manage scope.
15. **Open Technical Questions / Decisions from PRD:**
    *   List any remaining technical questions or areas needing further investigation or decisions.
    *   **Summarize how "Open Questions" from the PRD have been addressed in this TDD. If any PRD open question remains unresolved technically, list it here with a note on why it's still open or what's needed for a decision.**

## Target Audience

The primary readers of the TDD are **developers** (including junior developers) who will implement the feature, as well as **tech leads** and **architects** who will review the technical design. The document should be detailed enough to guide implementation, yet clear and concise for effective review and understanding. Avoid excessive jargon where simpler terms suffice, or explain crucial technical terms if necessary.

## Output

*   **Format:** Markdown (`.md`)
*   **Location:** `/tasks/`
*   **Filename:** `tdd-[prd-file-name].md` (e.g., if PRD is `prd-user-authentication.md`, the TDD filename should be `tdd-prd-user-authentication.md`).

## Final Instructions

1.  The AI should prioritize eliciting sufficient technical detail through clarifying questions if the PRD is not technically explicit enough for design, **especially concerning PRD "Open Questions" or stated "Technical Considerations."**
2.  The TDD must be grounded in the requirements of the referenced PRD and **explicitly demonstrate how it addresses them.**
3.  **If the AI proposes a technical solution that seems to diverge from a suggestion or consideration in the PRD (e.g., using a PWA when "native apps" are mentioned, or NoSQL when "relational" is mentioned), it must explicitly acknowledge this in the TDD, justify its choice, and if necessary, ask clarifying questions beforehand to confirm if the PRD's point was a strict requirement or a preference.**
4.  The aim is to create a practical document that aids development, rather than a purely theoretical one.

---

Key changes made:

*   **Process > Analyze PRD:** Added emphasis on "technical considerations" and "Open Questions."
*   **Process > Ask Clarifying Technical Questions:** Broadened the trigger for asking questions to include PRD open questions and potential deviations from PRD considerations.
*   **Process > Generate TDD:** Added that TDD must aim to address all relevant PRD parts.
*   **Clarifying Technical Questions (Examples):**
    *   Added specific examples for "System Architecture & PRD Alignment" regarding mobile strategy and database choices if PRD mentions them.
    *   Added specific examples for "Data Model & Lifecycle" regarding derived data, account deletion impact (PRD Open Question), and recurring tasks with exceptions (PRD Open Question).
    *   Added a general category for "Addressing PRD Open Questions."
*   **TDD Structure:**
    *   **PRD Reference:** Added optional "Key PRD Requirements Addressed."
    *   **Technical Overview & Architecture:** Added requirement to explicitly state alignment/deviation from PRD technical considerations with rationale.
    *   **Data Model Design:** Added specifics on complex data types, derived data, and data lifecycle based on PRD questions.
    *   **Open Technical Questions / Decisions from PRD:** Enhanced to explicitly track how PRD open questions were addressed or why they remain open.
*   **Final Instructions:**
    *   Reinforced focus on PRD open questions and technical considerations.
    *   Emphasized that TDD must demonstrate how it addresses PRD requirements.
    *   Added a specific instruction (Instruction 3) about handling divergences between the TDD's proposal and PRD suggestions.

These changes should make the AI more thorough in aligning the TDD with the PRD, particularly in the areas highlighted by the feedback.