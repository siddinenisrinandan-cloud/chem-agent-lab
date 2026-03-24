class TaskAnalyzer:
    def decompose(self, input_data):
        return [
            {"type": "safety", "data": input_data},
            {"type": "reaction", "data": input_data},
            {"type": "tutor", "data": input_data}
        ]
      
