import copy


def get_realnum(n):
	a = []
	i = 0
	while i < n:
		l = [0,0]
		print("Coordinate %d: " % i)
		l[0]=input("Please enter the X coordinate: ")
		l[1]=input("Please enter the Y coordniate: ")
		a.append(l)
		print (l)
		i += 1


total_numbers = 3
get_realnum(total_numbers)





