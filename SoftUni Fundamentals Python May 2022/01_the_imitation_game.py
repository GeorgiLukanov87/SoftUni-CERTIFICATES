message = input()
command = input()

while not command == "Decode":
    command = command.split("|")
    if command[0] == "ChangeAll":
        substring = command[1]
        replace = command[2]
        message = message.replace(substring, replace)

    elif command[0] == "Insert":
        index = int(command[1])
        value = command[2]
        message = message[:index] + value + message[index:]

    elif command[0] == 'Move':
        num = int(command[1])
        message = message[num:] + message[:num]

    command = input()

print(f"The decrypted message is: {message}")

