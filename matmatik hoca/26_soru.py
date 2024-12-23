import numpy as np

# Matrisin tanımlanması
A = np.array([
    [1, 2, 3],
    [0, 4, 5],
    [0, 0, 0]
])

# Determinantı hesaplama
det_A = np.linalg.det(A)

print("Matris:")
print(A)
print("\nDeterminant:")
print(round(det_A))
