count_order = int(input())
type_order = input()
delivery = input()
if count_order <=10:
    print('Invalid order')
    exit()
if type_order == '90X130':
    total_price = 110 * count_order
    if count_order > 30 and count_order <60:
        total_price *= 0.95
    elif count_order > 60:
        total_price *= 0.92
elif type_order == '100X150':
    total_price = 140 * count_order
    if count_order > 40 and count_order < 80:
        total_price *=0.94
    elif count_order > 80:
        total_price *=0.90
elif type_order == '130X180':
    total_price = 190 * count_order
    if count_order > 20 and count_order < 50:
        total_price *= 0.93
    elif count_order > 50:
        total_price *= 0.88
elif type_order == '200X300':
    total_price = 250 * count_order
    if count_order > 25 and count_order < 50:
        total_price *= 0.91
    elif count_order > 50:
        total_price *= 0.86
if delivery == 'With delivery':
    total_price += 60
if count_order >99:
    total_price *= 0.96
print(f'{total_price:.2f} BGN')
