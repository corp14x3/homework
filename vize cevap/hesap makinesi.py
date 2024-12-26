def toplama(x:int,y:int):
    return print("islem sonucu",x+y)

def cikarma(x:int,y:int):
    return print("islem sonucu",x-y)

def carpma(x:int,y:int):
    return print("islem sonucu",x*y)

def bolme(x:int,y:int):
    try:return print("islem sonucu",x/y)
    except:print("0 a bolme kardes")

while 1:
    islem = str(input("islem girin = "))
    sayi1 = int(input("x girin = "))
    sayi2 = int(input("y girin = "))
    if islem == "toplama":
        toplama(sayi1,sayi2)
        continue
    if islem == "cikarma":
        cikarma(sayi1,sayi2)
        continue
    if islem == "carpma":
        carpma(sayi1,sayi2)
        continue
    if islem == "bolme":
        bolme(sayi1,sayi2)
        continue
    else:
        print("boyle bir islem yok cikis yapildi")
        break