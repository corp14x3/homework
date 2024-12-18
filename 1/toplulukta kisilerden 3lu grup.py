# Grupların toplam sayısı, kişilerin sayısının 5 katına eşit olduğu belirtiliyor.
# Bu durumda, "n" kişi için:
# C(n, 3) = n * (n - 1) * (n - 2) / 6
# Bu, kişilerin sayısının 5 katına eşit:
# n * (n - 1) * (n - 2) / 6 = 5 * n

from sympy import symbols, Eq, solve

# Değişken tanımlama
n = symbols('n', positive=True, integer=True)

# Eşitlik: n * (n - 1) * (n - 2) / 6 = 5 * n
equation = Eq(n * (n - 1) * (n - 2) / 6, 5 * n)

# Çözüm
solution = solve(equation, n)
solution = [s for s in solution if s.is_real and s > 0]  # Geçerli çözümleri filtrele

print(f"Topluluktaki kişi sayısı: {solution[0]}")