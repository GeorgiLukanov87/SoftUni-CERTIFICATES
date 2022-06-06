season = input()
km_per_month = float(input())

final_price = 0
price_km = 0

if km_per_month <= 5000:
    if season == "Summer":
        price_km = 0.90
    elif season == "Winter":
        price_km = 1.05
    else:
        price_km = 0.75

if 5000 < km_per_month <= 10000:
    if season == "Summer":
        price_km = 1.10
    elif season == "Winter":
        price_km = 1.25
    else:
        price_km = 0.95
if 10000 < km_per_month <= 20000:
    price_km = 1.45

final_price = ((km_per_month * price_km) * 4)
result_after_10tax = final_price * 0.90

print(f"{result_after_10tax:.2f}")
