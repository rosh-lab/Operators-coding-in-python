#program for deciding whether the given number is even or odd with +ve numbers
#EvenOddPos.py
#If user enter -ve numbers the display invalid input
n=float(input("Enter a number:"))
res="Invalid input" if (n<0) else "Even" if (n%2==0) else "Odd"
print("{} is {}".format(n,res))