import json
import os
from datetime import datetime

FILE = "tasks.json"

TREE_STAGES = [
    "🌱",
    "🌿",
    "🌳",
    "🌳 + 🍃",
    "🌳 + 🌸",
]

def load_tasks():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def add_task():
    text = input("Task name: ").strip()
    if not text:
        print("❌ Empty task!")
        return
    deadline = input("Deadline (YYYY-MM-DD, optional): ").strip()
    task = {"task": text, "done": False, "deadline": deadline}
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print("✅ Task added!")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("📭 No tasks yet.")
        return
    for i, t in enumerate(tasks):
        status = "✓" if t["done"] else " "
        deadline = f"(by {t['deadline']})" if t["deadline"] else ""
        print(f"{i+1}. [{status}] {t['task']} {deadline}")

def mark_done():
    list_tasks()
    tasks = load_tasks()
    i = int(input("Which task to mark as done? ")) - 1
    if 0 <= i < len(tasks):
        tasks[i]["done"] = True
        save_tasks(tasks)
        print("🎉 Great job!")
    else:
        print("❌ Invalid selection.")

def delete_task():
    list_tasks()
    tasks = load_tasks()
    i = int(input("Which task to delete? ")) - 1
    if 0 <= i < len(tasks):
        del tasks[i]
        save_tasks(tasks)
        print("🗑 Task deleted.")
    else:
        print("❌ Invalid selection.")

def view_tree():
    tasks = load_tasks()
    if not tasks:
        print("🌱 No tasks, your tree is just a seedling.")
        return

    total = len(tasks)
    done = sum(1 for t in tasks if t["done"])
    percent = done / total

    if percent == 1:
        stage = 4
    elif percent >= 0.75:
        stage = 3
    elif percent >= 0.5:
        stage = 2
    elif percent >= 0.25:
        stage = 1
    else:
        stage = 0

    print("\n🌳 Your Productivity Tree 🌳")
    print("Tasks completed:", done, "/", total)
    print("Tree stage:", TREE_STAGES[stage])
    print()

def menu():
    while True:
        print("\n📝 To-Do Menu")
        print("1. Add task")
        print("2. List tasks")
        print("3. Mark task as done")
        print("4. Delete task")
        print("5. View tree progress")
        print("0. Exit")

        choice = input("Choose: ").strip()
        if choice == "1":
            add_task()
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            mark_done()
            view_tree()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            view_tree()
        elif choice == "0":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid option.")

if __name__ == "__main__":
    menu()
