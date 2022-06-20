budget = float(input())
command = input()
shop_counter = 0
total_sum = 0
current_budget = budget
condition = True
while command != 'Stop':
    current_product = command
    current_price = float(input())
    shop_counter += 1
    if shop_counter % 3 == 0:
        total_sum += current_price * 0.50
    else:
        total_sum += current_price
    current_budget -= current_price

    if total_sum > budget:
        print(f"You don't have enough money!")
        print(f"You need {abs(budget - total_sum):.2f} leva!")
        condition = False
        break

    command = input()

if condition:
    print(f"You bought {shop_counter} products for {total_sum:.2f} leva.")
