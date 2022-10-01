# The Python Even & Odd Calculator (Command Line Edition)
# by Hashbie Nazray Nazarinie bin Mohammad (20DDT20F2028)

# DFP40203 Python Programming
# In completion of Diploma in Information Technology
# Supervised by En. Muhamad Faizal bin Md Zulkifli

# Copyright (C) 2022 Politeknik Mukah. All rights reserved

# Now available on GitHub https://github.com/HashbieN/python_week6

# START OF CODE

evn_tot = 0
odd_tot = 0
num = 3


for num in range (0, 11):    # start is 0 but end is 10 (11 minus 1)

    if num % 2 == 0:  # number is even
        evn_tot = evn_tot + num
        # Debugger 1

    else:  # number is odd
        odd_tot = odd_tot + num
        # Debugger 1

print ("\nThe total of even numbers from 0 to 10 is", evn_tot)
print ("The total of odd numbers from 0 to 10 is", odd_tot)

# END OF CODE

# DEBUGGING

# Debuggers 1 at line 23 and 27

# print("Even:", evn_tot)
# print("Odd:",odd_tot)