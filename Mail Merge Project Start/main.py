with open("./Input/Names/invited_names.txt", "r") as data:
    names = []
    for name in data.readlines():
        line = name.strip()
        names.append(line)

with open("./Input/Letters/starting_letter.txt") as start_file:
    starting_letter = start_file.read()

for name in names:
    letter = starting_letter.replace('[name]', name)
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", "w") as file:
        file.write(f"{letter}")