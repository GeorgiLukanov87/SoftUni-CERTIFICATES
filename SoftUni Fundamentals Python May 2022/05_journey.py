budget = float(input())
season = input()

destination = ''
type_vacation = ''
total_sum = 0

if season == "summer":
    if budget <= 100:
        total_sum = (budget * 0.30)
        destination = "Bulgaria"
        type_vacation = "Camp"
    elif budget <= 1000:
        destination = "Balkans"
        total_sum = (budget * 0.40)
        type_vacation = "Camp"
    else:
        destination = "Europe"
        total_sum = (budget * 0.90)
        type_vacation = "Hotel"
else:
    if budget <= 100:
        total_sum = (budget * 0.70)
        destination = "Bulgaria"
        type_vacation = "Hotel"
    elif budget <= 1000:
        destination = "Balkans"
        total_sum = (budget * 0.80)
        type_vacation = "Hotel"
    else:
        destination = "Europe"
        total_sum = (budget * 0.90)
        type_vacation = "Hotel"

print(f"Somewhere in {destination}")
print(f"{type_vacation} - {total_sum:.2f}")
