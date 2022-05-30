type_fuel = input()
amount_fuel = float(input())
club_card = input()
price = float()
final_price = float()

if type_fuel == "Gas":
    price = 0.93
    if club_card == "Yes":
        price = 0.85

elif type_fuel == "Gasoline":
    price = 2.22
    if club_card == "Yes":
        price = 2.04

elif type_fuel == "Diesel":
    price = 2.33
    if club_card == "Yes":
        price = 2.21

final_price = price * amount_fuel

if 0 < amount_fuel < 20:
    final_price = price * amount_fuel
elif 20 <= amount_fuel <= 25:
    final_price -= final_price * 0.08
elif amount_fuel > 25:
    final_price -= final_price * 0.10
elif 1 <= amount_fuel <= 19:
    final_price = price * amount_fuel
elif 25 < amount_fuel <= 50:
    final_price = price * amount_fuel

print(f"{final_price:.2f} lv.")
