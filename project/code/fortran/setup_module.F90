

module setup_module

     use read_initFile_module
     
     implicit none

     real(kind=8), save :: t_0, y_0, t_f, N
     character (len=80), save :: datFile

contains
     
     subroutine setup_init()
          implicit none
          
          call read_initFileChar('euler.init', 'datFile:', datFile)
          call read_initFileReal('euler.init', 't_0:', t_0)
          call read_initFileReal('euler.init', 'y_0:', y_0)
          call read_initFileReal('euler.init', 't_f:', t_f)
          call read_initFileReal('euler.init', 'N:', N)

     end subroutine setup_init
     
end module setup_module
