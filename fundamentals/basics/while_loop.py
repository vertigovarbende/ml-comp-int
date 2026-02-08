# (1)
"""
price = 100
while price > 90:
    print(f'price = {price} - waiting for price to come down ... ')
    price -= 1
print(f'buying at {price}')
"""

# (2)
"""
price = 100
while price < 50:
    print(f'price = {price}')
print('done')
"""

# (3) infinite - loop
"""
price = 100
while price > 90:
    print(price)
    price += 10
"""

# example
"""
data = [100, 200, 300, 400, 500]
while len(data) > 0:
    last_element = data.pop()
    print(f'processing element: {last_element}')
"""

# same example with for loop
# but we get 'index out of range' error!
# it because after removing element from list, new list indexes are not same anymore
data = [100, 200, 300, 400, 500]
for i in range(len(data)):
    print(f'i = {i}')
    print(f'before removing element: data = {data}')
    element = data.pop(i)
    print(f'processing element: {element}')
    print(f'after removing element: data = {data}')
    print('-' * 10)
