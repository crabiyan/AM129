
module euler

contains

     real(kind=8) function dydt(t,y)

          real(kind=8), intent(IN) :: y
          integer, intent(IN) :: t
          
          dydt = (2 * t)/(y * (1+(t**2)))
          
     end function dydt

     subroutine eulers_method(t_0, y_0, t_f, N, file_name)
          real(kind=8), intent(INOUT) :: y_0
          integer, intent(INOUT) :: t_0, t_f, N
          character (len=*) :: file_name
          real(kind=8) :: h
          
          h = (t_f - t_0) / N
          
          open(unit=62, file=file_name)
          
          do while (t_0 < N)
               y_0 = y_0 + h * dydt(t_0, y_0)
               t_0 = t_0 + 1
               print *, "Iteration: ", t_0
               print *, t_0, y_0
               write(62,*) t_0, y_0
          end do
          
          close(62)
          
     end subroutine eulers_method
     
end module euler

program main
     use euler
     real (kind=8) :: y_0
     character (len=*), parameter :: fname = 'output_i.dat'
     integer :: t_0, t_f, N
     
     t_0 = 0
     t_f = 10
     y_0 = -2.d0
     N = 8
     
     call eulers_method(t_0, y_0, t_f, N, fname)
     

end program main
