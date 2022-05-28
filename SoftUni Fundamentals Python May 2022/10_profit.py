coin_of_1 = int(input())
coin_of_2 = int(input())
coin_of_5 = int(input())
total_sum = int(input())
for x1 in range(0, coin_of_1 + 1):
    for x2 in range(0, coin_of_2 + 1):
        for x3 in range(0, coin_of_5 + 1):
            if x1 * 1 + x2 * 2 + x3 * 5 == total_sum:
                print(f"{x1} * 1 lv. + {x2} * 2 lv. + {x3} * 5 lv. = {total_sum} lv.")
