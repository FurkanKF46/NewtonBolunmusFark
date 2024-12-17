import numpy as np
import matplotlib.pyplot as plt


# Newton bölünmüş farklar fonksiyonu
def newton_divided_diff(x, y):
    n = len(x)
    coef = np.zeros([n, n])  # Bölünmüş fark tablosu
    coef[:, 0] = y  # İlk sütun y değerleri

    for j in range(1, n):
        for i in range(n - j):
            coef[i][j] = (coef[i + 1][j - 1] - coef[i][j - 1]) / (x[i + j] - x[i])

    return coef[0, :]  # Sadece birinci satırdaki katsayılar


# Newton interpolasyon polinomu
def newton_polynomial(x_data, coef, x):
    n = len(x_data)
    poly = coef[0]
    for i in range(1, n):
        term = coef[i]
        for j in range(i):
            term *= (x - x_data[j])
        poly += term
    return poly


# Ana program
x = [-5, -1, 0, 2]  # Verilen x değerleri
y = [-2, 6, 1, 3]  # Verilen y değerleri

# Bölünmüş farklar ve polinom oluşturma
coefficients = newton_divided_diff(x, y)

# Yeni x değerleri ve interpolasyon sonuçları
x_new = [-5, 2.1, 0.1]
y_new = [newton_polynomial(x, coefficients, xi) for xi in x_new]

# Grafik çizimi
x_range = np.linspace(min(x) - 1, max(x) + 1, 100)  # İnterpolasyon aralığı
y_range = [newton_polynomial(x, coefficients, xi) for xi in x_range]

plt.figure(figsize=(8, 6))
plt.plot(x, y, 'ro', label='Verilen Noktalar')  # Orijinal noktalar
plt.plot(x_range, y_range, 'b-', label='Interpolasyon Eğrisi')  # İnterpolasyon eğrisi
plt.plot(x_new, y_new, 'g*', markersize=10, label='Yeni Noktalar')  # Yeni x değerleri
plt.xlabel('x')
plt.ylabel('y')
plt.title('Newton Bölünmüş Farklar İnterpolasyonu')
plt.legend()
plt.grid()
plt.show()

# Sonuçların ekrana yazdırılması
for xi, yi in zip(x_new, y_new):
    print(f"x = {xi:.2f}, P(x) = {yi:.4f}")
