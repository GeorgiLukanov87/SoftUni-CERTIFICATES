n_cars = int(input())
data = {}
command = input()
for _ in range(n_cars):
    car, mileage, fuel = command.split("|")
    data[car] = [int(mileage)] + [int(fuel)]
    command = input()
while not command == 'Stop':
    command = command.split(' : ')
    if command[0] == 'Drive':
        car = command[1]
        distance = int(command[2])
        fuel = int(command[3])
        if data[car][1] >= fuel:
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            data[car][0] += distance
            data[car][1] -= fuel
        else:
            print(f"Not enough fuel to make that ride")
        if data[car][0] >= 100000:
            print(f"Time to sell the {car}!")
            del data[car]
    elif command[0] == 'Refuel':
        car = command[1]
        fuel = int(command[2])
        temp_tank = data[car][1]
        if temp_tank + fuel >= 75:
            print(f"{car} refueled with {75-temp_tank} liters")
            data[car][1] = 75
        else:
            print(f"{car} refueled with {fuel} liters")
            data[car][1] += fuel
    elif command[0] == 'Revert':
        car = command[1]
        kilometers = int(command[2])
        print(f"{car} mileage decreased by {kilometers} kilometers")
        data[car][0] -= kilometers
        if data[car][0] < 10000:
            data[car][0] = 10000
    command = input()
for car in data:
    print(f"{car} -> Mileage: {data[car][0]} kms, Fuel in the tank: {data[car][1]} lt.")
