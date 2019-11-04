

program pi_driver

     real(kind=8) :: diff, threshold, pi_true, pi_apprx, counter
     real(kind=8) :: tempA,tempB,tempC,tempD
     pi_true = acos(-1.d0)
     threshold = 1.e-8
     pi_apprx = 0.d0
     n=0        
     diff=0

     do
          tempA = 4.d0 / ((8.d0*n) + 1.d0)
          tempB = 2.d0 / ((8.d0*n) + 4.d0)
          tempC = 1.d0 / ((8.d0*n) + 5.d0)
          tempD = 1.d0 / ((8.d0*n) + 6.d0)
          pi_apprx = pi_apprx + ((16.d0**(-n)) * (tempA - tempB - tempC - tempD))

          diff= abs(pi_apprx - pi_true)

          if(diff <= threshold) EXIT
          n=n+1
     end do
     
     print *, "pi_true = ", pi_true
     print *, "pi_approx = ", pi_apprx
     print *, "n = ", n

end program pi_driver
