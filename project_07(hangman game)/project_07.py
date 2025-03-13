from word_list import word_list
import random 
from hangman import stages
selected_word = random.choice(word_list)
display = []
len_of_selected_word = len(selected_word)
lives = 6
from hangman import logo
print(logo)

for num in range(len_of_selected_word) :
    display += "_"
end_of_game = False

while not end_of_game :
    guess = input("plz guess a letter : ").lower()
    for num in range(len_of_selected_word) :
        letter = selected_word[num]
        if guess == letter :
            if guess in display :
                print ("you already choose this letter")
            else:
                display [num] = letter
     
          
    print(f" ".join(display))
    if guess not in selected_word:
        lives -= 1
        if lives == 0 :
            print ("you lose")
            end_of_game = True
    if "_" not in display :
        print("you win")
        end_of_game = True
    
    print(stages[lives])
 

