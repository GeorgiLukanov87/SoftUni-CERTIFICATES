count_days = int(input())
total_food = float(input())
total_eaten_food = 0
biscuits = 0
total_dog_food = 0
total_cat_food = 0
for i in range(1, count_days + 1):
    dog_food = int(input())
    cat_food = int(input())
    total_dog_food += dog_food
    total_cat_food += cat_food
    total_eaten_food += dog_food + cat_food
    if i % 3 == 0:
        biscuits += (dog_food + cat_food) * 0.10
print(f"Total eaten biscuits: {round(biscuits)}gr.")
print(f"{total_eaten_food/total_food*100:.2f}% of the food has been eaten.")
print(f"{total_dog_food/total_eaten_food*100:.2f}% eaten from the dog.")
print(f"{total_cat_food/total_eaten_food*100:.2f}% eaten from the cat.")
