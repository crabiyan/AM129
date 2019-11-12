word=raw_input("Please enter a palindrome(Case-Sensitive): ")
if(word==word[::-1]):
	print("This word is a palindrome")
else:
	print("This word is not a palindrome")