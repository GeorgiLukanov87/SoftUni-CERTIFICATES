loot = input().split('|')

command = input()
average_gain = 0
while not command == 'Yohoho!':
    command = command.split()

    if command[0] == 'Loot':
        command.pop(0)
        for item in command:
            if item in loot:
                continue
            else:
                loot.insert(0, item)

    elif command[0] == 'Drop':
        index = command[1]
        index = int(index)
        if index >= 0 and index <= len(loot):
            x = loot.pop(index)
            loot.append(x)
        else:
            command = input()
            continue

    elif command[0] == 'Steal':
        stolen_items = []
        count = command[1]
        count = int(count)
        counter = 0
        bol = False
        for item in range(len(loot) - 1, -1, -1):
            counter += 1
            stolen_items.insert(0, loot[item])
            loot.pop(-1)
            if counter == count:
                print(', '.join(stolen_items))
                bol = True
                break
        if not bol:
            print(', '.join(stolen_items))

    command = input()

if len(loot) <= 0:
    print(f"Failed treasure hunt.")
else:
    for item in loot:
        average_gain += len(item)
    average_gain /= len(loot)
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")
