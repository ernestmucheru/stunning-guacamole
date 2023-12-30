text = str(input("Enter your word: \n"))

def isPalindrome(text):
    return text == text[::-1]

reversed_text = text[::-1]
ans = isPalindrome(text)

if ans == True:
    print(f"{text.capitalize()} is a palindrome.")
else:
    print(f"{text.capitalize()} and {reversed_text.capitalize()} can never be a palindrome, not in a million years. Try malayalam!")