from csv import *

# Открываем и читаем файл по стандарту "utf-8"
with open("/home/itclass/Документы/TestProj/students.csv", encoding="utf-8") as infile:
    # Парсинг студентов в отдельную переменную построчно
    students_data = reader(infile, delimiter=",")

    # Счётчик
    counter = 0

    # Перебор всех людей в списке и поиск совпадений в ФИО независимо от регистра
    for item in students_data:
        if "Мухы".lower() in item[1].lower():
            counter += 1
            print(item)
    print(counter)
