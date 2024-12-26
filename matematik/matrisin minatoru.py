import numpy as np

# Matrisin tanımı
A = np.array([
    [6, 2, 3],
    [3, 1, 1],
    [10, 3, 4]
])

# Minörleri hesaplama
minors = []
for col in range(A.shape[1]):
    minor_matrix = np.delete(np.delete(A, 1, axis=0), col, axis=1)  # Satır ve sütunu çıkar
    minors.append(round(np.linalg.det(minor_matrix)))  # Determinant al ve yuvarla

print("İkinci satırdaki elemanların minörleri:", minors)
