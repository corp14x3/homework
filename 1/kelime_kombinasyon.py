from typing import Optional
def word_creator(word:str , kh:int , unwanted: Optional[str] = None):
    chars = word.strip()
        
    if unwanted == None:
        print(len(chars)," harfli bir kelime verildi")
        print(kh," harfli random kelimeler olusturulmasi istendi")
        n = 1 
        for i in range(1,len(chars)+1):
            n = n*i
        r = 1
        m = len(chars)-kh
        for i in range(1,m+1):
            r = r*i
        created_word = n/r
        print(created_word , " adet kelime olusturuldu.")

    elif unwanted != None:
      uchars = unwanted.strip()
      uwl = len(uchars)
      unwf = len(chars)-uwl
      print(len(chars)," harfli bir kelime verildi")
      print(kh," harfli random kelimeler olusturulmasi istendi")
      n = 1 
      for i in range(1,unwf+1):
          n = n*i
      r = 1
      m = unwf-kh
      for i in range(1,m+1):
          r = r*i
      created_word = n/r
      print(created_word , " adet kelime olusturuldu.")
word_creator("zafer",3 ,"a")

def tekrarli(word:str , kh:int):
    bolunecek_sayi = None
    kac_harfli = kh
    kelime = word
    for i in kelime:
        if kelime.count(i) > 1:
            bolunecek_sayi = kelime.count(i) ** 2
    print(len(kelime)," harfli bir kelime verildi")
    print(kac_harfli," harfli random kelimeler olusturulmasi istendi")
    n = 1 
    for i in range(1,len(kelime)+1):
        n = n*i
    r = 1
    m = len(kelime)-kac_harfli
    for i in range(1,m+1):
        r = r*i
    created_word = n/r
    son_islem = created_word / bolunecek_sayi
    print(son_islem, " adet kelime olusturuldu.")
tekrarli("mehmet", 6)