def power(a,n):
    result=1
    for i in range(n):
       result*=a
    return result

a=int(input("Enter the base number: "))
n=int(input("Enter the power: "))
print(power(a,n))

