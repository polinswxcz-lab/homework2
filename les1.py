vacancies = [
    {"title": "Python Developer", "city": "New York", "salary": 100000, "location": "Remote"},
    {"title": "Data Scientist", "city": "San Francisco", "salary": 120000, "location": "Office"},
    {"title": "Web Developer", "city": "Los Angeles", "salary": 90000, "location": "Remote"},
    {"title": "Software Engineer", "city": "Chicago", "salary": 110000, "location": "Office"},
    {"title": "Frontend Developer", "city": "Austin", "salary": 85000, "location": "Remote"},
    {"title": "Backend Developer", "city": "Seattle", "salary": 95000, "location": "Office"},
    {"title": "Machine Learning Engineer", "city": "Boston", "salary": 130000, "location": "Remote"},
    {"title": "QA Engineer", "city": "Denver", "salary": 70000, "location": "Office"},
    {"title": "DevOps Engineer", "city": "Miami", "salary": 115000, "location": "Remote"},
    {"title": "Mobile Developer", "city": "San Diego", "salary": 98000, "location": "Office"}
]

while True:

    print("\nменю:")
    print("1 - показати всі вакансії")
    print("2 - фільтр по місту")
    print("3 - фільтр по зарплаті")
    print("4 - тільки remote")
    print("5 - середня зарплата")
    print("6 - найдорожча вакансія")
    print("7 - вийти")

    choice = input("оберіть пункт меню: ")

    if choice == "1":
        for v in vacancies:
            print(v)

    elif choice == "2":
        city = input("введіть місто: ")
        for v in vacancies:
            if v["city"].lower() == city.lower():
                print(v)

    elif choice == "3":
        try:
            min_salary = int(input("введіть мінімальну зарплату: "))
            for v in vacancies:
                if v["salary"] > min_salary:
                    print(v)
        except ValueError:
            print("помилка, введіть число")

    elif choice == "4":
        for v in vacancies:
            if v["location"].lower() == "remote":
                print(v)

    elif choice == "5":
        total = 0
        for v in vacancies:
            total += v["salary"]
        average = total / len(vacancies)
        print("середня зарплата:", average)

    elif choice == "6":
        max_vacancy = vacancies[0]
        for v in vacancies:
            if v["salary"] > max_vacancy["salary"]:
                max_vacancy = v
        print("найдорожча вакансія:", max_vacancy)

    elif choice == "7":
        print("вихід з програми")
        break

    else:
        print("невірний вибір")