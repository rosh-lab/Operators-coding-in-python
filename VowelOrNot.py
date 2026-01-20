#program for deciding whether the word is vowel or not
#VowelOrNot
word=input("Enter a word:")
res="Vowel" if "a" in word or "e" in word or "i" in word or "o" in word or "u" in word else "Not vowel"
print("{} is {}".format(word,res))