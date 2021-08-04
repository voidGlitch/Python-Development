def caeser(plain_text,shift_amount,cipher_direction):
    cipher=""
    if cipher_direction =="decode" :
        shift_amount = shift_amount * -1
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter=alphabet[new_position]
        cipher +=new_letter
    print(f"your {cipher_direction}d word is {cipher}")


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
i=1
while i:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caeser(plain_text=text,shift_amount=shift,cipher_direction=direction)
        


    res=int(input("do you want to continue? for yes 1 and for no 0 \n"))
    if(res == 1):
        i=1
    else:
        i=0