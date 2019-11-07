s = 'spam'

def do_twice(f, s):
     f(s)
     f(s)

def print_spam():
     print ('spam')
 
def print_twice(s):
	print (s)
	print (s)
	
do_twice(print_twice, s)
