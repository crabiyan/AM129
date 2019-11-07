
l = ["cameron", "rabiyan"]

def print_yourName(l, param=None):
	if param is not None:
		if param == False:
			for i in reversed(l):
				if i == 0:
					print (l[i].capitalize())
				else:
					print (l[i].capitalize(), end = ", ")
		else:
			print ("true")
	else:
		for i, value in enumerate(l):
			print (l[i].capitalize(), end = " ")
		print ("")
		
print_yourName(l)
