import sys

# �V���v����ToDo���X�g���Ǘ�����N���X
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        # �������F�^�X�N�����X�g�ɒǉ�����@�\
        pass

    def list_tasks(self):
        # �������F���X�g���̃^�X�N��\������@�\
        for i in range(len(tasks)):
            print("tasks_number:"+i)
            print(tasks[i])
        pass

    def remove_task(self, task_number):
        # �������F�w�肳�ꂽ�^�X�N�����X�g����폜����@�\
        pass

    def complete_task(self, task_number):
        # �������F�w�肳�ꂽ�^�X�N�������ς݂Ƃ��ă}�[�N����@�\
        pass

def print_help():
    print("Usage:")
    print("  python todo.py add <task>")
    print("  python todo.py list")
    print("  python todo.py remove <task_number>")
    print("  python todo.py complete <task_number>")
    print("  python todo.py help")

def main():
    if len(sys.argv) < 2:
        print_help()
        return

    command = sys.argv[1]
    todo_list = ToDoList()

    match command:
        case "add":
            if len(sys.argv) != 3:
                print("Error: Task description is required.")
            else:
                task = sys.argv[2]
                todo_list.add_task(task)
        case "list":
            todo_list.list_tasks()
        case "remove":
            if len(sys.argv) != 3:
                print("Error: Task number is required.")
            else:
                try:
                    task_number = int(sys.argv[2])
                    todo_list.remove_task(task_number)
                except ValueError:
                    print("Error: Task number must be an integer.")
        case "complete":
            if len(sys.argv) != 3:
                print("Error: Task number is required.")
            else:
                try:
                    task_number = int(sys.argv[2])
                    todo_list.complete_task(task_number)
                except ValueError:
                    print("Error: Task number must be an integer.")
        case _:
            print_help()

if __name__ == "__main__":
    main()