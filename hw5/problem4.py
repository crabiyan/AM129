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



import copy

l = [1,2,3]
L = copy.copy(l)

def cumulative_sum(l):
	for i, value, in enumerate(l):
		if i == 0:
			temp = copy.copy(value)
		else:
		     L[i] = value + temp
		temp = copy.copy(L[i])

def print_list(summed_list):
	for i, value, in enumerate(summed_list):
		print ('L[%s] is %16s' % (i, summed_list[i]))

cumulative_sum(l)
print_list(L)
