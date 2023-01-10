import random

def play_game():
    options = ['rock', 'paper', 'scissors']

    # Get player's choice
    player = input("Enter rock, paper, or scissors: ").lower()
    while player not in options:
        player = input("Invalid choice. Enter rock, paper, or scissors: ").lower()

    # Get computer's choice
    computer = random.choice(options)

    # Compare choices and determine winner
    if player == computer:
        print("It's a tie!")
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'scissors' and computer == 'paper') or \
         (player == 'paper' and computer == 'rock'):
        print("You win! Got some swagssss")
    else:
        print("You lose!")

if __name__ == "__main__":
    play_game()
