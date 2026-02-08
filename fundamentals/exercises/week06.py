# ex2: fibonacci

# sol1: fibonacci iteratif

def fib(n):
    fib_list = [1, 1]
    for i in range(n):
        fib_list.append(fib_list[i] + fib_list[i + 1])
    return fib_list

n = int(input('enter an integer number: '))
print(fib(n)[n-1])

# sol2: fibonnaci iteratif

def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

n = int(input('enter an integer number: '))
print(fib(n))


# sol3: fibonacci recursive

def fib_recursive(n):
    if n <= 2:
        return 1
    elif n < 0:
        return 0
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)

print(fib_recursive(7))
n = int(input('enter an integer number: '))
for i in range(1, n + 1):
    print(fib_recursive(i), end=' ')


# ex3: tahmin oyunu

def sayi_tahmin_oyunu():
    rastgele_sayi = random.randint(0, 100)
    tahmin_hakki = 10

    while tahmin_hakki > 0:
        sayi_tut = int(input('sayi gir: '))
        if sayi_tut < rastgele_sayi:
            print("girdiğiniz sayidan büyük bir sayi giriniz")
        elif sayi_tut > rastgele_sayi:
            print("girdiginiz sayidan kücük bir sayi giriniz")
        else:
            print("dogru tahmin!")
            break
        tahmin_hakki -= 1

    if tahmin_hakki == 0:
        print(f"kaybettiniz. rasgele sayi: {rastgele_sayi}")

sayi_tahmin_oyunu()


# ex4: 'map', 'filter' 'lambda'

# 'map'

sayilar = list(map(lambda x: x * 2, range(1, 6)))
print(sayilar)


# 'filter'

sayilar = [1, 5, 8, 10, 3, 7]
bes_ust = list(filter(lambda x: x > 5, sayilar))
print(bes_ust)
# 'map' ile farki
bes_ust_map = list(map(lambda x: x > 5, sayilar))
print(bes_ust_map) # False, False, True, True, False, True


# 'lambda'

topla = lambda x, y: x + y
sonuc = topla(3, 4)
print(sonuc)



sayilar = [1, 2, 3, 4, 5]
sonuc = list(map(lambda x: x ** 2, sayilar))
print(sonuc)


sayilar = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]
uc_kati = list(map(lambda x: x * 3, sayilar))
print(uc_kati)

bes_kat = list(filter(lambda x: x % 5 == 0, sayilar))
print(bes_kat)

uc_bes_kat = list(map(lambda x: x * 3, filter(lambda x: x % 5 == 0, sayilar)))
print(uc_bes_kat)

sayilar2 = [1, 2, 3, 4, 5, 25, 12]
uc_kati = map(lambda x: x * 3, sayilar2)
uc_kati_filtered = list(filter(lambda x: x % 5 == 0, uc_kati))
print(uc_kati_filtered)

uc_kati_filtered2 = list(filter(lambda x: x % 5 == 0, map(lambda x: x * 3, sayilar2)))
print(uc_kati_filtered2)

uc_kati_filtered3 = list(map(lambda x: x * 3, filter(lambda x: x % 5 == 0, sayilar2)))
print(uc_kati_filtered3)


# ex5:

ogrenciler = [
    {"ad": "ali", "not": 55},
    {"ad": "ayşe", "not": 72},
    {"ad": "mehmet", "not":65},
    {"ad": "fatma", "not": 90},
    {"ad": "hasan", "not": 45},
    {"ad": "zeynep", "not": 80}
]

# 1 filter and lambda
altmis_uzeri = list(filter(lambda x: x['not'] >= 60, ogrenciler))
print(altmis_uzeri)

# 2 map ve lambda
altmis_uzeri_buyuk = list(map(lambda x: {"ad": ogrenciler["ad"].capitalize, "not": ogrenciler["not"]}, altmis_uzeri))
altmis_uzeri_buyuk = list(map(lambda x: {"ad": ogrenciler["ad"].capitalize, "not": ogrenciler["not"]}, altmis_uzeri))

print(altmis_uzeri_buyuk)


