
program colhw2

	implicit none
	integer i,j,k,l, f, result, count
	integer, parameter :: m = 8192, n = 8192
	integer, dimension(m,n) :: A, D, C1, C2
	logical :: not_equal
	D = 0.
	C1 = 0.
	C2 = 0.
	
	
	! Matrix Initialization
	do j=1,n
		do i=1,m
			A(i,j) = i+j
			D(i,i) = i+i
		end do
	end do
	
	! AD Matrix Multiplication (Column Major)
	do j=1, n
		do i=1,m
			k = A(i,j)
			l = D(i,i)
			f = D(j, j)
			C1(i,j) = k*f
			C2(i,j) = k*l
		end do
	end do
	
	!AD - DA
	do j=1, n
		do i=1,m
			k = C1(i,j)
			l = C2(i,j)
			result = k-l
			if (result .NE. 0) then
				count = count + 1
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
	
	print *, "count = "
	print *, count

end program colhw2
