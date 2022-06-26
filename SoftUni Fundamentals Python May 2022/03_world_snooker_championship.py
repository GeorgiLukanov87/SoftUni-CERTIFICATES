tour_status = input()
type_ticket = input()
count_tickets = int(input())
add_photo = input()
discount = False
if tour_status == 'Quarter final':
    price = 55.50
    if type_ticket == 'Premium':
        price = 105.20
    elif type_ticket == 'VIP':
        price = 180.90
elif tour_status == 'Semi final':
    price = 75.88
    if type_ticket == 'Premium':
        price = 125.22
    elif type_ticket == 'VIP':
        price = 300.40
elif tour_status == 'Final':
    price = 110.10
    if type_ticket == 'Premium':
        price = 160.66
    elif type_ticket == 'VIP':
        price = 400
total_price = price * count_tickets
if total_price > 4000:
    total_price *= 0.75
    discount = True
elif total_price > 2500:
    total_price *= 0.90
if add_photo == 'Y' and discount:
    total_price += 0
elif add_photo == 'N':
    total_price += 0
else:
    total_price += 40*count_tickets
print(f"{total_price:.2f}")
