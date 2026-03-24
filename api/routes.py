from fastapi import APIRouter
from core.task_analyzer import TaskAnalyzer
from core.swarm_orchestrator import SwarmOrchestrator
from core.hitl import HITL

from agents.reaction_agent import ReactionAgent
from agents.safety_agent import SafetyAgent
from agents.tutor_agent import TutorAgent

router = APIRouter()

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
    tasks = analyzer.decompose(input)

    approved_tasks = []
    for task in tasks:
        if hitl.require_approval(task):
            approved_tasks.append(task)

    results = []
    for task in approved_tasks:
        result = await orchestrator.execute(task)
        results.append(result)

    return {
        "tasks": approved_tasks,
        "results": results
    }
