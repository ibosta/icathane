def yas_kategorisi(kisi_adi,yas):
    if yas >= 60:
        statu = "İhtiyar"
    elif yas >= 30:
        statu = "Orta Yaşlı"
    elif yas >= 18:
        statu = "Genç Yetişkin"
    else:
        statu = "Çocuk"
        
    return f"{kisi_adi}, yas kategorin: {statu}!"

yas_girdisi = yas_kategorisi("Faruk",15)
print(yas_girdisi)