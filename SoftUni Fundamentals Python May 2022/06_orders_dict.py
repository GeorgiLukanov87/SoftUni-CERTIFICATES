data = input()
products = {}
while not data == 'buy':
    data = data.split()
    key = data[0]
    amount = data[1]
    value = data[2]

    if key not in products:
        products[key] = []
    else:
        if products[key][0] != amount:
            products[key][0] = amount
        products[key][1] = float(value) + float(products[key][1])
    if amount not in products[key]:
        products[key].append(amount)
    if value not in products[key]:
        products[key].append(value)

    data = input()

for el in products:
    print(f'{el} -> {float(products[el][0]) * float(products[el][1]):.2f}')
