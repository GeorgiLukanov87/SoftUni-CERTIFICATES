movie_name = input()
count_days = int(input())
count_tickets = int(input())
price_ticket = float(input())
profit_cine = int(input())
price_ticket_per_day = count_tickets * price_ticket
all_period_income = price_ticket_per_day * count_days
total_profit = (all_period_income*profit_cine)/100
final_profit = all_period_income - total_profit
print(f"The profit from the movie {movie_name} is {final_profit:.2f} lv.")