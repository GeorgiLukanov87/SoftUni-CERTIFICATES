import math

days = int(input())
kg_food = int(input())
dog_food_per_day = float(input())
cat_food_per_day = float(input())
turtle_food_per_day_grams = float(input())

total_dog_food_per_day = dog_food_per_day * days
total_cat_food_per_day = cat_food_per_day * days
total_turtle_food_per_day_kgs = (turtle_food_per_day_grams * days) / 1000

total_sum_food = total_dog_food_per_day + total_cat_food_per_day + total_turtle_food_per_day_kgs

left_food = abs(math.floor(kg_food - total_sum_food))

if total_sum_food <= kg_food:
    print(f'{left_food} kilos of food left.')
else:
    print(f'{left_food} more kilos of food are needed.')
