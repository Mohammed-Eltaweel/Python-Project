# print("Welcom to the tip calculator. ")
# bill_amount = input("what was the total bill ?")
# tip_percentage = input("what percentage tip would you like to give ? 10, 12,or 15 ? ")
# number_of_people = input("how many people to splite the bill ?")
# total_bill = float(bill_amount)+ ((int(tip_percentage)/100)*float(bill_amount))
# result = total_bill / int(number_of_people)

# print(f"Each person should pay : ${round(result,2)}")
bill = float(input("what was the total bill ? "))
tip = int(input("what is the tip you want to give ? 10, 12, or 15 ?"))
num_of_people = int(input("what is the number of people to splite the bill ?"))

totoal_bill = bill + tip / 100 * bill
result = totoal_bill / num_of_people
final_result = "{:.2f}".format(result)

print(f"Each person should pay : ${final_result}")
