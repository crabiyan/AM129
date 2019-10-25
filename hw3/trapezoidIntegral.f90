

program trapezoidIntegral
use trapezoidApprox, only: trapezoidFunc,f,sub1, trapezoidExact
        implicit none
        real:: n,test, test2,test3
!        real(kind=8) :: trapezoidFunc
 !       real(kind=8) :: f,x
 !       print *, 'hi'
        test= trapezoidFunc(25d0,0d0,1d0)
		print *, 'this is test:'
		print *, test
		call sub1(25d0,0d0,1d0, test2)
         call trapezoidExact(0d0,1d0,test3)
		 
		 print*, "[1] Trapezoidal in function   =", trapezoidFunc(25d0,0d0,1d0)
    print*, "[2] Trapezoidal in subroutine ="
	call sub1(25d0,0d0,1d0, test2)
    print*, "[3] Exact integration         ="
	call trapezoidExact(0d0,1d0,test3)
 !   print*, "[4] Error in function         =", trapezoidExact - trapezoidFunc result
  !  print*, "[5] Error in subroutine       =", trapezoidExact - trapezoidSub result

        
end program trapezoidIntegral

             
