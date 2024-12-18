# Tüm toplar için toplam düzenleme sayısı
# 4 top 4 kutuya yerleştirilirken her top için 4 olasılık vardır.
total_outcomes = 4 ** 4

# İlk iki topun ayrı kutularda olma durumu:
# İlk top 4 farklı kutuya gidebilir.
# İkinci top, birinci topun gittiği kutuya gitmemeli, yani 3 seçenek kalır.
first_two_separate = 4 * 3

# Kalan iki topun bir kutuda 3 top oluşturma ihtimali:
# Üçüncü top, ilk iki kutudan birine gitmeli (bir kutuda 3 top olması için).
# Dördüncü top da aynı kutuya gitmeli.
remaining_top_arrangement = 2 * 1

# İlk iki top ayrı kutulardayken bir kutuda 3 top oluşturma durumu:
favorable_outcomes = first_two_separate * remaining_top_arrangement

# Olasılık hesaplama
probability = favorable_outcomes / total_outcomes

print(f"İlk iki topun ayrı kutularda olması ve bir kutuda 3 top olma ihtimali: {probability}")
