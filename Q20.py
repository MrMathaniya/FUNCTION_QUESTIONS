def mrks(a,b,c,d,e):
    sum=a+b+c+d+e
    avg=sum/5

    if avg>=90:
        print("Grade A")
    elif avg>=75:
        print("Grade B")
    elif avg>=50:
        print("Grade C")
    elif avg>=30:
        print("Grade D")
    else:
        print("Grade E")

a=int(input("Enter the marks of the 1st subject: "))
b=int(input("Enter the marks of the 2nd subject: "))
c=int(input("Enter the marks of the 3rd subject: "))
d=int(input("Enter the marks of the 4th subject: "))
e=int(input("Enter the marks of the 5th subject: "))

print(mrks(a,b,c,d,e))