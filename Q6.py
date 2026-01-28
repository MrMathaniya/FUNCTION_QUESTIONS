def simple_interest(p,r,t):
    return p*r*t/100

p=eval(input("Enter the principal amount: "))
r=eval(input("Enter the rate per annum: "))
t=eval(input("Enter the time in years: "))

print(simple_interest(p,r,t))