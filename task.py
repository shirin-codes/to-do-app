class Task:

    def __init__(self, name: str, completion_status: bool):
        self.name = name
        self.completion_status = completion_status

    def __str__(self):
        if self.completion_status:
            return '[X] ' + self.name
        else:
            return '[ ] ' + self.name
