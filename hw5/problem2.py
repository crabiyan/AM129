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


s = 'spam'

def do_twice(f, s):
     f(s)
     f(s)

def print_spam():
     print ('spam')
 
def print_twice(s):
	print (s)
	print (s)
	
do_twice(print_twice, s)
