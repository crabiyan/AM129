import numpy as np
import matplotlib.pyplot as plt


def word_count(file):
	#f.open(file, 'r')
	d = dict()
	with open(file, 'r') as f:
		while True:
			c = f.read(1)			
			if not c:
				print ("-----------")
				print ("End of file")
				print ("-----------")
				break
			elif c != "\n":
				if c in d.keys():
					val = d[c]
					val += 1
					d.update({c:val})
				else:
					d[c] = 1
					#print ("character: ", c)
		for key, value in d.items():
			print (key, value)

	return d
if __name__ == "__main__":
	file_path = './words.txt'
	hist = word_count(file_path)
	
