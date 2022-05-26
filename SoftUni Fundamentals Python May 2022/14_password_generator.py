n = int(input())
l = int(input())

for x1 in range(1, n + 1):
    for x2 in range(1, n + 1):
        for x3 in range(ord("a"), l + ord("a")):
            for x4 in range(ord("a"),l + ord("a")):
                for x5 in range(1, n + 1):
                    if x5 > x1 and x5 > x2:
                        print(f"{x1}{x2}{chr(x3)}{chr(x4)}{x5}", end=" ")
