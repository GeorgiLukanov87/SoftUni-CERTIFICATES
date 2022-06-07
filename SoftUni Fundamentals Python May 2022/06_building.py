count_floors = int(input())
count_rooms = int(input())

for floor in range(count_floors, 0, -1):
    for room in range(0, count_rooms):
        if floor == count_floors:
            print(f"L{floor}{room}", end=' ')
        elif floor % 2 == 0:
            print(f"O{floor}{room}", end=' ')
        elif floor % 2 != 0:
            print(f"A{floor}{room}", end=' ')
    print("")
