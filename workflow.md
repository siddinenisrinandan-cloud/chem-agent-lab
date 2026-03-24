# Workflow – Multi-Agent Chemistry AI

This document explains how the system processes a user action from start to finish. The goal of this workflow is to ensure that every interaction is safe, accurate, and educational.

Rather than executing actions directly, the system follows a structured pipeline where each agent contributes a specific part of the solution.

---

## Overview

At a high level, the workflow follows this path:

**User Action → API → Orchestrator → Agents → Response**

Each step is designed to validate, compute, and explain the result in a clear and controlled manner.

---

## Step-by-Step Workflow

### 1. User Action

The process begins when the user performs an action in the virtual lab, such as mixing two chemicals.

Example:

* Mixing **HCl** with **NaOH**

This action is captured by the system and sent as a request.

---

### 2. API Layer

The API acts as the entry point of the system.

* Receives user input
* Converts it into a structured format (JSON)
* Forwards the request to the Central Orchestrator

This ensures consistency in how data is handled across the system.

---

### 3. Central Orchestrator

The Central Orchestrator is responsible for managing the entire workflow.

* Maintains the current experiment state
* Routes the request to appropriate agents
* Collects and combines responses

It acts as the backbone of the system, ensuring smooth coordination.

---

### 4. Safety Validation (Safety Agent)

Before any reaction is processed, the Safety Agent validates the input.

Responsibilities:

* Check for unsafe or forbidden combinations
* Ensure the reaction follows valid chemical rules
* Stop execution if the action is unsafe

If the input is invalid, the system returns a safe explanation instead of proceeding.

---

### 5. Reaction Computation (Reaction Agent)

Once validated, the Reaction Agent determines the outcome.

Responsibilities:

* Identify reaction type
* Compute products
* Provide additional data (e.g., energy change)

This step ensures scientific correctness.

---

### 6. Explanation Generation (Tutor Agent)

After computing the reaction, the Tutor Agent explains the result.

Responsibilities:

* Describe what happened in simple terms
* Explain the underlying concept (e.g., neutralization)
* Provide step-by-step reasoning if needed

This transforms the system from a simulator into a learning tool.

---

### 7. Adaptive Assistance (Hint Agent)

If the user struggles or makes mistakes, the Hint Agent provides guidance.

Types of support:

* Subtle hints
* Step-by-step suggestions
* Direct instructions when necessary

This helps users learn without feeling stuck.

---

### 8. Progress Tracking (Progress Agent)

Finally, the system updates the user’s learning progress.

Tracks:

* Concepts learned
* Mistakes and patterns
* Skill level progression

This enables personalization in future interactions.

---

## Example Workflow (JSON)

The following example shows how the system processes a reaction internally:

```json id="1v7zpx"
{
  "input": {
    "chemical_1": "HCl",
    "chemical_2": "NaOH"
  },
  "validation": {
    "status": "valid",
    "checked_by": "Safety Agent"
  },
  "reaction": {
    "type": "Neutralization",
    "products": ["NaCl", "H2O"],
    "energy_change": "-57 kJ/mol"
  },
  "explanation": {
    "agent": "Tutor Agent",
    "text": "This is a neutralization reaction where an acid reacts with a base to form salt and water."
  },
  "progress": {
    "concept": "Neutralization",
    "status": "completed"
  }
}
```

This structured output shows how each agent contributes to the final result in a transparent and organized way.

---

## Key Design Principles

The workflow is built on a few important principles:

* **Safety First**: Every action is validated before execution
* **Modularity**: Each agent handles a single responsibility
* **Transparency**: All steps are traceable and structured
* **Educational Focus**: Every result includes an explanation

---

## Summary

This workflow ensures that the system behaves in a controlled and meaningful way. Instead of simply producing results, it validates actions, explains outcomes, and adapts to the user’s learning journey.

By combining multiple agents into a coordinated pipeline, the system delivers an experience that is both technically reliable and educationally effective.
