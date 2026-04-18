import tkinter as tk
from tkinter import messagebox

Word bank
levels = [
    {"word": "cat", "hint": "A small pet"},
    {"word": "tree", "hint": "Grows in forests"},
    {"word": "apple", "hint": "A common fruit"},
    {"word": "river", "hint": "Flows with water"},
    {"word": "planet", "hint": "Earth is one"},
    {"word": "silver", "hint": "A shiny metal"},
    {"word": "mystery", "hint": "Something unknown"},
    {"word": "adventure", "hint": "An exciting journey"},
    {"word": "knowledge", "hint": "Gained by learning"},
    {"word": "spellbound", "hint": "Completely fascinated"}
]

current_level = 0

How the application works
def load_level():
    global current_word
    level_data = levels[current_level]
    current_word = level_data["word"]

    level_label.config(text=f"Level {current_level + 1}")
    hint_label.config(text=f"Hint: {level_data['hint']}")
    word_label.config(text=" ".join("_" * len(current_word)))
    entry.delete(0, tk.END)
    message_label.config(text="")

def check_guess():
    global current_level

    guess = entry.get().lower()

    if len(guess) != len(current_word):
        message_label.config(text=f"Must be {len(current_word)} letters!")
        return

    if guess == current_word:
        messagebox.showinfo("Correct!", "Nice job!")
        current_level += 1

        if current_level < len(levels):
            load_level()
        else:
            messagebox.showinfo("🎉 Winner!", "You completed all levels!")
            root.quit()
    else:
        message_label.config(text="Try again!")

# Game code
root = tk.Tk()
root.title("Spellbound Game")
root.geometry("400x400")

title = tk.Label(root, text="Welcome to Spellbound!", font=("Arial", 18))
title.pack(pady=10)

subtitle = tk.Label(root, text="A word guessing game")
subtitle.pack()

level_label = tk.Label(root, text="", font=("Arial", 14))
level_label.pack(pady=10)

word_label = tk.Label(root, text="", font=("Arial", 24))
word_label.pack(pady=10)

hint_label = tk.Label(root, text="", font=("Arial", 10, "italic"))
hint_label.pack(pady=5)

entry = tk.Entry(root, font=("Arial", 14), justify="center")
entry.pack(pady=10)

submit_btn = tk.Button(root, text="Submit", command=check_guess)
submit_btn.pack()

message_label = tk.Label(root, text="", fg="red")
message_label.pack(pady=10)

#start game
load_level()
root.mainloop()