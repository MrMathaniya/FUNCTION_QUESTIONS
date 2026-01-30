def is_palindrome(text):
    if text == text[::-1]:
        return "Palindrome"
    else:
        return "Not Palindrome"

a= input("Enter a string: ")
print(is_palindrome(a))
