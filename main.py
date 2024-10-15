import pandas

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_phonetic_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(nato_phonetic_alphabet)

nato_dict = {row.letter: row.code for (index, row) in nato_phonetic_alphabet.iterrows()}
# print(nato_dict)
# print(nato_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.


def generate_phonetic():
    word = input("please insert a word: ").upper()
    try:
        nato_list = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_phonetic()
    else:
        print(nato_list)


generate_phonetic()
