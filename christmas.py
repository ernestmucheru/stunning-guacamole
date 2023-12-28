#Ken's BMI CALC
# weight = float(input("Enter your weight: "))
# height = float(input("Enter your height: "))

# bmi = "Your BMI is" + " ", (weight/height ** 2)

# print(bmi)

#Steve's BMI calc
# weight = float(input('Enter your weight: '))
# height = float(input('Enter your height: '))

# bmi = weight/(height ** 2)

# print(bmi)

# Ken's Car loans calculator
total_loan  = 150000
monthly_salary = 15000
monthly_pay = (0.25 * monthly_salary)
months_owed = (total_loan / monthly_pay) 
month = float(input("Enter month "))

loan_balance = total_loan - (month * monthly_pay)

print( f'your total months owed is {months_owed} and your total loan balance is {loan_balance}')