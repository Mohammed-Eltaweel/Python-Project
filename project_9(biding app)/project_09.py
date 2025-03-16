# from importlib.abc import Traversable

import os
# capitals ={
#     "France" :"paris" ,
#     "Germany":"Berline" ,
#     }
# #Nesting a list in Dictionary
# tavel_log = {
#     "France" :["paris","lille" , "dijane"] ,
#     "Germany" :["Berline" ,"Hamburge","Stuttgart"] ,
# }
# #Nesting a Dictionary in Dictionary
# tavel_log = {
#     "France" :{"cities_visited":["paris","lille" , "dijane"],"total_visits" :12 },
#     "Germany" :{"cities_visited":["Berline" ,"Hamburge","Stuttgart"] ,"total_visits" :13},
# }
# #Nesting Dictionary in a list 
# travel_log = [
#     {
#         "Country":"France",
#         "cities_visited":["paris","lille" , "dijane"],
#         "total_visits" :12 
#     },
#     {
#         "Country":"Germany" ,
#         "cities_visited":["Berline" ,"Hamburge","Stuttgart"] ,
#         "total_visits" :13
#     },
# ]
# print(travel_log)
def clear() :
    os.system("cls")

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)



dictionary = {}
reap = True
while reap :

    name = input( "what is your name ?: ")
    bid = int(input("what is your bid ?: $"))
    another_one = input("Are ther any other bidders ? Type 'yes' or 'no' \n")
    dictionary[name] = bid
    if another_one == "yes" :
        clear()
        reap = True
    elif another_one == "no" :
        reap = False
    else :
        print("plz enter a values name")
max = 0
winner = ""
for item in dictionary :
    if dictionary[item] > max :
        max = dictionary[item]
        winner = item
    
# val_lis = list(dictionary.values())
# keys_lis = list(dictionary.keys())
# position = val_lis.index(max)
# winner = keys_lis[position]
clear()
print(f"congratulation to ' {winner} ' with the largest bid = {max}")
    

