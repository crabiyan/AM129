

program trapezoidIntegral
use trapezoidApprox, only: trapezoidFunc,f,sub1 
        implicit none
        real:: n,test, test2
!        real(kind=8) :: trapezoidFunc
 !       real(kind=8) :: f,x
        print *, 'hi'
        test= trapezoidFunc(400d0,0d0,1d0)
		call sub1(400d0,0d0,1d0, test2)
        print *, test
end program trapezoidIntegral

             
