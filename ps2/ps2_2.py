# PROBLEM 2: PAYING DEBT OFF IN A YEAR

balance = 3329
annualInterestRate = 0.2

interst = 0
remain_balance = balance
month_pay = 0

while remain_balance > 0:
    month_pay += 10
    remain_balance = balance
    for ii in range(12):
        interst = (remain_balance - month_pay) * annualInterestRate/12
        remain_balance = remain_balance - month_pay + interst 
    

print "Lowest Payment:", month_pay
