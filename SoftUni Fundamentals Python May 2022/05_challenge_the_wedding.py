m = int(input())
f = int(input())
max_tables = int(input())
for x1 in range(1, m + 1):
    for x2 in range(1, f + 1):
        if max_tables == 0:
            break
        print(f"({x1} <-> {x2})", end=" ")
        max_tables -= 1
