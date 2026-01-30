def string_length(text):
    count = 0
    for alphabets in text:
        count += 1
    return count

text = input("Enter a string: ")
print("Length of string:", string_length(text))
