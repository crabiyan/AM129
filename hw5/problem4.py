import copy
l = [1,2,3]
def is_sorted(l):
	for i,value in enumerate(l):
		if i == 0:
			temp = copy.copy(value)
		elif temp >= value:
			print ("False")
			break
		elif i == len(l)-1:
			print ("True")
		else:
			temp = copy.copy(value)

#is_sorted(l)

def cumulative_sum(l):
	for i, value, in enumerate(l):
		if i == 0:
			temp = copy.copy(value)
		L[i] = value + temp

def print_list(summed_list):
	for i, value, in enumerate(summed_list):
		print ('L[%s] is %16s' % (index, summed_list[index]))

cumulative_sum(l)

