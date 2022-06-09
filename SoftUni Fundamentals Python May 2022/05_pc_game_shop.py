games_sold = int(input())
g1 = 0
g2 = 0
g3 = 0
g4 = 0
for game in range(1, games_sold+1):
    game_name = input()

    if game_name == 'Hearthstone':
        g1 += 1
    elif game_name == 'Fornite':
        g2 += 1
    elif game_name == 'Overwatch':
        g3 += 1
    else:
        g4 += 1
print(f"Hearthstone - {g1/games_sold*100:.2f}%")
print(f"Fornite - {g2/games_sold*100:.2f}%")
print(f"Overwatch - {g3/games_sold*100:.2f}%")
print(f"Others - {g4/games_sold*100:.2f}%")

