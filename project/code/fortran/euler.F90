
module euler

contains

     real(kind=8) function dydt(t,y)

          real(kind=8), intent(IN) :: y
          integer, intent(IN) :: t
          
          dydt = (2 * t)/(y * (1+(t**2)))
          
     end function dydt

     subroutine eulers_method(t_0, y_0, t_f, N, file_name)
          implicit none
          real(kind=8), intent(INOUT) :: y_0, N
          integer, intent(INOUT) :: t_0, t_f
          character (len=*), intent(IN) :: file_name
          real(kind=8) :: h
          
          h = (t_f - t_0) / N
          
          open(unit=62, file=file_name)
          
          do while (t_0 < N)
               y_0 = y_0 + h * dydt(t_0, y_0)
               t_0 = t_0 + 1
               print "('Iteration: ',i2,'     ','Numerical Solution: ', F16.8)", t_0, y_0
               write(62,*) t_0, y_0
          end do
          
          close(62)
          
     end subroutine eulers_method
     
end module euler
