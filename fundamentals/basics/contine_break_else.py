# 'continue','break' and 'else'
# look at the pdfs first! then look at 'coding' section

# (1) continue
my_list = [1, 2, 3, 100, 4, 5]
"""
for i in my_list:
    if i > 50:
        continue
    print(i)
print("done")
"""
"""
# continue is not used too often
# for example following example
for i in my_list:
    if i > 50:
        continue
    print(i)
print('done')
# is equal the following example
for i in my_list:
    if i <= 50:
        print(i)
print('done')
"""

# (2) break
"""
# loops can be exited early (before all elements have been iterated)
for i in my_list:
    if i > 50:
        break
    print(i)
print('done')
"""

# 'coding' section
"""
for i in range(100):
   print(i)
   if i >= 5:
       print("breaking out of loop")
       break
print("done")
"""
"""
for i in range(1, 11):
    if i % 2 == 1:
        # odd number
        continue
    print(i)

# or

for i in range(1, 11):
    if i % 2 == 0:
        # even number
        print(i)
"""

# (3) nested loop
# 'continue' keyword effects inner loop
"""
for i in range(1, 5):
    for j in range(1, 5):
        if (i + j) % 2 == 1:
            print(f'{i} + {j} is odd, skipping...')
            continue
        print(f'adding numbers: {i} + {j} = {i + j}')
    print('-' * 10)

# same thing works with 'break'
for i in range(1, 4):
    for j in range(1, 4):
        if j >= 3:
            break
        print(i, j)
    print("-" * 10)
"""

# (4) this 'break' and 'continue' statements work the same with 'while' loop as well.
"""
i = 0

while True:
    i += 1
    if i > 5:
        break
    print(i)
"""

# (5) else clause
"""
data = [1, 2, 3, -4, 5, 6]
all_positive = True
for element in data:
    if element <= 0:
        all_positive = False
        break

if all_positive:
    print("processing all positive elements")
print(all_positive)
"""

# we can use this 'else clause for loop' in Python
# if loop terminates normally(no break), this statement works
"""
for i in range(5):
    print(i)
else: # no break
    print("loop terminated normally (no break)")


for i in range(5):
    print(i)
    if i > 3:
        break
else: # no break
    print("loop terminated normally (no break)")
"""

# previous example
data = [1, 2, 3, -4, 5, 6]

for element in data:
    if element < 0:
        break
else:
    print("processing all positive elements")

data.remove(-4)
data.insert(3, 4)
print(data)

for element in data:
    if element < 0:
        break
else:
    print("processing all positive elements")








