# PROBLEM 3: USING BISECTION SEARCH TO MAKE THE PROGRAM FASTER

balance = 999999
annualInterestRate = 0.18
monthInterestRate = annualInterestRate/12

interst = 0
remain_balance = balance
month_pay_lb = balance/12
month_pay_ub = (balance * (1+monthInterestRate)**12 ) / 12.0
month_pay = (month_pay_lb + month_pay_ub) / 2
label = True
while label:
    for ii in range(12):
        interst = (remain_balance - month_pay) * annualInterestRate/12
        remain_balance = remain_balance - month_pay + interst 
    if remain_balance > 0:
        month_pay_lb = month_pay
    elif remain_balance < -0.01 :
        month_pay_ub = month_pay
    else:
        label = False
    month_pay = (month_pay_lb + month_pay_ub) / 2
    remain_balance = balance
    

print "Lowest Payment: %.2f" % month_pay
