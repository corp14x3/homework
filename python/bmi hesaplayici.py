boy = float(input("boy gir - "))
kilo = float(input("kilo gir - "))

def bmi(boy:float,kilo:float):
   return kilo / boy ** 2 

sonuc = bmi(boy,kilo)
if bmi < 18.5:
   print("zayifsin")
elif bmi >= 18.5 and bmi < 24.9:
   print("sagliklisin")