!------------------------------------------
! AM129 hw5
!
! Students:
! Cameron Rabiyan - Driver
! Maya Apotheker - Navigator
! Manny Gamboa - Navigator
!
! Group 334-7
!------------------------------------------



word=raw_input("Please enter a palindrome(Case-Sensitive): ")
if(word==word[::-1]):
	print("This word is a palindrome")
else:
	print("This word is not a palindrome")
