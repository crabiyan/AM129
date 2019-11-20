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


import numpy.f2py as f2py
import os, sys
import os.path
import subprocess
from subprocess import Popen, PIPE

def bash_command(cmd, time_out):

	p = subprocess.Popen(['/bin/bash', '-c',cmd])
	p.wait(timeout=time_out)
	p.kill()
	
def make_make(file):

	cur_dir = os.chdir("../newton_rootFinder/")
	while True:
		file_list = os.listdir(cur_dir)
		if "rootFinder.exe" in file_list:
			bash_command("make clean", 300)
			bash_command('make', 300)
			break
		else:
			bash_command('make', 300)
			break
    
#def runtimeParameters_init(run_name, method_type, x_beg, x_end, max_iter, threshold, init_guess, multiplicity):
	
    # 1. Implement a routine that generates a new "rootFinder.init"
    #    runtime parameter file. Use a proper set of
    #    input arguments to produce a new rootFinder.init (with the same name)
    #    which has all the necessary input parameters to run the Fortran code.
    #    For instance, the first few lines look like:
    #      run_name     (... and some space ...) 'newton'
    #      method_type  (... and some space ...) 'newton'
    #      ...
    # 2. When writing a new "rootFinder.init", check if there is an old one already.
    #    If so, rename the old one to, say, "rootFinder.init.1" before
    #    creating a new "rootFinder.init". You would end up with having multiple
    #    of them, e.g., "rootFinder.init.1", "rootFinder.init.2", etc.,
    #    along with "rootFinder.init" which is the active runtime parameter file in use.
    
      
def run_rootFinder(bash_cmd):

	cur_dir = os.chdir("../newton_rootFinder/")
	bash_command(bash_cmd, 300)

    # This routine executes the Fortran excutable, "rootFinder.exe"
    # using "rootFinder.init" you just created.

    
#def plot_data(plotFileName, and more???):
    # 1. This function produces two figures:
    #     (1) solution (y-axis) vs. iteration number (x-axis), and
    #     (2) error (y-axis) vs. iteration number (x-axis).
    #
    # 2. You can plot the two as either subfigures or two separate figures.
    #
    # 3. In each figure, you need to have at least:
    #    xlabel, ylabel, title, line plot with reasonable choices of linestyle and marker.
    #    (see for instance, http://www.scipy-lectures.org/intro/matplotlib/matplotlib.html)
    #
    # 4. Your plots need to have big enough x and y ranges so that your solution and error
    #    graphs are properly fit in the figures.
    #    Make sure that you use a single same y-range for solutions and errors, respectively,
    #    so that ALL plots of three different threshold values have the same respective scales in y.
    #
    # 5. You need to plot your results to BOTH screen and png files.
    #    The png file names should bear information on ftn_type, threshold values at least, e.g.,
    #    the file name "result_2_1e-08.png" implies ftn_type = 2 and threshold value = 1.e-8.
    #    Do not hardcode three different file names, but use string manipulations in naming them
    #    in your implementation.
    #
    # 6. After plotting, you save the data file "rootFinder_newton.dat"
    #    to a new name, e.g.., "rootFinder_newton.dat.1", etc..
    #    At the end of running three runs for three different threshold values,
    #    you should have collected "rootFinder_newton.dat.1", "rootFinder_newton.dat.2",
    #    as well as the latest data file "rootFinder_newton.dat".

    
if __name__ == '__main__':
	
	
	file_name = "rootFinder.exe"
	make_make(file_name)

    # Set runtime parameters here
    # and call the above functions properly,
    # so that this Python code executes the Fortran code
    # for three different threshold values
    # 1.e-4, 1.e-6, 1.e-8
    # ...
    # ...
