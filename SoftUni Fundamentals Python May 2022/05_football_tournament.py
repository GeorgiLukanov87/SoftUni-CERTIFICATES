team_name = input()
games_played = int(input())
win = 0
draw = 0
lose = 0
total_result = 0

for game in range(1, games_played+1):
    result = input()
    if result == 'W':
        win += 1
        total_result += 3
    elif result == 'D':
        draw += 1
        total_result += 1
    else:
        lose += 1
        total_result += 0

if games_played <= 0:
    print(f"{team_name} hasn't played any games during this season.")
else:
    print(f"{team_name} has won {total_result} points during this season.")
    print(f'Total stats:')
    print(f"## W: {win}")
    print(f"## D: {draw}")
    print(f"## L: {lose}")
    print(f"Win rate: {win/games_played*100:.2f}%")
