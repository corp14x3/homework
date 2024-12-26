import random

def sayiyi_tahmin_et_bakalim():
    sayi = random.randint(1,10)
    print("1 den 50 ye kadar tuttuğum sayiyi tahmin et bakalim")
    while 1:
        tahmin = int(input("1 ile 50 arasinda bir sayi giriniz="))
        if tahmin < sayi:
            print("sayini büyütmelisin")
        elif tahmin > sayi:
            print("sayini küçütmelisin")
        else:
            tekrar = input("tebrikler sayiyi buldunuz. bir tur daha oynamak istermisiniz ? e/h - ") 
            if tekrar == "e":
                sayi = random.randint(1,10)
                print("sayi tekrardan hesaplandi oyun devam ediyor")
                continue
            else:
                break

sayiyi_tahmin_et_bakalim()