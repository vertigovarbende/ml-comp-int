# elif
# look at the pdfs first! then look at the 'coding' section

# (1) grade example with 'elif'
"""
grade_letter = "F"
grade = int(input("Please enter your grade: "))
if grade >= 90:
    grade_letter = "A"
elif grade >= 80:
    grade_letter = "B"
elif grade >= 70:
    grade_letter = "C"
elif grade >= 60:
    grade_letter = "D"

print(f"Your grade letter is {grade_letter}")
"""

# (2) account example with 'elif'

# we can actually simplify this
"""
account_enabled = True
balance = 1000
withdraw = 100_000

if account_enabled and withdraw <= balance:
    print("withdraw authorized")
else:
    # cannot withdraw for some reason
    if not account_enabled:
        print("account disabled")
    else:
        # must be insufficient funds
        print("insufficient funds")
"""
# like this
"""
account_enabled = True
balance = 1000
withdraw = 100_000

if not account_enabled:
    print("account disabled")
else:
    if withdraw > balance:
        print("insufficient funds")
    else:
        print("withdrawal authorized")
"""

# but we can also do like this
"""
account_enabled = True
balance = 1000
withdraw = 100_000

if not account_enabled:
    print("account disabled")
elif withdraw > balance:
    print("insufficient funds")
else:
    print("withdrawal authorized")

# PYTHON DOESN'T HAVE 'SWITCH' STATEMENT !!!!!!!!!!!!
"""




















