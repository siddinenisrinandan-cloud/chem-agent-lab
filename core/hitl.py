class HITL:
    def require_approval(self, task):
        if task.get("risk") == "high":
            return False  # simulate waiting for approval
        return True
