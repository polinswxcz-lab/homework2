def print_tasks(tasks):
    if not tasks:
        print("Немає задач")
        return

    for t in tasks:
        print(f"[{t.id}] {t.title} | {t.priority} | {t.status}")


def find_task(tasks, task_id):
    for t in tasks:
        if t.id == task_id:
            return t
    return None


def search_tasks(tasks, keyword):
    return [t for t in tasks if keyword.lower() in t.title.lower()]


def sort_tasks(tasks):
    priority_order = {"low": 1, "medium": 2, "high": 3}
    return sorted(tasks, key=lambda t: priority_order[t.priority])