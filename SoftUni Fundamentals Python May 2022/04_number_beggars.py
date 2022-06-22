coins = input()
beggars = int(input())

coins = [int(num) for num in coins.split(', ')]

beggars_list = [0] * beggars
counter_beggars = 0
for coin in coins:
    beggars_list[counter_beggars] += coin
    counter_beggars += 1
    if counter_beggars >= beggars:
        counter_beggars = 0

print(beggars_list)