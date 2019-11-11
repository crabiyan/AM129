"""
/lectureNote/chapters/chapt03/codes/examples/factorial/factorial.py

Computes n! using recursive function

"""
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
