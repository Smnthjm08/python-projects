#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#Write your code below this line 👇

print("Welcome to Tip Calculator")

total_bill=input("What was your total bill? $")
total_bill_int=int(total_bill)

tip_amount=input("How much tip would you like to give? 10? 12? 15?")
tip_amount_int=int(tip_amount)

no_of_people=input("How many people to split the bill?")
no_of_people_int=int(no_of_people)

total_bill_inc_tip=(total_bill_int+((tip_amount_int/100)*total_bill_int))
grand_total=int(total_bill_inc_tip)

final_split=round(grand_total/no_of_people_int,2)
print(f'Each should pay {final_split} including tip!')
