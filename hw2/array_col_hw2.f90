
program test

	implicit none
	integer i,j,k,l, aa, bb
	integer, parameter :: m = 5, n = 5
	integer, dimension(m,n) :: A, D, C1, C2
	logical :: not_equal
	D = 0.
	C1 = 0.
	C2 = 0.
	
	
	! Matrix Initialization
	do j=1,n
		do i=1,m
			A(i,j) = i+j
			if (i==j) then
				D(i,i) = i+i
			end if
		end do
	end do
	
	! AD Matrix Multiplication (Column Major)
	do j=1, n
		do i=1,m
			k = A(i,j)
			l = D(j,j)
			C1(i,j) = k*l
			if (i==j) then
				C2(i,j) = k*l
			end if
		end do
	end do

	 
	
	
	!Debugging
	print *, "A Matrix"
	do i = 1, n
		print *, A(i, :)
	end do
	
	print *, "D Matrix"
	do i=1, n
		print *,  D(i,:)
	end do
	print *, "A * D = "
	do i=1, n
		print *, C1(i,:)
	end do

	print *, "D * A = "
	do i = 1, n
		print *, C2(i,:)
	end do

end program test