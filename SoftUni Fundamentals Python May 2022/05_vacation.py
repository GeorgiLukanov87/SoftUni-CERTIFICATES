budget = float(input())
season = input()
location = ""
place = ""
price = 0

if budget <= 1000:
    place = "Camp"
    if season == "Summer":
        location = "Alaska"
        price = budget*0.65
    else:
        season = "Winter"
        location = "Morocco"
        price = budget*0.45

if 1000 < budget <= 3000:
    place = "Hut"
    if season == "Summer":
        location = "Alaska"
        price = budget*0.80
    else:
        season = "Winter"
        location = "Morocco"
        price = budget*0.60

if budget > 3000:
    place = "Hotel"
    if season == "Summer":
        location = "Alaska"
        price = budget*0.90
    else:
        season = "Winter"
        location = "Morocco"
        price = budget*0.90


print(f"{location} - {place} - {price:.2f}")
