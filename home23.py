import tkinter as tk
import random

choices = ["камінь", "ножиці", "папір"]

def play(user_choice):
    computer_choice = random.choice(choices)

    result_text.set(f"ти: {user_choice} | комп'ютер: {computer_choice}")

    if user_choice == computer_choice:
        winner.set("нічия 🤝")
    elif (
        (user_choice == "камінь" and computer_choice == "ножиці") or
        (user_choice == "ножиці" and computer_choice == "папір") or
        (user_choice == "папір" and computer_choice == "камінь")
    ):
        winner.set("ти виграв 🎉")
    else:
        winner.set("комп'ютер виграв 🤖")

window = tk.Tk()
window.title("камінь • ножиці • папір")
window.geometry("350x300")
window.configure(bg="#6e0000")

title = tk.Label(
    window,
    text="камінь • ножиці • папір",
    font=("Arial", 18, "bold"),
    bg="#6e0000"
)
title.pack(pady=15)

frame = tk.Frame(window, bg="#f0f4ff")
frame.pack()

btn_style = {
    "font": ("Arial", 12, "bold"),
    "width": 10,
    "height": 2,
    "bd": 0
}

tk.Button(frame, text="🪨 камінь",
          command=lambda: play("камінь"), **btn_style).grid(row=0, column=0, padx=5, pady=5)

tk.Button(frame, text="✂️ ножиці",
          command=lambda: play("ножиці"), **btn_style).grid(row=0, column=1, padx=5, pady=5)

tk.Button(frame, text="📄 папір",
          command=lambda: play("папір"), **btn_style).grid(row=0, column=2, padx=5, pady=5)

result_text = tk.StringVar()
winner = tk.StringVar()

result_label = tk.Label(window, textvariable=result_text,
                        font=("Arial", 12), bg="#6E0000")
result_label.pack(pady=15)

winner_label = tk.Label(window, textvariable=winner,
                        font=("Arial", 14, "bold"), bg="#6e0000")
winner_label.pack()

window.mainloop()