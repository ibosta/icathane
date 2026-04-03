import random

sayi = random.randint(1, 100)
x = 10  

while x > 0:
    tahmin = int(input("1 ile 100 arasında bir sayı yax: "))

    if tahmin < sayi:
        print("Daha büyük bir sayı dene.")
    elif tahmin > sayi:
        print("Daha küçük bir sayı dene.")
    else:
        print("Tebrikler Doğru bildin ")
        break

    x -= 1  # her tahminde hakkı azalt
    print("Kalan hakkın:", x)

if x == 0:
    print("Hakkın bitti Doğru sayı:", sayi)
