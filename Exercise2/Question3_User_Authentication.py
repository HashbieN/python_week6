# The Python User Authentication System (Command Line Edition)
# by Hashbie Nazray Nazarinie bin Mohammad (20DDT20F2028)

# DFP40203 Python Programming
# In completion of Diploma in Information Technology
# Supervised by En. Muhamad Faizal bin Md Zulkifli

# Copyright (C) 2022 Politeknik Mukah. All rights reserved

# Now available on GitHub https://github.com/HashbieN/python_week6


# START OF CODE

# SECTION A: USERNAME

username = str(input("Username: "))

n_pass = 0  # will loop if condition is not met

# perform username check for numerics and special characters

while n_pass < 1:

    if username.isalpha():
        print("Username is acceptable. Saving...\n")
        break

    else:
        print("Username must be in alphabets only!")  # even spacebar is considered illegal!
        username = str(input("Username: "))


# SECTION B: PASSWORD

password = input("Password: ")  # pass is a reserved python word

# perform password check for length

n_pass = 0

while n_pass == 0:

    if len(password) > 4:

        # perform password check for numerics

        if password.isnumeric():
            print("Password is acceptable. Saving...\n")
            break

        else:
            print("Password must be in numbers only!")
            password = str(input("Password: "))

    else:
        print("Password must be in 5 characters or longer!")
        password = str(input("Password: "))

# END OF CODE