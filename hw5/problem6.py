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


def verify_palindrome(s, i, count):
	if i >= 2:
		if s[i] == s[count]:
			i=i-1
			count=count+1
			verify_palindrome(s, i, count)
		else:
			print ("False")
			return False
	else:
		print ("True")
		return True

count = 0
word = input("Please enter a palindrome(Case-Sensitive): ")

verify_palindrome(word, len(word)-1, count)

