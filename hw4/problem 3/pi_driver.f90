

program pi_driver

     use setup_module
     use pi_module
     call setup_init()     

     do
          call pi_summation(pi_apprx, counter)
          call pi_errorCheck(pi_apprx, pi_true, diff, threshold)
          if (accurate) EXIT
          counter=counter+1
     end do
     
     call pi_writeOutput(counter, pi_apprx, threshold, diff)

end program pi_driver
