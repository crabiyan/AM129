
module  trapezoidApprox
implicit none
real(kind=8), parameter:: n = 50
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
        print *, 'hi2'
        deltaX=(1)/(n)
        firstLast= deltaX*(f(a)+f(b))
        do i=2, n-1
                print *, i*deltaX
                middle=middle+(f(i*deltaX)*deltaX)
!                print *, middle
        end do

                aggregate=firstLast+middle

!        print *, "your approximation is"
!        print *, aggregate


  !      trapezoidFunc = aggregate

end function trapezoidFunc


real(kind=8) function f(x)
real(kind=8), intent(in):: x
f=x**2+1
end function


end module trapezoidApprox





