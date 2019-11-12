import os, sys
import math
from numpy import pi as np
sys.path.append('../factorial/')

from factorial import get_factorial


def exp_appx(x,n):
	global exp
	
	numer = (x**n)
	denom = get_factorial(n)
	temp = numer/denom
	exp += temp
	print (exp, n)

	if n <= 0:
		print (exp)
		return (exp)
	else:
		n-=1
		return exp_appx(x,n)

def sin_appx(x,n):
	global sin_num, term
	exponent = (2*n) + 1
	numer = x**(exponent)
	denom = get_factorial(exponent)
	temp = numer/denom
	#temp = exp_appx(x,exponent)
	if n % 2 == 0:
		print ("EVEN: n=",n, "temp value: ", temp, "numerator/denom: ", sin_num)
		sin_num = sin_num + temp
		print ("new sum: ", sin_num)
	else:
		print ("ODD: n=", n, "temp value: ", temp, "numerator/denom: ", sin_num)
		sin_num = sin_num - temp
		print ("new sum: ", sin_num)
		
	if n == 0:
		print (sin_num)
		return (sin_num)
	else:
		return sin_appx(x,n-1)
	
	
#def cos_appx(x,n):



#exp=0
#exp_appx(1.,1)

term=-1
n=0
sin_num=0
exp=0
temp=0
n_val=0
#print (math.sin(np/2))
sin_appx((np/2),2)
