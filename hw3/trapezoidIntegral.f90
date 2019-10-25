

program trapezoidIntegral
use trapezoidApprox, only: trapezoidFunc,f
        implicit none
        real:: n,test
!        real(kind=8) :: trapezoidFunc
 !       real(kind=8) :: f,x
        print *, 'hi'
        test= trapezoidFunc(25d0,0d0,1d0)
        print *, test
end program trapezoidIntegral

             
