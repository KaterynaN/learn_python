import pandas

#TODO 1. Create a dictionary:
data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    name = list(input("Enter your name: ").upper())
    try:
        output_list = [nato_dict[letter] for letter in name]
    except KeyError:
        print("Only letters!")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()




