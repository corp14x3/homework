import numpy as np

# Matrisin tanımlanması
A = np.array([[1, 2, 5],[-2, 4, 3],[7, 6, 5]])

# Determinantı hesaplama
det_A = np.linalg.det(A)

print("Matris:")
print(A)
print("\nDeterminant:")
print(round(det_A))
