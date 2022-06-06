tournaments = int(input())
total_money = 0
total_wins = 0
total_loses = 0
for i in range(1, tournaments + 1):
    command = input()
    money = 0
    wins = 0
    loses = 0
    while command != 'Finish':
        sport = command
        result = input()
        if result == 'win':
            wins += 1
            money += 20
        else:
            loses += 1
        command = input()
    if wins > loses:
        money *= 1.10
    total_money += money
    total_wins += wins
    total_loses += loses
if total_wins > total_loses:
    total_money *= 1.20
    print(f"You won the tournament! Total raised money: {total_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_money:.2f}")