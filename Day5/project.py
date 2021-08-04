import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))

nr_numbers = int(input(f"How many numbers would you like?\n"))
# for easy version

# password= ""
# for n in range(1,nr_letters+1):
# #   random_letter = random.randint(0,len(letters))
# #   # print(random_letter) prints the random numbers
# #   print(letters[random_letter])

# #or you can write

#     random_letters = random.choice(letters)
#     # print(random_letters)
#     password = password + random_letters
#     # print(password)
# # print(f"your final password is {password} ")




# for n in range(1,nr_symbols+1):
# #   random_letter = random.randint(0,len(letters))
# #   # print(random_letter) prints the random numbers
# #   print(letters[random_letter])

# #or you can write

#     random_symbols = random.choice(symbols)
#     # print(random_symbols)
#     password = password + random_symbols
#     # print(password)
# # print(f"your final password is {password} ")





# for n in range(1,nr_numbers+1):
# #   random_letter = random.randint(0,len(letters))
# #   # print(random_letter) prints the random numbers
# #   print(letters[random_letter])

# #or you can write

#     random_numbers = random.choice(numbers)
#     # print(random_numbers)
#     password = password + random_numbers
#     # print(password)
# print(f"your final password is {password} ")

# for hard version
password_list = []

for char in range(1,nr_letters+1):

    password_list += random.choice(letters)

for char in range(1,nr_symbols+1):

    password_list += random.choice(symbols)


for char in range(1,nr_numbers+1):


    password_list = password_list + [random.choice(numbers)]
 # or 
    # password_list += random.choice(numbers)
print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password = password + char

print(f"you final password is : {password}" )