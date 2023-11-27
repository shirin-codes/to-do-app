from task_manager import TaskManager
from cli import CLI

task_manager_obj = TaskManager([])
cli_obj = CLI(task_manager_obj)


while True:
    cli_obj.display_menu()
    cli_obj.execute_tasks()


# task_manager_obj.add('task_1')
#task_manager_obj.view()
# task_manager_obj.add('task_2')
# task_manager_obj.view()
#
#
# task_manager_obj.delete(0)
# task_manager_obj.view()
#
# task_manager_obj.edit(0,'updated_name')
# task_manager_obj.view()
#
# task_manager_obj.mark_as_complete(0)
# task_manager_obj.view()
