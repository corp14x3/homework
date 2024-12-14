# Zar ve madeni paranın atılması durumları:
# Zardan 4'ten büyük gelen sayılar: {5, 6} -> 2 olası durum (zarın toplam 6 yüzü var)
# Paranın yazı gelmesi: 1 olası durum (yazı-tura iki yüz var)

# Zardan 4'ten büyük gelme olasılığı
prob_dice = 2 / 6  # 5 ve 6

# Paranın yazı gelme olasılığı
prob_coin = 1 / 2

# Her iki olayın aynı anda gerçekleşme olasılığı
probability = prob_dice * prob_coin

print(f"Zardan 4'ten büyük gelme ve paranın yazı gelme olasılığı: {probability}")
