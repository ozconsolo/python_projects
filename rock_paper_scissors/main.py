import random
import time


def game_start():

    rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''

    # Write your code below this line 👇

    player_choice = input("Choose rock, paper, or scissors ").lower()
    computer_choice_random = random.randint(0, 2)

    if computer_choice_random == 0:
        computer_choice = "rock"
    elif computer_choice_random == 1:
        computer_choice = "paper"
    elif computer_choice_random == 2:
        computer_choice = "scissors"

    if player_choice == "rock":
        print(f"You chose rock\n{rock}")
        time.sleep(3)

        if computer_choice == "scissors":
            print(f"\nComputer chooses scissors\n{scissors}")
            restart_game = input("Rock beats Scissors. You Win! Would you like to play again? Type 'Y' or 'N' ").upper()

            if restart_game == "Y":
                game_start()

        elif computer_choice == "paper":
            print(f"\nComputer chooses paper\n{paper}")
            restart_game = input("Paper beats rock. You Lose. Would you like to play again? Type 'Y' or 'N' ").upper()

            if restart_game == 'Y':
                game_start()

        elif computer_choice == "rock":
            print(f"\nComputer chooses rock.\n{rock}")
            restart_game = input("Draw game. Would you like to play again? Type 'Y' or 'N ").upper()

            if restart_game == 'Y':
                game_start()

    if player_choice == "paper":
        print(f"You chose paper\n{paper}")
        time.sleep(3)

        if computer_choice == "scissors":
            print(f"\nComputer chooses scissors\n{scissors}")
            restart_game = input("Scissors beats Paper. You lose. Would you like to play again? Type 'Y' or 'N' ").upper()

            if restart_game == "Y":
                game_start()

        elif computer_choice == "paper":
            print(f"\nComputer chooses paper\n{paper}")
            restart_game = input("Draw game. Would you like to play again? Type 'Y' or 'N' ").upper()

            if restart_game == 'Y':
                game_start()

        elif computer_choice == "rock":
            print(f"\nComputer chooses rock.\n{rock}")
            restart_game = input("Paper beats Rock. You Win! Would you like to play again? Type 'Y' or 'N ").upper()

            if restart_game == 'Y':
                game_start()

    if player_choice == "scissors":
        print(f"You chose scissors\n{scissors}")
        time.sleep(3)

        if computer_choice == "scissors":
            print(f"\nComputer chooses scissors\n{scissors}")
            restart_game = input("Draw game. Would you like to play again? Type 'Y' or 'N' ").upper()

            if restart_game == "Y":
                game_start()

        elif computer_choice == "paper":
            print(f"\nComputer chooses paper\n{paper}")
            restart_game = input("Scissors beats Paper. You Win! Would you like to play again? Type 'Y' or 'N' ").upper()

            if restart_game == 'Y':
                game_start()

        elif computer_choice == "rock":
            print(f"\nComputer chooses rock.\n{rock}")
            restart_game = input("Rock beats Paper. You lose. Would you like to play again? Type 'Y' or 'N ").upper()

            if restart_game == 'Y':
                game_start()


if __name__ == "__main__":
    game_start()
