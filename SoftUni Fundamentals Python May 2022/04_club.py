income_needed = float(input())
command = input()
left_income = income_needed
current_sum = 0
total_income = 0
condition = False
while command != 'Party!':
    cocktail_name = command
    count_cocktails = int(input())
    current_sum += len(cocktail_name) * count_cocktails
    if current_sum % 2 != 0:
        current_sum *= 0.75
    left_income -= current_sum
    total_income += current_sum
    if total_income >= income_needed:
        print("Target acquired.")
        condition = True
        break
    command = input()
    current_sum = 0
if not condition:
    print(f"We need {left_income:.2f} leva more.")
print(f"Club income - {total_income:.2f} leva.")
