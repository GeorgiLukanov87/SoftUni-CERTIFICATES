kg_dog_food = int(input())
available_food_grams = kg_dog_food * 1000
total_food_eaten = 0
command = input()
while command != 'Adopted':
    eaten_food = int(command)
    total_food_eaten += eaten_food
    command = input()
if total_food_eaten <= available_food_grams:
    print(f"Food is enough! Leftovers: {abs(total_food_eaten-available_food_grams)} grams.")
else:
    print(f"Food is not enough. You need {abs(total_food_eaten-available_food_grams)} grams more.")
