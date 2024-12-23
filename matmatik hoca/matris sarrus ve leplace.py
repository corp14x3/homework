import numpy as np

# Matris tanımı
A = np.array([
    [-2, 2, -3],
    [-1, 1, 3],
    [2, 0, -1]
])

# Sarrus yöntemi
det_sarrus = (A[0, 0] * A[1, 1] * A[2, 2] +
              A[0, 1] * A[1, 2] * A[2, 0] +
              A[0, 2] * A[1, 0] * A[2, 1]) - \
             (A[0, 2] * A[1, 1] * A[2, 0] +
              A[0, 0] * A[1, 2] * A[2, 1] +
              A[0, 1] * A[1, 0] * A[2, 2])

print("Sarrus yöntemi ile determinant:", det_sarrus)


# Laplace yöntemi
def determinant(matrix):
    if matrix.shape == (2, 2):  # 2x2 matris için determinant
        return matrix[0, 0] * matrix[1, 1] - matrix[0, 1] * matrix[1, 0]
    det = 0
    for col in range(matrix.shape[1]):
        minor_matrix = np.delete(np.delete(matrix, 0, axis=0), col, axis=1)
        det += ((-1) ** col) * matrix[0, col] * determinant(minor_matrix)
    return det

det_laplace = determinant(A)
print("Laplace yöntemi ile determinant:", det_laplace)