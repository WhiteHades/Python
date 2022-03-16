# Cypher

from unittest import result


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def cypher(start_text, shiftamount, cypher_direction):
    end_text = ""
    if cypher_direction == "decode":
        shiftamount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shiftamount
            end_text += alphabet[new_position]
        else:
            end_text += char

    print(f"The {cypher_direction}d text is {end_text}.\n")


should_continue = True
while should_continue:
    direction = input(
        "Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    cypher(start_text=text, shiftamount=shift, cypher_direction=direction)
    result = input(
        "Type 'yes' if you want to go again. Otherwise, type 'no'.\n")
    if result == "no":
        should_continue = False
        print("Goodbye.")
