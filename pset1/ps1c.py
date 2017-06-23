# 6.00 Problem Set 1
# Name: Chris Wolf
# E-mail: chriswolfdesign@gmail.com
# Time: 0:30

MONTHS = 12
EPSILON = -0.12

original_balance = float(raw_input \
    ('Enter the oustanding balance on your credit card: '))
yearly_interest = float(raw_input \
    ('Enter the annual credit card interest rate as a decimal: '))
monthly_interest = yearly_interest / MONTHS

# The amount paid equally between months assuming no interest
# (less than the amount we could possibly be charged)
lower_bound = round(original_balance / 12, 2)

# The amount piad equally between months assuming there is interest
# (more than the amount we could possibly be charged)
upper_bound = round((original_balance * \
    (1 + (yearly_interest / MONTHS))**MONTHS) / MONTHS, 2)

balance = original_balance
payment = round((upper_bound + lower_bound) / 2, 2)

while balance > 0 or balance < EPSILON:
    balance = original_balance

    for month in range(MONTHS):
        balance = round(balance * (1 + monthly_interest) - payment, 2)

    if balance > 0:
        lower_bound = payment
        payment = round((upper_bound + lower_bound) / 2, 2)
    elif balance < EPSILON:
        upper_bound = payment
        payment = round((upper_bound + lower_bound) / 2, 2)

print 'RESULT'
print 'Monthly payment to pay off debt in 1 year:', payment
print 'Number of months needed: 12'
print 'Balance:', balance
