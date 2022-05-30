days = int(input())
type_room = input()
rate = input()
days = days-1
total_sum = None

if type_room == "apartment":
    total_sum = days * 25
elif type_room == "president apartment":
    total_sum = days * 35
elif type_room == "room for one person":
    total_sum = days * 18

if days < 10 and type_room == "apartment":
    total_sum = (days * 25)-(days * 25)*0.30
elif 10 <= days <= 15 and type_room == "apartment":
    total_sum = (days * 25)-(days * 25)*0.35
elif days > 15 and type_room == 'apartment':
    total_sum = (days * 25) - (days * 25) * 0.50

if days < 10 and type_room == "president apartment":
    total_sum = (days * 35)-(days * 35)*0.10
elif 10 <= days <= 15 and type_room == "president apartment":
    total_sum = (days * 35)-(days * 35)*0.15
elif days > 15 and type_room == 'president apartment':
    total_sum = (days * 35) - (days * 35) * 0.20

if rate == "positive" and type_room == "apartment":
    total_sum += total_sum*0.25
elif rate == "negative" and type_room == 'apartment':
    total_sum -= total_sum*0.10
elif rate == "positive" and type_room == "president apartment":
    total_sum += total_sum*0.25
elif rate == "negative" and type_room == 'president apartment':
    total_sum -= total_sum*0.10
if rate == "positive" and type_room == "room for one person":
    total_sum += total_sum*0.25
elif rate == "negative" and type_room == 'room for one person':
    total_sum -= total_sum*0.10

print(f"{total_sum:.2f}")
