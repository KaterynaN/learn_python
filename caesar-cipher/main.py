alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

def caesar(text, shift, direction):
    list = []
    for letter in text:
        list += letter
    if direction == 'decode':
        shift *= -1
    for i in range(len(list)):
        if list[i] in alphabet:
            letter_index = alphabet.index(list[i]) + shift
            if letter_index < 0:
                letter_index += 26
            elif letter_index > 25:
                letter_index -= 26
            list[i] = alphabet[letter_index]
    print(f"The {direction}d text is '{''.join(list)}'")

from art import logo
print(logo)

is_continuing = True

while is_continuing:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    continued = input(
        "Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if continued == 'no':
        is_continuing = False
