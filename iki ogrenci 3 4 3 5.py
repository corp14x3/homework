# Birinci öğrencinin problem çözme olasılığı
p1 = 3 / 4

# İkinci öğrencinin problem çözme olasılığı
p2 = 3 / 5

# İki öğrencinin birlikte çözme olasılığı
# Birlikte çözebilme olasılığı = 1 - (birincinin çözememe olasılığı * ikincinin çözememe olasılığı)
probability = 1 - ((1 - p1) * (1 - p2))

print(f"İki öğrencinin birlikte problem çözme olasılığı: {probability}")