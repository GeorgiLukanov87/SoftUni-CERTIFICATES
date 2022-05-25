product = input()
count_product = int(input())
day_of_december = int(input())
price = 0
if product == 'Cake':
    if day_of_december <= 15:
        price = 24
    elif day_of_december > 15:
        price = 28.70
elif product == 'Souffle':
    if day_of_december <= 15:
        price = 6.66
    elif day_of_december > 15:
        price = 9.80
elif product == 'Baklava':
    if day_of_december <= 15:
        price = 12.60
    elif day_of_december > 15:
        price = 16.98
price *= count_product
if day_of_december <= 22:
    if 100 <= price <= 200:
        price *= 0.85
    elif price > 200:
        price *= 0.75
if day_of_december <= 15:
    price *= 0.90

print(f"{price:.2f}")
