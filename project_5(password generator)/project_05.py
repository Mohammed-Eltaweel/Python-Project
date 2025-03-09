import random
from typing import final

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("""
                                                            _                                                  _                  
                                                           | |                                                | |                 
  _ __     __ _   ___   ___  __      __   ___    _ __    __| |     __ _    ___   _ __     ___   _ __    __ _  | |_    ___    _ __ 
 | '_ \   / _` | / __| / __| \ \ /\ / /  / _ \  | '__|  / _` |    / _` |  / _ \ | '_ \   / _ \ | '__|  / _` | | __|  / _ \  | '__|
 | |_) | | (_| | \__ \ \__ \  \ V  V /  | (_) | | |    | (_| |   | (_| | |  __/ | | | | |  __/ | |    | (_| | | |_  | (_) | | |   
 | .__/   \__,_| |___/ |___/   \_/\_/    \___/  |_|     \__,_|    \__, |  \___| |_| |_|  \___| |_|     \__,_|  \__|  \___/  |_|   
 | |                                                               __/ |                                                          
 |_|                                                              |___/                                                           
""")

nr_letters= int(input("How many letters would you like in your password : ")) 
nr_symbols = int(input(f"How many symbols would you like : "))
nr_numbers = int(input(f"How many numbers would you like : "))


symbole_rand = random.randint(0 , 8)
new_letters = []
for i in range( 0 , nr_letters) :
   
    new_letters += random.choice(letters)

new_number = ""
for i in range( 0 , nr_symbols ) :
   
    new_letters += random.choice(symbols)
new_symbol = ""
for i in range( 0 , nr_numbers ) :
    
    new_letters += random.choice(numbers)



random.shuffle(new_letters)
result = ""
for i in new_letters :
    result += i
print("_____________________________________")
print(f"\nYour password is : {result}")
print("_____________________________________\n")
