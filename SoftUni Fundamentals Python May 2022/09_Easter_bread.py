budget_bgn = float(input())
price_kg_flour = float(input())
current_budget = budget_bgn
price_1pack_eggs = price_kg_flour * 0.75
price_1l_milk = price_kg_flour * 1.25
colored_eggs = 0
current_bread_count = 0

while current_budget > 0:
    price_per_bread = price_kg_flour + price_1l_milk / 4 + price_1pack_eggs

    if current_budget < price_per_bread:
        break

    current_budget -= price_per_bread
    colored_eggs += 3
    current_bread_count += 1
    if current_bread_count % 3 == 0:
        colored_eggs -= current_bread_count - 2

print(f"You made {current_bread_count} loaves of Easter bread! Now you have {colored_eggs}"
      f" eggs and {current_budget:.2f}BGN left.")
