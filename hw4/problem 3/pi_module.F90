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

module pi_module

     logical :: accurate = .false.
     
     contains

     subroutine pi_summation(pi_apprx, counter)
          
          real(kind=8) :: A, B, C, D = 0

          A = 4.d0 / ((8.d0*counter) + 1.d0)
          B = 2.d0 / ((8.d0*counter) + 4.d0)
          C = 1.d0 / ((8.d0*counter) + 5.d0)
          D = 1.d0 / ((8.d0*counter) + 6.d0)
          pi_apprx = pi_apprx + ((16.d0**(-counter)) * (A - B - C - D))
   
     end subroutine pi_summation
     
     
     subroutine pi_errorCheck(pi_apprx, pi_true, diff, threshold)
     
          diff = abs(pi_apprx - pi_true)
          if (diff <= threshold) then
               accurate = .true.
          end if
     end subroutine pi_errorCheck
     
     subroutine pi_writeOutput(counter, pi_apprx, threshold, diff)

          print *, "N = ", counter
          print *, "Approximation = ", pi_apprx
          print *, "threshold = ", threshold
          print *, "difference(residual) = ", diff
             
     end subroutine pi_writeOutput
     
end module pi_module

