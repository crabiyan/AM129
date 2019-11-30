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

#import #import some necessary Python modules
import numpy as np
import matplotlib.pyplot as plt
import os
import subprocess



# Run Bash commands from current working directory
def bash_command(cmd, time_out):

	p = subprocess.Popen(['/bin/bash', '-c', cmd])
	p.wait(timeout=time_out)
	p.kill()

# Run makefile on passed file, runs 'make clean' if .exe file exists already
def make_make(file):

	cur_dir = os.chdir("../fortran/")
	while True:
		file_list = os.listdir(cur_dir)
		if file in file_list:
			bash_command("make clean", 300)
			bash_command('make', 300)
			break
		else:
			bash_command('make',300)
			break

def check_multiple_files(cur_dir, file_name):

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


def runtimeParameters_init(t_0, y_0, t_f, N, initFile):

	fortran_dir = os.chdir("../fortran/")
	check_multiple_files(fortran_dir, initFile)
	
	with open(initFile, "w+") as f:
		f.write("t_0:" + "\t\t" + str(t_0) + "\n")
		f.write("y_0:" + "\t\t" + str(y_0) + "\n")
		f.write("t_f:" + "\t\t" + str(t_f) + "\n")
		f.write("N:" + "\t\t" + str(N) + "\n")


# Calculates the real solution and places the solutions into the real_sol numPy array
def real_solution(real_sol, increment):
	t = 0
	num = 0
	
	#solution formula: y(t) = -( (2ln(t^2 + 1) + 4) )^(1/2)
	for i, index in enumerate (real_sol):
		real_sol[i] = -( 2 * np.log( (t**2) + 1 ) +4 )**(.5)
		t = t + increment
		
def calculate_error(initFile, datFile, outFile):
	
	os.chdir("../fortran/")
	initial_t = 0
	final_t = 0	

	# Initialize Variables from initFile
	with open (initFile, "r") as f:
		while True:
			line = f.readline()
			if not line:
				break
			elif line.startswith("N"):
				arr = line.split()
				num = float(arr[1])
			elif line.startswith("t_0"):
				arr = line.split()
				initial_t = float(arr[1])
			elif line.startswith("t_f"):
				arr = line.split()
				final_t = int(arr[1])

	t_increment = (final_t - initial_t)/num
	
	#create numPy arrays with number of indices
	Numerical_Soln_y = np.zeros(int(num)+1)
	Numerical_Soln_t = np.zeros(int(num)+1)
	Real_Soln = np.zeros(int(num)+1)
	error = 0
	t_val = 0
	
	#initialize numPy array with values from datFile
	with open (datFile, 'r') as f:
		index = 0
		while index <= int(num):
			line = f.readline()
			current_line = line.split()
			t_val = float(current_line[0])
			solution = float(current_line[1])
			Numerical_Soln_y[index] = solution
			Numerical_Soln_t[index] = t_val
			index = index + 1
			
	real_solution(Real_Soln, t_increment)
	
	for i, index in enumerate (Real_Soln):
		error = error + abs(Real_Soln[i] - Numerical_Soln_y[i])
	
	plot_euler(outFile, Numerical_Soln_y, Numerical_Soln_t, Real_Soln, error)
	
def plot_euler(outFile, Numerical_Soln_y, Numerical_Soln_t, Real_Soln, error):
     
	cur_dir = os.chdir("../pyRun/")
     
	fig = plt.figure()
	
	fig.suptitle("Error: "+str(error))
	plt.xlabel('t axis')
	plt.ylabel('y axis')
	plt.plot(Numerical_Soln_t, Numerical_Soln_y, dashes=[6,2], marker='o', color="red", label='Numerical Solution')
	real_line = plt.plot(Numerical_Soln_t, Real_Soln, color="blue", label='Real Solution')
	plt.legend()
	plt.grid(True)
	plt.savefig(outFile)
	plt.draw()


if __name__ == '__main__':
	
	# Variable Declaration
	png_file_8 = "result_8.png"
	png_file_16 = "result_16.png"
	png_file_32 = "result_32.png"
	png_file_64 = "result_64.png"
		
	fortran_dir = os.chdir("../fortran/")
	
	file_name = "main.exe"
	command = "./main.exe"
	
	t_0 = 0.0
	t_f = 10
	y_0 = -2.0
	N_8 = 8.0
	N_16 = 16.0
	N_32 = 32.0
	N_64 = 64.0
	datname_8 = "output_8.dat"
	datname_16 = "output_16.dat"
	datname_32 = "output_32.dat"
	datname_64 = "output_64.dat"
	
	initFileName = "euler.init"
	
	# Run Commands
	make_make(file_name)
	
	runtimeParameters_init(t_0, y_0, t_f, N_8, initFileName)
	bash_command(command, 300)
	calculate_error(initFileName, datname_8, png_file_8)

		
	runtimeParameters_init(t_0, y_0, t_f, N_16, initFileName)
	bash_command(command, 300)
	calculate_error(initFileName, datname_16, png_file_16)
		
	runtimeParameters_init(t_0, y_0, t_f, N_32, initFileName)
	bash_command(command, 300)
	calculate_error(initFileName, datname_32, png_file_32)
	
	runtimeParameters_init(t_0, y_0, t_f, N_64, initFileName)
	bash_command(command, 300)
	calculate_error(initFileName, datname_64, png_file_64)	
	
	
	plt.show()


