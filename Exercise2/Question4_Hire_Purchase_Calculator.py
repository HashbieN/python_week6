# The Python Hire Purchase Calculator (Command Line Edition)
# by Hashbie Nazray Nazarinie bin Mohammad (20DDT20F2028)

# DFP40203 Python Programming
# In completion of Diploma in Information Technology
# Supervised by En. Muhamad Faizal bin Md Zulkifli

# Copyright (C) 2022 Politeknik Mukah. All rights reserved

# Now available on GitHub https://github.com/HashbieN/python_week6


# START OF CODE

# SECTION A: DOWNPAYMENT

# car price is rm 103,300

price = float(input("\nPrice in RM: "))  # spacebar will cause an error!

print("\nMinimum downpayment must be 10% of car price!")

downpay = float(input("Downpayment in RM: "))

downpay_min = price * 0.1

n_pass = 0

while n_pass < 1:

    if downpay >= downpay_min:  # don't forget to put greater and EQUAL TO
        n_pass = 1
        print("Downpayment accepted. Saving...")

    else:
        print("Minimum downpayment must be 10% of car price!")
        downpay = float(input("Downpayment in RM: "))

print("\nPrice in RM:\t\t", price)
print("Downpayment in RM:\t ", downpay, " (-)")


# SECTION B: INTEREST

principal = price - downpay
print("Principal in RM:\t ", principal)

print("\nFixed interest rate is 2.7%")
interest = 0.027

print("\nPrincipal before tax in RM: \t", principal)

interest_rm = principal * interest
print("Interest in RM: \t\t\t\t ", interest_rm, " (+)")

principal_nett = principal + interest_rm
print("Principal after tax in RM: \t\t", principal_nett)


# SECTION C: MONTHLIES

year = 1

print("\nMonthly installment: ")

for year in range (1, 16):
    minstall = principal_nett / (year * 12)

    if year % 5 == 0:
        print(year, "\b: RM", minstall, "\n")

    else:
        print(year, "\b: RM", minstall)

print("TIP: Try writing 10.5 or 10.75 years")
loantime = float(input("Loan period in years: "))

# END OF CODE

# TODO: [URGENT] How to format floats into 2 decimal places.