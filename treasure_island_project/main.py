def start_game():
    print('''
    *******************************************************************************
              |                   |                  |                     |
     _________|________________.=""_;=.______________|_____________________|_______
    |                   |  ,-"_,=""     `"=.|                  |
    |___________________|__"=._o`"-._        `"=.______________|___________________
              |                `"=._o`"=._      _`"=._                     |
     _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
    |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
    |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
              |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
     _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
    |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
    |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
    ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
    /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
    ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
    /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
    ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
    /______/______/______/______/______/______/______/______/______/______/_____ /
    *******************************************************************************
    ''')
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.")
    first_choice = input("You are at a crossroad. Which way would you like to go, left or right? ").lower()

    if first_choice == "left":
        second_choice()

    else:
        print("You have fallen into a hole. Game over.")
        start_over = input("Would you like to play again? Y or N: ").upper()

        if start_over == "Y":
            print("\n\n")
            restart_game()


def restart_game():
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.")
    first_choice = input("You are at a crossroad. Which way would you like to go, left or right? ").lower()

    if first_choice == "left":
        second_choice()

    else:
        print("You have fallen into a hole. Game over.")
        start_over = input("Would you like to play again? Y or N: ").upper()

        if start_over == "Y":
            print("\n\n")
            restart_game()


def second_choice():
    second_choice_input = input('You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. ').lower()

    if second_choice_input == "wait":
        third_choice()

    else:
        start_over = input("Attacked by a trout. Game Over. Would you like to start again? Y or N: ").upper()

        if start_over == "Y":
            print("\n\n")
            restart_game()


def third_choice():
    third_choice_input = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. What color do you choose? ").lower()
    start_over = None

    if third_choice_input == "yellow":
        print("You have found the treasure. You Win!")

    elif third_choice_input == "red":
        start_over = input("You got burned by fire. Game Over. Would you like to start again? Y or N: ").upper()

        if start_over == "Y":
            print("\n\n")
            restart_game()

    elif third_choice_input == "blue":
        start_over = input("You have been eaten by beasts. Game Over. Would you like to start again? Y or N: ").upper()

        if start_over == "Y":
            print("\n\n")
            restart_game()
    else:
        start_over = input("Not a choice! Game Over. Would you like to start again? Y or N: ").upper()

        if start_over == "Y":
            print("\n\n")
            restart_game()


if __name__ == "__main__":
    start_game()
