pirate = list(map(int, input().split('>')))
warship = list(map(int, input().split('>')))
max_health_cap = int(input())
command = input()
finished_battle = False
while not command == 'Retire':
    command = command.split()

    if command[0] == 'Fire':
        index = int(command[1])
        damage = int(command[2])
        if 0 <= index <= len(warship):
            warship[index] -= damage
            if warship[index] <= 0:
                print('You won! The enemy ship has sunken.')
                finished_battle = True
                break
        else:
            command = input()
            continue

    elif command[0] == 'Defend':
        start_index = int(command[1])
        end_index = int(command[2])
        damage = int(command[3])
        if start_index >= 0 and start_index <= end_index and end_index < len(pirate):
            for shot in range(start_index, end_index + 1):
                pirate[shot] -= damage
                if pirate[shot] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    finished_battle = True
                    break
        else:
            command = input()
            continue

    elif command[0] == 'Repair':
        index = int(command[1])
        health = int(command[2])
        if 0 <= index < len(pirate):
            pirate[index] += health
            if pirate[index] > max_health_cap:
                pirate[index] = max_health_cap
        else:
            command = input()
            continue

    elif command[0] == 'Status':
        sections_counter = 0
        for section in pirate:
            if section < max_health_cap * 0.20:
                sections_counter += 1
        print(f'{sections_counter} sections need repair.')

    command = input()

if not finished_battle:
    print(f"Pirate ship status: {sum(pirate)}")
    print(f"Warship status: {sum(warship)}")
