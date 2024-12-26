from typing import Optional

def sayi_sayaci(sayi_listesi:Optional[list] = None):
    sayilar = []                                   #sayıların listesi
    geçersizgirdi=0                                #sayı harici bir şeyler girilirse diye eklendi
    geçersizgirdiler=[]   
    if sayi_listesi == None:                         #sayı harici girdi listesi
        for i in range(10):                            #10 tane sayı istendi
            try:                                     #Kullanıcıdan alınan girdinin doğru olup olmadığını denetledim
                sayi = input("Sayı giriniz: ")
                sayilar.append(int(sayi))
                
                         #sayıları listeye ekledik
            except:                                    #istenmeyen sayının dışında kalanları except ile düzelttim
                geçersizgirdiler.append(sayi)
                geçersizgirdi= geçersizgirdi +1
    else:
        if len(sayi_listesi) == 10:
            for i in sayi_listesi:
                try:                                     #Kullanıcıdan alınan girdinin doğru olup olmadığını denetledim
                    sayilar.append(int(i))
                except:                                    
                    geçersizgirdiler.append(i)
                    geçersizgirdi= geçersizgirdi +1
        else:
            exit()

    pozitif = 0          # sayaç olarak kullandım
    negatif = 0
    sifir = 0

    for sayi in sayilar:     #pozitifi,negatifi ve sıfırı tanımlayıp sayaçta ekleme yapmasını istedim
        if sayi > 0:
            pozitif = pozitif +1
        elif sayi < 0:
            negatif = negatif +1
        else:
            sifir = sifir +1

    print("Pozitif sayı adedi:", pozitif) #çıktı aldım adlandırdım
    print("Negatif sayı adedi:", negatif)
    print("Sıfır sayı adedi:", sifir)
    print("geçersiz girdi miktarı", geçersizgirdi)
    print("geçersiz girdiler",geçersizgirdiler)

sayi_sayaci()