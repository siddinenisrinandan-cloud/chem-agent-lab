![Python](https://img.shields.io/badge/Python-3.10+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![GSoC](https://img.shields.io/badge/GSoC-2026-orange)
![Status](https://img.shields.io/badge/Status-Active-success)


# 🧪 Chem Agent Lab

🚀 *GSoC 2026 Proposal Project | MoFA Org*

---

## 📌 Overview

**Chem Agent Lab** is a multi-agent AI system designed to simulate, explain, and guide interactive chemistry experiments. Instead of acting as a static virtual lab, the platform behaves like an intelligent assistant that helps users understand **what happens in a reaction and why it happens**.

The system combines **chemical reaction simulation**, **AI-driven explanations**, and **collaborative agent orchestration** to create an interactive learning environment. Multiple specialized AI agents work together to analyze inputs, validate experiments, compute results, and explain the science behind them.

This project is being developed as part of **Google Summer of Code (GSoC) 2026 under MoFA**, with the goal of demonstrating how **multi-agent architectures can support real educational applications**.

> 💡 **Goal:** Make chemistry learning interactive, explainable, and as intuitive as performing experiments in a real laboratory.

---

## 📚 Documentation

* [System Architecture](./ARCHITECTURE.md)
* [Workflow](./workflow.md)
* [Future Enhancements](./FUTURE_ENHANCEMENTS.md)
* [Why MOFA](./MOFA.md)

---

## ❗ Problem Statement

Many existing virtual chemistry labs focus primarily on simulation, but they often lack deeper learning support. Common limitations include:

* No real-time intelligent guidance
* Little explanation of **why reactions occur**
* No adaptive feedback based on student progress

Because of this, students often perform experiments **without truly understanding the concepts behind them**.

---

## 💡 Solution

Chem Agent Lab addresses this problem by introducing a **collaborative multi-agent AI architecture**.

Instead of a single system handling everything, multiple specialized agents work together to:

* Validate experiments
* Predict chemical reactions
* Explain results in simple language
* Guide learners through the process

This transforms virtual experiments into **interactive, concept-driven learning experiences**.

---

## 🎯 Objectives

* Build a **multi-agent system for chemistry simulation**
* Provide **real-time explanations of chemical reactions**
* Enable **adaptive learning through AI-driven feedback**
* Demonstrate **agent collaboration in an educational environment**

---

## ⚙️ Workflow Diagram

![Workflow](https://dcdenfkxagtaydgekexj.supabase.co/storage/v1/object/public/generated-images/gemini_create_same_thing_1774380792.png)

---

## 🤖 System Architecture

The platform is built around a set of **specialized AI agents**, each responsible for a specific role.

### 🧪 Reaction Agent

* Predicts the outcomes of chemical reactions
* Uses rule-based logic and chemical datasets

### 📘 Tutor Agent

* Explains reactions in clear, natural language
* Helps users understand the underlying concepts

### ⚠️ Safety Agent

* Validates chemical combinations
* Prevents incorrect or unsafe inputs

### 💡 Hint Agent

* Provides contextual hints during experiments
* Assists users when they encounter difficulties

### 📊 Progress Agent

* Tracks user learning progress
* Adapts difficulty and guidance accordingly

---

## 🧠 Swarm Orchestration

The system now includes a **Swarm Orchestration layer**, inspired by the design principles of the **MoFA ecosystem**.

Rather than relying on a single agent, the system decomposes tasks and coordinates multiple agents in a structured workflow.

### 🔄 Execution Flow

User → API → Task Analyzer → HITL → Swarm Orchestrator → Agents

### ⚙️ Key Components

* **Task Analyzer** – Breaks down user input into subtasks
* **HITL (Human-in-the-Loop)** – Adds validation before execution
* **Swarm Orchestrator** – Coordinates task execution across agents
* **Agents** – Handle specialized tasks (Safety, Reaction, Tutor)

### 🧪 Example Input

```json
{
  "chemical_1": "HCl",
  "chemical_2": "NaOH"
}
```

### 🔬 Agent Collaboration

User → API → Orchestrator → Agents
├── Reaction Agent
├── Safety Agent
├── Tutor Agent
├── Hint Agent
└── Progress Agent

The orchestrator manages communication between agents, ensuring tasks are executed in the correct order while keeping the system modular and scalable.

---

## 🔄 Workflow

1. User performs an action (e.g., mixing chemicals)
2. Safety Agent validates the input
3. Reaction Agent computes the result
4. Tutor Agent explains the reaction
5. Hint Agent assists if needed
6. Progress Agent updates the learning state

---

## 🛠️ Tech Stack

**Backend**

* Python
* FastAPI

**AI / Agents**

* Multi-agent architecture
* Rule-based chemical logic
* LLM integration

**Frontend**

* React / Unity (prototype)

**Data**

* JSON-based chemical knowledge base

---

## 📦 Features

* Multi-agent collaboration
* Swarm orchestration system
* Real-time chemical simulation
* Natural language explanations
* Adaptive learning support
* Modular and extensible architecture

---

## 🚀 Getting Started

### Prerequisites

* Python 3.10+
* Node.js (for frontend)
* Unity (optional)

### Installation

```bash
git clone https://github.com/siddinenisrinandan-cloud/chem-agent-lab.git
cd chem-agent-lab
pip install -r requirements.txt
```

### Run Backend

```bash
uvicorn main:app --reload
```

Open in browser:
http://127.0.0.1:8000/docs

---

## 📂 Project Structure

chem-agent-lab/
│
├── agents/
│   ├── reaction_agent.py
│   ├── tutor_agent.py
│   ├── safety_agent.py
│   ├── hint_agent.py
│   └── progress_agent.py
│
├── core/
│   ├── orchestrator.py
│   ├── swarm_orchestrator.py
│   ├── task_analyzer.py
│   └── hitl.py
│
├── api/
│   └── routes.py
│
├── data/
│   └── chemical_db.json
│
├── main.py
└── requirements.txt

---

## 📈 Roadmap (GSoC Timeline)

**Weeks 1–3**
Project setup and base agent structure

**Weeks 4–6**
Implement Reaction and Tutor agents

**Weeks 7–9**
Agent communication and orchestration

**Weeks 10–12**
UI integration and testing

---

## 🔮 Future Scope

* Voice-based AI lab assistant
* Advanced 3D interactive lab environment
* Integration with educational platforms
* Expansion to physics and biology simulations

---

## 👨‍💻 About Me

**Sri Nandan**
🎓 Student at SRM University
💡 Aspiring Freelancer | AI & Software Enthusiast

* Interested in multi-agent systems
* Passionate about AI-powered education
* Focused on building interactive learning platforms

---

## 🤝 Contributing

Contributions are welcome. Feel free to open issues or submit pull requests.

---

## 📄 License

This project is open-source under the MIT License.

---

## 🌟 Acknowledgment

Developed as part of **Google Summer of Code (GSoC) 2026 under MoFA**, focusing on building scalable and modular multi-agent systems for education.
