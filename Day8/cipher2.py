def encrypt(plain_text,shiftAmount):
    cipher=""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position+shiftAmount
        new_letter=alphabet[new_position]
        cipher += new_letter
    print(f"your encoded result is {cipher}")
def decrypt(cypher_text,shiftAmount):
    cipher=""
    for letter in cypher_text:
        position = alphabet.index(letter)
        new_position = position-shiftAmount
        new_letter=alphabet[new_position]
        cipher += new_letter
    print(f"your decoded result is {cipher}")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
i=1
while i:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == "encode":
        encrypt(plain_text=text, shiftAmount=shift)
    elif direction=="decode":
        decrypt(cypher_text=text,shiftAmount=shift)
    else:
        break
    res=int(input("do you want to continue? for yes 1 and for no 0 \n"))
    if(res == 1):
        i=1
    else:
        i=0