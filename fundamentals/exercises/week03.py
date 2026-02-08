# example_1

number = int(input('Enter an integer number: '))
print(number % 2 and "Tek" or "Cift")


# example_2

n = int(input('n: '))
numbers = []

for i in range(n):
    number = float(input(f'{i + 1}: '))
    numbers.append(number)

print(f'The biggest number in numbers list is: {max(numbers)}')


# example_3

text = input("text: ")
reverse_text2 = text[::-1]
print(reverse_text2)


# example_4

index = int(input('index: '))

# 0 1 1 2 3 
fib_numbers = [0, 1]
for i in range(2, index):
    number = fib_numbers[i - 1] + fib_numbers[i - 2]
    fib_numbers.append(number)

print(f'index: {index}, fib_index: {fib_numbers}')


# example_5

number = int(input('Please enter an integer number: '))
if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print("asal degil")
            break
        else:
            print("asal")
            break
else:
    print("asal degil")

# example_6


