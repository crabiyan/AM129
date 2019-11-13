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


def get_realnum(n):
	a = []
	i = 0
	while i < n:
		l = [0,0]
		print("Coordinate %d: " % i)
		l[0]=float(input("Please enter the X coordinate: "))
		l[1]=float(input("Please enter the Y coordniate: "))
		a.append(l)
		print (l)
		i += 1
	return a
def is_triangle(points):
	num1 = points[0]
	num2 = points[1]
	num3 = points[2]
	if num1[0] == num2[0] == num3[0] or num1[1] == num2[1] == num3[1]:
		print ("Not a triangle")
		return False
	elif num1==num2 or num1 == num3 or num2==num3:
		print ("Not a triangle")
		return False
	else:
		print ("Is a triangle")
		return True
	
total_numbers = 3
is_triangle(get_realnum(total_numbers))





