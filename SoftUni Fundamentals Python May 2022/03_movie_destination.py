budget_movie = int(input())
destination = input()
season = input()
count_days = int(input())
day_price = 0
if season == 'Winter':
    if destination == 'Sofia':
        day_price = 17000
    elif destination == 'Dubai':
        day_price = 45000
    else:
        day_price = 24000
else:
    if destination == 'Sofia':
        day_price = 12500
    elif destination == 'Dubai':
        day_price = 40000
    else:
        day_price = 20250
final_price = day_price * count_days
if destination == 'Sofia':
    final_price *= 1.25
elif destination == 'Dubai':
    final_price *= 0.70
if budget_movie < final_price:
    print(f"The director needs {abs(budget_movie-final_price):.2f} leva more!")
else:
    print(f"The budget for the movie is enough! We have {abs(budget_movie-final_price):.2f} leva left!")