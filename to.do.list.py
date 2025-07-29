import json
import os

TASKS_FILE = 'tasks.json'

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

def display_tasks(tasks):
    if not tasks:
        print("No tasks to show.")
        return
    for i, task in enumerate(tasks, 1):
        status = "✅" if task['done'] else "❌"
        print(f"{i}. [{status}] {task['title']}")

def add_task(tasks):
    title = input("Enter task: ")
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)

def mark_done(tasks):
    display_tasks(tasks)
    idx = int(input("Enter task number to mark as done: ")) - 1
    if 0 <= idx < len(tasks):
        tasks[idx]['done'] = True
        save_tasks(tasks)

def delete_task(tasks):
    display_tasks(tasks)
    idx = int(input("Enter task number to delete: ")) - 1
    if 0 <= idx < len(tasks):
        tasks.pop(idx)
        save_tasks(tasks)

def main():
    tasks = load_tasks()
    while True:
        print("\n--- TO-DO LIST ---")
        print("1. View Tasks\n2. Add Task\n3. Mark as Done\n4. Delete Task\n5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_done(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
