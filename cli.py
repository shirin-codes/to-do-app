import sys

from task_manager import TaskManager


class CLI():

    def __init__(self, taskManager: TaskManager):
        self.taskManager = taskManager

    def display_menu(self):
        print('Welcome to the to-do-app!' '\n'
              '1. Create a new task' '\n'
              '2. View all tasks' '\n'
              '3. Edit a task' '\n'
              '4. Delete a task' '\n'
              '5. Exit')

    def execute_tasks(self):
        user_input = int(input())
        if user_input == 1:
            self.taskManager.add(input('Kindly provide a name for the task'))
        elif user_input == 2:
            self.taskManager.view()
        elif user_input == 3:
            self.taskManager.edit(int(input('Choose a task_no: ')), (input('Choose alternative name for the task: ')))
        elif user_input == 4:
            self.taskManager.delete(int(input('Choose a task_no to delete a task')))
        elif user_input == 5:
            sys.exit(0)

