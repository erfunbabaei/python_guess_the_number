import random
from colorama import Fore, Style

print(Fore.CYAN + "Welcome to random number Game" + Style.RESET_ALL)

while True:

    randomNumber = random.randint(1, 100)

    health: int = 0

    def gameOver():
        print(Fore.GREEN + f"Game Over, The correct number is {randomNumber}" + Style.RESET_ALL)

    difficulty: str = str(input(Fore.YELLOW + "Choose a difficulty level( easy , normal , hard ): " + Style.RESET_ALL))

    if difficulty == "easy":
        health = 10
    elif difficulty == "e":
        health = 10
    elif difficulty == "normal":
        health = 6
    elif difficulty == "n":
        health = 6
    elif difficulty == "hard":
        health = 3
    elif difficulty == "h":
        health = 3
    else:
        print(Fore.RED + "<<Invalid difficulty>>" + Style.RESET_ALL)
        continue

    while health > 0:

        print(Fore.BLUE + f"Your health is: {health}" + Style.RESET_ALL)

        try:
            playerNumber:int = int(input(Fore.YELLOW + "Enter a number between 1 and 100: " + Style.RESET_ALL))
        except ValueError:
            print(Fore.RED + "<<Invalid input! Please enter a number.>>" + Style.RESET_ALL)
            continue

        if playerNumber > 100 or playerNumber < 1:
            print(Fore.RED + "<<Your number must be between 1 and 100>>" + Style.RESET_ALL)
            continue

        else:

            if playerNumber == randomNumber:
                print(Fore.CYAN + "winner winner chicken dinner!" + Style.RESET_ALL)
                break
            elif playerNumber < randomNumber:
                health -= 1
                if health == 0:
                    gameOver()
                    break
                else:
                    print(Fore.GREEN + "Try larger number!\n" + Style.RESET_ALL)

            elif playerNumber > randomNumber:
                health -= 1
                if health == 0:
                    gameOver()
                    break
                else:
                    print(Fore.GREEN + "Try smaller number!\n" + Style.RESET_ALL)

    continueGame: str = str(input(Fore.YELLOW + "Do you want to play again? (y/n): " + Style.RESET_ALL))

    if continueGame == "y":
        continue
    elif continueGame == "n":
        break
    else:
        print(Fore.RED + "<<Invalid input>>" + Style.RESET_ALL)
        continue