import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
images = [rock , paper , scissors]
user_choose = int( input("please enter 0 for rock or 1 for paper or 2 for scissors. "))
print (f"you choose {user_choose}")
print(images[user_choose])
comp_choose = random.randint(0 , 2)
print (f"computer choose {comp_choose}")
print(images[comp_choose])

if user_choose == comp_choose :
    print(" its a draw ")
elif user_choose == 2 and comp_choose == 0 :
    print (" you loose ")
elif comp_choose == 2 and user_choose == 0 :
    print(" you win ")
elif comp_choose == 1 and user_choose == 0: