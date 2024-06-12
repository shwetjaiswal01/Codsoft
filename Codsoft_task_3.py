import tkinter as tk
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.user_choice = None
        self.computer_choice = None
        self.user_score = 0
        self.computer_score = 0

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Choose Rock, Paper or Scissors", font=("Arial", 14))
        self.label.pack(pady=10)

        self.score_label = tk.Label(self.root, text="Player: 0 - Computer: 0", font=("Arial", 14))
        self.score_label.pack(pady=10)

        self.rock_button = tk.Button(self.root, text="Rock", command=lambda: self.play("rock"))
        self.rock_button.pack(side=tk.LEFT, padx=20, pady=20)

        self.paper_button = tk.Button(self.root, text="Paper", command=lambda: self.play("paper"))
        self.paper_button.pack(side=tk.LEFT, padx=20, pady=20)

        self.scissors_button = tk.Button(self.root, text="Scissors", command=lambda: self.play("scissors"))
        self.scissors_button.pack(side=tk.LEFT, padx=20, pady=20)

        self.result_label = tk.Label(self.root, text="", font=("Arial", 14))
        self.result_label.pack(pady=20)

        self.reset_button = tk.Button(self.root, text="Reset", command=self.reset_game)
        self.reset_button.pack(pady=10)

    def play(self, user_choice):
        self.user_choice = user_choice
        self.computer_choice = random.choice(["rock", "paper", "scissors"])

        result = self.determine_winner()
        self.result_label.config(text=f"Computer chose: {self.computer_choice}\n{result}")
        self.update_score()

    def determine_winner(self):
        if self.user_choice == self.computer_choice:
            return "It's a tie!"
        elif (self.user_choice == "rock" and self.computer_choice == "scissors") or \
             (self.user_choice == "paper" and self.computer_choice == "rock") or \
             (self.user_choice == "scissors" and self.computer_choice == "paper"):
            self.user_score += 1
            return "You win!"
        else:
            self.computer_score += 1
            return "You lose!"

    def update_score(self):
        self.score_label.config(text=f"Player: {self.user_score} - Computer: {self.computer_score}")

    def reset_game(self):
        self.user_score = 0
        self.computer_score = 0
        self.update_score()
        self.result_label.config(text="")
        self.label.config(text="Choose Rock, Paper or Scissors")

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsGame(root)
    root.mainloop()
