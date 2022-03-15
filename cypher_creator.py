# Cypher

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input(
    "Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plaintext, shiftamount):
    cypher_word = ""
    for letter in plaintext:
        position = alphabet.index(letter)
        n_position = position + shiftamount
        n_letter = alphabet[n_position]
        cypher_word += n_letter
    print(f"The encoded text is {cypher_word}")


encrypt(plaintext=text, shiftamount=shift)
