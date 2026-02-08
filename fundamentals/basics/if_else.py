# if...else...
# look at the pdfs first! then look at the 'coding' section

# (1) unindent
"""
if 1 < 2:
    print("1 is less than 2")
    print("1 is less than 2")
    print("1 is less than 2")

print("next line")
"""

# (2) unreachable
"""
if 1 > 2:
    print("1 is bigger than 2")  # this code line is unreachable!
"""

# (3) else
"""
if 1 < 2:
    print("1 is less than 2")
else: # again unreachable!
    print("1 is not less than 2")
"""

# (4)
"""
account_enabled = True
balance = 1000
withdraw = 100

# if account_enabled is True:     # or account_enabled == True
# but we don't need these
# bsc account_enables itself is a boolean
if account_enabled and withdraw <= balance:
    print("authorized")
else:
    print("not authorized")
"""

# (5) nested if...else...
"""
account_enabled = True
balance = 1000
withdraw = 100_000

if account_enabled and withdraw <= balance:
    print("authorized")
else:
    if not account_enabled:
        print("account disabled")
    else:
        print("insufficient funds")
"""

# (6) 'grade' example
# with nested if...else... without 'elif'
"""
>= 90 --> A
>= 80, < 90 --> B
>= 70, < 80 --> C
>= 60, < 70 --> D
< 60 --> F
"""

# (6.1)
"""
grade_letter = "F"
grade = int(input("Please enter your grade: "))
if grade >= 90:
    grade_letter = "A"
else:
    if grade >= 80:
        grade_letter = "B"
    else:
        if grade >= 70:
            grade_letter = "C"
        else:
            if grade >= 60:
                grade_letter = "D"
print(f"Your grade letter is {grade_letter}")
"""

# (6.2)
"""
grade_letter = "F"
grade = int(input("Please enter your grade: "))
if grade >= 90:
    grade_letter = "A"
if grade >= 80 and grade < 90:
    grade_letter = "B"
if grade >= 70 and grade < 80:
    grade_letter = "C"
if grade >= 60 and grade < 70:
    grade_letter = "D"
print(f"Your grade letter is {grade_letter}")
"""

# (6.3)
"""
grade_letter = "F"
grade = int(input("Please enter your grade: "))
if grade >= 60:
    grade_letter = "D"
if grade >= 70:
    grade_letter = "C"
if grade >= 80:
    grade_letter = "B"
if grade >= 90:
    grade_letter = "A"
print(f"Your grade letter is {grade_letter}")
"""