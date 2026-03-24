analyzer = TaskAnalyzer()
tasks = analyzer.decompose(input)

# check HITL
approved_tasks = [t for t in tasks if hitl.require_approval(t)]

# run swarm
orchestrator.run_sequential(approved_tasks)
