array = list(map(int, input().split()))

command = input()
while not command == 'end':
    if 'swap' in command:
        command = command.split()
        index1 = int(command[1])
        index2 = int(command[2])
        array[index1], array[index2] = array[index2], array[index1]

    elif 'multiply' in command:
        command = command.split()
        index1 = int(command[1])
        index2 = int(command[2])
        result = array[index1] * array[index2]
        array[index1] = result
    else:
        for i in range(len(array)):
            array[i] -= 1

    command = input()

print(', '.join(list(map(str,array))))
