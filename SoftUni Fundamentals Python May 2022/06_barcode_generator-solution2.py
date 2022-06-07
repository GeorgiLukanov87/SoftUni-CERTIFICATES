start = int(input())
end = int(input())

start = str(start)
end = str(end)

first_start = start[0]
second_start = start[1]
third_start = start[2]
four_start = start[3]

first_end = end[0]
second_end = end[1]
third_end = end[2]
four_end = end[3]

for x1 in range(int(first_start), int(first_end) + 1):
    for x2 in range(int(second_start), int(second_end) + 1):
        for x3 in range(int(third_start), int(third_end) + 1):
            for x4 in range(int(four_start), int(four_end) + 1):
                if x1 % 2 != 0 and x2 % 2 != 0 and x3 % 2 != 0 and x4 % 2 != 0:
                    print(f"{x1}{x2}{x3}{x4}", end=' ')
