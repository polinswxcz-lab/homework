# 1

# from datetime import datetime

# text = input("введи запис у щоденник: ")

# with open("diary.txt", "a", encoding="utf-8") as file:
#     file.write(f"{datetime.now()} — {text}\n")

# print("запис збережено ✨")

# 2

# import os

# filename = "grades.txt"

# if os.path.exists(filename):
#     with open(filename, "r", encoding="utf-8") as file:
#         grades = list(map(int, file.read().split()))
#     average = sum(grades) / len(grades)
#     print("середня оцінка:", average)
# else:
#     print("файл grades.txt не знайдено ❌")

# 3

# login = input("логін: ")
# password = input("пароль: ")

# with open("users.txt", "a", encoding="utf-8") as file:
#     file.write(f"{login}:{password}\n")

# print("користувача збережено 🔐")

# 4

# import os

# filename = "data.txt"

# if os.path.exists(filename):
#     with open(filename, "r", encoding="utf-8") as file:
#         print(file.read())
# else:
#     print("файл не знайдено ❌")

# 5

# a = float(input("перше число: "))
# b = float(input("друге число: "))
# op = input("операція (+, -, *, /): ")

# if op == "+":
#     result = a + b
# elif op == "-":
#     result = a - b
# elif op == "*":
#     result = a * b
# elif op == "/":
#     result = a / b
# else:
#     print("невідома операція")
#     exit()

# with open("calc_history.txt", "a", encoding="utf-8") as file:
#     file.write(f"{a} {op} {b} = {result}\n")

# print("результат:", result)

# 6

# import json
# import os

# filename = "planner.json"

# if os.path.exists(filename):
#     with open(filename, "r", encoding="utf-8") as file:
#         planner = json.load(file)
# else:
#     planner = {}

# event = input("назва події: ")
# date = input("дата: ")

# planner[event] = date

# with open(filename, "w", encoding="utf-8") as file:
#     json.dump(planner, file, ensure_ascii=False, indent=4)

# print("подію збережено 📅")

# 7

with open("numbers.txt", "r", encoding="utf-8") as file:
    numbers = list(map(int, file.read().split()))

numbers.sort()

with open("numbers_sorted.txt", "w", encoding="utf-8") as file:
    file.write(" ".join(map(str, numbers)))

print("дані відсортовано ⭐")