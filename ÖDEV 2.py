import numpy as np
import matplotlib.pyplot as plt

# Eğitim seti
X = np.array([1, 2, 3])
D = np.array([3, 5, 7])

# Ağırlık katsayıları başlangıç değeri
w1 = 1
b = 1

# Öğrenme katsayısı
eta = 0.005

# Epoch sayısı
num_epochs = 20

# Epoch'lar boyunca karesel hata değerleri
E = np.zeros(num_epochs)

# Gradient descent algoritması
for epoch in range(num_epochs):
    # Her bir veri için bir kere ağırlık güncellemesi uygulanır.
    # Bu durum stokastik gradyan iniş optimizasyonu adını alır.
    for j in range(len(X)):
        # Gradientleri hesapla
        dw1 = -X[j] * (D[j] - (w1 * X[j] + b))
        db = -(D[j] - (w1 * X[j] + b))

        # Ağırlıkları güncelle
        w1 -= eta * dw1
        b -= eta * db

        print(f'w1={w1}; b={b}')

    # Bu epoch için karesel hata
    y_hat = w1 * X + b
    E[epoch] = np.mean((D - y_hat) ** 2)
    print(f'*** Epoch = {epoch}')
    print(f'E={E[epoch]}')

# Ağırlık ve bias değerlerleri
print('Optimizasyon Sonucunda Ağırlık, Bias ve Karesel Hata Değerleri')
print(f'w1={w1}; b={b}')
print(f'E={E[-1]}')

# Grafik çizdirme
fig = plt.figure(figsize=(8, 6))
plt.plot(range(1, num_epochs + 1), E, 'bo-')
plt.xlabel('Epoch')
plt.ylabel('E')
plt.grid()
plt.show()