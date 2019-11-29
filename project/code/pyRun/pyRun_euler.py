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

# Calculates the real solution and places the solutions into the real_sol numPy array
def real_solution(real_sol, increment):
	t = 0
	
	#solution formula: y(t) = -( (2ln(t^2 + 1) + 4) )^(1/2)
	for i, index in enumerate (real_sol):
		real_sol[i] = -( 2 * np.log( (t**2) + 1 ) +4 )**(.5)
		t = t + increment
		
def calculate_error(datFile, outFile):
	
	# Get the number of grid points from the datFile
	num = int((datFile.split('_')[1]).split('.')[0])

	t_increment = 10/num
	
	#create numPy array with number of indices
	Numerical_Soln_y = np.zeros(num+1)
	Numerical_Soln_t = np.zeros(num+1)
	Real_Soln = np.zeros(num+1)
	error = 0
	t_val = 0
	
	#initialize numPy array with values from datFile
	with open (datFile, 'r') as f:
		index = 0
		while index <= num:
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
	
	plot_euler(datFile, outFile, Numerical_Soln_y, Numerical_Soln_t, Real_Soln, error)
	
def plot_euler(datFile, outFile, Numerical_Soln_y, Numerical_Soln_t, Real_Soln, error):

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
	
	png_file_8 = "result_8.png"
	png_file_16 = "result_16.png"
	png_file_32 = "result_32.png"
	png_file_64 = "result_64.png"
		
	fortran_dir = os.chdir("../fortran/")
	dat_name = ("output_i.dat")
	
	file_name = "main.exe"
	command = "./main.exe"
	
	make_make(file_name)
	bash_command(command, 300)
	
	calculate_error("output_8.dat", png_file_8)
	calculate_error("output_16.dat", png_file_16)
	calculate_error("output_32.dat", png_file_32)
	calculate_error("output_64.dat", png_file_64)
	
	plt.show()


