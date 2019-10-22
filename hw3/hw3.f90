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
	real(kind=8) :: n, pi_apprx, pi_true, threshold, diff
	integer i
	pi_true = acos(-1.d0)
	threshold = 1.e-8
	diff = abs(pi_apprx - pi_true)
	
	do i=1, n
		if (diff > threshold) then
			call apprxPi(pi_apprx, n)
		endif
	end do	
	
	print *, "pi_true = ", pi_true
	print *, "pi_approx = ", pi_apprx
	print *, "n = ", i
end program driver


subroutine apprxPi(pi_apprx, limit)
	implicit none
	real(kind=8) :: tempA, tempB, tempC, tempD
	real(kind=8), intent(in) :: limit
	real(kind=8), intent(out) :: pi_apprx
	
	tempA = 4 / ((8*limit) + 1)
	tempB = 2 / ((8*limit) + 4)
	tempC = 1 / ((8*limit) + 5)
	tempD = 1 / ((8*limit) + 6)
	pi_apprx = pi_apprx + (16**(-limit) * (tempA + tempB + tempC + tempD))
		
end subroutine apprxPi



function trapezoidFunc()

end function trapezoidFunc

subroutine trapezoidSub()

end subroutine trapezoidSub

subroutine trapezoidExact()

end subroutine trapezoidExact