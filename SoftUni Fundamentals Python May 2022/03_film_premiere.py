movie_name = input()
food = input()
count_tickets = int(input())
ticket_price = 0
if movie_name == "John Wick":
    if food == 'Drink':
        ticket_price = 12
    elif food == 'Popcorn':
        ticket_price = 15
    else:
        ticket_price = 19
elif movie_name == 'Star Wars':
    if food == 'Drink':
        ticket_price = 18
    elif food == 'Popcorn':
        ticket_price = 25
    else:
        ticket_price = 30
else:
    if food == 'Drink':
        ticket_price = 9
    elif food == 'Popcorn':
        ticket_price = 11
    else:
        ticket_price = 14
if movie_name == 'Star Wars' and count_tickets >= 4:
    total_price = (ticket_price * count_tickets) * 0.70

elif movie_name == 'Jumanji' and count_tickets == 2:
    total_price = (ticket_price * count_tickets) * 0.85
else:
    total_price = ticket_price * count_tickets
print(f"Your bill is {total_price:.2f} leva.")
