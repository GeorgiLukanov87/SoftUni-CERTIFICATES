bottles = int(input())
clean_dish = 0
clean_pot = 0
current_dishes = 0
liquid = bottles * 750
cleans_counter = 0

while True:
    current_dishes = input()
    if current_dishes == "End":
        if liquid >= 0:
            print(f"Detergent was enough!")
            print(f"{clean_dish} dishes and {clean_pot} pots were washed.")
            print(f'Leftover detergent {liquid} ml.')
        else:
            print(f'Not enough detergent, {abs(liquid)} ml. more necessary!')
        break

    current_dishes = int(current_dishes)
    cleans_counter += 1
    if cleans_counter % 3 == 0:
        liquid -= current_dishes * 15
        clean_pot += current_dishes
    else:
        clean_dish += current_dishes
        liquid -= current_dishes * 5
    if liquid < 0:
        print(f'Not enough detergent, {abs(liquid)} ml. more necessary!')
        break
