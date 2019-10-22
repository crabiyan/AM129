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
program driver

	implicit none
	real(kind=8) :: diff, threshold, pi_true, pi_apprx, counter
	pi_true = acos(-1.d0)
	threshold = 1.e-16

	call recursion(diff, threshold, pi_true, pi_apprx, counter)
	
	print *, "pi_true = ", pi_true
	print *, "pi_approx = ", pi_apprx
	print *, "n = ", counter
end program driver

subroutine recursion(diff, threshold, pi_true, pi_apprx, m)

	implicit none
	real(kind=8), intent(in) :: threshold, pi_true
	real(kind=8), intent(inout) :: diff, pi_apprx, m
	diff = abs(pi_apprx - pi_true)
	
	if (diff > threshold) then
		call apprxPi(pi_apprx, m)
		m = m + 1
	else
		return
	endif
end subroutine recursion

subroutine apprxPi(pi_apprx, limit)
	implicit none
	real(kind=8) :: tempA, tempB, tempC, tempD, x, f
	real(kind=8), intent(in) :: limit
	real(kind=8), intent(out) :: pi_apprx
	x = limit
	f = x * (-1)
	
	tempA = 4. / ((8.*x) + 1.)
	tempB = 2. / ((8.*x) + 4.)
	tempC = 1. / ((8.*x) + 5.)
	tempD = 1. / ((8.*x) + 6.)
	pi_apprx = pi_apprx + (16**(f)) * ((tempA - tempB - tempC - tempD))
		
end subroutine apprxPi



function trapezoidFunc()

end function trapezoidFunc

subroutine trapezoidSub()

end subroutine trapezoidSub

subroutine trapezoidExact()

end subroutine trapezoidExact