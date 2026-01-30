def count_vowels(text):
    count = 0
    for vowel in text:
        if vowel in "aeiouAEIOU":
            count += 1
    return count

a=input("Enter a string: ")
print("Number of vowels:", count_vowels(a))
