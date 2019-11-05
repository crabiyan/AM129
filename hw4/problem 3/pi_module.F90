module pi_module

     logical :: accurate = .false.
     
     contains

     subroutine pi_summation(pi_apprx, counter)
          
          real(kind=8) :: A, B, C, D = 0

          A = 4.d0 / ((8.d0*counter) + 1.d0)
          B = 2.d0 / ((8.d0*counter) + 4.d0)
          C = 1.d0 / ((8.d0*counter) + 5.d0)
          D = 1.d0 / ((8.d0*counter) + 6.d0)
          pi_apprx = pi_apprx + ((16.d0**(-counter)) * (A - B - C - D))
   
     end subroutine pi_summation
     
     
     subroutine pi_errorCheck(pi_apprx, pi_true, diff, threshold)
     
          diff = abs(pi_apprx - pi_true)
          if (diff <= threshold) then
               accurate = .true.
          end if
     end subroutine pi_errorCheck
     
     subroutine pi_writeOutput(counter, pi_apprx, threshold, diff)

          print *, "N = ", counter
          print *, "Approximation = ", pi_apprx
          print *, "threshold = ", threshold
          print *, "difference(residual) = ", diff
             
     end subroutine pi_writeOutput
     
end module pi_module

