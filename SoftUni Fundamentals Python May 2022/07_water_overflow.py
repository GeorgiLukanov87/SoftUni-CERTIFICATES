n = int(input())
cap = 255
total_liters = cap
sum_liters = 0
for i in range(1, n + 1):
    current_liters = int(input())
    if current_liters > total_liters:
        last_cap = sum_liters
        print(f"Insufficient capacity!")
        continue
    sum_liters += current_liters
    total_liters -= current_liters
print(sum_liters)
