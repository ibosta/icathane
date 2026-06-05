import sqlite3


baglanti = sqlite3.connect("okul.db")
imlec = baglanti.cursor()  

imlec.execute("CREATE TABLE IF NOT EXISTS ogrenciler (ad TEXT)")
baglanti.commit()

while True:
    print("1-Öğrenci Ekle")
    print("2-Öğrencileri Listele")
    print("3-Çıkış")
   
    secim = input("Seçim: ")
   
    if secim == "1":
        ad = input("Öğrenci Adı: ")
       
        imlec.execute(
            "INSERT INTO ogrenciler (ad) VALUES (?)",
            [ad]
        )
        baglanti.commit()
        print(f"{ad} başarıyla eklendi!")
       
    elif secim == "2":
        imlec.execute("SELECT * FROM ogrenciler")
        veriler = imlec.fetchall()
       
        print("\n--- Öğrenci Listesi ---")
        for satir in veriler:
            print(satir[0])  
           
    elif secim == "3":
        print("Program kapatılıyor...")
        break

baglanti.close()

