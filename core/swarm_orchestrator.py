class SwarmOrchestrator:
    def __init__(self, agents):
        self.agents = agents

    async def execute(self, task):
        task_type = task["type"]
        data = task["data"]

        if task_type == "reaction":
            return self.agents["reaction"].run(data)

        elif task_type == "safety":
            return self.agents["safety"].run(data)

        elif task_type == "tutor":
            return self.agents["tutor"].run(data)

        else:
            return {"error": "Unknown task type"}
