# Guess the Number Game 🎮
import random
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)


# Function to show game over message
def game_over(correct_number):
    print(Fore.RED + f"\n💀 Game Over! The correct number was {correct_number} 💀\n")


# Function to choose difficulty level
def choose_difficulty():
    while True:
        difficulty = input(
            Fore.YELLOW + "Choose a difficulty level (easy/e, normal/n, hard/h): " + Style.RESET_ALL).lower()
        if difficulty in ("easy", "e"):
            return 10
        elif difficulty in ("normal", "n"):
            return 6
        elif difficulty in ("hard", "h"):
            return 3
        else:
            print(Fore.RED + "<< Invalid difficulty! Please try again >>")


# Main game loop
print(Fore.CYAN + "🎉 Welcome to the Guess The Number Game 🎉")
print(Fore.MAGENTA + "-" * 50)

while True:
    random_number = random.randint(1, 100)
    health = choose_difficulty()

    # Inner loop for guessing
    while health > 0:
        print(Fore.BLUE + f"❤️ Your health: {health}")

        # Get user input
        try:
            player_number = int(input(Fore.YELLOW + "Enter a number between 1 and 100: " + Style.RESET_ALL))
        except ValueError:
            print(Fore.RED + "<< Invalid input! Please enter a valid number. >>")
            continue

        # Check number range
        if not 1 <= player_number <= 100:
            print(Fore.RED + "<< Your number must be between 1 and 100! >>")
            continue

        # Check guess
        if player_number == random_number:
            print(Fore.GREEN + "\n🏆 Winner Winner Chicken Dinner! 🏆\n")
            break
        elif player_number < random_number:
            health -= 1
            print(Fore.CYAN + "Try a larger number!\n" + Style.RESET_ALL)
        else:
            health -= 1
            print(Fore.CYAN + "Try a smaller number!\n" + Style.RESET_ALL)

        if health == 0:
            game_over(random_number)

    # Ask to continue
    while True:
        continue_game = input(Fore.YELLOW + "Do you want to play again? (y/n): " + Style.RESET_ALL).lower()

        if continue_game in ("y", "yes"):
            break
        elif continue_game in ("n", "no"):
            print(Fore.MAGENTA + "\n👋 Thanks for playing! Goodbye!\n")
            print(Fore.MAGENTA + "-" * 50)
            exit()
        else:
            print(Fore.RED + "<< Invalid input! Please enter 'y' or 'n' >>")