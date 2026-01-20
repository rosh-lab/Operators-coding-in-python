#program for accepting a word or value and decide whether it is palindrome or not
word=input("Enter a word:").lower()
res="Palindrome" if (word==word[::-1]) else "Not Palindrome"
print("{} is {}".format(word,res))