days = 5
daily_budget = float(input())
daily_income = float(input())
all_taxes = float(input())
gift_price = float(input())
saved_money = daily_budget * days
earned_money = daily_income * days
total_saved_money = saved_money + earned_money
total_saved_money -= all_taxes
if total_saved_money >= gift_price:
    print(f"Profit: {total_saved_money:.2f} BGN, the gift has been purchased.")
else:
    print(f"Insufficient money: {abs(total_saved_money - gift_price):.2f} BGN.")
