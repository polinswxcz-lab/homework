import json

file_name = "planner.json"

def load_events():
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            planner = json.load(f)
        next_id = max(map(int, planner.keys())) + 1 if planner else 1
        return planner, next_id
    except FileNotFoundError:
        return {}, 1

def save_events(planner):
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(planner, f, ensure_ascii=False, indent=4)

def show_menu():
    print("\n📅 персональний планувальник")
    print("1️⃣ додати подію")
    print("2️⃣ переглянути всі події")
    print("3️⃣ видалити подію")
    print("4️⃣ знайти події за датою")
    print("5️⃣ вийти")

def add_event(planner, event_id):
    title = input("📝 назва: ")
    date = input("📆 дата (yyyy-mm-dd): ")
    time = input("⏰ час (hh:mm): ")
    desc = input("✏️ опис: ")

    planner[str(event_id)] = {
        "title": title,
        "date": date,
        "time": time,
        "desc": desc
    }

    save_events(planner)
    print("✅ подію додано")
    return event_id + 1

def show_events(planner):
    if not planner:
        print("📭 подій немає")
        return

    for id, e in planner.items():
        print(f"\nid: {id}")
        print(f"📝 {e['title']}")
        print(f"📆 {e['date']} ⏰ {e['time']}")
        print(f"✏️ {e['desc']}")

def delete_event(planner):
    id = input("🗑️ введіть id події: ")
    if id in planner:
        del planner[id]
        save_events(planner)
        print("🗑️ подію видалено")
    else:
        print("❌ подію не знайдено")

def find_by_date(planner):
    date = input("🔍 введіть дату (yyyy-mm-dd): ")
    found = False

    for id, e in planner.items():
        if e["date"] == date:
            print(f"\nid: {id}")
            print(f"📝 {e['title']} ⏰ {e['time']}")
            print(f"✏️ {e['desc']}")
            found = True

    if not found:
        print("❌ подій на цю дату немає")

def main():
    planner, event_id = load_events()

    while True:
        show_menu()
        choice = input("➡️ оберіть дію: ")

        if choice == "1":
            event_id = add_event(planner, event_id)

        elif choice == "2":
            show_events(planner)

        elif choice == "3":
            delete_event(planner)

        elif choice == "4":
            find_by_date(planner)

        elif choice == "5":
            print("👋 до побачення")
            break

        else:
            print("❗ невірний вибір")

if __name__ == "__main__":
    main()