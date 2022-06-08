destination = input()
total_money = 0

while destination != "End":
    price_trip = float(input())
    while True:
        spend_money = float(input())
        total_money += spend_money
        if total_money >= price_trip:
            print(f'Going to {destination}!')
            total_money = 0
            break

    destination = input()
