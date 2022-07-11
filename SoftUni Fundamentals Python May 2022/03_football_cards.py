input_line = input()
team_A = []
team_B = []
for i in range(1, 11 + 1):
    team_A.append("A-" + str(i))
for i in range(1, 11 + 1):
    team_B.append("B-" + str(i))
data = [input_line]
result = list(map(str, input_line.split()))
condition = False
for i in range(len(result)):
    if result[i] in team_A:
        team_A.remove(result[i])
    if result[i] in team_B:
        team_B.remove(result[i])
    if len(team_A) < 7 or len(team_B) < 7:
        condition = True
        break
print(f"Team A - {len(team_A)}; Team B - {len(team_B)}")
if condition:
    print('Game was terminated')

