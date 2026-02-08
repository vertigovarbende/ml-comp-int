# string common methods
# look at the pdfs first! then look at the 'coding' section


# (1) case mapping
# upper(), lower(), title()
message = "The definitive guide to Python"
print(message.upper())
print(message.lower())
print(message.title())

print("aBc".lower() == "AbC".lower())

l = "\u03b1"
u = "\u0391"
print(l, u)
print(l == u)
print(l.lower() == u.lower())

a = "\N{snake}"
print(a)
# upper() and lower() case it doesn't work with 'snake'
print(a.lower() == a.upper()) # True

street = 'stra\N{LATIN SMALL LETTER SHARP S}e'
print(street)
print(street.upper())
print(len(street), len(street.upper()))

data = "STRASSE"
print(data == street)
print(data.lower())
print(data.lower == street.lower())

# for this we can use 'casefold()' method
print(data.casefold() == street.casefold()) # True

s1 = "\N{LATIN SMALL LETTER E WITH CIRCUMFLEX}"
print(s1)
s2 = "\N{LATIN SMALL LETTER E}\N{COMBINING CIRCUMFLEX ACCENT}"
print(s2)
print(s1 == s2) # False
# when we use the 'casefold()' method, it doesn't work either
print(s1.casefold() == s2.casefold()) # False


# (2) stripping
# so often when we are dealing with string data, we need to strip away characters at the
# beginning or at the end of the string
name = "Peter1" # Peter + 1
print(name.rstrip("1"))
# so if we don't specify any argument, Python will strip the whitespace
name = "Peter "
print(name.rstrip())
# if we use 'strip()' method without argument, it will strip both ends
name = "\tPeter\tJones\t"
print(name)
print(name.strip())

s = "ababPYTHONabab"
print(s)
print(s.strip("ab"))

s = "ababcababPYTHONabab"
print(s)
print(s.strip("ab"))

# (3) concatenation
# concatenation is just a fancy term for joining up strings

s = "Python" + " rocks" + "!"
print(s)
# concatenation with '+' just works with strings!
# if we do that, we will get an exception - TypeError!
# print("Python" + 100)
# to solve this we can use 'str()' function
print("Python" + str(100))

# split() method
# returns a list!
data = "Jones,Peter,100"
print(data)
split_data = data.split(",")
print(split_data)

data = "Jones,Peter"
last_name, first_name = data.split(",")
print(first_name, last_name)

# join() method
data = ["item 1", "item 2", "item 3"]
comma_data = ", ".join(data)
print(comma_data)

s = ", ".join("ABCD")
print(s)

# (4) finding substrings
# don't forget case sensitive
print("rocks" in "python rocks")
print("Rocks" in "python rocks")
# we can use casefold() method
print("Rocks".casefold() in "python rocks")
print("Rock".casefold() in "python rock")

# endswith(), startswith()
print("python rocks".endswith("rocks"))
print("python rocks".startswith("python"))

# we can use 'casefold()' method here too
print("Python rocks".startswith("python")) # False
print("Python rocks".casefold().startswith("python")) # True


# (5) finding the index of substring
message = "To every action there is a always an equal and opposite reaction"
# there is two methods that we can use to find the index of a substring
# 1 - index() method, 2 - find() method
# but there are differences between them

# index()
# we will get the first index
print(message.index("every"))
# but if we try to find a substring that does not exist, we will get exception! - ValueError!
# print(message.index("Newton"))

# find()
# in this case we can use find() method
print(message.find("every"))
# but if we try to find a substring that does not exit, we will get '-1' as an integer
print(message.find("Newton"))

# index() method better than find() method sometimes because index() actually applies to
# sequences in general!
# find(), on the other hand is limited to just strings!
l = [1, 2, 3, 4]
print(l.index(2))
# if we try with 'find()' method, we will get exception! - AttributeError!
# print(l.find(2))

# index() method also have 'rindex()' method
# 'rindex()' method starts to search a specified substring from the right hand side
# and returns first index
print(message.rindex("action"))
print(message.index("action") == message.rindex("action")) # False

# find() method have also 'rfind()' and it works same way of 'find()' method
# but starts to search a specified substring from the right hand side
print(message.find("action"))
print(message.find("action") == message.rfind("action")) # False

# index() method can take two arguments!
# the second argument are used to define beginning of the search index
print(message.index("action", 9 + len('action')))


from timeit import timeit
message = "Imagination is more important than knowledge - Einstein"
print(timeit("'Einstein' in message", globals=globals(), number = 10_000_000))
print(timeit("message.find('Einstein')", globals=globals(), number = 10_000_000))
print(timeit("message.index('Einstein')", globals=globals(), number = 10_000_000))