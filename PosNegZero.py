#program for accepting a number and decide whether it is pos negative or zero
n=float(input("Enter a number:"))
res="Zero" if (n==0) else "positive" if (n>0) else "negative"
print("{} is {}".format(n,res))