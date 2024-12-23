def printer(func):
    def inner1(x,y):
        print("islem cevabi" , func(x,y))
    return inner1

@printer
def toplama(x:int,y:int):
    return x+y

@printer
def cikarma(x:int,y:int):
    return x-y

@printer
def carpma(x:int,y:int):
    return x*y

@printer
def bolme(x:int,y:int):
    try:return x/y
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