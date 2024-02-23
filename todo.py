# Define functions for various operations

def add_task(tasks, task):
    tasks.append(task)
    print("Task added successfully!")

def remove_task(tasks, task_index):
    if task_index < 1 or task_index > len(tasks):
        print("Invalid task number!")
    else:
        del tasks[task_index - 1]
        print("Task removed successfully!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks in the list.")
    else:
        print("Your To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

# Main program

def main():
    tasks = []

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            task = input("Enter task: ")
            add_task(tasks, task)
        elif choice == '2':
            if not tasks:
                print("No tasks to remove.")
            else:
                task_index = int(input("Enter task number to remove: "))
                remove_task(tasks, task_index)
        elif choice == '3':
            view_tasks(tasks)
        elif choice == '4':
            print("Exiting the To-Do List Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if _name_ == "_main_":
    main()