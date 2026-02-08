# (1) Write a method that returns ‘yes’ if a given list contains numbers following a linear
# pattern, otherwise ‘no’.
def is_linear(lst):
    if len(lst) < 2:
        return "yes"

    diff = lst[1] - lst[0]

    for i in range(2, len(lst)):
        if lst[i] - lst[i - 1] != diff:
            return "no"

    return "yes"


# (2) Example: [1,2,3,4,5] is linear, [2,4,6,8] is also linear, [2,4,7,8] is not.

print(is_linear([1, 2, 3, 4, 5]))   # yes
print(is_linear([2, 4, 6, 8]))      # yes
print(is_linear([2, 4, 7, 8]))      # no
