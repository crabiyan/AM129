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

	if n <= 0:
		value=exp
		exp=0
		return (value)
	else:
		return exp_appx(x,n-1)

def sin_appx(x,n):
	global sin_num, term, j
	if n < 0 or (n-int(n) != 0):
		print ("-ERROR- Invalid Input: n must be a non-negative integer")
		return np.nan
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
		if (j-n) > 1:
			print ("-ERROR- Invalid Input: n must be an integer")
			return np.nan
		print ("Sin(x) Approximation = ", sin_num)
		return (sin_num)
	else:
		print ("ERROR")

	
	
def cos_appx(x,n):
	global cos_num, term, j
	if n < 0 or (n-int(n) != 0):
		print ("-ERROR- Invalid Input: n must be a non-negative integer")
		return np.nan
	if j == 0:
		j+= 1
		cos_num += 1
		return cos_appx(x,n)
	elif j <= n:
		if j % 2 == 0:
			term = term*(-1)
			numer=x**j
			denom = get_factorial(j)
			temp = term * (numer/denom)
			cos_num = cos_num + temp
			j+=1
			return cos_appx(x,n)
			
		else:
			j+=1
			return cos_appx(x,n)
	elif j > n:
		if (j-n) > 1:
			print ("-ERROR- Invalid Input: n must be an integer")
			return np.nan
		print ("Cos(x) Approximation = ", cos_num)
		return (cos_num)


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
sin_appx((np.pi/2),(1.65465))

term=1
value=0
n=0
cos_num=0
numer=0
denom=0
exp=0
temp=0
j=0
cos_appx((np.pi/2),5.6)





