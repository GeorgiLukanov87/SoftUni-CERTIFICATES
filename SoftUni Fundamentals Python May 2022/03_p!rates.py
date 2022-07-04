command = input()
data = {}

while not command == 'End':
    if "||" in command:
        command = command.split("||")
        city = command[0]
        population = int(command[1])
        gold = int(command[2])
        if city not in data:
            data[city] = [population] + [gold]
        else:
            data[city][0] += population
            data[city][1] += gold
    else:
        command = command.split("=>")
        if command[0] == 'Plunder':
            town = command[1]
            people = int(command[2])
            gold_stolen = int(command[3])
            if town in data:
                data[town][0] -= people
                data[town][1] -= gold_stolen
                print(f"{town} plundered! {gold_stolen} gold stolen, {people} citizens killed.")
                if data[town][0] == 0 or data[town][1] == 0:
                    del data[town]
                    print(f"{town} has been wiped off the map!")

        elif command[0] == 'Prosper':
            town = command[1]
            gold_added = int(command[2])
            if gold_added < 0:
                print(f"Gold added cannot be a negative number!")
            else:
                data[town][1] += gold_added
                print(f"{gold_added} gold added to the city treasury. {town} now has {data[town][1]} gold.")

    command = input()

if len(data) <= 0:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    print(f"Ahoy, Captain! There are {len(data)} wealthy settlements to go to:")
    for key, value in data.items():
        print(f"{key} -> Population: {value[0]} citizens, Gold: {value[1]} kg")
