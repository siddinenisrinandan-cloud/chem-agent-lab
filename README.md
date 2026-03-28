![Python](https://img.shields.io/badge/Python-3.10+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![GSoC](https://img.shields.io/badge/GSoC-2026-orange)
![Status](https://img.shields.io/badge/Status-Active-success)


# 🧪 Chem Agent Lab

🚀 *GSoC 2026 Proposal Project | MoFA Org*

---

## 📌 Overview

Chem Agent Lab isn’t just another virtual chemistry lab. It’s more like a team of smart assistants ready to walk you through experiments — showing you what’s actually happening in a reaction, and more importantly, why it’s happening.

Here’s the cool part: the system combines real-time reaction simulations, clear AI explanations, and a variety of specialized agents that handle different aspects of the process. These agents don’t work alone — they bounce ideas off each other, check your inputs, crunch the numbers, and break down the science in plain language.

The project is part of Google Summer of Code 2026 with MoFA. The main idea? Prove that multi-agent AI systems aren’t just buzzwords — they can actually make learning real subjects, like chemistry, a hands-on experience.

Goal: Make chemistry interactive, easy to understand, and just as engaging as messing around with beakers in a real lab.

---

##  Documentation

* [System Architecture](./ARCHITECTURE.md)
* [Workflow](./workflow.md)
* [Future Enhancements](./FUTURE_ENHANCEMENTS.md)
* [Why MOFA](./MOFA.md)

---

##  Problem Statement

Many current virtual chemistry labs mainly focus on simulation, but they often do not provide enough support for deeper learning. Common limitations include: * No real-time intelligent guidance. * Little explanation of why reactions occur. * No adaptive feedback based on student progress. As a result, students often conduct experiments without fully understanding the concepts behind them.

---

##  Solution

Chem Agent Lab tackles this issue by introducing a collaborative multi-agent AI structure. Rather than relying on a single system to do all the work, several specialized agents join forces to: * Validate experiments * Predict chemical reactions * Explain results in simple language * Guide learners through the process This changes virtual experiments into interactive, concept-driven learning experiences.

---

## 🎯 Objectives

Build a **multi-agent system for chemistry simulation**

Provide **real-time explanations of chemical reactions**

Enable **learning through AI-driven feedback**

show **agent collaboration in an educational environment**


---

## ⚙️ Workflow Diagram

![Workflow](https://dcdenfkxagtaydgekexj.supabase.co/storage/v1/object/public/generated-images/gemini_create_same_thing_1774380792.png)

---

## 🤖 System Architecture

The platform brings together a team of AI agents, each with its own unique job.

### Reaction Agent
 
* Figures out what happens when chemicals react with each other.
* Uses rule-based logic and chemical datasets

### Tutor Agent

* Explains reactions in clear, natural language
* Helps users understand the underlying concepts

### Safety Agent

* Validates chemical combinations.
* Prevents incorrect or unsafe inputs.
### Hint Agent

* Gives contextual hints during experiments.
*  Helps users when they run into problems.
### Progress Agent 

* Tracks user learning progress.
* Adjusts difficulty and guidance as needed.

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

## Workflow 
1. User performs an action (for example, mixing chemicals).
2. Safety Agent checks the input.
3. Reaction Agent calculates the result.
4. Tutor Agent explains the reaction.
5. Hint Agent provides help if needed.
6. Progress Agent updates the learning state.

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

## Features

- Work with multiple agents at once
- Coordinate tasks through a powerful swarm system
- Run chemical simulations in real time
- Get explanations in plain English
- Adaptive learning that grows with you
- Built to be modular—easy to expand or customize

## Getting Started

### What you need

- Python 3.10 or newer
- Node.js if you want to use the frontend
- Unity, but only if you need it—it's optional

## How to install

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

## Here’s how the chem-agent-lab project is organized:

Everything starts in the main folder. Inside, you’ll find a bunch of folders:

- The “agents” folder holds different Python files, each one dedicated to a specific agent—reaction_agent, tutor_agent, safety_agent, hint_agent, and progress_agent. They all focus on their own tasks.
- “core” is where you’ll find the backbone of the system. There are orchestrator and swarm_orchestrator files (to manage agent interactions), task_analyzer (handles task logic), and hitl (human-in-the-loop stuff).
- The “api” folder has routes.py, which handles the API endpoints.
- “data” contains chemical_db.json, the database for chemical info.

Outside the folders, you have main.py, the entry point for running the app, and requirements.txt, which lists all the dependencies you need.

---

## Roadmap (GSoC Timeline)

Weeks 1–3: Set up the project and lay the groundwork for the main agent.

Weeks 4–6: Build the Reaction and Tutor agents.

Weeks 7–9: Get agents talking to each other and working together.

Weeks 10–12: Tie everything into the UI and run tests.


## Future Scope

- Add a voice-powered AI lab assistant
- Create a detailed 3D interactive lab
- Connect the system with popular educational platforms
- Bring in physics and biology simulations to expand beyond chemistry

---
## About ME 

Hey, I’m Sri Nandan from SRM University. AI? That’s my jam. I spend most of my free time building software projects—especially ones where AI twists the usual ways people learn. Lately, I’ve been obsessed with multi-agent systems and interactive learning tools. That’s basically my life right now.

##  Acknowledgment

If you want to get involved, just open an issue or send a pull request. I’d love to hear your thoughts or see your ideas in action. Everything here’s open source with the MIT License. Massive thanks to Google Summer of Code 2026 and MoFA—they got this project going. I dove into designing scalable, modular multi-agent platforms for education, and honestly, I haven’t looked back.
