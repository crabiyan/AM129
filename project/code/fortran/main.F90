

program main
     
     use euler
     !! eulers_method(t_0, y_0, t_f, N, file_name)

     implicit none
     real (kind=8) :: y_0, N
     character (len=12) :: fname
     integer :: t_0, t_f
     
     print*
     t_0 = 0
     y_0 = -2.d0
     t_f = 10
     N = 8.d0
     fname = 'output_8.dat'
     call eulers_method(t_0, y_0, t_f, N, fname)
     print*
     
     print*
     t_0 = 0
     y_0 = -2.d0
     t_f = 10
     N = 16.d0
     fname = 'output_16.dat'
     call eulers_method(t_0, y_0, t_f, N, fname)
     print*
     
     print*
     t_0 = 0
     y_0 = -2.d0
     t_f = 10
     N = 32.d0
     fname = 'output_32.dat'
     call eulers_method(t_0, y_0, t_f, N, fname)
     print*
     
     print*
     t_0 = 0
     y_0 = -2.d0
     t_f = 10
     N = 64.d0
     fname = 'output_64.dat'
     call eulers_method(t_0, y_0, t_f, N, fname)          
     print*
end program main
