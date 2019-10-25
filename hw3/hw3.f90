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





program driver
	



	real(kind=8) :: diff, threshold, pi_true, pi_apprx, counter
        real(kind=8) :: tempA,tempB,tempC,tempD
	pi_true = acos(-1.d0)
	threshold = 1.e-16
	pi_apprx = 0.d0
        n=0        
	diff=0

tempA = 4.d0 / ((8.d0*n) + 1.d0)
		tempB = 2.d0 / ((8.d0*n) + 4.d0)
		tempC = 1.d0 / ((8.d0*n) + 5.d0)
		tempD = 1.d0 / ((8.d0*n) + 6.d0)
		

                do while(n<=25)

		pi_apprx = pi_apprx + ((16.d0**(-n)) * (tempA - tempB - tempC - tempD))
		print *, 'pi_apprx is'
                print *, pi_apprx

                diff= abs(pi_true - pi_apprx)
                print *, 'diff is'
                print *, diff

		if(diff < threshold) then 
			EXIT
                else
                n=n+1
                print *, 'n is'
                print *, n
                end if
		end do
!	call recursion(diff, pi_apprx, counter)
	
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
