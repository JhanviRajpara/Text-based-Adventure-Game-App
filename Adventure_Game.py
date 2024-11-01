import tkinter as tk
from tkinter import messagebox

class AdventureGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Text-Based Adventure Game")
        self.root.geometry("500x400")

        # Initialize game state
        self.story_text = tk.StringVar()
        self.story_text.set("Welcome to the Adventure Game!\nYou are standing in a dark forest.\n"
                            "Will you go left or right?")

        # Story display
        story_label = tk.Label(root, textvariable=self.story_text, wraplength=400, font=("Arial", 14))
        story_label.pack(pady=20)

        # Choice buttons
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=20)

        self.left_button = tk.Button(self.button_frame, text="Left", font=("Arial", 14), command=self.choose_left)
        self.left_button.grid(row=0, column=0, padx=20)

        self.right_button = tk.Button(self.button_frame, text="Right", font=("Arial", 14), command=self.choose_right)
        self.right_button.grid(row=0, column=1, padx=20)

    def choose_left(self):
        self.story_text.set("You walk left and find a river.\nWill you swim across or build a raft?")
        self.left_button.config(text="Swim", command=self.choose_swim)
        self.right_button.config(text="Build Raft", command=self.choose_raft)

    def choose_right(self):
        self.story_text.set("You walk right and encounter a wild animal.\nWill you fight or run?")
        self.left_button.config(text="Fight", command=self.choose_fight)
        self.right_button.config(text="Run", command=self.choose_run)

    def choose_swim(self):
        self.story_text.set("You try to swim across but the current is too strong.\nYou didn't make it. Game Over.")
        self.end_game()

    def choose_raft(self):
        self.story_text.set("You successfully build a raft and cross the river.\nYou find a treasure! You Win!")
        self.end_game()

    def choose_fight(self):
        self.story_text.set("You fight bravely but the animal overpowers you.\nGame Over.")
        self.end_game()

    def choose_run(self):
        self.story_text.set("You run and escape safely.\nYou find a hidden path to a treasure! You Win!")
        self.end_game()

    def end_game(self):
        # Disable buttons and show restart option
        self.left_button.config(state="disabled")
        self.right_button.config(state="disabled")
        restart_button = tk.Button(self.root, text="Play Again", font=("Arial", 14), command=self.restart_game)
        restart_button.pack(pady=10)

    def restart_game(self):
        self.story_text.set("Welcome to the Adventure Game!\nYou are standing in a dark forest.\n"
                            "Will you go left or right?")
        self.left_button.config(text="Left", state="normal", command=self.choose_left)
        self.right_button.config(text="Right", state="normal", command=self.choose_right)

if __name__ == "__main__":
    root = tk.Tk()
    app = AdventureGame(root)
    root.mainloop()
