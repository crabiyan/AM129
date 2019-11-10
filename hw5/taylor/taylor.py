import numpy

def exp_appx(x,n):
	j = 0
	exp = 0
	for j in range(n):
		temp = ((x**j)/(numpy.math.factorial(j)))
		exp = exp + temp
		print(temp)
		print (exp)
	return exp
	

exp_appx(2,2)
