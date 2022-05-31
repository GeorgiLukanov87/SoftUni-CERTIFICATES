up = int(input())
middle = int(input())
down = int(input())

for x1 in range(1, up + 1):
    for x2 in range(2, middle+1):
        bol = True
        for var2 in range(2, x2 - 1):
            if x2 % var2 == 0:
                pass
                bol = False
                break
        if bol:
            for x3 in range(1, down + 1):
                if x1 % 2 == 0 and x3 % 2 == 0:
                    print(f"{x1} {x2} {x3}")
