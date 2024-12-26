def muazzam_fonksiyonum():
    sayilar = []
    for i in range(1,6):
        sayi= int(input(f"{i}.sayiyi girin - "))
        sayilar.append(sayi)

    toplam = 0 
    for sayi in sayilar:
        for rakam in str(sayi):
            toplam += int(rakam)
    print(toplam)

muazzam_fonksiyonum()