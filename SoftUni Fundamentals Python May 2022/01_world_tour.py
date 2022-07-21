data = input()
command = input()

while not command == 'Travel':
    command = command.split(":")
    if command[0] == 'Add Stop':
        index = int(command[1])
        string = command[2]
        if 0 <= index < len(data):
            data = data[:index] + string + data[index:]

    elif command[0] == 'Remove Stop':
        start_index = int(command[1])
        end_index = int(command[2])
        if (0 <= start_index < len(data)) and (0 <= end_index < len(data)):
            data = data[:start_index]+data[end_index+1:]

    elif command[0] == 'Switch':
        old_str = command[1]
        new_str = command[2]
        if old_str in data:
            data = data.replace(old_str, new_str)

    print(data)
    command = input()

print(f"Ready for world tour! Planned stops: {data}")
