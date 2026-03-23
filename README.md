# 🧪 Chem Agent Lab

## 📌 Overview

Chem Agent Lab is a multi-agent AI system designed to simulate, explain, and guide interactive chemistry experiments. The project combines chemical reaction simulation with intelligent tutoring using a collaborative network of specialized AI agents.

This system is developed as part of Google Summer of Code (GSoC) under MoFA Org, focusing on building scalable and modular AI agent architectures for real-world educational applications.

---

## 🎯 Objectives

* Build a multi-agent system for chemistry simulation
* Provide real-time explanations of chemical reactions
* Enable adaptive learning through AI-driven feedback
* Demonstrate agent collaboration in an educational context

---

## 🤖 System Architecture

The platform is built using multiple specialized AI agents:

### 🧪 Reaction Agent

* Predicts outcomes of chemical reactions
* Uses rule-based logic and chemical datasets

### 📘 Tutor Agent

* Explains reactions in simple, natural language
* Answers user queries interactively

### ⚠️ Safety Agent

* Validates chemical combinations
* Prevents incorrect or unsafe inputs

### 💡 Hint Agent

* Provides contextual hints during experiments
* Assists users when they are stuck

### 📊 Progress Agent

* Tracks user performance
* Adapts difficulty based on learning progress

---

## 🔄 Workflow

1. User performs an action (e.g., mixing chemicals)
2. Reaction Agent predicts the result
3. Safety Agent validates the action
4. Tutor Agent explains the outcome
5. Hint Agent assists if needed
6. Progress Agent updates learning state

---

## 🛠️ Tech Stack

* **Backend:** Python, FastAPI
* **AI/Agents:** LLMs, Rule-based systems
* **Frontend:** Unity / React (prototype)
* **Data:** JSON-based chemical knowledge base

---

## 📦 Features

* Multi-agent collaboration
* Real-time chemical simulation
* Natural language explanations
* Adaptive learning system
* Modular and extensible architecture

---

## 🚀 Getting Started

### Prerequisites

* Python 3.10+
* Node.js (if using React frontend)
* Unity (optional for simulation UI)

### Installation

```bash
git clone https://github.com/your-username/chem-agent-lab.git
cd chem-agent-lab
pip install -r requirements.txt
```

### Run Backend

```bash
uvicorn main:app --reload
```

---

## 📂 Project Structure

```
chem-agent-lab/
│── agents/
│   ├── reaction_agent.py
│   ├── tutor_agent.py
│   ├── safety_agent.py
│   ├── hint_agent.py
│   └── progress_agent.py
│
│── core/
│   ├── orchestrator.py
│   └── communication.py
│
│── data/
│   └── chemical_db.json
│
│── api/
│   └── routes.py
│
│── main.py
│── requirements.txt
```

---

## 📈 Roadmap (GSoC Timeline)

* Week 1–3: Setup project and basic agent structure
* Week 4–6: Implement Reaction and Tutor agents
* Week 7–9: Agent communication and orchestration
* Week 10–12: UI integration and testing

---

## 🤝 Contributing

Contributions are welcome. Please open issues or submit pull requests for improvements.

---

## 📄 License

This project is open-source and available under the MIT License.

---

## 🌟 Acknowledgment

Developed as part of Google Summer of Code (GSoC) under MoFA Org, focusing on advancing multi-agent AI systems for education.
