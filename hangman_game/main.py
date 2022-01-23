import random
import hangman_words
import ASCII_art

print(ASCII_art.hangman_logo)
print(ASCII_art.hangman_pics_mid[0] + "\n")

# Word List computer chooses random word from list
chosen_word = random.choice(hangman_words.word_list)

# Create a list to display blanks
display = []
guesses = []

for i in chosen_word:
    display.append("_")

# Make Game loop
game_loop = True

# Add a counter for number of tries
counter = 0

while game_loop:

    # Asks user for a letter
    guess = input("Guess a letter: ").lower()
    letter_check = guess[0]

    for i in range(len(chosen_word)):

        if letter_check in chosen_word[i]:
            display[i] = letter_check

    if letter_check in guesses:
        print("You already guessed this letter. Try again")

    elif letter_check in chosen_word:
        print(f"------------------------------------------------\nYou guessed {guess}. That IS is the word. Nice!")
        print(ASCII_art.hangman_pics_left[counter])

    elif letter_check not in chosen_word:
        print(f"------------------------------------------------\nYou guessed {guess}. That is not in the word")
        counter += 1
        print(ASCII_art.hangman_pics_left[counter])

    print("\n")
    for i in range(len(display)):
        print(display[i], end=" ")

    if "_" not in display:
        print("\n\nYou figured out the word. You Win!")
        game_loop = False
        break

    if counter == 6:
        print(f"\n\nYour hangman is hanged. You Lose! Your word was {chosen_word}")
        game_loop = False
        break

    guesses.append(letter_check)
    print("\n")
