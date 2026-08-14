tasks = []


def add_task(title):
    task = {
        "title": title,
        "completed": False
    }
    tasks.append(task)


def main():
    add_task("Learn GitHub")
    print(tasks)


if __name__ == "__main__":
    main()
