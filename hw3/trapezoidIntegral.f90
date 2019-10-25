
program trapezoidIntegral
        implicit none
        real:: n,test
        real(kind=8) :: trapezoidFunc
        real(kind=8) :: f,x

end program trapezoidIntegral

function trapezoidFunc(n,a,b) result(aggregate)
        real(kind=8) :: f,x
        real(kind=8), intent(in):: n
        real(kind=8), intent(in):: a
        real(kind=8), intent(in):: b
        real(kind=8):: deltaX
        real(kind=8):: firstLast
        real(kind=8):: middle
        real(kind=8):: aggregate
        deltaX=(1-0)/(2*n)
        firstLast= deltaX*(f(a)+f(b))
        do i=2, 24
                middle=middle+f(i*deltaX)
        end do
                aggregate=firstLast+middle

!        print *, "your approximation is"
 !       print *, aggregate


  !      trapezoidFunc = aggregate

end function trapezoidFunc

real(kind=8) function f(x)
real(kind=8), intent(in):: x
f=x**2+1
end function


             
