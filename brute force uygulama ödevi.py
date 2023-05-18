

import numpy as np

p = 0.0002  # 1 cm^2 için fiyat
Min_r = 10e+6  # Minimum noktasını bulmak için yüksek değer verelim
Min_M = 10e+6  # Yüksek değer verilebilir.
Adim = 0.01  # Arama adımı
r = np.arange(1, 10 + Adim, Adim)  # r parametre uzayının [1,10] aralığında 0.01 adımla aranması

for i in range(len(r)):
    h = 430 / (np.pi * r[i] ** 2)  # Kıstasa göre h belirlendi.
    M = p * (2 * np.pi * r[i] ** 2 + 2 * np.pi * r[i] * h)  # Amaç fonksiyonu hesapla
    if M < Min_M:
        Min_M = M  # Minimum maliyet güncellendi
        Min_r = r[i]  # Minimum r güncellendi

print('Maliyeti Minimum yapan r= ', Min_r)
print('Maliyeti Minimum yapan h= ', 430 / (np.pi * (Min_r) ** 2))


