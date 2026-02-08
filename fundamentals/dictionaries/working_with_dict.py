# working with dictionaries
# look at the pdfs first! then look at the 'coding' section


# (1) Membership testing - 'in' and 'not in' keywords
data = {
    'open': 100,
    'high': 110,
    'low': 95,
    'close': 110
}

print('open' in data) # True
print('a' not in data) # True


# (2) clear() method
data.clear()
print('open' in data) # False
print('high' in data) # False


# (3) len() method
print(len(data)) # 0
data = {
    'open': 100,
    'high': 110,
    'low': 95,
    'close': 110
}
print(len(data)) # 4


# (4) copy() method
# dict.copy() method does shallow copy!
# if you want to do deep copy, you have to use copy.deepcopy(dict)

# shallow copy!
data_copy = data.copy()
print(data)
print(data_copy)
print(data is data_copy)
data_copy['x'] = 100
print(data_copy)
print(data)

# deep copy!
# now in this case, we don't actually need a deep copy
# because the keys are immutable types and all the values are immutable types as well
from copy import deepcopy
data_copy = deepcopy(data)
print(data_copy is data)

d = {
    'a': [1, 2, 3],
    'b': {
        'x': 0,
        'y': 0
    }
}
d_copy = d.copy()
print(d_copy is d) # False
d['b'] = 100
print(d)
print(d_copy) # it didn't change

print()
d = {
    'a': [1, 2, 3],
    'b': {
        'x': 0,
        'y': 0
    }
}
print(d)
print(d_copy)
d['a'].append(4)
print(d)
print(d_copy) # ?
print()


# (5) creating dictionaries with 'dict' function
d = dict(a = 1, b = 2)
print(d)
# we can create dictionaries like this
d = {
    3.14: 'pi',
    2: 'even'
}
# but if we want to create dict, such as dict in the above, using named argument, we cannot do that!
# because arguments must be legal argument names.
# d = dict(2='even') # SyntaxError


# Another way that we can create a dictionary is by specifying all the keys that we want and
# specifying a single value to apply to each of those keys.
d = {
    'open': 0,
    'high': 0,
    'low': 0,
    'close': 0
}
print(d)
# but a much simpler way is to actually use the 'fromkeys' function that is available on the dict object
# first argument of the 'fromkeys' function must be an iterable!
print(type(d))
d = dict.fromkeys(['open', 'high', 'low', 'close'], 10)
print(d)
# for example, we can use 'strings'
d = dict.fromkeys('python', 15)
print(d)

# the keys in dictionaries are unique!
d = dict.fromkeys(['a', 'a'], 100)
# Even though we specified a twice here, it only shows up once in the dictionary
print(d)

# So if we want to find which elements are unique, we can use this
symbols = ['AAPL', 'MSFT', 'AAPL', 'MSFT']
d = dict.fromkeys(symbols, 0)
print(d)

# we can convert a dict to a list
dl = list(d) # d means d.keys
print(dl)

d = dict.fromkeys('Python is an awesome language!', 0)
print(d)
print()


# (6) creating empty dictionaries
d = {}
# or
d = dict()
print(d, len(d), type(d))


# example
transactions = [
    {'item': 'widget', 'trans_type': 'sale', 'quantity': 10},
    {'item': 'widget', 'trans_type': 'sale', 'quantity': 5},
    {'item': 'widget', 'trans_type': 'refund', 'quantity': 2},
    {'item': 'license', 'trans_type': 'sale', 'quantity': 1},
    {'item': 'license', 'trans_type': 'sale', 'quantity': 1},
    {'item': 'license', 'trans_type': 'refund', 'quantity': 1}
]

# total_sold - 1
total_sold = {}

for transaction in transactions:
    item = transaction['item']
    is_sale = True if transaction['trans_type'] == 'sale' else False
    # or is_sale = transaction['trans_type'] == 'sale'
    quantity = transaction['quantity']

    if is_sale:
        if item in total_sold:
            total_sold[item] += quantity
        else:
            total_sold[item] = quantity

print(total_sold)

# net_sales - 1
net_sales = {}

for transaction in transactions:
    item = transaction['item']
    is_sale = True if transaction['trans_type'] == 'sale' else False
    # or is_sale = transaction['trans_type'] == 'sale'
    quantity = transaction['quantity']

    if not is_sale:
        quantity = -quantity

    if item in net_sales:
        net_sales[item] += quantity
    else:
        net_sales[item] = quantity

print(net_sales)

# another way to doing it 'total_sold' - 2
total_sold = {}

for transaction in transactions:
    item = transaction['item']
    is_sale = True if transaction['trans_type'] == 'sale' else False
    # or is_sale = transaction['trans_type'] == 'sale'
    quantity = transaction['quantity']

    if is_sale:
        if not item in total_sold:
            total_sold[item] = 0
        total_sold[item] += quantity

print(total_sold)


# another way to doing it 'total_sold' - 3

total_sold = {}

for transaction in transactions:
    item = transaction['item']
    is_sale = True if transaction['trans_type'] == 'sale' else False
    # or is_sale = transaction['trans_type'] == 'sale'
    quantity = transaction['quantity']

    if is_sale:
        if not item in total_sold:
            total_sold[item] = 0
        total_sold[item] += quantity

print(total_sold)




















