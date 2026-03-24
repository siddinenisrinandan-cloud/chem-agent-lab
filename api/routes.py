from fastapi import APIRouter
from core.task_analyzer import TaskAnalyzer
from core.swarm_orchestrator import SwarmOrchestrator
from core.hitl import HITL

# import your agents
from agents.reaction_agent import ReactionAgent
from agents.safety_agent import SafetyAgent
from agents.tutor_agent import TutorAgent

router = APIRouter()

# create objects
analyzer = TaskAnalyzer()
hitl = HITL()

agents = {
    "reaction": ReactionAgent(),
    "safety": SafetyAgent(),
    "tutor": TutorAgent()
}

orchestrator = SwarmOrchestrator(agents)


@router.post("/swarm/run")
async def run_swarm(input: dict):
    # Step 1: Decompose task
    tasks = analyzer.decompose(input)

    # Step 2: HITL filtering
    approved_tasks = []
    for task in tasks:
        if hitl.require_approval(task):
            approved_tasks.append(task)

    # Step 3: Execute tasks
    results = []
    for task in approved_tasks:
        result = await orchestrator.execute(task)
        results.append(result)

    return {
        "tasks": approved_tasks,
        "results": results
    }
