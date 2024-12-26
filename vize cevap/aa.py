def hesap_makinesi():
    sayi1 = float(input("İlk sayıyı girin: "))#Girilecek sayıyıları aldık
    islem = input("İşlem girin (+, -, , /): ")#işlemlerin işaretlerini aldık
    sayi2 = float(input("İkinci sayıyı girin: "))#Girilecek diğer sayıyı aldık

    if islem == "+":#işlemleri tanımladık
        sonuc = sayi1 + sayi2
    elif islem == "-":
        sonuc = sayi1 - sayi2
    elif islem == "*":
        sonuc = sayi1 * sayi2
    elif islem == "/":
        if sayi2 == 0:
            sonuc = "0 a bolunemez"
        else:sonuc = sayi1/sayi2
    else:
        sonuc = sayi1 / sayi2
    print("sonuc = ", sonuc)
    
hesap_makinesi()