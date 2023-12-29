# taken numbers
numTaken = [3,5,7,11,13]

print("Available numbers")

# loop
for available_number in range(1,21):
    if available_number in numTaken:
        continue
    print(available_number)