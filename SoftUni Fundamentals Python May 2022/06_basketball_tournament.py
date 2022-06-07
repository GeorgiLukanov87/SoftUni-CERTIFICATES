tournament_name = input()
count_games = int(input())
games_counter = 0
wins_counter = 0
loses_counter = 0
while tournament_name != 'End of tournaments':
    for i in range(1, count_games + 1):
        games_counter += 1
        score1 = int(input())
        score2 = int(input())
        if score1 > score2:
            result = abs(score1 - score2)
            wins_counter += 1
            print(f"Game {i} of tournament {tournament_name}: win with {result} points.")
        else:
            result = abs(score1 - score2)
            loses_counter += 1
            print(f"Game {i} of tournament {tournament_name}: lost with {result} points.")
    tournament_name = input()
    if tournament_name == 'End of tournaments':
        break
    else:
        count_games = int(input())
print(f'{wins_counter/games_counter*100:.2f}% matches win')
print(f'{loses_counter/games_counter*100:.2f}% matches lost')
