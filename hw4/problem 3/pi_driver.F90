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

program pi_driver

     use setup_module
     use pi_module
     call setup_init()     

     do
          call pi_summation(pi_apprx, counter)
          call pi_errorCheck(pi_apprx, pi_true, diff, threshold)
          if (accurate) EXIT
          counter=counter+1
     end do
     
     call pi_writeOutput(counter, pi_apprx, threshold, diff)

end program pi_driver
