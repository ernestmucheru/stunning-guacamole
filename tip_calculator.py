bill = float(input('Enter your bill: '))
level_of_satisfaction = int(input('\nEnter \n\n1 for Great Service \n2 for Good Service \n3 for Terrible Service \n\nYour input goes here: ' ))

if level_of_satisfaction == 1:
    tip = 0.2 * bill
    total_bill = tip + bill
    print(f"Your total cost is {total_bill}")
elif level_of_satisfaction == 2:
    tip = 0.15 * bill
    total_bill = tip + bill
    print(f"Your total cost is {total_bill}")
else:
    print(f"Your total cost is {bill}")






