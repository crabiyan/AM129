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
import numpy.f2py as f2py
import os, sys
import subprocess
from subprocess import Popen, PIPE

def bash_command(cmd):

	cur_dir= os.getcwd()
	file_name = "rootFinder.exe"
	sys.path.append('../newton_rootFinder/')
	p = subprocess.Popen(['/bin/bash', '-c',cmd], cwd='../newton_rootFinder/')
	p.wait(timeout=30)
	p.kill()

#	while True:
#		entries = os.listdir(cur_dir)
#		for entry in entries:
#			if entry == 'rootFinder.exe':
#				p.kill()
#		break	
def make_make(fsource,mod_name,args,ext):

	bash_command('make')
	#subprocess = Popen(["make"], stdout=subprocess.PIPE, cwd="../newton_rootFinder")
	
	#with open('RootFinder.F90') as fid:
	#	fsource = fid.read()
	#with open('findRootMethod_module.F90') as fid:
	#	fsource = fid.read()
	#with open('read_initFile_module') as fid:
	#f2py.compile(fsource,modulename=mod_name,extra_args=args,verbose=True,extension=ext)

	
    # 1. Compile the Fortran code if has not been compiled
    #    (i.e., if 'rootFinder.exe' does not exist yet);
    #
    # 2. Otherwise do "make clean" first and then "make".
    #
    # 3. You need to change your directory from "pyRun/" to
    #    "newton_rootFinder/" to compile the Fortran code.

    
#def runtimeParameters_init(some inputs???):
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
    
      
#def run_rootFinder(some inputs???):
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
	
	make_make('RootFinder.F90', 'RootFinder', 'gfortran -o RootFinder.exe', '.F90')
	
#	make_make('RootFinder.F90', 'rootFinder', 'gfortran -ggdb -03 -fdefault-real-8 -fdefault-double-8 -ffree-line-length-none -Wuninitialized -c RootFinder.o read_initFile_module.o findRootMethod_module.o ftn_module.o output_module.o setup_module.o -o rootFinder.exe', '.F90')
	
    # Set runtime parameters here
    # and call the above functions properly,
    # so that this Python code executes the Fortran code
    # for three different threshold values
    # 1.e-4, 1.e-6, 1.e-8
    # ...
    # ...
