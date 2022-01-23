import art


def caesar(text, shift, direction):

    # alphabet list and encrypted text variable
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    encrypted_decrypted_text = ""

    # for each letter in text, the position is equal to the index in the alphabet in letter
    for letter in text:

        if letter in alphabet:
            position = alphabet.index(letter)

            if direction == "encode":
                if (position + shift) > len(alphabet) - 1:
                    position = (position + shift) % len(alphabet)
                    encrypted_decrypted_text += alphabet[position]

                else:
                    encrypted_decrypted_text += alphabet[position + shift]

            elif direction == "decode":
                if (position - shift) < 0:
                    position = (position - shift) % len(alphabet)
                    encrypted_decrypted_text += alphabet[position]

                else:
                    encrypted_decrypted_text += alphabet[position - shift]

        else:
            encrypted_decrypted_text += letter

    if direction == "encode":
        print(f"Your encrypted text is: {encrypted_decrypted_text}")
    else:
        print(f"Your decrypted text is {encrypted_decrypted_text}")


print(art.logo)
caesar_loop = True

while caesar_loop:

    direction_loop = True
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    while direction_loop:

        if direction != "encode" and direction != "decode":
            print("Error! Try Again")
            direction = input("Type 'encode' to encrypt, type 'decode to decrypt:\n")

        else:
            direction_loop = False

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)

    user_input = input("Would you like to go again? Type 'yes' or 'no': ").lower()
    print("\n")

    if user_input == "no":
        print("Goodbye!!!!")
        caesar_loop = False

