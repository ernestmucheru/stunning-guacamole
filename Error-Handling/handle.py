# def get_age():
#     age = int(input("How old are you:\n"))
#     return age

# print(get_age())

# Handling invalid input
def get_age():
    print("How old are you: ")
    try:
        age = int(input())
        return age
    except ValueError:
        return "We expected numerical characters"
    
new_age = get_age()
print(new_age)