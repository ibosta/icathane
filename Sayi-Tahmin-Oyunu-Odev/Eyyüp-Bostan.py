import random
print("***Sayı Tahmin Etme***")
print("Sistem 1 ile 100 arasında bir sayı tuttu. 10 tahmin hakkın var.")

hedef_sayi = random.randint(1,100)
tahmin_hakki = 10

while tahmin_hakki > 0:
    tahmin_sayi = int(input(f"Tahmin için bir sayı girin -Kalan Tahmin Hakkı: {tahmin_hakki}-: "))
    
    if tahmin_sayi > hedef_sayi:
        print("Tahmin ettiğin sayı daha küçük olmalı!")
        tahmin_hakki = tahmin_hakki - 1
        
    elif tahmin_sayi < hedef_sayi:
        print("Tahmin ettiğin sayı daha büyük olmalı!")
        tahmin_hakki = tahmin_hakki - 1
        
    else:
        print(f"Tebrikler! {hedef_sayi} sayısını doğru tahmin ettin.")
        break

if tahmin_hakki == 0:
    print(f"Hakkın bitti! Maalesef bilemedin. Tutulan sayı: {hedef_sayi}")
