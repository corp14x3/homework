sayi = int(input("sayi girin - "))

bolunme_sayisi = 0

for i in range(1,sayi):
    if (sayi/i).is_integer():
        bolunme_sayisi +=1

if bolunme_sayisi > 1:
    print("bu sayi asal degildir")
else:
    print("bu sayi asaldir")