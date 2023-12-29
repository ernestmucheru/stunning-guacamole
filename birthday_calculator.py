import datetime
from datetime import datetime


print("Enter your age here: ")
age = int(input())

year_of_birth = datetime.now().year - age

print(year_of_birth)

turn_eighty = 80 - age

print(f"You will be turning 80 in {turn_eighty} years time.")