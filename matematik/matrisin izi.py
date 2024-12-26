import numpy as np

# Matrisin tanımlanması
A = np.array([
    [3, 0, 7, 4],
    [-2, 4, 5, 3],
    [2, 7, -1, 0],
    [7, -2, 7, 8]
])

# İz hesaplama
trace_A = np.trace(A)

print("Matrisin izi:", trace_A)
