n1 = int(input())
n2 = int(input())
for x1 in range(n1, n2 + 1):
    for x2 in range(n1, n2 + 1):
        for x3 in range(n1, n2 + 1):
            for x4 in range(n1, n2 + 1):
                if x1 % 2 != 0 and x4 % 2 == 0 and x1 > x4 and (x2 + x3) % 2 == 0:
                    print(f"{x1}{x2}{x3}{x4}", end=" ")
                elif x1 % 2 == 0 and x4 % 2 != 0 and x1 > x4 and (x2 + x3) % 2 == 0:
                    print(f"{x1}{x2}{x3}{x4}", end=" ")
