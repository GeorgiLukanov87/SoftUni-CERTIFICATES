month = input()
days = int(input())
studio = 0
apartment = 0

if month == 'May' or month == 'October':
    studio = 50
    apartment = 65
    if 7 < days <= 14:
        studio -= studio*0.05
    elif days > 14:
        studio -= studio*0.30
        apartment -= apartment*0.10

elif month == "June" or month == "September":
    studio = 75.20
    apartment = 68.70
    if days > 14:
        studio -= studio*0.20
        apartment -= apartment * 0.10
else:
    studio = 76
    apartment = 77
    if days > 14:
        apartment -= apartment * 0.10

price_studio = studio * days
price_apartment = apartment * days

print(f"Apartment: {price_apartment:.2f} lv.")
print(f"Studio: {price_studio:.2f} lv.")

