# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

import pandas

data = pandas.read_csv("E:\\python on udemy\\Day26\\nato_phonetic_alphabet.csv")
# print(data)
data_letters = {row.letter:row.code for  (index,row) in data.iterrows()}
# print(data_letters)


user_input = input("please enter your name :").upper()
new_name=[data_letters[letters] for letters in user_input]
print(new_name)
