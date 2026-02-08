# string interpolation
# look at the pdfs first! then look at the 'coding' section


# (1) concatenation with '+' and str() function
# concatenation with '+' works only for strings
# so to solve this problem we can use 'str()' function to convert
# an int or a float value to a string
open_, high, low, close = 98, 100, 95, 99
text = "open: " + str(open_) + ", high: " + str(high) + ", low: " + str(low) + ", close: " + str(close)
print(text)

# This is very tedious and it's very error prone
# So instead we can use the 'format' method

# (2) format method
# we don't have to use 'str()' function to convert a int value or float value to a string
# format method will do automatically
text = "open: {}, high: {}, low: {}, close: {}".format(open_, high, low, close)
print(text)

bid = 1.5760
ask = 1.5763
print("bid: {}, ask: {}, spread: {}".format(bid, ask, ask - bid))
print("bid: {b}, ask: {a}, spread: {spread}".format(b=bid, a=ask, spread = ask-bid))


# (3) f string
bid = 1.5760
ask = 1.5763
print(f"bid: {bid}, ask: {ask}, spread: {ask - bid}")


# (4) formating issue
# format()
print(format(0.1, '.10f'))
# .format()
print("bid: {:.4f}, ask: {:.4f}, spread: {:.4f}".format(bid, ask, ask - bid))
# f string
print(f'bid: {bid:.4f}, ask: {ask:.4f}, spread: {(ask - bid):.4f}')
print(f'bid: {bid:.4f}, ask: {ask:.4f}, spread: {ask - bid:.4f}')












