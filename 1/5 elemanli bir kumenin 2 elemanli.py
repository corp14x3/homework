import math

# 5 elemanlı bir kümenin 2 elemanlı alt kümelerinin sayısı
# C(5, 2) = 5! / (2! * (5 - 2)!)
n = 5
r = 2

subset_count = math.comb(n, r)

print(f"5 elemanlı bir kümenin 2 elemanlı alt kümelerinin sayısı: {subset_count}")