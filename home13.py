# 1

# class student:
#     def __init__(self, name, age, course):
#         self.name = name
#         self.age = age
#         self.course = course
#
# s1 = student("anna", 18, 1)
# s2 = student("max", 19, 2)
#
# print(s1.name, s1.age, s1.course)
# print(s2.name, s2.age, s2.course)

# 2 

# class student:
#     def __init__(self, name, age, course):
#         self.name = name
#         self.age = age
#         self.course = course
#
#     def show_info(self):
#         print(f"👩‍🎓 {self.name}, {self.age} років, курс {self.course}")
#
# s = student("anna", 18, 1)
# s.show_info()

# 3

# class student:
#     def __init__(self, name, age, course):
#         self.name = name
#         self.age = age
#         self.course = course
#
#     def change_course(self, new_course):
#         self.course = new_course
#
# s = student("anna", 18, 1)
# s.change_course(2)
# print(s.course)

# 4
  
# class task:
#     def __init__(self, title):
#         self.title = title
#         self.completed = false
#
#     def mark_done(self):
#         self.completed = true
#
# t = task("зробити дз")
# t.mark_done()
# print(t.completed)

# 5

# class task:
#     def __init__(self, title):
#         self.title = title
#         self.completed = false
#
# tasks = [
#     task("дз 📚"),
#     task("прибрати 🧹"),
#     task("відпочити 😴")
# ]
#
# for t in tasks:
#     print(t.title, t.completed)

# 6 

# class event:
#     def __init__(self, title, date):
#         self.title = title
#         self.date = date
#
#     def show(self):
#         print(f"📅 {self.title} — {self.date}")
#
# e = event("урок", "2026-02-01")
# e.show()

# 7 

class event:
    def __init__(self, title, date, description):
        self.title = title
        self.date = date
        self.description = description

    def update_description(self, new_description):
        self.description = new_description

    def show(self):
        print(f"📅 {self.title}")
        print(f"📆 {self.date}")
        print(f"📝 {self.description}")

e = event("урок python 🐍", "2026-02-01", "вчимо ооп")
e.update_description("вчимо ооп і практикуємо класи 💪")
e.show()
