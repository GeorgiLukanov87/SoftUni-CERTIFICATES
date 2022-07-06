numbers = input().split()
command = input()
moves = 0
no_match = True

while not command == 'end':
    command = command.split()
    moves += 1
    index1 = int(command[0])
    index2 = int(command[1])

    if index1 == index2 or index1 < 0 or index2 < 0 or index1 >= (len(numbers)) or index2 >= (len(numbers)):
        print("Invalid input! Adding additional elements to the board")
        middle = len(numbers) // 2
        numbers.insert(middle, f"-{moves}a")
        numbers.insert(middle, f"-{moves}a")
        command = input()
        continue

    for twins in range(len(numbers)):
        no_match = True
        if numbers[index1] == numbers[index2]:
            if index1 < index2:
                x2 = numbers.pop(int(index2))
                x1 = numbers.pop(int(index1))
            else:
                x1 = numbers.pop(int(index1))
                x2 = numbers.pop(int(index2))
            print(f"Congrats! You have found matching elements - {x1}!")
            no_match = False
            break

    if no_match:
        print('Try again!')

    if len(numbers) == 0:
        print(f"You have won in {moves} turns!")
        break

    command = input()

if len(numbers) > 0:
    print("Sorry you lose :(")
    print(f"{' '.join(numbers)}")