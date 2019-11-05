!!------------------------------------------------------------------
!! A Fortran example code for finding a root of a user-defined 
!! function f(x) = 0.
!! 
!! This code is written by Prof. Dongwook Lee for AMS 209.
!!
!! This module has one subroutine which initialize your setup
!! by reading in runtime parameters from 'rootFinder.init' file.
!! The setup_init subroutine calls read_initFile*** subroutines
!! that are implemented as subroutines in read_initFile_module. 
!!
!!------------------------------------------------------------------


module setup_module
  
  !! include a C-type header file:
  !! this is why the file extensions are .F90, instead of .f90
  
 use read_initFile_module
 implicit none
  real(kind=8), save :: pi_true, pi_apprx, threshold, diff, counter
  !real, save :: tempA,tempB,tempC,tempD
  !integer, save :: counter = 0

  
contains

  subroutine setup_init()

    implicit none

     call read_initFileReal('pi_apprx.init', 'pi_true', pi_true)
     call read_initFileReal('pi_apprx.init', 'pi_apprx', pi_apprx)
     call read_initFileReal('pi_apprx.init', 'threshold', threshold)
     call read_initFileReal('pi_apprx.init', 'diff', diff)
    
  end subroutine setup_init

  
end module setup_module
