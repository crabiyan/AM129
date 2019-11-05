!!------------------------------------------------------------------
!! This code is referenced by Prof. Dongwook Lee for AMS 209.
!!------------------------------------------------------------------

! AM129 hw2

! Students:
! Cameron Rabiyan - Driver
! Maya Apotheker - Navigator
! Manny Gamboa - Navigator

! Group 334-7

! Command Lines:
!gfortran -c -fdefault-double-8 -fdefault-real-8 read_initFile_module.F90
!gfortran -c -fdefault-double-8 -fdefault-real-8 setup_module.F90
!gfortran -c -fdefault-double-8 -fdefault-real-8 pi_module.f90
!gfortran -fdefault-real-8 -fdefault-double-8 -o pi pi_driver.f90 read_initFile_module.F90 setup_module.F90 pi_module.f90
!./pi

! Or just run:
! make

! Makefiles:
! makefile

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
