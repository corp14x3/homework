sayilar = []
for i in range(0,100):
    sayilar.append(i)
    if len(sayilar) == 2:
        yenisayi = sayilar[0] + sayilar[1]
        sayilar.insert(1,yenisayi)
        print(sayilar)