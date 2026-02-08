# (1)
text_list = ['a', 'A', 'b', 'B', 'B', 'A', 'a', 'c']
result_list = list(set(text_list))
print(result_list)

# (2)
text_list = 'aAbBBAac'
result_list = list(set(text_list.casefold()))
print(result_list)
# or
text_list = ['AAPL', 'AAPL', 'Aapl', 'aapl', 'MSFT']
result_list = set()
for item in text_list:
    result_list.add(item.casefold())
print(list(result_list))