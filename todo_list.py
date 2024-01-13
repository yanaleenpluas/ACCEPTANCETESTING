from doctest import debug_script
from queue import Empty
class Task:
    def __init__(self, name, status, description):
        self.name = name
        self.status = status
        self.description = description

class ToDoSystem:
    def __init__(self):
        self.listTaskPending = []

    def addTask(self, task):
        self.listTaskPending.append(task)

    def enumerateTasks(self):
        print("Tasks:")
        for i, task in enumerate(self.listTaskPending, start=1):
            print(f"{i}. {task.name} ({task.status})")

    def markComplete(self, i):
        if 0 <= i < len(self.listTaskPending):
            task = self.listTaskPending[i]
            task.status = 'complete'
            self.listTaskPending[i] = task
            print(f'Task "{task.name}" marked as complete.')

    def clearList(self):
        self.listTaskPending.clear()
        print("The to-do list has been cleared.")

    def editTask(self, i):
        if 0 <= i < len(self.listTaskPending):
            task = self.listTaskPending[i]
            print(f"Editing task: {task.name}")
            new_name = input("Enter the new task name: ")
            new_description = input("Enter the new task description: ")
            task.name = new_name
            task.description = new_description
            print(f'Task "{task.name}" edited successfully.')

    def showTaskDetails(self, i):
        if 0 <= i < len(self.listTaskPending):
            task = self.listTaskPending[i]
            print(f"\nTask Details:")
            print(f"Name: {task.name}")
            print(f"Status: {task.status}")
            print(f"Description: {task.description}")

def run_todo_system():
    todo_system = ToDoSystem()
    print("Welcome to the To-Do List Manager!")

    while True:
        print("\nMenu:")
        print("1. Add a task to the to-do list.")
        print("2. List all tasks in the to-do list.")
        print("3. Mark a task as completed.")
        print("4. Clear the to-do list.")
        print("5. Edit an existing task.")
        print("6. Show details of a task.")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task_name = input("Enter task name: ")
            task_description = input("Enter task description: ")
            new_task = Task(task_name, 'pending', task_description)
            todo_system.addTask(new_task)
            print(f'Task "{task_name}" added to the to-do list.')

        elif choice == "2":
            todo_system.enumerateTasks()

        elif choice == "3":
            todo_system.enumerateTasks()
            task_index = int(input("Enter the index of the task to mark as completed: ")) - 1
            todo_system.markComplete(task_index)

        elif choice == "4":
            todo_system.clearList()

        elif choice == "5":
            todo_system.enumerateTasks()
            task_index = int(input("Enter the index of the task to edit: ")) - 1
            todo_system.editTask(task_index)

        elif choice == "6":
            todo_system.enumerateTasks()
            task_index = int(input("Enter the index of the task to show details: ")) - 1
            todo_system.showTaskDetails(task_index)

        elif choice == "7":
            print("Exiting To-Do List Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    run_todo_system()
