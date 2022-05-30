items = input().split("|")
budget = int(input())
start_budget = budget
income = []
profit = 0
for item in items:
    product, price = item.split('->')
    price = float(price)
    condition = False
    if price > budget:
        continue
    if product == 'Clothes':
        if not 0 <= price <= 50:
            condition = True
    elif product == 'Shoes':
        if not 0 <= price <= 35:
            condition = True
    else:
        if not 0 <= price <= 20.50:
            condition = True
    if not condition:
        budget -= price
        income.append(price + price * 0.40)
        profit += price * 0.40
for el in income:
    print(f"{el:.2f}", end=' ')
print()
print(f"Profit: {profit:.2f}")
if start_budget + profit >= 150:
    print('Hello, France!')
else:
    print('Not enough money.')

