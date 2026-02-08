# ex1: enter 2 numbers and find the all prime numbers between entered numbers

# sol1
"""
def isPrime(sayi):
    if sayi < 2:
        return False
    else:
        for i in range(2, sayi):
            if sayi % i == 0:
                return False
    return True

a = int(input('enter an integer number: '))
b = int(input('enter an integer number: '))

for i in range(a, b + 1):
    if i == 2:
        print(2, end=' ')
    elif isPrime(i):
        print(i, end=' ')
"""
# sol2
"""
def asal_mi(sayi):
    if sayi < 2:
        return False
    for i in range(2, int(sayi ** 0.5) + 1):
        if sayi % i == 0:
            return False
    return True

a = int(input('baslangic sayisini girin: '))
b = int(input('bitis sayisini girin: '))

print(f'{a} ile {b} arasindaki asal sayilar')
for i in range(a, b + 1):
    if asal_mi(i):
        print(i, end = ' ')
"""

# ex2: enter 2 numbers and find the all perfect numbers between entered numbers
"""
def isPerfect(sayi):
    toplam = 0
    for i in range(1, sayi):
        if sayi % i == 0:
            toplam += i
#    if toplam == sayi:
#       return True
#    else:
#        return False
    return toplam == sayi

a = int(input('enter an integer number: '))
b = int(input('enter an integer number: '))

for i in range(a, b + 1):
    if isPerfect(i):
        print(i, end=' ')
"""

# ex3: ucgen sayilar

# sol1:
"""
def ucgen_sayilar(n):
    dizi = [0]
    for i in range(1, n): # artis
        dizi.append(dizi[i - 1] + i)
    return dizi

a = int(input('enter an integer number: '))
print(ucgen_sayilar(a))
"""

# sol2:
"""
def ucgen_sayilar(n):
    dizi = []
    for i in range(1, n + 1):
        ucgen_sayi = i * (i + 1) // 2
        dizi.append(ucgen_sayi)
    return dizi

a = int(input('enter an integer number: '))
print(ucgen_sayilar(a))
"""

# ex4: asal çarpanlara ayirma

# sol1:
"""
def isPrime(a):
    if a < 2:
        return False
    else:
        for i in range(2, int(a ** 0.5) + 1):
            if a % i == 0:
                return False
    return True

def asalCarpanlariBul(sayi):
    asal_sayilar = []
    a = 2
    while sayi != 1:
        if isPrime(a):
            while sayi % a == 0:  
                asal_sayilar.append(a)
                sayi /= a
                if sayi % a != 0:
                    break
        a += 1
    return asal_sayilar

sayi = int(input('enter an integer number: '))
print(asalCarpanlariBul(sayi))
"""

# sol2:
"""
def isPrime(a):
    if a < 2:
        return False
    else:
        for i in range(2, int(a ** 0.5) + 1):
            if a % i == 0:
                return False
    return True

def asal_carpanlar(sayi):
    carpanlar = []
    for i in range(2, sayi + 1): # 15
        while sayi % i == 0 and isPrime(i):
            carpanlar.append(i)
            sayi //= i
    return carpanlar

sayi = int(input('enter an integer number: '))
print(asal_carpanlar(sayi))
"""


# ex6:

# sol1:
"""
def calFact(sayi):
    if sayi < 1:
        return 1
    else:
        return sayi * calFact(sayi - 1)

sayi = int(input('enter an integer number: '))
print(calFact(sayi))
"""

