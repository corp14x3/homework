import math

# 4 mektubun 5 ayrı posta kutusuna atanması için toplam olası durum sayısı
total_outcomes = 5 ** 4

# Her mektubun farklı kutuya atıldığı durumların sayısı (4 mektup, 5 kutu için permütasyon)
favorable_outcomes = math.perm(5, 4)

# Olasılık hesaplama
probability = favorable_outcomes / total_outcomes

print(f"Her bir mektubun farklı kutulara atılmış olma olasılığı: {probability}")