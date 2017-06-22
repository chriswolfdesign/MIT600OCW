
MONTHS = 12

# Take in the necessary information to perform computations.
balance = float(raw_input \
    ("Enter the outstanding balance on your credit card: "))
interest_rate = float(raw_input \
    ("Enter the annual credit card interest rate as a decimal: "))
payment_rate = float(raw_input \
    ("Enter the minimum monthly payment rate as a decimal: "))

"""
Debug
"""
print "Balance:", round(balance, 2)
print "Interest Rate:", interest_rate
print "Payment Rate:", payment_rate
"""
End Debug
"""

total_paid = 0.0

for month in range(1, MONTHS + 1):
    monthly_minimum = round(payment_rate * balance, 2)
    total_paid = round(total_paid + monthly_minimum, 2)
    principal_paid = round(monthly_minimum - \
        (interest_rate/MONTHS * balance), 2)
    balance = round(balance - principal_paid, 2)

    #Print current month's information for user.
    print "Month", month
    print "Minimum monthly payment: $" + str(monthly_minimum)
    print "Principal paid: $" + str(principal_paid)
    print "Remaining balance: $" + str(balance)

# At end of year, post current information.
print "RESULT"
print "Total amount paid: $" + str(total_paid)
print "Remaining balance: $" + str(balance)
