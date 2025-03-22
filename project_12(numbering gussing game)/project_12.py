logo = '''
 _______               ___.                .__                   ________                    .__                
 \      \  __ __  _____\_ |__   ___________|__| ____    ____    /  _____/ __ __  ______ _____|__| ____    ____  
 /   |   \|  |  \/     \| __ \_/ __ \_  __ \  |/    \  / ___\  /   \  ___|  |  \/  ___//  ___/  |/    \  / ___\ 
/    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/  |   |  \/ /_/  > \    \_\  \  |  /\___ \ \___ \|  |   |  \/ /_/  >
\____|__  /____/|__|_|  /___  /\___  >__|  |__|___|  /\___  /   \______  /____//____  >____  >__|___|  /\___  / 
        \/            \/    \/     \/              \//_____/           \/           \/     \/        \//_____/  
'''

from cgitb import handler
import random
from timeit import repeat
print(logo)
print("Welcom to numbering gussing game !")
rand_num = random.randint(1,100)
print("I am thinking of a number between '1' and '100' ")
lives = 0
print(f"the correct number is : {rand_num}")
def if_error() :
    level = input ("choose the difficulty , type 'easy' or 'hard' : ").strip()
    global lives

    if level == "easy" :
        lives = 10
        print(f"you have {lives} attempts remaining to guess the number.")
    elif level == "hard":
        lives = 5
        print(f"you have {lives} attempts remaining to guess the number.")
    else :
        print("Wrong answer , you must choose 'easy' or 'hard' . ")
        if_error()
if_error()

  
while lives > 0 :
    user_num = int(input("Make a guess : "))

    if user_num > rand_num :
        print("too high . \nguess again")
        lives -= 1
        
    elif user_num < rand_num :
        print("too low . \nguess again .")
        lives -= 1
        print(f"you have {lives} attempts remaining to guess the number. ")
    elif user_num == rand_num :
        print("that is Correct , you Win . " + ":)")
        lives = 0    
    else :
        print("you lose .")




