# def format_name(f_name , l_name) :
#     """take first name and last name and mirge them in full name with title """
#     if f_name == "" or l_name == "" :
#         return "You didn't provide valid name  !!"
#     new_f_name = f_name.title()
#     new_l_name = l_name.title()
#     full_name = new_f_name +" "+ new_l_name
#     return full_name
import os
# print(format_name(input("plz enter your first name ? "),input("plz enter your last name ? ")))
# format_name()
def clear() :
    os.system("cls")
def add(n1 , n2) :
    return n1 +n2 
def subtract(n1 , n2) :
    return n1 - n2 
def multiply(n1 , n2) :
    return n1 * n2
def divide( n1 , n2) :
    return n1 / n2 

operations = {
    "+" :add ,
    "-" : subtract ,
    "*" : multiply ,
    "/" :divide ,
 }
def clculation() :
    repeat = True 
    num1 = int(input("enter the first number : "))

    while repeat :
        for key in operations :
            print(key)
        ask = input("enter the operation type you wante to do : ")
        num2 = int(input("enter the second number : "))

        calc_func = operations[ask]
        result = calc_func(num1 , num2)
        print(f"{num1} {ask} {num2} = {result}")
        rep = input("type 'yes' to continue calculation or 'no' to exit or 'new' to start from the begining : ")
        if rep == "yes" :
            num1 = result
            repeat = True
        elif rep == "no" :
            repeat = False
        elif rep == "new" :
            repeat = False
            clear()
            clculation()
clculation()

