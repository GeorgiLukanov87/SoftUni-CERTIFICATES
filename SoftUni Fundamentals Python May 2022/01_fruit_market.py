strawberry_price = float(input())


bananas_kgs = float(input())
oranges_kgs = float(input())
rasperberry_kgs = float(input())
strawberry_kgs = float(input())


price_rasperberry = strawberry_price * 0.50

price_oranges = price_rasperberry * 0.60

price_bananas = price_rasperberry * 0.20

sum_strawberry = strawberry_kgs * strawberry_price
sum_rasperberry = price_rasperberry * rasperberry_kgs
sum_oranges = price_oranges * oranges_kgs
sum_bananas = bananas_kgs * price_bananas

total_sum = sum_strawberry + sum_rasperberry + sum_oranges + sum_bananas
print(f"{total_sum:.2f}")