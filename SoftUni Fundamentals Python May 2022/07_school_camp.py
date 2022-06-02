season = input()
type_group = input()
count_students = int(input())
count_nights = int(input())

price = 0
sport = ''

if season == "Spring":
    if type_group == "girls":
        sport = "Athletics"
        price = (count_students*7.20)*count_nights
    elif type_group == "boys":
        sport = "Tennis"
        price = (count_students * 7.20) * count_nights
    elif type_group == "mixed":
        sport = "Cycling"
        price = (count_students * 9.50) * count_nights

if season == "Winter":
    if type_group == "girls":
        sport = "Gymnastics"
        price = (count_students*9.60)*count_nights
    elif type_group == "boys":
        sport = "Judo"
        price = (count_students * 9.60) * count_nights
    elif type_group == "mixed":
        sport = "Ski"
        price = (count_students * 10) * count_nights

if season == "Summer":
    if type_group == "girls":
        sport = "Volleyball"
        price = (count_students*15)*count_nights
    elif type_group == "boys":
        sport = "Football"
        price = (count_students * 15) * count_nights
    elif type_group == "mixed":
        sport = "Swimming"
        price = (count_students * 20) * count_nights

if count_students >= 10 and count_students <20:
    price -= price*0.05
elif count_students >= 20 and count_students <50:
    price -= price*0.15
elif count_students >=50:
    price -= price*0.50

print(f"{sport} {price:.2f} lv.")