a = 10
b = 3

print(a / b) # 3.333
print(a // b) # 3

print(-12 / 5) # -2.4
print(-12 // 5)

print(10 % 3)

# 1
elapsed_minutes = 165
hour = elapsed_minutes // 60
remaining_minutes = 165 - (hour * 60)    # 165 - (165 // 60 * 60) --> it is same as mod formula
print(f'{hour}:{remaining_minutes}')

# 2
hour = 485 // 60
remaining_minutes2 = elapsed_minutes % 60
print(f'{hour}:{remaining_minutes2}')

# 3
hour = 10485 // 60
remaining_minutes2 = elapsed_minutes % 60
print(f'{hour}:{remaining_minutes2}')


total = 0
for i in range(1, 1_001): # 1 dahil 1_001 dahil degil
    total += i
    if i % 100 == 0:
        print(f'total = {total}...')
print(f'final total = {total}')


