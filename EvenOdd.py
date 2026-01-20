#PRogram for deciding whether the given number is even or odd
n=float(input("Enter a number:"))
res="Even" if (n%2==0) else "Odd"
print("{} is {}".format(n,res))