from doctest import debug_script
from queue import Empty
class Task:
    def __init__(self, name, status, description):
        self.name=name
        self.status=status
        self.description=description

class ToDoSystems:
    def addTask(listTaskpendient, task):
        listTaskpendient.append(task)

    def enumListTask (listkTaskPendient ):
        print("Tasks: \n")
        for task in listkTaskPendient:
            print ('-', task.name)
    def enumListTaskStatus  (listkTaskPendient ):
        print("Tasks: \n")
        for task in listkTaskPendient:
            print ('-', task.name ," - ",task.status)


    def changeStatusComplete (listkTaskPendient, i ):
        task = listkTaskPendient[i]
        task.status='complete'
        listkTaskPendient[i]= task

    def clearList(listkTaskPendient):
        listkTaskPendient.clear()

    def run_todo_system(self):
        listkTaskPendient=[]
        print("Welcome to Manager TO-DO list!")
        while True:
            print("\nMenu:")
            print("1. Add a task to the to-do list.")
            print("2. List all tasks in the to-do list.")
            print("3. Mark task as completed")
            print("4. Clear the to-do list")

            choice = input("Enter your choice: ")

            if choice == "1":
                task = input("Name task:")
                description = input("Description task: ")
                Task(task,'pendient',description)
                self.addTask(listkTaskPendient, task)
                if(listkTaskPendient.__contains__(task)):
                    print("¡the task was added to the list successfully !")

            elif choice == "2":
                self.enumListTask(listkTaskPendient)
            elif choice =="3":
                self.enumListTaskStatus(listkTaskPendient)
                choice2= input("Enter your choice: ")
                if choice2 <= len(listkTaskPendient):
                    self.changeStatusComplete(listkTaskPendient, choice2-1)
                
            elif choice == "4":
                self.clearList(listkTaskPendient)
                if len(listkTaskPendient) ==0 :
                    print("¡the list was clear successfully !")
            else:
                print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    task = ToDoSystems()
    task.run_todo_system()