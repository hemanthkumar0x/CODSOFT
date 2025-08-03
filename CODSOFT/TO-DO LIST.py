tasks = []

def show_menu():
    print("\n--- To-Do List Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter new task: ")
        tasks.append({"task": task, "done": False})
        print("Task added successfully.")

    elif choice == "2":
        if not tasks:
            print("No tasks yet.")
        else:
            print("\nYour To-Do List:")
            for i, t in enumerate(tasks, 1):
                status = "FINISHED" if t["done"] else "NOT FINISHED"
                print(f"{i}. {t['task']} [{status}]")

    elif choice == "3":
        task_no = int(input("Enter task number to mark as done: "))
        if 0 < task_no <= len(tasks):
            tasks[task_no-1]["done"] = True
            print("Task marked as done!")
        else:
            print("Invalid!! Task Number.")

    elif choice == "4":
        print("Exiting To-Do List.")
        break

    else:
        print("Invalid choice!!. Try again!!.")


