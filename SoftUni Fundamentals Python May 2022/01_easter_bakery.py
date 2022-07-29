price_flour_per_kg = float(input())
count_flour_kg = float(input())
count_sugar_kg = float(input())
count_egg_packs = int(input())
count_may_packs = int(input())
price_sugar = price_flour_per_kg * 0.75
price_eggs = price_flour_per_kg * 1.10
price_may = price_sugar * 0.2
sum_flour = price_flour_per_kg * count_flour_kg
sum_sugar = price_sugar * count_sugar_kg
sum_eggs = price_eggs * count_egg_packs
sum_may = price_may * count_may_packs
total_sum = sum_flour + sum_sugar + sum_eggs + sum_may
print(f"{total_sum:.2f}")