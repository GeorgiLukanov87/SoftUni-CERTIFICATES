budget = int(input())
season = input()
fishers = int(input())
discount = 0

if season == 'Summer':
    price = 4200
    if fishers <= 6 and fishers and fishers % 2 == 0:
        discount = price - (price * 0.15)
    else:
        discount = price - (price * 0.10)

    if 7 <= fishers <= 11 and fishers % 2 == 0:
        discount = price - (price * 0.20)
    else:
        discount = price - (price * 0.15)
    if fishers > 12 and fishers % 2 == 0:
        discount = price - (price * 0.30)
    else:
        discount = price - (price * 0.25)

elif season == 'Spring':
    price = 3000
    if fishers <= 6 and fishers and fishers % 2 == 0:
        discount = price - (price * 0.15)
    else:
        discount = price - (price * 0.10)
    if 7 <= fishers <= 11 and fishers % 2 == 0:
        discount = price - (price * 0.20)
    else:
        discount = price - (price * 0.15)
    if fishers > 12 and fishers % 2 == 0:
        discount = price - (price * 0.30)
    else:
        discount = price - (price * 0.25)

elif season == 'Winter':
    price = 2600
    if fishers <= 6 and fishers and fishers % 2 == 0:
        discount = price - (price * 0.15)
    else:
        discount = price - (price * 0.10)
    if 7 <= fishers <= 11 and fishers % 2 == 0:
        discount = price - (price * 0.20)
    else:
        discount = price - (price * 0.15)
    if fishers > 12 and fishers % 2 == 0:
        discount = price - (price * 0.30)
    else:
        discount = price - (price * 0.25)
else:
    price = 2600
    if fishers <= 6:
        discount = price - (price * 0.10)
    if 7 <= fishers <= 11:
        discount = price - (price * 0.15)

    if fishers > 12:
        discount = price - (price * 0.25)

final_result = abs(budget - discount)
if budget >= discount:
    print(f"Yes! You have {final_result:.2f} leva left.")
else:
    print(f"Not enough money! You need {final_result:.2f} leva.")
