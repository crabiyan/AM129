####################################################
# AM129 hw6
#
# Students:
# Cameron Rabiyan - Driver
# Maya Apotheker - Navigator
# Manny Gamboa - Navigator
#
# Group 334-7
####################################################

import numpy as np
import matplotlib.pyplot as plt

def word_count(file):
	d = dict()
	with open(file, 'r') as f:
		while True:
			c = f.read(1)			
			if not c:
				break
			elif c != "\n":
				if c in d.keys():
					val = d[c]
					val += 1
					d.update({c:val})
				else:
					d[c] = 1
	return d

if __name__ == "__main__":
	l = list()
	arr = np.array([], dtype=int)
	
	file_path = './words.txt'
	hist = word_count(file_path)
	
	x = np.arange( len(hist.keys()) )
	y = np.arange( len(hist.values()) )
	nCounts = []
	plt.xlabel('Character')
	plt.ylabel('Frequency')
	
	for key in sorted(hist.keys()):
		l.append(key)
		arr = np.append(arr, [hist[key]])
		print ("'"+key+"'"+":",hist[key])
		plt.bar(key, hist[key], color='blue')
	
	plt.plot(x,arr,marker='o', color='r')
	plt.xticks(x, l)
	plt.yticks(np.arange(0,120000, 20000))
	plt.grid(b=None, which = 'major', axis='both')
	plt.savefig('results_prob1.png')
	plt.show()

