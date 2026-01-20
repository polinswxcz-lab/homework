#1️⃣

# while True:
#     try:
#         n = int(input("Введи число: "))
#         print("Ти ввів число:", n)
#         break
#     except ValueError:
#         print("❌ це не число, спробуй ще раз")

#2️⃣

# try:
#     a = float(input("введи перше число: "))
#     b = float(input("введи друге число: "))
# except ValueError:
#     print("❌ потрібно вводити числа")
#     exit()

# print("1 — +")
# print("2 — -")
# print("3 — *")
# print("4 — /")

# choice = input("обери операцію: ")

# if choice == "1":
#     print("результат:", a + b)
# elif choice == "2":
#     print("результат:", a - b)
# elif choice == "3":
#     print("результат:", a * b)
# elif choice == "4":
#     try:
#         print("результат:", a / b)
#     except ZeroDivisionError:
#         print("❌ ділення на нуль!")
# else:
#     print("❌ невірний вибір")

#3️⃣

# name = input("введи ім'я: ")

# while True:
#     try:
#         age = int(input("введи вік: "))
#         if 1 <= age <= 120:
#             break
#         else:
#             print("❌ вік має бути від 1 до 120")
#     except ValueError:
#         print("❌ вік має бути числом")

# print("привіт,", name, "тобі", age, "років")

#4️⃣

# numbers = [10, 20, 30, 40, 50]

# try:
#     index = int(input("Введи індекс (0–4): "))
#     print("елемент:", numbers[index])
# except ValueError:
#     print("❌ індекс має бути числом")
# except IndexError:
#     print("❌ такого індексу немає")

#5️⃣

# try:
#     file = open("data.txt", "r")
#     print(file.read())
#     file.close()
# except FileNotFoundError:
#     print("❌ файл не знайдено")

#6️⃣

# rate = 43

# try:
#     uah = float(input("введи суму в гривнях: "))
#     print("у доларах:", uah / rate)
# except ValueError:
#     print("❌ потрібно вводити число")

#7️⃣

import random

code = random.randint(100, 999)

for _ in range(3):
    try:
        guess = int(input("введи код (100–999): "))

        if guess == code:
            print("🔓 сейф відкрито!")
            break
        else:
            print("❌ неправильний код")

    except ValueError:
        print("❌ потрібно вводити число")
else:
    print("💥 сейф заблоковано. код був:", code)

try:
    file = open("log.txt", "w")
    file.write("гра завершена")
    file.close()
except IOError:
    print("❌ помилка запису у файл")