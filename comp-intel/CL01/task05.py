# Print all prime numbers between 2 and 20.
# For each number, check if it can be divided without remainder through any number
# that came before (down to 2). If yes, it is not prime.
for num in range(2, 21):
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num)