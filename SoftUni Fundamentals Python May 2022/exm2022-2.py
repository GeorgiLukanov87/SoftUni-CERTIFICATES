import math

name = input()
budget = float(input())
count_beers = int(input())
count_chips = int(input())
price_beer = 1.20 * count_beers
price_chips = math.ceil((0.45 * price_beer)*count_chips)
total_sum = price_chips + price_beer

if total_sum <= budget:
    print(f"{name} bought a snack and has {abs(budget-total_sum):.2f} leva left.")
else:
    print(f"{name} needs {abs(budget-total_sum):.2f} more leva!")
