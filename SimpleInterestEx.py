#program for calculating simple interest and total amount to pay
p=float(input("Enter principal amount:"))
t=float(input("Enter time:"))
r=float(input("Enter rate of interest:"))
si=p*t*r/100
totamt=p+si
print("Area of Interest: {}".format(si))
print("Total amt to pay: {}".format(totamt))