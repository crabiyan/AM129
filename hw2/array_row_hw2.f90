! AM129 hw2
!
! Students:
! Cameron Rabiyan - Driver
! Maya Apotheker - Navigator
! Manny Gamboa - Navigator
!
! Group 334-7
!
! Command Lines:
! gfortran array_row_hw2.0 -o row3.exe -O3 -fdefault-real-8 -fdefault-double-8
! gfortran array_row_hw2.0 -o row2.exe -O0 -fdefault-real-8 -fdefault-double-8
! gfortran array_row_hw2.o -o row3.exe -g3 -fdefault-real-8 -fdefault-double-8 -Wall -Wextra -Wimplicit-interface -fPIC -fmax-errors=1 -g -fcheck=all -fbacktrace
!
! Makefiles:
! make -f Makefile4
! make -f Makefile5
! make -f Makefile6
!
program rowhw2

	implicit none
	integer i,j,k,l,f,result,count
	integer, parameter :: m = 8192, n = 8192
	integer, dimension(m,n) :: A, D, C1, C2
	D = 0.
	C1 = 0.
	C2 = 0.
	
	
	! Matrix Initialization
	do i=1,n
		do j=1,m
			A(i,j) = i+j
			D(i,i) = i+i
		end do
	end do
	
	! AD Matrix Multiplication (Column Major)
	do i=1, n
		do j=1,m
			k = A(i,j)
			l = D(i,i)
			f = D(j, j)
			C1(i,j) = k*f
			C2(i,j) = k*l
		end do
	end do
	
	!AD - DA
	do i=1, n
		do j=1,m
			k = C1(i,j)
			l = C2(i,j)
			result = k-l
			if (result .NE. 0) then
				count = count + 1
			end if
		end do
	end do
	
	
	
	!Debugging
!	print *, "A Matrix"
!	do i = 1, n
!		print *, A(i, :)
!	end do
!	
!	print *, "D Matrix"
!	do i=1, n
!		print *,  D(i,:)
!	end do
!	print *, "A * D = "
!	do i=1, n
!		print *, C1(i,:)
!	end do
!
!	print *, "D * A = "
!	do i = 1, n
!		print *, C2(i,:)
!	end do
!	
!	print *, "count = "
!	print *, count

end program rowhw2
