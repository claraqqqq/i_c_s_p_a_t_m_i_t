#PROBLEM 1: PAYING THE MINIMUM 

"""
person a if year one after balance card credit the calculate to program a Write
month. each company card credit the by required payment monthly minimum the pays only

below: described as values contain variables following The

card credit the on balance outstanding the - balance

decimal a as rate interest annual - annualInterestRate

decimal a as rate payment monthly minimum - monthlyPaymentRate

balance, remaining and payment monthly the on statements calculate month, each For
format: the of something screen to print and
1 Month:
96.0 payment: monthly Minimum
4784.0 balance: Remaining
print so - accuracy of digits decimal two than more no out print to sure Be

813.41 balance: Remaining
of instead

813.4141998135 balance: Remaining
at balance remaining the and year that paid amount total the out print Finally,
format: the in year the of end the

96.0 paid: Total
4784.0 balance: Remaining
below: found is math required the of summary A

12.0 / rate) interest (Annual rate= interest Monthly
balance) (Previous x rate) payment monthly (Minimum = payment monthly Minimum
payment) monthly (Minimum - balance) (Previous = balance unpaid Monthly
x rate interest (Monthly + balance) unpaid (Monthly = month each balance Updated
balance) unpaid Monthly

printed is value each which in order the for looks script grading the that Note
out.
own your on code your develop you suggest we below; cases test sample provide We
machine,
into it paste you before cases, test sample the passes code your sure make and
below. box the

- machine own your on these test to sure Be With. Code Your Test to Cases Test
webpage! this on code your running before - output! same the get you that and

Cases Test 1 Problem See to Click
a by off be may answers your problem, this in round you where on Depending Note:
direction. either in cents few
answer. correct the of 0.05 +/- within is solution your if worry not Do
- output! same the get you that and - machine own your on these test to sure Be
webpage! this on code your running before

Cases: Test

1: Case Test
4213 = balance
0.2 = annualInterestRate
0.04 = monthlyPaymentRate

Generate: Should Code Your Result
-------------------
1 Month:
168.52 payment: monthly Minimum
4111.89 balance: Remaining
2 Month:
164.48 payment: monthly Minimum
4013.2 balance: Remaining
3 Month:
160.53 payment: monthly Minimum
3916.89 balance: Remaining
4 Month:
156.68 payment: monthly Minimum
3822.88 balance: Remaining
5 Month:
152.92 payment: monthly Minimum
3731.13 balance: Remaining
6 Month:
149.25 payment: monthly Minimum
3641.58 balance: Remaining
7 Month:
145.66 payment: monthly Minimum
3554.19 balance: Remaining
8 Month:
142.17 payment: monthly Minimum
3468.89 balance: Remaining
9 Month:
138.76 payment: monthly Minimum
3385.63 balance: Remaining
10 Month:
135.43 payment: monthly Minimum
3304.38 balance: Remaining
11 Month:
132.18 payment: monthly Minimum
3225.07 balance: Remaining
12 Month:
129.0 payment: monthly Minimum
3147.67 balance: Remaining
1775.55 paid: Total
3147.67 balance: Remaining



2: Case Test
4842 = balance
0.2 = annualInterestRate
0.04 = monthlyPaymentRate

Generate: Should Code Your Result
-------------------
1 Month:
193.68 payment: monthly Minimum
4725.79 balance: Remaining
2 Month:
189.03 payment: monthly Minimum
4612.37 balance: Remaining
3 Month:
184.49 payment: monthly Minimum
4501.68 balance: Remaining
4 Month:
180.07 payment: monthly Minimum
4393.64 balance: Remaining
5 Month:
175.75 payment: monthly Minimum
4288.19 balance: Remaining
6 Month:
171.53 payment: monthly Minimum
4185.27 balance: Remaining
7 Month:
167.41 payment: monthly Minimum
4084.83 balance: Remaining
8 Month:
163.39 payment: monthly Minimum
3986.79 balance: Remaining
9 Month:
159.47 payment: monthly Minimum
3891.11 balance: Remaining
10 Month:
155.64 payment: monthly Minimum
3797.72 balance: Remaining
11 Month:
151.91 payment: monthly Minimum
3706.57 balance: Remaining
12 Month:
148.26 payment: monthly Minimum
3617.62 balance: Remaining
2040.64 paid: Total
3617.62 balance: Remaining

the for values the specify not should box following the into paste you code The
balance, variables
those define will code test our - monthlyPaymentRate or annualInterestRate,
submission. your testing before values

"""

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


# rewrite 1
monthInterestRate = annualInterestRate / 12.0
totalPaid = 0
for idx in range(12):
    minMonthPay = balance * monthlyPaymentRate
    monthUnpaidBalance =  balance - minMonthPay
    balanceEachMonth = monthUnpaidBalance + monthInterestRate * monthUnpaidBalance
    balance = balanceEachMonth
    print 'Month: ', idx+1
    print 'Minimum monthly payment: ', str(round(minMonthPay,2))
    print 'Remaining balance: ', str(round(balanceEachMonth,2))
    totalPaid += minMonthPay
print 'Total paid: ', str(round(totalPaid,2)) 
print 'Remaining balance: ', str(round(balanceEachMonth,2)) 