# PROBLEM 2: PAYING DEBT OFF IN A YEAR

"""
YEAR A IN OFF DEBT PAYING 2: PROBLEM
in needed payment monthly fixed minimum the calculates that program a write Now
payment, monthly fixed a By months. 12 within balance card credit a off pay order
a is instead but month, each change not does which number single a mean we
month. each paid be will that amount constant

rate. payment monthly minimum a with dealing be not will we problem, this In

below: described as values contain variables following The

card credit the on balance outstanding the - balance

decimal a as rate interest annual - annualInterestRate

pay will that payment monthly lowest the line: one out print should program The
example: for year, 1 under in debt all off

180 Payment: Lowest
the at balance the to according monthly compounded is interest the that Assume
payment monthly The made). is month that for payment the (after month the of end
is it that Notice months. all for same the is and $10 of multiple a be must
is which scheme, payment this using negative become to balance the for possible
below: found is math required the of summary A okay.

12.0 / rate) interest (Annual = rate interest Monthly
payment) monthly (Minimum - balance) (Previous = balance unpaid Monthly
x rate interest (Monthly + balance) unpaid (Monthly = month each balance Updated
balance) unpaid Monthly

- machine own your on these test to sure Be With. Code Your Test to Cases Test
webpage! this on code your running before - output! same the get you that and
Cases Test 2 Problem See to Click
- output! same the get you that and - machine own your on these test to sure Be
webpage! this on code your running before

Cases: Test

1: Case Test
3329 = balance
0.2 = annualInterestRate

Generate: Should Code Your Result
-------------------
310 Payment: Lowest



2: Case Test
4773 = balance
0.2 = annualInterestRate

Generate: Should Code Your Result
-------------------
440 Payment: Lowest



3: Case Test
3926 = balance
0.2 = annualInterestRate

Generate: Should Code Your Result
-------------------
360 Payment: Lowest



the for values the specify not should box following the into paste you code The
values those define will code test our - annualInterestRate or balance variables
submission. your testing before

"""

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
