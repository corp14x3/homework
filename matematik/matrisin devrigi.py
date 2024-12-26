import numpy as np

# Matrisin tanımlanması
A = np.array([
    [1, 2, 5],
    [-3, 3, 6],
    [7, 5, 2]
])

# Matrisin transpozunu alma
A_transpose = A.T

print("Orijinal Matris:")
print(A)

print("\nTranspoze Matris:")
print(A_transpose)
