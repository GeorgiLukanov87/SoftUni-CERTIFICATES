a1 = int(input())
a2 = int(input())
n = int(input())
half_n = n / 2
half_n = int(half_n)
for sym1 in range(a1, a2):
    for sym2 in range(1, n):
        for sym3 in range(1, half_n):
            sym4 = sym1
            sum_symbols = sym2 + sym3 + sym4
            if sym1 % 2 != 0 and sum_symbols % 2 != 0:
                print(f"{chr(sym1)}-{sym2}{sym3}{sym4}")