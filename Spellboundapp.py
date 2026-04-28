import tkinter as tk
from tkinter import messagebox

# Word bank (30 levels total)
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
    {"word": "spellbound", "hint": "Completely fascinated"},
    {"word": "house", "hint": "A place to live"},
    {"word": "chair", "hint": "Used for sitting"},
    {"word": "bread", "hint": "Baked food"},
    {"word": "clock", "hint": "Tells time"},
    {"word": "ocean", "hint": "Large body of water"},
    {"word": "bridge", "hint": "Connects two sides"},
    {"word": "garden", "hint": "Place where flowers grow"},
    {"word": "window", "hint": "You look through it"},
    {"word": "thunder", "hint": "Loud storm sound"},
    {"word": "diamond", "hint": "A precious stone"},
    {"word": "library", "hint": "Place full of books"},
    {"word": "blanket", "hint": "Keeps you warm"},
    {"word": "journey", "hint": "A trip somewhere"},
    {"word": "freedom", "hint": "State of being free"},
    {"word": "picture", "hint": "An image or photo"},
    {"word": "captain", "hint": "Leader of a ship"},
    {"word": "sunrise", "hint": "Morning start of the day"},
    {"word": "treasure", "hint": "Hidden valuable reward"},
    {"word": "mountain", "hint": "Very high landform"},
    {"word": "champion", "hint": "A winner"}
]

current_level = 0

def load_level():
    global current_word
    level_data = levels[current_level]
    current_word = level_data["word"]

    level_label.config(text=f"⭐ Level {current_level + 1} ⭐")
    hint_label.config(text=f"💡 Hint: {level_data['hint']}")
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
            messagebox.showinfo("🏆 Winner!", "You completed all 30 levels!")
            root.quit()
    else:
        message_label.config(text="❌ Try again!")

# Main window
root = tk.Tk()
root.title("Spellbound Game")
root.geometry("500x500")
root.configure(bg="#1e1e2f")

# Title Screen Design
title = tk.Label(
    root,
    text="✨ SPELLBOUND ✨",
    font=("Impact", 28),
    fg="gold",
    bg="#1e1e2f"
)
title.pack(pady=20)

subtitle = tk.Label(
    root,
    text="Enter a world of mystery and word magic!",
    font=("Arial", 14, "italic"),
    fg="white",
    bg="#1e1e2f"
)
subtitle.pack()

desc = tk.Label(
    root,
    text="Guess the hidden words, unlock levels,\nand become the Word Champion!",
    font=("Arial", 12),
    fg="lightblue",
    bg="#1e1e2f"
)
desc.pack(pady=15)

level_label = tk.Label(root, text="", font=("Arial", 16, "bold"), fg="white", bg="#1e1e2f")
level_label.pack(pady=10)

word_label = tk.Label(root, text="", font=("Arial", 28, "bold"), fg="cyan", bg="#1e1e2f")
word_label.pack(pady=10)

hint_label = tk.Label(root, text="", font=("Arial", 11, "italic"), fg="yellow", bg="#1e1e2f")
hint_label.pack(pady=5)

entry = tk.Entry(root, font=("Arial", 16), justify="center", width=20)
entry.pack(pady=15)

submit_btn = tk.Button(
    root,
    text="Submit Guess",
    command=check_guess,
    font=("Arial", 14, "bold"),
    bg="gold",
    fg="black",
    width=18
)
submit_btn.pack(pady=10)

message_label = tk.Label(root, text="", fg="red", bg="#1e1e2f", font=("Arial", 12))
message_label.pack(pady=10)

# Start game
load_level()
root.mainloop()
