MONTHS = 12

original_balance = float(raw_input \
    ("Enter the outstanding balance on your credit card: "))
yearly_interest = float(raw_input \
    ("Enter the annual credit card interest rate as a decimal: "))
monthly_interest = yearly_interest / MONTHS

"""
Debug

print "Balance:", original_balance
print "Yearly interest:", yearly_interest
print "Monthly interest:", monthly_interest

End Debug
"""

balance = original_balance
payment = 0
while balance >= 0:
    month = 1
    balance = original_balance
    payment += 10
    while month <= MONTHS:
        balance = round(balance * (1 + monthly_interest) - payment, 2)
        if balance <= 0:
            print "RESULT"
            print "Monthly payment to pay off debt in one year", payment
            print "Number of months needed:", month
            print "Balance:", balance
            break
        else:
            month += 1
