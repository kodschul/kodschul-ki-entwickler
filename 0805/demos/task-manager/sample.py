"""
Sample Python file demonstrating basic task operations using the DbManager.
"""

from db import DbManager

db = DbManager()
db.func_init_db()


def list_tasks():
    tasks = db.func_get_tasks()
    if not tasks:
        print("No tasks found.")
        return
    for task in tasks:
        print(f"[{task['id']}] {task['title']} — {task['status']}")


def add_task(title: str):
    db.func_create_task(title)
    print(f"Added task: {title}")


def delete_task(task_id: int):
    db.func_delete_task(task_id)
    print(f"Deleted task {task_id}")


if __name__ == "__main__":
    add_task("Buy groceries")
    add_task("Write tests")
    add_task("Deploy to production")
    print("\nAll tasks:")
    list_tasks()
    delete_task(1)
    print("\nAfter deletion:")
    list_tasks()
