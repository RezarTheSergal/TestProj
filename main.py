## Переменные:
# students_data - 
#
#
#
##

from csv import *

# Открываем и читаем файл по стандарту "utf-8"
with open("/home/itclass/Документы/TestProj/students.csv", encoding="utf-8") as infile:
    # Парсинг студентов в отдельную переменную построчно
    stud_data = list(reader(infile, delimiter=","))

    # Перебор всех людей в списке и поиск совпадений в ФИО независимо от регистра
    for item in stud_data:
        if "Хадаров".lower() in item[1].lower():
            print(f"Ты получил: {item[4]}, за проект - {item[2]}")

    # Создание словаря по формату: "Класс": [кол-во учеников, сумма их оценок]
    class_stat = dict()
    header_string = stud_data.pop(0)

    # Магия рептилий :D
    for id, name, pr_id, school_class, score in stud_data:
        if score != "None":
            if school_class not in class_stat.keys():
                class_stat[school_class] = [0, 0]
            class_stat[school_class][0] += 1
            class_stat[school_class][1] += int(score)
    
    stud_data_new = list()
    for id, name, pr_id, school_class, score in stud_data:
        if score != "None":
            score = class_stat[school_class][1] / class_stat[school_class][0]
            score = str(round(score, 3))
            stud_data_new.append([id, name, pr_id, school_class, score])

with open("/home/itclass/Документы/TestProj/students_new.csv", "w") as outfile:
    file_data = writer(outfile, delimiter=",")
    file_data.writerows(stud_data_new)


