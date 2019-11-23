"""
Template file for hw6:

Directory structure:

   hw6/Prob2/code/
               |-- newton_rootFinder/RootFinder.F90
               |                     findRootMethod_module.F90
               |                     makefile
               |                     read_initFile_module.F90
               |                     definition.h
               |                     ftn_module.F90
               |                     output_module.F90
               |                     setup_module.F90
               |                     (excluding rootFinder.init)
               |
               |-- pyRun/pyRun_rootFinder_prob2.py
       

"""


#import #import some necessary Python modules
import numpy as np
import matplotlib.pyplot as plt
import os
import subprocess
from subprocess import Popen

file_num = 0
dupExists= 0


def bash_command(cmd, time_out):

	p = subprocess.Popen(['/bin/bash', '-c',cmd])
	p.wait(timeout=time_out)
	p.kill()

def make_make(file):

	cur_dir = os.chdir("../newton_rootFinder/")
	while True:
		file_list = os.listdir(cur_dir)
		if file in file_list:
			bash_command("make clean", 300)
			bash_command('make', 300)
			break
		else:
			bash_command('make',300)
			break
			
def split(words):
	return list(words)

def check_multiple_file(cur_dir, file_name):
	file_count = 0
	file_list = os.listdir(cur_dir)
	original_exists = False
	copy_exists = False
	
	if file_name in file_list:
		
		original_exists = True
		file_name += '.'
		
		for file in file_list:
			if file.startswith(file_name):
				copy_exists = True
				file_count += 1

		if file_name+str(file_count) in file_list:
			file_count+=1
		file_name = file_name[:-1]
		
		if original_exists == True:
			if file_count == 0:
				os.rename(file_name, file_name+'.'+str(1))
			elif copy_exists == True:
				new_file = file_name+'.'+str(file_count)
				os.rename(file_name, new_file)
	
				
def runtimeParameters_init(run_name, method_type, x_beg, x_end, max_iter, threshold, ftn_type, init_guess, multiplicity):

	newton_dir = os.chdir("../newton_rootFinder/")
	file_name = ("rootFinder.init")
	check_multiple_file(newton_dir, file_name)
	
	with open("rootFinder.init", "w+") as f:

		f.write("run_name" + "\t\t" +run_name+"\t"+"# [char] Specify your outputfile name, eg., 'rootFinder_[run_name].dat' \n")
		f.write("method_type" + "\t" +method_type+"\t"+"# [char] Choose a search method between 'newton' and 'modified_newton' \n")

		f.write("x_beg" + "\t\t" +str(x_beg) + "\t" + "#[real] Setting up the search domain \n")
		f.write("x_end" + "\t\t" +str(x_end)  + "\t\t" + "#[real] Setting up the search domain \n")

		f.write("max_iter" + "\t\t" +str(max_iter)+"\t"+"#[int] Maximum number of iteration\n")
		f.write("threshold" + "\t\t" + str(threshold) +"\t"+ "#[int] Maximum number of iteration\n")

		f.write("ftn_type" + "\t\t" + str(ftn_type)+ "\t\t" + "#[int] Types of function -- either 1 or 2\n")
		f.write("init_guess" + "\t" + str(init_guess) +  "\t\t" + "#[real] Initial guess for root search. Users are responsible to pick a good one.\n")
		f.write("multiplicity" + "\t" + str(multiplicity) + "\t\t" + "#[int] The mulitiplicity of the root when using the modified newton method\n")
 

def run_rootFinder(bash_cmd):

	cur_dir = os.chdir("../newton_rootFinder/")
	bash_command(bash_cmd, 300)
    

def plot_data(initFileName, datFileName, pngFileName):
	guess = "init_guess"
	
	solution = 0.
	error = 0.
	init_guess = 0.
	iteration = 0
	
	
	#initial guess value = init_guess
	with open(initFileName, 'r') as f:
		while True:
			line = f.readline()
			if not line:
				break
			elif line.startswith(guess):
				arr = line.split()
				init_guess = float(arr[1])
				break
	
	with open (datFileName, 'r') as f:
		d = dict()
		x_list = list()
		y_list = list()
		error_list = list()
		while True:
			line = f.readline()
			if not line:
				break
			else:
				arr = line.split()
				key = int(arr[0])
				value = float(arr[1])
				d.update({key:value})
	
	for key in sorted(d.keys()):
		iteration = key
		solution = d[key]
		error = abs(solution-init_guess)
		x_list.append(iteration)
		y_list.append(solution)
		error_list.append(error)
		print ("'",iteration,"'"+":",solution,":",error )

	xlim = len(x_list) + 5
	ylim = max(y_list) + 5
	fig, (ax1, ax2) = plt.subplots(2)
	fig.suptitle('HW6 Figure')
	ax1.plot(x_list, y_list, marker='.', mfc='black')
	ax1.set_xlim([0,xlim])
	ax1.set_ylim([-ylim,ylim])
	ax1.set(xlabel='Iteration',ylabel='Calculated Solutions')
	ax1.grid(True)
	
	ax2.plot(x_list, error_list, marker='.', mfc='black')
	ax2.set_xlim([0,xlim])
	ax2.set_ylim([-ylim,ylim])
	ax2.set(xlabel='Iterations', ylabel='Error')
	ax2.grid(True)

	plt.draw()
	plt.savefig(pngFileName)
	
	
if __name__ == '__main__':

	# init File Parameters
	run_name = 'newton'
	method_type = 'newton'
	x_beg = -1000.0
	x_end = 1000.0
	max_iter = 10000
	threshold_1 = 1.e-4
	threshold_2 = 1.e-6
	threshold_3 = 1.e-8
	ftn_type = 1
	init_guess = 0.00039
	multiplicity = 4
	
	png_file_1 = "result_"+str(ftn_type)+"_"+str(threshold_1)+".png"
	png_file_2 = "result_"+str(ftn_type)+"_"+str(threshold_2)+".png"
	png_file_3 = "result_"+str(ftn_type)+"_"+str(threshold_3)+".png"
	
	newton_dir = os.chdir("../newton_rootFinder/")
	dat_name = ("rootFinder_newton.dat")
	
	file_name = "rootFinder.exe"
	command = "./rootFinder.exe"
	
	make_make(file_name)
	runtimeParameters_init(run_name, method_type, x_beg, x_end, max_iter, threshold_1, ftn_type, init_guess, multiplicity)
	bash_command(command, 300)
	plot_data("rootFinder.init", "rootFinder_newton.dat", png_file_1)
	
	check_multiple_file(newton_dir, dat_name)
	runtimeParameters_init(run_name, method_type, x_beg, x_end, max_iter, threshold_2, ftn_type, init_guess, multiplicity)
	bash_command(command, 300)
	plot_data("rootFinder.init", "rootFinder_newton.dat", png_file_2)	
	
	check_multiple_file(newton_dir, dat_name)
	runtimeParameters_init(run_name, method_type, x_beg, x_end, max_iter, threshold_3, ftn_type, init_guess, multiplicity)
	bash_command(command, 300)
	plot_data("rootFinder.init", "rootFinder_newton.dat", png_file_3)
	
	plt.show()


