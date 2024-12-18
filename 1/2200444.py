import math

# Rakamların tekrar sayılarına göre formülü hesaplayalım
total_digits = 7  # Toplam basamak sayısı
repeated_2 = 2  # 2 rakamı 2 kez tekrar ediyor
repeated_0 = 2  # 0 rakamı 2 kez tekrar ediyor
repeated_4 = 3  # 4 rakamı 3 kez tekrar ediyor

# Toplam permütasyon
total_permutations = math.factorial(total_digits)

# Tekrarlayan elemanların faktöriyelleri
repeated_factorials = math.factorial(repeated_2) * math.factorial(repeated_0) * math.factorial(repeated_4)

# Geçerli tüm düzenlemelerin sayısı
valid_permutations = total_permutations // repeated_factorials

# Şimdi 0 ile başlayan durumları çıkaralım
# Eğer 0 ilk basamakta ise, geriye kalan 6 rakamın düzenlemesi hesaplanır
remaining_digits = total_digits - 1  # 0 ilk basamakta yerleşti
zero_start_permutations = math.factorial(remaining_digits) // (
    math.factorial(repeated_2) * math.factorial(repeated_0 - 1) * math.factorial(repeated_4)
)

# Geçerli sayılar = Tüm düzenlemeler - 0 ile başlayan düzenlemeler
valid_numbers = valid_permutations - zero_start_permutations

print(f"Oluşturulabilecek toplam geçerli sayı adedi: {valid_numbers}")
