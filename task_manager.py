from task import Task


class TaskManager:

    def __init__(self, tasks: list):
        self.tasks = tasks

    def view(self):
        for index, task in enumerate(self.tasks):
            print('{}{} {}'.format(index + 1, ')', task))

    def add(self, name):
        newtask = Task(name, False)
        self.tasks.append(newtask)

    def delete(self, task_no):
        self.tasks.pop(task_no)

    def edit(self, task_no, name):
        self.tasks[task_no].name = name

    def mark_as_complete(self, task_no):
        self.tasks[task_no].completion_status = True
