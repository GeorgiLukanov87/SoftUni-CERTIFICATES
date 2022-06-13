player_name = input()

max_goals = -10000000
best_player = ""
hat_trick = False
while player_name != 'END':
    current_goals = int(input())
    if current_goals > max_goals:
        max_goals = current_goals
        best_player = player_name
        if current_goals >= 3:
            max_goals = current_goals
            best_player = player_name
            hat_trick = True
    if max_goals >= 10:
        break
    player_name = input()
print(f"{best_player} is the best player!")
if hat_trick:
    print(f"He has scored {max_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {max_goals} goals.")