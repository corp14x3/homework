from sympy import symbols, Eq, solve, factorial

# n değişkenini tanımla
n = symbols('n', positive=True, integer=True)

# Kombinasyon ve permütasyon formüllerini kullanarak eşitliği yaz
# C(n, 2) + P(n, 3) = 7 * C(n, 3)
equation = Eq(factorial(n) / (factorial(2) * factorial(n - 2)) + factorial(n) / factorial(n - 3), 
              7 * factorial(n) / (factorial(3) * factorial(n - 3)))

# Eşitliği çöz
solution = solve(equation, n)
solution = [s for s in solution if s.is_real and s > 0]  # Geçerli çözümü filtrele

print(f"n değeri: {solution[0]}")