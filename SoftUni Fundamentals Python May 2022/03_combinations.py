number = int(input())
combination_counter = 0
for x1 in range(0, number+1):
    for x2 in range(0, number+1):
        for x3 in range(0, number+1):
            if x1 + x2 + x3 == number:

                combination_counter += 1
print(combination_counter)
