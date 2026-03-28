import random

game_over = False
player = {}

def create_character():
    global player
    name = input("Введи ім'я персонажа: ")
    player = {
        "name": name,
        "hp": 100,
        "attack": 15,
        "gold": 0,
        "inventory": []
    }

def show_status():
    print("\n--- СТАТУС ---")
    print("Ім'я:", player["name"])
    print("HP:", player["hp"])
    print("Атака:", player["attack"])
    print("Золото:", player["gold"])
    print("Інвентар:", player["inventory"] if player["inventory"] else "порожній")

def choose_action():
    print("\nОберіть дію:")
    print("1 — Подорожувати")
    print("2 — Статус")
    print("3 — Інвентар")
    print("4 — Вийти")

    try:
        choice = int(input("Ваш вибір: "))
        if choice not in [1, 2, 3, 4]:
            raise ValueError
        return choice
    except ValueError:
        print("Помилка: введіть число від 1 до 4")
        return None

def fight():
    enemy_hp = random.randint(30, 60)
    enemy_attack = random.randint(5, 12)

    print("\n⚔️ З'явився ворог!")

    while enemy_hp > 0 and player["hp"] > 0:
        print("\n1 — Атакувати")
        print("2 — Захищатися")
        print("3 — Втекти")

        choice = input("Ваш вибір: ")

        if choice == "1":
            damage = player["attack"]
            enemy_hp -= damage
            print(f"Ви нанесли {damage} урону")

        elif choice == "2":
            reduced = enemy_attack // 2
            player["hp"] -= reduced
            print(f"Ви захистились. Отримали {reduced} урону")
            continue

        elif choice == "3":
            print("Ви втекли з бою")
            return

        else:
            print("Невірна команда")
            continue

        if enemy_hp > 0:
            player["hp"] -= enemy_attack
            print(f"Ворог атакує! Ви отримали {enemy_attack} урону")

    if player["hp"] <= 0:
        end_game(False)
    else:
        reward = random.randint(10, 30)
        player["gold"] += reward
        print(f"🎉 Ворог переможений! Золото +{reward}")

def random_event():
    event = random.choice(["enemy", "gold", "potion", "nothing"])

    if event == "enemy":
        fight()
    elif event == "gold":
        gold = random.randint(5, 20)
        player["gold"] += gold
        print(f"💰 Ви знайшли {gold} золота")
    elif event == "potion":
        player["inventory"].append("зілля")
        print("🧪 Ви знайшли зілля")
    else:
        print("Нічого не відбулося")

def use_inventory():
    if not player["inventory"]:
        print("Інвентар порожній")
        return

    print("1 — Використати зілля")
    choice = input("Ваш вибір: ")

    if choice == "1" and "зілля" in player["inventory"]:
        player["inventory"].remove("зілля")
        player["hp"] += 25
        print("HP +25")
    else:
        print("Невірний вибір")

def end_game(win):
    global game_over
    game_over = True
    if win:
        print("\n🏆 Ви перемогли у грі!")
    else:
        print("\n💀 Ви програли. HP = 0")

def game_loop():
    global game_over

    while not game_over and player["hp"] > 0:
        action = choose_action()
        if action is None:
            continue

        if action == 1:
            random_event()
            if player["gold"] >= 100:
                end_game(True)

        elif action == 2:
            show_status()

        elif action == 3:
            use_inventory()

        elif action == 4:
            end_game(False)

print("🎮 Ласкаво просимо до RPG!")
create_character()
game_loop()