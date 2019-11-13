####################################################
# AM129 hw5
#
# Students:
# Cameron Rabiyan - Driver
# Maya Apotheker - Navigator
# Manny Gamboa - Navigator
#
# Group 334-7
#
# Code written by Professor Dongwook Lee
#
####################################################

from numpy import sqrt as np_sqrt

def get_factorial(n):
    if n == 0:
        return 1
    else:
        result  = n * get_factorial(n-1)
        return result

if __name__ == "__main__":
    n=5
    print(n, ' factorial = ', get_factorial(n))
