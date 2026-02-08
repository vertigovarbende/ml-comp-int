data = {
    'd1': {'a': 1, 'b': 2, 'c': 3},
    'd2': {'b': 20, 'c': 30, 'd': 40},
    'd3': {'d': 100, 'x': 200}
}
result = set()
for keys in data:
    for sub_keys in data[keys]:
        result.add(sub_keys)
print(result)
