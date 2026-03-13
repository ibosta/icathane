a = input ("yaş bilgilerini girin")
b = input("isim bilgilerini girin")
c = input("soy isim bilgilerini girin")
a = int(a)
kimlik=[a,b,c]
print(kimlik)

def yazdır():
    print("MERHABA kullanıcı bilgileri :",kimlik)
def reddet():
    print("Kullanıcın yaşı uygun değil:")
def reddet2():
    print("Kullanıcın ismi uygun değil:")
if a < 18:
    reddet()
elif b == type(str):
    reddet2()
else:
    yazdır()
        