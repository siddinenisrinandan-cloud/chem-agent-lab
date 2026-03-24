class HITL:
    def require_approval(self, task):
        # simple logic (you can improve later)
        if task.get("risk") == "high":
            return False
        return True
