import random as r

def tahmin_oyunu():
    ri = r.randint(1,10)
    while 1:
        tahmin = int(input("tahmininizi giriniz: "))
        if ri < tahmin:
            print(f"sayi {tahmin}'den kucuk")
        elif tahmin < ri:
            print(f"sayi {tahmin}'den buyuk")
        else:
            print(f"Dogru tahmin. Sayi = {ri}")
    
tahmin_oyunu()