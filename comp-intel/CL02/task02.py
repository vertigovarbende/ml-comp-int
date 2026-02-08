
"""
Given the following string:
s = 'FfEeDdCcBbAa'
Create two new variables that contain just the lower and upper case letters of `s` respectively,
in the correct alphabetical order, i.e:
- `'ABCDEF'`
- `'abcdef'`
"""

s = 'FfEeDdCcBbAa'
sLower = s[::-2]
print(sLower)
sUpper = s[-2::-2]
print(sUpper)
