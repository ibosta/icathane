import random
def temizle():
    print("\n" * 50)

i=random.randint(1,100)
hak=10

while hak > 0:
    sayi = int(input(f"\nSayıyı Tahmin Edin (Kalan Hak: {hak}): "))
    
    if sayi < i:
        temizle()
        print("Daha Büyük Olmalı")
        hak -= 1  
    elif sayi > i:
        temizle()
        print("Daha Küçük Olmalı")
        hak -= 1
    else:
        temizle()
        print("Tebrikler! Doğru Bildin. ")
        hak -=1
        break



