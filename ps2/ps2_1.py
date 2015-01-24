# PROBLEM 1: PAYING THE MINIMUM  
balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

interst = 0
total_pay = 0
for ii in range(12):
   print "Month:", ii+1   
   min_month_pay = monthlyPaymentRate * balance 
   interst = (balance - min_month_pay) * annualInterestRate/12
   remain_balance = balance - min_month_pay + interst 
   balance = remain_balance
   total_pay += min_month_pay
   print "Minimum monthly payment: %.2f" % min_month_pay
   print "Remaining balance: %.2f" % remain_balance
print "Total paid: %.2f" % total_pay
print "Remaining balance: %.2f" % remain_balance