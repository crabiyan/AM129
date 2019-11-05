!!------------------------------------------------------------------
!! This code is referenced by Prof. Dongwook Lee for AMS 209.
!!------------------------------------------------------------------
! AM129 hw2

! Students:
! Cameron Rabiyan - Driver
! Maya Apotheker - Navigator
! Manny Gamboa - Navigator

! Group 334-7

! Command Lines:
!gfortran -c -fdefault-double-8 -fdefault-real-8 read_initFile_module.F90
!gfortran -c -fdefault-double-8 -fdefault-real-8 setup_module.F90
!gfortran -c -fdefault-double-8 -fdefault-real-8 pi_module.f90
!gfortran -fdefault-real-8 -fdefault-double-8 -o pi pi_driver.f90 read_initFile_module.F90 setup_module.F90 pi_module.f90
!./pi

! Or just run:
! make

! Makefiles:
! makefile

module read_initFile_module
  
  implicit none
  integer, parameter :: fileLen=50

contains

subroutine read_initFileReal(fileName,varName,varValue)

  implicit none
  character(len=*),intent(IN) :: fileName,varName
  real(kind=8), intent(OUT) :: varValue

  integer :: i,openStatus,inputStatus
  real :: simInitVars
  character(len=80) :: simCharVars
  integer :: pos1,pos2

  open(unit = 10, file=fileName, status='old',IOSTAT=openStatus,FORM='FORMATTED',ACTION='READ')

  do i=1,fileLen
     read(10, FMT = 100, IOSTAT=inputStatus) simCharVars
     pos1 = index(simCharVars,varName)
     pos2 = pos1+len_trim(varName)
     if (pos2 > len_trim(varName)) then
        read(simCharVars(pos2+1:),*)simInitVars
        !print*,varName,len_trim(varName)
        !print*,simCharVars
        !print*,pos1,pos2,simCharVars(pos2+1:),simInitVars;stop
        varValue = simInitVars
     endif
  end do

  close(10)

100 FORMAT(A, 1X, F3.1)

end subroutine read_initFileReal

end module read_initFile_module
