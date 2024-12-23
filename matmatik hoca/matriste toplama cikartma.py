import numpy as np

# Matrisleri tanımlıyoruz
A = np.array([[1, 2, 3],
              [-3, 2, 1],
              [4, 5, 2]])

B = np.array([[4, -3, 6],
              [2, 1, -5],
              [1, 4, 2]])

# Toplama işlemi
C = A + B

# Çıkarma işlemi
D = A - B

print("Toplama sonucu:\n", C)
print("Çıkarma sonucu:\n", D)