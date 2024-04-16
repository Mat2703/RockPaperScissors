import random

class RockPaperScissors:
    choices = [
        "water", "dragon", "devil", "gun", "rock",
        "fire", "scissors", "snake", "human", "tree",
        "wolf", "sponge", "paper", "air", "lightning"
    ]
    choices_default = ["rock", "paper", "scissors"]
    wins_against_default = {
        "rock": ["scissors"],
        "paper": ["rock"],
        "scissors": ["paper"]
    }
    wins_against = {
        'rock': ['lizard'],
        'paper': ['rock', 'spock'],
        'scissors': ['paper','rock'],
        'lizard': ['paper','scissors'],
        'spock': ['scissors', 'lizard'],
        'water': ['scissors', 'fire', 'rock', 'gun', 'lightning', 'devil', 'dragon'],
        'dragon': ['snake', 'scissors', 'fire', 'rock', 'gun', 'lightning', 'devil'],
        'devil': ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun'],
        'gun': ['wolf', 'tree', 'human', 'snake', 'scissors', 'fire', 'rock'],
        'fire': ['paper', 'sponge', 'wolf', 'tree', 'human', 'snake', 'scissors'],
        'snake': ['water', 'air', 'paper', 'sponge', 'wolf', 'tree', 'human'],
        'human': ['dragon', 'water', 'air', 'paper', 'sponge', 'wolf', 'tree'],
        'tree': ['devil', 'dragon', 'water', 'air', 'paper', 'sponge', 'wolf'],
        'wolf': ['lightning', 'devil', 'dragon', 'water', 'air', 'paper', 'sponge'],
        'sponge': ['gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'paper'],
        'air': ['fire', 'rock', 'gun', 'lightning', 'devil', 'dragon', 'water'],
        'lightning': ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun']
    }

    def __init__(self, filename="rating.txt"):
        self.filename = filename
        self.name = input("Enter your name: ")
        print(f"Hello, {self.name}")
        self.rating = self.get_rating()
        print(f"Your rating is {self.rating}")
        self.configure_game()

    def get_rating(self):
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    parts = line.strip().split()
                    if len(parts) < 2:
                        continue
                    if parts[0] == self.name:
                        return int(parts[1])
        except FileNotFoundError:
            open(self.filename, 'a').close()
        return 0

    def update_rating_file(self):
        found = False
        lines = []
        try:
            with open(self.filename, 'r+') as file:
                lines = file.readlines()
                file.seek(0)
                file.truncate()
                for line in lines:
                    parts = line.strip().split()
                    if parts[0] == self.name:
                        line = f"{self.name} {self.rating}\n"
                        found = True
                    file.write(line)
        except FileNotFoundError:
            pass  # If file doesn't exist, it will be created in the if not found block below

        if not found:
            with open(self.filename, 'a') as file:
                file.write(f"{self.name} {self.rating}\n")

    def configure_game(self):
        options_input = input("Enter game options separated by a comma, or press enter for default: ")
        if options_input.strip():
            self.active_choices = [option.strip() for option in options_input.split(',')]
            # Assuming all custom options are valid and exist in 'wins_against'
            self.active_wins_against = {key: self.wins_against[key] for key in self.active_choices if key in self.wins_against}
        else:
            self.active_choices = self.choices_default
            self.active_wins_against = self.wins_against_default
        print("Okay, let's start")
        self.game_loop()

    def game_loop(self):
        while True:
            player_input = input(">").lower()
            if player_input == "!exit":
                self.update_rating_file()
                print("Bye!")
                break
            elif player_input == "!rating":
                print(f"Your rating: {self.rating}")
            elif player_input in self.active_choices:
                self.play_round(player_input)
            else:
                print("Invalid input")

    def play_round(self, player_choice):
        computer_choice = random.choice(self.active_choices)
        if player_choice == computer_choice:
            print(f"There is a draw ({computer_choice})")
            self.rating += 50
        elif computer_choice in self.active_wins_against.get(player_choice, []):
            print(f"Well done. The computer chose {computer_choice} and failed.")
            self.rating += 100
        else:
            print(f"Sorry, but the computer chose {computer_choice}.")

if __name__ == "__main__":
    game = RockPaperScissors()
