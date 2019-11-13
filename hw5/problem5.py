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

l = ["cameron", "rabiyan"]

def print_yourName(l, param=None):
	if param is not None:
		if param == False:
			for i in reversed(range(len(l))):
				if i == 0:
					print (l[i].capitalize())
				else:
					print (l[i].capitalize(), end = ", ")
		else:
			for i, value in enumerate(l):
				print (l[i].capitalize(), end = " ")
			print ("")
	else:
		for i, value in enumerate(l):
			print (l[i].capitalize(), end = " ")
		print ("")
		
print_yourName(l)
print_yourName(l, True)
print_yourName(l, False)
