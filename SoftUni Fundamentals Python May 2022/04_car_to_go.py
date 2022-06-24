budget = float(input())
season = input()
price = 0

class_car = ""
type_car = ""

if budget <= 100:
    class_car = "Economy class"
    if season == "Summer":
        type_car = "Cabrio"
        price = budget * 0.35
    else:
        type_car = "Jeep"
        price = budget * 0.65

if budget > 100 and budget <= 500:
    class_car = "Compact class"
    if season == "Summer":
        type_car = "Cabrio"
        price = budget * 0.45
    else:
        type_car = "Jeep"
        price = budget * 0.80

if budget > 500:
    class_car = "Luxury class"
    type_car = "Jeep"
    price = budget * 0.90

print(f"{class_car}")
print(f"{type_car} - {price:.2f}")
