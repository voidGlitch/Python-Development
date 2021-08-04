import random
#Step 1 


word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.


# list = random.randint(0,len(word_list)-1)
# print(word_list[list])
# chosen_word = word_list[list]

#or

chosen_word = random.choice(word_list)

guess = input("guess a letter  : \n")
guess = guess.lower()
print(f"you have entered the word {guess}")

for letter in chosen_word:

    if letter == guess:
        print("guess is true")
    else:
        print("guess is wrong")