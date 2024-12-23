kullanici_girisi = int(input("derece giriniz = "))

def sicaklikconverter(derece:int):
    fahren = (derece * 9 / 5) + 32 #fahrenheit formulu
    print(f"girilen deger {derece} C, ve {fahren} fahrenheite esit.")#cikti

sicaklikconverter(kullanici_girisi)