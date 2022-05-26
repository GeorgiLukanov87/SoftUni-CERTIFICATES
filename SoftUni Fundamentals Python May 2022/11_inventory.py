collection = input().split(', ')
command = input()

while not command == 'Craft!':
    command = command.split(' - ')

    if command[0] == 'Collect':
        item = command[1]
        if item not in collection:
            collection.append(item)

    elif command[0] == 'Drop':
        item = command[1]
        if item in collection:
            collection.remove(item)

    elif command[0] == 'Combine Items':
        to_combine = command[1].split(':')
        old_item = to_combine[0]
        new_item = to_combine[1]
        for indx in range(len(collection)):
            if old_item == collection[indx]:
                collection.insert(indx + 1, new_item)

    elif command[0] == 'Renew':
        item = command[1]
        for indx in range(len(collection)):
            if item == collection[indx]:
                collection.remove(item)
                collection.insert(len(collection), item)

    command = input()
print(', '.join(collection))
