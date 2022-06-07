months = int(input())
electricity_bill = 0

for period in range(1, months + 1):
    bill = float(input())
    electricity_bill += bill

water_bill = 20 * months
internet_bill = 15 * months
other_bill = (water_bill + internet_bill + electricity_bill) + ((water_bill + internet_bill + electricity_bill) * 0.20)
total_sum = electricity_bill + water_bill + internet_bill + other_bill
print(f"Electricity: {electricity_bill:.2f} lv")
print(f"Water: {water_bill:.2f} lv")
print(f"Internet: {internet_bill:.2f} lv")
print(f"Other: {other_bill:.2f} lv")
print(f"Average: {total_sum / months:.2f} lv")
