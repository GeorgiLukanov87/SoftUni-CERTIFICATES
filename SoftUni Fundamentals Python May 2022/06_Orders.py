all_orders = int(input())
total_price = 0
price = 0
invalid = False
for i in range(1, all_orders + 1):
    price_per_capsule = float(input())
    days = int(input())
    capsules_count = int(input())
    invalid = False

    if not 0.01 <= price_per_capsule <= 100:
        invalid = True
    if not 1 <= days <= 31:
        invalid = True
    if not 1 <= capsules_count <= 2000:
        invalid = True
    if invalid:
        continue

    price = days * capsules_count * price_per_capsule
    total_price += price
    if price <= 0:
        continue
    else:
        print(f"The price for the coffee is: ${price:.2f}")
print(f"Total: ${total_price:.2f}")
