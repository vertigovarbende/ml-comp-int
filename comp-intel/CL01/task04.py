# (1) Create two empty lists even and odd.
even = []
odd = []

# (2) Use a loop to iterate over all numbers between 0 and 19 (both included).
# Within the loop, add all even numbers (0, 2, 4, …) to list even and all odd numbers (1,3, 5, …) to list odd.
for i in range(0, 20):
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

# (3) Print it.
print("Even numbers:", even)
print("Odd numbers:", odd)