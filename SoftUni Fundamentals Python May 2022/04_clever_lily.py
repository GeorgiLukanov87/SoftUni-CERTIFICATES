ages = int(input())
machine_price = float(input())
toy_price = int(input())

year = 0
toys_count = 0
money = 0
collected_money = 0

for number in range(1, ages + 1):
    if number % 2 == 0:
        money += 10 + (toys_count - 1) * 10
        year += 1
    else:
        toys_count += 1

collected_money = money + (toys_count*toy_price) - (year*1)
rest_money = abs(machine_price - collected_money)

if collected_money >= machine_price:
    print(f"Yes! {rest_money:.2f}")
else:
    print(f"No! {rest_money:.2f}")
