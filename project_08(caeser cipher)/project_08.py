import art
print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def caesar(type ,text, shift) :
    encrypted_word = ""
    
    for letter in text :
        if letter in alphabet :
            index = alphabet.index(letter)
            if type == "encode" :
                encrypted_word += alphabet[index + shift]
            elif type == "decode" :
                encrypted_word += alphabet[index - shift]
        else :
            encrypted_word += letter
    print (encrypted_word)

# def decrypt(text , shift) :
#     decrypted_word = ""
#     for letter in text :
#         index = alphabet.index(letter)
#         decrypted_word += alphabet[index - shift]
#     print (decrypted_word)


repeat = True

while repeat :
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    repeat = True


    if direction == "encode" :
        caesar("encode",text,shift)
    elif direction == "decode" :
        caesar("decode",text,shift)
    else: 
        print("plz enter a valid type of incryption")
    is_rapeat = input ("do you want to rapeat ? Yes or No . ")
    if is_rapeat == "No" :
        repeat = False
        print("Goodby")
    elif is_rapeat == "Yes" :
        repeat = True 
    else: 
        print("plz enter a valued word !")
        repeat = False
    