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


def main():
    add_task("Learn GitHub")
    add_task("Learn IntelliJ IDEA")

    list_tasks()


if __name__ == "__main__":
    main()