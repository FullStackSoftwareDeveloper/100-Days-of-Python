import pandas

user = input("Write your name: ")

alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

dict_nato = {row.letter:row.code for (index, row) in alphabet.iterrows()}

name_letters = [dict_nato[n] for n in user.upper()]

print(name_letters)