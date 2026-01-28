def even_or_odd(a):
    if a%2==0:
        return("Even Number")
    else:
        return("Odd Number")



num=int(input("Enter a number:"))
print(even_or_odd(num))