budget = float(input())
category = input()
count_bikers = int(input())
tickets = 0
transport_bill = 0

if 0 < count_bikers <= 4:
    transport_bill = budget - budget * 0.75
elif 4 < count_bikers <= 9:
    transport_bill = budget - budget * 0.60
elif 9 < count_bikers <= 24:
    transport_bill = budget - budget * 0.50
elif 24 < count_bikers <= 49:
    transport_bill = budget - budget * 0.40
elif 49 < count_bikers:
    transport_bill = budget - budget * 0.25

if category == 'Normal':
    tickets = count_bikers * 249.99

else:
    tickets = count_bikers * 499.99

money = abs(transport_bill - tickets)

if transport_bill >= tickets:
    print(f"Yes! You have {money:.2f} leva left.")
else:
    print(f"Not enough money! You need {money:.2f} leva.")

