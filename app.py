import random
import tkinter as tk
from tkinter import messagebox

class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Number Guessing Game")

        self.max_attempts = 10
        self.secret_number = random.randint(1, 100)
        self.total_attempts = 0
        self.games_played = 0

        self.label_intro = tk.Label(self.master, text="Welcome to the Number Guessing Game!")
        self.label_intro.pack(pady=10)

        self.label_instruction = tk.Label(self.master, text="Guess a number between 1 and 100:")
        self.label_instruction.pack()

        self.entry_guess = tk.Entry(self.master, width=10)
        self.entry_guess.pack(pady=5)

        self.button_guess = tk.Button(self.master, text="Guess", command=self.check_guess)
        self.button_guess.pack(pady=10)

        self.button_reset = tk.Button(self.master, text="Reset", command=self.reset_game)
        self.button_reset.pack(pady=5)

        self.label_result = tk.Label(self.master, text="")
        self.label_result.pack()

        self.label_attempts = tk.Label(self.master, text="Total attempts: 0")
        self.label_attempts.pack()

        self.label_games = tk.Label(self.master, text="Games played: 0")
        self.label_games.pack()

    def check_guess(self):
        guess = self.get_guess()
        if guess is None:
            return

        self.total_attempts += 1

        if self.total_attempts > self.max_attempts:
            result = f"Sorry, you've exceeded the maximum of {self.max_attempts} attempts. The correct number was {self.secret_number}."
            self.games_played += 1
            self.reset_secret_number()
        elif guess < self.secret_number:
            result = "Too low! Try again."
        elif guess > self.secret_number:
            result = "Too high! Try again."
        else:
            self.games_played += 1
            average_attempts = self.total_attempts / self.games_played
            result = f"Congratulations! You guessed it right in {self.total_attempts} attempts. Average attempts per game: {average_attempts:.2f}"
            self.reset_secret_number()

        self.update_labels(result)
        self.entry_guess.delete(0, tk.END)

    def get_guess(self):
        try:
            guess = int(self.entry_guess.get())
            if guess < 1 or guess > 100:
                self.update_labels("Error: Please enter a number between 1 and 100.")
                return None
            return guess
        except ValueError:
            self.update_labels("Error: Please enter a valid number.")
            return None

    def reset_secret_number(self):
        self.secret_number = random.randint(1, 100)
        self.total_attempts = 0

    def reset_game(self):
        self.reset_secret_number()
        self.total_attempts = 0
        self.games_played = 0
        self.update_labels("Game reset. Start guessing again!")

    def update_labels(self, result):
        self.label_result.config(text=result)
        self.label_attempts.config(text=f"Total attempts: {self.total_attempts}")
        self.label_games.config(text=f"Games played: {self.games_played}")

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()
