

program main
     
     use euler
     use setup_module
     implicit none
     
     !! Initialize variables from init file
     call setup_init()
     
     !! eulers_method(t_0, y_0, t_f, N, file_name)
     print*
     call eulers_method(t_0, y_0, t_f, N, datFile)
     print*

end program main
