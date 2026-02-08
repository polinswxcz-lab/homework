class Event:
    def __init__(self, title, date):
        self.title = title
        self.date = date

    def show(self):
        print(self.get_info())

    def get_info(self):
        return f"Подія: {self.title}, дата: {self.date}"


class Training(Event):
    def __init__(self, title, date, topic):
        super().__init__(title, date)
        self.topic = topic

    def show(self):
        print(self.get_info())

    def get_info(self):
        return f"Тренування: {self.title}, дата: {self.date}, тема: {self.topic}"


class Birthday(Event):
    def __init__(self, title, date, person):
        super().__init__(title, date)
        self.person = person

    def show(self):
        print(self.get_info())

    def get_info(self):
        return f"День народження: {self.title}, дата: {self.date}, іменинник: {self.person}"


class OnlineEvent(Event):
    def __init__(self, title, date, link):
        super().__init__(title, date)
        self.link = link

    def show(self):
        print(self.get_info())

    def get_info(self):
        return f"Онлайн-подія: {self.title}, дата: {self.date}, посилання: {self.link}"


events = [
    Event("Зустріч", "10.02.2026"),
    Training("Python урок", "12.02.2026", "ООП"),
    OnlineEvent("Вебінар", "17.02.2026", "https://dfghjhg.com")
]

for event in events:
    event.show()

print("\n--- get_info окремо ---")
for event in events:
    print(event.get_info())