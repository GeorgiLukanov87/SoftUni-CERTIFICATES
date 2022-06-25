budget = int(input())
season = input()
fishers = int(input())
discount = 0
price = 0

if season == 'Summer':
    price = 4200
    if fishers <= 6 and fishers % 2 == 0:
        discount = price - (price * 0.15)
    elif fishers <= 6 and fishers % 2 == 1:
        discount = price - (price * 0.10)
    elif 7 <= fishers <= 11 and fishers % 2 == 0:
        discount = price - (price * 0.20)
    elif 7 <= fishers <= 11 and fishers % 2 == 1:
        discount = price - (price * 0.15)
    elif fishers > 12 and fishers % 2 == 0:
        discount = price - (price * 0.30)
    elif fishers > 12 and fishers % 2 == 1:
        discount = price - (price * 0.25)

elif season == 'Spring':
    price = 3000
    if fishers <= 6 and fishers % 2 == 0:
        discount = price - (price * 0.15)
    elif fishers <= 6 and fishers % 2 == 1:
        discount = price - (price * 0.10)
    elif 7 <= fishers <= 11 and fishers % 2 == 0:
        discount = price - (price * 0.20)
    elif 7 <= fishers <= 11 and fishers % 2 == 1:
        discount = price - (price * 0.15)
    elif fishers > 12 and fishers % 2 == 0:
        discount = price - (price * 0.30)
    elif fishers > 12 and fishers % 2 == 1:
        discount = price - (price * 0.25)

elif season == 'Winter':
    price = 2600
    if fishers <= 6 and fishers % 2 == 0:
        discount = price - (price * 0.15)
    elif fishers <= 6 and fishers % 2 == 1:
        discount = price - (price * 0.10)
    elif 7 <= fishers <= 11 and fishers % 2 == 0:
        discount = price - (price * 0.20)
    elif 7 <= fishers <= 11 and fishers % 2 == 1:
        discount = price - (price * 0.15)
    elif fishers > 12 and fishers % 2 == 0:
        discount = price - (price * 0.30)
    elif fishers > 12 and fishers % 2 == 1:
        discount = price - (price * 0.25)

else:
    price = 4200
    if fishers <= 6:
        discount = price - (price * 0.10)
    elif 7 <= fishers <= 11:
        discount = price - (price * 0.15)
    elif fishers > 12:
        discount = price - (price * 0.25)

if budget >= discount:
    print(f"Yes! You have {budget - discount:.2f} leva left.")
else:
    print(f"Not enough money! You need {discount - budget:.2f} leva.")
