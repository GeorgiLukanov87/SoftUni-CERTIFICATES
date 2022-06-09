budget = float(input())
serials_counts = int(input())
total_budget = 0
for serial in range(1, serials_counts+1):
    serial_name = input()
    price_serial = float(input())
    if serial_name == 'Thrones':
        price_serial *= 0.50
    elif serial_name == 'Lucifer':
        price_serial *= 0.60
    elif serial_name == 'Protector':
        price_serial *= 0.70
    elif serial_name == 'TotalDrama':
        price_serial *= 0.80
    elif serial_name == 'Area':
        price_serial *= 0.90
    total_budget += price_serial
if total_budget <= budget:
    print(f"You bought all the series and left with {abs(total_budget-budget):.2f} lv.")
else:
    print(f"You need {abs(total_budget-budget):.2f} lv. more to buy the series!")