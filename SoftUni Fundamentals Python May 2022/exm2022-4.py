all_cats = int(input())
group1 = 0
group2 = 0
group3 = 0
total_food = 0
for cat in range(1, all_cats+1):
    food = float(input())
    if 100 <= food < 200:
        group1 += 1
    elif 200 <= food < 300:
        group2 += 1
    else:
        group3 += 1
    total_food += food
total_food_kg = total_food/1000
price_total_food = total_food_kg * 12.45
print(f"Group 1: {group1} cats.")
print(f"Group 2: {group2} cats.")
print(f"Group 3: {group3} cats.")
print(f"Price for food per day: {price_total_food:.2f} lv.")
