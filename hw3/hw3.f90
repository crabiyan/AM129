! AM129 hw3pi
!
! Students:
! Cameron Rabiyan - Driver
! Maya Apotheker - Navigator
! Manny Gamboa - Navigator
!
! Group 334-7
!
! Command Lines:
! gfortran array_col_hw2.0 -o col3.exe -O3 -fdefault-real-8 -fdefault-double-8
! gfortran array_col_hw2.0 -o col2.exe -O0 -fdefault-real-8 -fdefault-double-8
! gfortran array_col_hw2.o -o col3.exe -g3 -fdefault-real-8 -fdefault-double-8 -Wall -Wextra -Wimplicit-interface -fPIC -fmax-errors=1 -g -fcheck=all -fbacktrace
!
! Makefiles:
! make -f Makefile1
! make -f Makefile2
! make -f Makefile3
!

module part1

implicit none
integer, parameter :: dp = kind(1.0d0)
real(dp) :: diff, threshold, pi_true, pi_apprx, counter
pi_true = acos(-1.d0)
threshold = 1.e-16d0
pi_apprx = 0.d0
counter = 1.d0
contains

	subroutine recursion(diff, pi_apprx, counter)
	
		implicit none
		real(dp), intent(inout) :: diff, pi_apprx, counter
		diff = abs(pi_apprx - pi_true)
		
		if (diff > threshold) then
			call apprxPi(pi_apprx, counter)
			counter = counter + 1.d0
		else
			return
		endif
		
	end subroutine recursion
	
	subroutine apprxPi(pi_apprx, counter)
		implicit none
		real(dp) :: tempA, tempB, tempC, tempD
		real(dp), intent(inout) :: pi_apprx, counter
		
		tempA = 4.d0 / ((8.d0*counter) + 1.d0)
		tempB = 2.d0 / ((8.d0*counter) + 4.d0)
		tempC = 1.d0 / ((8.d0*counter) + 5.d0)
		tempD = 1.d0 / ((8.d0*counter) + 6.d0)
		pi_apprx = pi_apprx + ((16.d0**(-counter)) * (tempA - tempB - tempC - tempD))
		call recursion(pi_apprx, counter)
	end subroutine apprxPi

end module part1

program driver
	
	use part1
	
	implicit none
	integer, parameter :: dp = kind(1.0d0)
	real(dp) :: diff, threshold, pi_true, pi_apprx, counter
	pi_true = acos(-1.d0)
	threshold = 1.e-16
	pi_apprx = 0.d0

	call recursion(diff, pi_apprx, counter)
	
	print *, "pi_true = ", pi_true
	print *, "pi_approx = ", pi_apprx
	print *, "n = ", counter
	
end program driver


function trapezoidFunc()

end function trapezoidFunc

subroutine trapezoidSub()

end subroutine trapezoidSub

subroutine trapezoidExact()

end subroutine trapezoidExact