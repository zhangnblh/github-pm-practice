tasks = []


def add_task(title):
    task = {
        "title": title,
        "completed": False
    }
    tasks.append(task)


def list_tasks():
    for index, task in enumerate(tasks, start=1):
        status = "Done" if task["completed"] else "Todo"
        print(f"{index}. [{status}] {task['title']}")

def complete_task(task_id):
    index = task_id - 1

    if index < 0 or index >= len(tasks):
        print("Invalid task ID")
        return

    tasks[index]["completed"] = True

def main():
    add_task("Learn GitHub")
    add_task("Learn IntelliJ IDEA")

    complete_task(1)

    list_tasks()


if __name__ == "__main__":
    main()