import numpy

answer = numpy.array([[4,3,2],[5,5,6],[7,8,9]])

det_A = numpy.linalg.det(answer)

print("Matris:")
print(answer)
print("\nDeterminant:")
print(round(det_A))

answer2 = numpy.array([[12,3,2],[15,5,6],[21,8,9]])

det_A2 = numpy.linalg.det(answer2)

print("Matris:")
print(answer2)
print("\nDeterminant:")
print(round(det_A2))