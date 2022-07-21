password = input()
command = input()
while not command == 'Done':
    raw_password = ""
    command = command.split()
    if command[0] == 'TakeOdd':
        for odd_indx in range(len(password)):
            if odd_indx % 2 != 0:
                raw_password += password[odd_indx]
        password = raw_password

    elif command[0] == 'Cut':
        index = int(command[1])
        length = int(command[2])
        password = password[:index] + password[index+length:]

    elif command[0] == 'Substitute':
        substring = command[1]
        substitute = command[2]
        if substring in password:
            password = password.replace(substring, substitute)
        else:
            print("Nothing to replace!")
            command = input()
            continue

    print(password)
    command = input()

print(f"Your password is: {password}")
