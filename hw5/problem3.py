####################################################
# AM129 hw5
#
# Students:
# Cameron Rabiyan - Driver
# Maya Apotheker - Navigator
# Manny Gamboa - Navigator
#
# Group 334-7
####################################################


import copy
l = [1,2,3]
def is_sorted(l):
	for i,value in enumerate(l):
		if i == 0:
			temp = copy.copy(value)
		elif temp >= value:
			print ("False")
			break
		elif i == len(l)-1:
			print ("True")
		else:
			temp = copy.copy(value)

is_sorted(l)
