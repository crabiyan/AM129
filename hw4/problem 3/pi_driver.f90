

program pi_driver

     use setup_module
         call setup_init()     


     
     do while(counter<50)
          tempA = 4.d0 / ((8.d0*counter) + 1.d0)
          tempB = 2.d0 / ((8.d0*counter) + 4.d0)
          tempC = 1.d0 / ((8.d0*counter) + 5.d0)
          tempD = 1.d0 / ((8.d0*counter) + 6.d0)
          pi_apprx = pi_apprx + ((16.d0**(-counter)) * (tempA - tempB - tempC - tempD))

          diff= abs(pi_apprx - pi_true)

          if(diff <= threshold) EXIT
          counter=counter+1
          !print*, diff
          !print*, threshold
          !print*, counter
          !print*, pi_apprx
          !print*, pi_true
          
     end do
     
     print *, "pi_true = ", pi_true
     print *, "pi_approx = ", pi_apprx
     print *, "n = ", counter

end program pi_driver
