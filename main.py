from task import Task
from storage import load_tasks, save_tasks
from utils import print_tasks, find_task, search_tasks, sort_tasks

tasks = load_tasks()

while True:

    print("\nМеню:")
    print("1. Показати всі задачі")
    print("2. Додати задачу")
    print("3. Видалити задачу")
    print("4. Позначити як виконану")
    print("5. Редагувати задачу")
    print("6. Пошук")
    print("7. Сортування")
    print("8. Вийти")

    choice = input("Оберіть: ")

    if choice == "1":
        print_tasks(tasks)

    elif choice == "2":
        title = input("Назва: ")
        desc = input("Опис: ")
        priority = input("Пріоритет (low/medium/high): ")

        new_id = tasks[-1].id + 1 if tasks else 1
        task = Task(new_id, title, desc, "todo", priority)

        tasks.append(task)
        save_tasks(tasks)

    elif choice == "3":
        try:
            task_id = int(input("ID: "))
            task = find_task(tasks, task_id)

            if task:
                tasks.remove(task)
                save_tasks(tasks)
                print("Видалено")
            else:
                print("Не знайдено")

        except ValueError:
            print("Введіть число")

    elif choice == "4":
        try:
            task_id = int(input("ID: "))
            task = find_task(tasks, task_id)

            if task:
                task.status = "done"
                save_tasks(tasks)
                print("Готово")
            else:
                print("Не знайдено")

        except ValueError:
            print("Введіть число")

    elif choice == "5":
        try:
            task_id = int(input("ID: "))
            task = find_task(tasks, task_id)

            if task:
                task.title = input("Нова назва: ")
                task.description = input("Новий опис: ")
                task.priority = input("Новий пріоритет: ")
                save_tasks(tasks)
                print("Оновлено")
            else:
                print("Не знайдено")

        except ValueError:
            print("Введіть число")

    elif choice == "6":
        keyword = input("Пошук: ")
        result = search_tasks(tasks, keyword)
        print_tasks(result)

    elif choice == "7":
        sorted_tasks = sort_tasks(tasks)
        print_tasks(sorted_tasks)

    elif choice == "8":
        break

    else:
        print("Невірно")