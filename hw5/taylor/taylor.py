import os, sys
import math
import numpy as np
sys.path.append('../factorial/')

from factorial import get_factorial


def exp_appx(x,n):
	global exp
	
	numer = (x**n)
	denom = get_factorial(n)
	temp = numer/denom
	exp += temp
	#print (exp, n)

	if n <= 0:
		#print (exp)
		value=exp
		exp=0
		return (value)
	else:
		return exp_appx(x,n-1)

def sin_appx(x,n):
	global sin_num, term, j
	#exponent = (2*n) + 1
	#numer = x**(exponent)
	#denom = get_factorial(exponent)
	#temp = numer/denom
	#temp = exp_appx(x,exponent)
	if j == 1:
		j+= 1
		sin_num += x
		return sin_appx(x,n)
	elif j <= n:
		if j % 2 == 0:
			j+=1
			return sin_appx(x,n)
		else:
			term = term*(-1)
			numer=x**j
			denom = get_factorial(j)
			temp = term * (numer/denom)
			sin_num = sin_num + temp
			j+=1
			return sin_appx(x,n)
	elif j > n:
		print ("Sin(x) Approximation = ", sin_num)
		return (sin_num)
	else:
		j+=1
		return sin_appx(x,n)
	
	
#def cos_appx(x,n):



exp=0
print ("Exp(x) Approximation = ", exp_appx(1.,20))

term=1
value=0
n=0
sin_num=0
numer=0
denom=0
exp=0
temp=0
j=1
#print (math.sin(np/2))
sin_appx((np.pi/2),5)
