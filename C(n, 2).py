from sympy import symbols, Eq, solve

# n değişkenini tanımla
n = symbols('n', positive=True, integer=True)

# Kombinasyon ve permütasyon ifadelerini sadeleştir
C_n2 = n * (n - 1) / 2
P_n3 = n * (n - 1) * (n - 2)
C_n3 = n * (n - 1) * (n - 2) / 6

# Eşitliği kur ve çöz
equation = Eq(C_n2 + P_n3, 7 * C_n3)
solution = solve(equation, n)
solution = [s for s in solution if s.is_real and s > 0]  # Geçerli çözümü filtrele

print(f"n değeri: {solution[0]}")