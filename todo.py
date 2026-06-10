import json
import os

FILENAME = "tasks.json"

def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(FILENAME, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(tasks):
    task = input("Enter task: ")
    priority = input("Priority (high / medium / low): ").lower()
    if priority not in ["high", "medium", "low"]:
        priority = "medium"
    tasks.append({"id": len(tasks) + 1, "task": task, "priority": priority, "done": False})
    save_tasks(tasks)
    print("-> Task added!")

def view_tasks(tasks):
    if not tasks:
        print("-> No tasks yet.")
        return
    print("\n YOUR TASKS ")
    for i, t in enumerate(tasks, 1):
        status = "[X]" if t["done"] else "[ ]"
        print(f"{i}. {status} [{t['priority'].upper()}] {t['task']}")

def mark_done(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Enter task number to mark done: "))
        tasks[num - 1]["done"] = True
        save_tasks(tasks)
        print("-> Marked as done!")
    except (IndexError, ValueError):
        print("-> Invalid number.")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Enter task number to delete: "))
        removed = tasks.pop(num - 1)
        save_tasks(tasks)
        print(f"-> Deleted: {removed['task']}")
    except (IndexError, ValueError):
        print("-> Invalid number.")

def main():
    tasks = load_tasks()
    menu = {
        "1": ("Add Task",    add_task),
        "2": ("View Tasks",  view_tasks),
        "3": ("Mark Done",   mark_done),
        "4": ("Delete Task", delete_task),
        "5": ("Exit",        None)
    }
    while True:
        print("\n TO-DO LIST ")
        for key, (label, _) in menu.items():
            print(f"  {key}. {label}")
        choice = input("Choose: ")
        if choice == "5":
            print("Goodbye!")
            break
        elif choice in menu:
            menu[choice][1](tasks)
        else:
            print("-> Invalid choice.")

if __name__ == "__main__":
    main()