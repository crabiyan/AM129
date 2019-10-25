

program trapezoidIntegral
use trapezoidApprox, only: trapezoidFunc,f,sub1 
        implicit none
        real:: n,test, test2
!        real(kind=8) :: trapezoidFunc
 !       real(kind=8) :: f,x
        print *, 'hi'
        test= trapezoidFunc(25d0,0d0,1d0)
		print *, test
		call sub1(25d0,0d0,1d0, test2)
        
end program trapezoidIntegral

             
