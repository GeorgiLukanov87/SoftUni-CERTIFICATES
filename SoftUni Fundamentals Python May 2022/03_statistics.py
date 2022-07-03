data = input()
products = {}
while not data == 'statistics':
    data = data.split(': ')
    key = data[0]
    value = int(data[1])
    if key not in products:
        products[key] = value
    else:
        products[key] += value

    data = input()

print("Products in stock:")

for key, value in products.items():
    print(f"- {key}: {value}")

print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")
