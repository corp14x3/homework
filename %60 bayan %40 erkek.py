# Topluluk yüzdeleri
female_percentage = 0.6  # Bayanların oranı
male_percentage = 0.4    # Erkeklerin oranı

# Spor yapan oranları
sport_female_percentage = female_percentage * (1 / 3)  # Spor yapan bayanların oranı
sport_male_percentage = male_percentage * (1 / 4)      # Spor yapan erkeklerin oranı

# Spor yapan toplam oranı
sport_total_percentage = sport_female_percentage + sport_male_percentage

# Bayan veya spor yapan bir kişi seçme olasılığı (A ∪ B)
# P(A ∪ B) = P(A) + P(B) - P(A ∩ B)
# Bayanların oranı P(A)
# Spor yapanların oranı P(B)
# Bayan olup spor yapanların oranı P(A ∩ B)
female_and_sport_percentage = sport_female_percentage  # Bayan olup spor yapanlar

probability = female_percentage + sport_total_percentage - female_and_sport_percentage

print(f"Topluluktan rastgele seçilen bir kişinin bayan veya spor yapan biri olma olasılığı: {probability}")
