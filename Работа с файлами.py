import pickle

#1 task1 A


with open("task1.txt", "r") as file:
    a1 = file.readlines()
    a1 = [line.rstrip("\n") for line in a1]
    print(a1)
    dict_1 = {a1[i]: a1[i + 1] for i in range(0, len(a1), 2)}
    print(dict_1)

with open("task1.txt", "w") as file_1:
    for val in a1:
        file_1.write(f"{val}")

del a1[0: len(a1):2]
file_1.close()

#2 task2


file = open("task2", "rb")

file_1 = pickle.load(file)
total_sum = sum(file_1) / len(file_1)

file.close()
print(total_sum)


#3 Task 3
# Використовуючи openpyxl (або будь-яку іншу зручну для вас бібліотеку), напишіть контекстний менеджер для роботи з ексель.
# Даний менеджер повинен бути аналогом методу open()

import openpyxl


class FileExcel:
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file_obj.close()


with FileExcel("Excel.xlsx", 'w') as file:
    file.write('Add this string in cell.')

print(file)



