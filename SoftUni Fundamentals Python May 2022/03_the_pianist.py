n = int(input())
data = {}
for _ in range(n):
    add_piece, add_composer, add_key = input().split("|")
    data[add_piece] = [add_composer] + [add_key]
command = input()
while not command == 'Stop':
    command = command.split("|")
    if command[0] == 'Add':
        piece = command[1]
        composer = command[2]
        key = command[3]
        if piece in data:
            print(f"{piece} is already in the collection!")
        else:
            data[piece] = [composer] + [key]
            print(f"{piece} by {composer} in {key} added to the collection!")

    elif command[0] == 'Remove':
        piece = command[1]
        if piece not in data:
            print(f"Invalid operation! {piece} does not exist in the collection.")
        else:
            print(f"Successfully removed {piece}!")
            del data[piece]

    elif command[0] == 'ChangeKey':
        piece = command[1]
        new_key = command[2]
        if piece not in data:
            print(f"Invalid operation! {piece} does not exist in the collection.")
        else:
            data[piece][1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")

    command = input()
for piece, value in data.items():
    print(f"{piece} -> Composer: {value[0]}, Key: {value[1]}")
