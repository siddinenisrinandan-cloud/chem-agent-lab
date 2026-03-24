# System Architecture – Multi-Agent Chemistry AI

This project is built around a simple but powerful idea: instead of relying on a single system to handle everything, it uses a group of specialized AI agents that work together under a central controller. This makes the system easier to understand, safer to use, and more flexible to expand in the future.

At the core of the system is the **Central Orchestrator**, which acts like a coordinator. Whenever a user performs an action—such as mixing chemicals—the orchestrator receives the request and decides which agent should handle each part of the task.

## Overall Flow

The system follows a structured flow:

User → API → Orchestrator → Agents

The orchestrator then interacts with the following agents:

* Safety Agent
* Reaction Agent
* Tutor Agent
* Hint Agent
* Progress Agent

Each agent has a clear and independent responsibility, which keeps the system modular and easy to maintain.

## How the System Works

1. The user performs an action (for example, mixing two chemicals).
2. The request is sent to the Central Orchestrator.
3. The Safety Agent first checks whether the action is safe and valid.
4. If approved, the Reaction Agent computes the chemical result.
5. The Tutor Agent generates a clear explanation of what happened.
6. If the user is struggling, the Hint Agent provides guidance.
7. The Progress Agent updates the user’s learning profile.

This step-by-step pipeline ensures that the system is not only functional but also educational.

## Core Components

| Component      | Role                                          |
| -------------- | --------------------------------------------- |
| Orchestrator   | Manages communication and flow between agents |
| Safety Agent   | Validates inputs and prevents unsafe actions  |
| Reaction Agent | Determines the outcome of chemical reactions  |
| Tutor Agent    | Explains results in an understandable way     |
| Hint Agent     | Provides guidance when users make mistakes    |
| Progress Agent | Tracks learning progress and skill level      |

## State Management

To support multi-step experiments, the system maintains a persistent state using a JSON structure. This allows the system to remember previous actions and build more complex interactions.

## Example System Workflow (JSON Representation)

To better understand how the system operates internally, the following example demonstrates how a simple chemical reaction is processed step by step using a structured JSON format.

In this scenario, the user mixes hydrochloric acid (HCl) with sodium hydroxide (NaOH). The system processes this input through multiple agents, each responsible for a specific task.

```json
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

This example highlights how the system is not just executing a reaction, but coordinating multiple intelligent components:

* The **Safety Agent** ensures that the combination is valid and safe to proceed
* The **Reaction Agent** determines the type of reaction and its products
* The **Tutor Agent** provides a clear and educational explanation
* The **Progress Agent** updates the learner’s understanding and tracks concept completion

By structuring the workflow in this way, the system remains transparent, modular, and easy to extend, while also delivering meaningful educational feedback to the user.


This structure helps in tracking experiments, analyzing user behavior, and restoring sessions if needed.

## Why This Architecture Works

This design aligns well with modern multi-agent system principles and MOFA goals:

* **Modular**: Each agent works independently and can be developed or improved separately
* **Reusable**: The same architecture can be applied to other domains beyond chemistry
* **Scalable**: New agents (like visualization or voice assistants) can be added easily
* **Safe**: The Safety Agent ensures strict validation before any action is executed

Overall, this architecture creates a balance between accuracy, adaptability, and user-friendly learning, making the system behave more like a real lab assistant rather than a static simulator.
