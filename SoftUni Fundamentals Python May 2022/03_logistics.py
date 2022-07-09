all_cargos = int(input())
counter_cargo = 0
bus = 0
truck = 0
train = 0
count_bus = 0
count_truck = 0
count_train = 0

for number in range(1, all_cargos + 1):
    new_cargo = int(input())

    if 3 >= new_cargo > 0:
        counter_cargo += new_cargo
        bus += new_cargo*200
        count_bus += new_cargo

    elif 3 < new_cargo <= 11:
        counter_cargo += new_cargo
        truck += new_cargo*175
        count_truck += new_cargo
    elif new_cargo >= 12:
        counter_cargo += new_cargo
        train += new_cargo*120
        count_train += new_cargo
result = bus + truck + train

#print(result)
#print(counter_cargo)


#print(count_bus)
#print(count_truck)
#print(count_train)

print(f"{result/counter_cargo:.2f}")
print(f"{(count_bus/counter_cargo*100):.2f}%")
print(f"{(count_truck/counter_cargo*100):.2f}%")
print(f"{(count_train/counter_cargo*100):.2f}%")
