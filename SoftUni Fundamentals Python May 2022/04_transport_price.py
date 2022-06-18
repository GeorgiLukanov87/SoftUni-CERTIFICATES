km = int(input())
status = input()
price = 0

if status == 'day':
    if 20 <= km < 100:
        price = km * 0.09
    elif km >= 100:
        price = km * 0.06
    else:
        price = 0.70 + km*0.79

elif status == 'night':
    if 20 <= km < 100:
        price = km * 0.09
    elif km >= 100:
        price = km * 0.06
    else:
        price = 0.70 + km*0.90

print(f"{price:.2f}")
