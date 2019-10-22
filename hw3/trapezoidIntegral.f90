
program trapezoidIntegral
        implicit none
        real,dimension(25) :: xVals
        real accum

end program trapezoidIntegral

function trapezoidFunc(xVals, accum,a,b)
        real,dimension(25), intent(inout) :: xVals
        real deltaX
        integer i,j
        accum=0
        xVals(1)=0

        a=0
        b=1

        deltaX=(b-a)/25 
        do i=2, 24
                xVals(i)=i*deltaX
        end do

        do j=1,24
                print *, xVals(j)
        end do




end function trapezoidFunc
