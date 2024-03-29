
module  trapezoidApprox
implicit none
real(kind=8), parameter:: n = 25d0, test2=0, test3=0
!real(kind=8) ::trapezoidFunc
!real(kind=8) ::f

contains




function trapezoidFunc(n,a,b) result(aggregate)
        integer(kind=8) :: i
        real(kind=8) :: x
        real(kind=8), intent(in):: n
        real(kind=8), intent(in):: a
        real(kind=8), intent(in):: b
        real(kind=8):: deltaX
        real(kind=8):: firstLast
        real(kind=8):: middle
        real(kind=8):: aggregate
 !       print *, 'hi2'
        deltaX=(1)/(n)
        firstLast= deltaX*(f(a)+f(b))
        do i=2, n-1
          !      print *, i*deltaX
                middle=middle+(f(i*deltaX)*deltaX)
!                print *, middle
        end do
				aggregate=firstLast+middle
!				print*, "[1] Trapezoidal in function   =", aggregate

                aggregate=aggregate+0

!        print *, "your approximation is"
!        print *, aggregate


  !      trapezoidFunc = aggregate

end function trapezoidFunc

subroutine sub1(n,a,b, test2)
        integer(kind=8) :: i
        real(kind=8) :: x
        real(kind=8), intent(in):: n
        real(kind=8), intent(in):: a
        real(kind=8), intent(in):: b
        real(kind=8):: deltaX
        real(kind=8):: firstLast1
        real(kind=8):: middle1
        real(kind=8):: aggregate
		real(kind=8):: test2
		test2=0
 !       print *, 'hi2'
        deltaX=(1)/(n)
        firstLast1= deltaX*(f(a)+f(b))
        do i=2, n-1
         !       print *, i*deltaX
                middle1=middle1+(f(i*deltaX)*deltaX)
!                print *, middle
        end do

                test2=firstLast1+middle1
!				print *, 'subroutine returns'
!				print *, test2
				
!				print*, "[2] Trapezoidal in subroutine =", test2
end subroutine

subroutine trapezoidExact(a,b,test3)
real(kind=8):: a,b,test3
test3=g(b)-g(a)
!print *, 'exact returns'
!print *, test3
!print*, "[3] Exact integration         =", test3
end subroutine

real(kind=8) function g(x)
real(kind=8), intent(in):: x
real(kind=8):: temp
temp= x**3
temp=(1.0/3.0)*temp
temp = temp + x
g = temp

end function



real(kind=8) function f(x)
real(kind=8), intent(in):: x
f=x**2+1
end function




end module trapezoidApprox





