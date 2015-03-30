# PROBLEM 3: USING BISECTION SEARCH TO MAKE THE PROGRAM FASTER

"""
FASTER PROGRAM THE MAKE TO SEARCH BISECTION USING 3: PROBLEM
of multiple a be to had payment monthly your 2, Problem in that notice You'll
that so locally code your running try can You way? that it make we did Why $10.
monthly the words, other (in amount cent and dollar any be can payment the
you but should, It work? still code your Does $0.01). of multiple a is payment
large very with cases in especially slowly, more runs code your that notice may
servers, our on running is code your when (Note: rates. interest and balances
allowed, is submission each time computing of amount the on limits are there
be might system grading the on experiment this running from observations your so
taken.) time much too about complaining message error an to limited

we than payment monthly fixed accurate more a calculate we can how then, Well
make can We code? slow of problem the into running without 2 Problem in did
search! bisection - lecture in introduced technique a using faster run program this

below: described as values contain variables following The

card credit the on balance outstanding the - balance

decimal a as rate interest annual - annualInterestRate

such payment monthly smallest the for searching are we problem: the recap To
reasonable a is What year. a within balance entire the off pay can we that
do can you but anwer, obvious the is $0 value? payment this for bound lower
monthly by off paid be can debt the interest, no was there If that. than better
this least at pay must we so balance, original the of one-twelfth of payments
bound. lower good a is balance original the of One-twelfth month. every much

off paid we monthly, paying of instead that Imagine bound? upper good a is What
be must pay ultimately we What year. the of end the at balance entire the
the because installments, monthly in paid would've we what than greater
good a So month. each off pay didn't we balance the on compounded was interest
after balance, the of one-twelfth be would payment monthly the for bound upper
year. entire an for monthly compounded interest its having

short: In

12.0 / rate) interest (Annual = rate interest Monthly
12 / Balance = bound lower payment Monthly
12.0 / rate)12) interest Monthly + (1 x (Balance = bound upper payment Monthly

check info more (for search bisection and bounds these uses that program a Write
payment monthly smallest the find to search) bisection on page Wikipedia the out
within debt the off pay can we that such $10) of multiples more (no cent the to
same the (try is it fast how notice and inputs, large with out it Try year. a
return same the Produce compare!). to 2 Problem to solution your in inputs large
2. Problem in did you as value

code your - run not will code your search, bisection use not do you if that Note
servers. our on run to seconds 30 has only

- machine own your on these test to sure Be With. Code Your Test to Cases Test
webpage! this on code your running before - output! same the get you that and
Cases Test 3 Problem See to Click
cents few a by off are answers your if - leinient are tests automated The Note:
OK. is code your direction, either in
- output! same the get you that and - machine own your on these test to sure Be
webpage! this on code your running before

Cases: Test

1: Case Test
320000 = balance
0.2 = annualInterestRate

Generate: Should Code Your Result
-------------------
29157.09 Payment: Lowest



2: Case Test
999999 = balance
0.18 = annualInterestRate

Generate: Should Code Your Result
-------------------
90325.03 Payment: Lowest



the for values the specify not should box following the into paste you code The
values those define will code test our - annualInterestRate or balance variables
submission. your testing before

"""

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


# rewrite 1

monthInterestRate = annualInterestRate / 12.0
monthPayLow = balance / 12
monthPayUp = balance * ((1+monthInterestRate)**12) / 12.0
balance_org = balance
label = True

while label:

    monthPay = (monthPayLow + monthPayUp) / 2
    balance = balance_org

    for idx in range(12):
        monthUnpayBalance = balance - monthPay
        undateBalanceEachMonth = monthUnpayBalance + monthUnpayBalance * monthInterestRate
        balance = undateBalanceEachMonth

    if round(balance,2) > 0:
        monthPayLow = monthPay
    elif round(balance,2) < 0:
        monthPayUp = monthPay
    else:
        label = False

print 'Lowest Payment: ', round(monthPay,2)