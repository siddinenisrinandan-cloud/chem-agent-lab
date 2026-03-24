class SwarmOrchestrator:
    def __init__(self, agents):
        self.agents = agents

    def run_sequential(self, tasks):
        results = []
        for task in tasks:
            result = self.execute(task)
            results.append(result)
        return results

    def run_parallel(self, tasks):
        import asyncio
        return asyncio.gather(*(self.execute(task) for task in tasks))

    async def execute(self, task):
        # simple routing logic
        if task["type"] == "reaction":
            return self.agents["reaction"].run(task)
        elif task["type"] == "safety":
            return self.agents["safety"].run(task)
