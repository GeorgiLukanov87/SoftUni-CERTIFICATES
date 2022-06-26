destination = input()
type_packet = input()
vip = input()
count_days = int(input())
total_sum = 0
if count_days < 1:
    print("Days must be positive number!")
    exit()
if destination != "Bansko" and destination != "Borovets" and destination != "Varna" and destination != "Burgas":
    print('Invalid input!')
    exit()
elif type_packet != "noEquipment" and type_packet != "withEquipment" and type_packet != "noBreakfast" \
        and type_packet != "withBreakfast":
    print('Invalid input!')
    exit()
if destination == "Bansko" or destination == 'Borovets':
    price = 80
    if vip == 'yes':
        price *= 0.95
    if type_packet == 'withEquipment':
        price = 100
        if vip == 'yes':
            price *= 0.90
elif destination == 'Varna' or destination == 'Burgas':
    price = 100
    if vip == 'yes':
        price *= 0.93
    if type_packet == 'withBreakfast':
        price = 130
        if vip == 'yes':
            price *= 0.88
if count_days > 7:
    total_sum = price * (count_days-1)
else:
    total_sum = price * count_days
print(f"The price is {total_sum:.2f}lv! Have a nice time!")
