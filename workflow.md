# 🔄 Workflow – Multi-Agent Chemistry AI (Swarm-Oriented)

This document explains how the system processes a user action from start to finish. The workflow is designed to ensure that every interaction is safe, accurate, and educational, while also demonstrating structured multi-agent collaboration.

Unlike a simple execution pipeline, the system now follows a **Swarm-Oriented Workflow**, where tasks are first analyzed, validated, and then orchestrated across multiple agents.

---

## 🧠 Updated Flow

**User → API → Task Analyzer → HITL → Swarm Orchestrator → Agents → Response**

This enhanced flow introduces task decomposition and controlled execution, aligning with modern orchestration principles.

---

## ⚙️ Step-by-Step Workflow

### 1. User Action

The process begins when the user performs an action in the virtual lab, such as mixing two chemicals.

Example:
* Mixing **HCl** with **NaOH**

---

### 2. API Layer

The API acts as the entry point of the system.

* Receives user input  
* Converts it into structured JSON format  
* Sends the request to the processing pipeline  

---

### 3. Task Analysis (Task Analyzer)

Before execution, the system analyzes the request and breaks it into smaller subtasks.

Example decomposition:
* Safety validation  
* Reaction computation  
* Explanation generation  

This ensures that each step can be handled independently and efficiently.

---

### 4. Human-in-the-Loop (HITL)

The HITL layer introduces a validation checkpoint.

* Reviews tasks based on risk level  
* Allows safe tasks to proceed automatically  
* Blocks or flags risky operations  

This step reflects real-world systems where critical actions require oversight.

---

### 5. Swarm Orchestration (Swarm Orchestrator)

The Swarm Orchestrator coordinates the execution of all tasks.

Responsibilities:
* Routes tasks to the correct agents  
* Maintains execution order  
* Manages communication between agents  

Instead of direct execution, the system now behaves like a **coordinated team**, where each agent contributes in a structured manner.

---

### 6. Agent Execution

Each agent performs its specialized role:

**⚠️ Safety Agent**
* Validates chemical inputs  
* Prevents unsafe combinations  

**🧪 Reaction Agent**
* Determines reaction type  
* Computes products  

**📘 Tutor Agent**
* Explains the reaction clearly  
* Provides conceptual understanding  

**💡 Hint Agent**
* Assists users when needed  

**📊 Progress Agent**
* Tracks learning progress  

---

### 7. Response Aggregation

The system collects outputs from all agents and combines them into a structured response.

This response includes:
* Validation status  
* Reaction results  
* Explanation  
* Progress updates  

---

## 🧪 Example Workflow (JSON)

```json
{
  "input": {
    "chemical_1": "HCl",
    "chemical_2": "NaOH"
  },
  "tasks": ["safety", "reaction", "tutor"],
  "results": [
    { "status": "valid" },
    { "type": "Neutralization", "products": ["NaCl", "H2O"] },
    { "explanation": "Acid reacts with base to form salt and water" }
  ]
}
```
