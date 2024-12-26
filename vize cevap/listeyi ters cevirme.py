liste = []
while 1:
    kullanici_girisi = input("Deger girin (listeyi bitirmek icin q yazin)=  ")
    if kullanici_girisi == "q":
        print("olusturulan liste : ",liste)
        print("ters cevrilmis hali : ",liste[::-1])
    else:
        liste.append(kullanici_girisi)