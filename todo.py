my_tasks = []

def show_menu():
    print("\n--- To-Do List ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Quit")

def add_task():
    task = input("Enter your task: ")
    my_tasks.append({"task": task, "done": False})
    print("Task added!")

def view_tasks():
    if len(my_tasks) == 0:
        print("No tasks yet!")
    else:
        print("\n--- Your Tasks ---")
        for index, task in enumerate(my_tasks, 1):
            status = "✓" if task["done"] else "✗"
            print(f"{index}. [{status}] {task['task']}")

def mark_done():
    view_tasks()
    if len(my_tasks) > 0:
        try:
            num = int(input("Enter task number to mark as done: "))
            if 1 <= num <= len(my_tasks):
                my_tasks[num-1]["done"] = True
                print("Task marked as done!")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number!")

def delete_task():
    view_tasks()
    if len(my_tasks) > 0:
        try:
            num = int(input("Enter task number to delete: "))
            if 1 <= num <= len(my_tasks):
                removed = my_tasks.pop(num-1)
                print(f"Task deleted: {removed['task']}")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number!")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()