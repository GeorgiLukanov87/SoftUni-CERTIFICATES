a = int(input())
b = int(input())
cake_size = a * b
taken = 0
while True:
    take_piece = input()
    if take_piece == "STOP":
        print(f"{cake_size-taken} pieces are left.")
        break

    take_piece = int(take_piece)
    taken += take_piece

    if taken >= cake_size:
        print(f"No more cake left! You need {taken-cake_size} pieces more.")
        break
