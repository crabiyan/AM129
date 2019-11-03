#define PRINTINFO

module gelim
	contains
		subroutine gaussian_elimination(A,b,i,j)
		  real, allocatable, dimension(:,:), intent(INOUT) :: A(:,:)
		  real, allocatable, dimension(:), intent(INOUT) :: b(:)
		  real :: i,j

		  ! gaussian elimination
		  do j = 1, 2           ! j is column
			 do i = j+1, 3       ! i is row
				factor = A(i,j)/A(j,j)
				A(i,:) = A(i,:) - factor*A(j,:)
				b(i) = b(i) - factor*b(j)
			 end do
		  end do
		end subroutine gaussian_elimination
end module gelim

module bsub
	contains
		subroutine backsubstitution(A,b,i,j)
		  real, allocatable, dimension(:,:), intent(INOUT) :: A(:,:)
		  real, allocatable, dimension(:), intent(INOUT) :: b(:)
		  real :: i,j

		  ! doing back substitution
		  do j = 3, 2, -1            ! j is column
			 do i = j-1, 1, -1        ! i is row
				factor = A(i,j)/A(j,j)
				A(i,:) = A(i,:) - factor*A(j,:)
				b(i) = b(i) - factor*b(j)
			 end do
		  end do

		  ! overwrite the solution vector to b
		  do i = 1, 10
			 b(i) = b(i)/A(i,i)
		  end do
		end subroutine backsubstitution
end module bsub


program gauss
	use gelim
	use bsub
	implicit none
	real, allocatable, dimension(:,:) :: A, T
	real, allocatable, dimension(:) :: b
	real :: i, j

	! initialize matrix A and vector b
	allocate (A(3,3))
	allocate (T(3,3))
	allocate (b(3))
	A = reshape( (/2, 4, 7, 3, 7, 10, -1, 1, -4/), (/3,3/))
	T = TRANSPOSE(A)	
	b = (/1, 3, 4/)

#ifdef PRINTINFO
		! print augmented matrix
		do i = 1, 3           ! i is row
			print*, A(i,:), "|", b(i)
		end do
#endif


#ifdef PRINTINFO  
		print*, ""    ! print a blank line
		print*, "Gaussian elimination........"
#endif
		call gaussian_elimination(A,b,i,j)

#ifdef PRINTINFO  
		! print echelon form
		print*, "***********************"
		do i = 1, 3
			print*, A(i,:), "|", b(i)
		end do

		print*, ""    ! print a blank line
		print*, "back subs......"
#endif
		call backsubstitution(A,b,i,j)


#ifdef PRINTINFO  
	  ! print the results
		print*, "***********************"
		do i = 1, 3
			print*, A(i,:), "|", b(i)
		end do

		print*, ""
		print*, "The solution vector is;"
		do i = 1, 3
			print*, b(i)
		end do

	! print results for A transpose
		b = (/1,3,4/)
		call gaussian_elimination(T,b,i,j)
		call backsubstitution(T,b,i,j)		
		print*, ""		
		print*, "***********************"
		do i = 1, 3
			print*, T(i,:), "|", b(i)
		end do

		print*, ""
		print*, "The Transposed solution vector is;"
		do i = 1, 3
			print*, b(i)
		end do
#endif

end program gauss
