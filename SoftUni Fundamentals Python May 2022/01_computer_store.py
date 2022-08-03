command = input()
price_without_taxes = 0
total_amount_taxes = 0
special = False
while True:
    if command == 'regular':
        break
    if command == 'special':
        special = True
        break

    money = float(command)
    if money < 0:
        print('Invalid price!')
        command = input()
        continue

    price_without_taxes += money
    total_amount_taxes += money * 0.20

    command = input()

if price_without_taxes == 0:
    print('Invalid order!')
    exit()

print(f"Congratulations you've just bought a new computer!")
print(f"Price without taxes: {price_without_taxes:.2f}$")
print(f"Taxes: {total_amount_taxes:.2f}$")
print("-----------")

final_price = price_without_taxes * 1.20

if special:
    final_price *= 0.90
    print(f"Total price: {final_price:.2f}$")
else:
    print(f"Total price: {final_price:.2f}$")
