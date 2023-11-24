from csv import *

with open("/home/itclass/Документы/TestProj/students.csv", encoding="utf-8") as infile:
    students_data = reader(infile, delimiter=",")
    counter = 0
    for item in students_data:
        if "Юля".lower() in item[1].lower():
            counter += 1
            print(item)
    print(counter)
