money = float(input())

money = (money * 100)
money = int(money)

coin_counter = 0
while True:
    if money >= 200:
        money -= 200
        coin_counter += 1

    elif money >= 100:
        money -= 100
        coin_counter += 1

    elif money >= 50:
        money -= 50
        coin_counter += 1

    elif money >= 20:
        money -= 20
        coin_counter += 1

    elif money >= 10:
        money -= 10
        coin_counter += 1

    elif money >= 5:
        money -= 5
        coin_counter += 1

    elif money >= 2:
        money -= 2
        coin_counter += 1

    elif money >= 1:
        money -= 1
        coin_counter += 1
    if money <= 0:
        print(coin_counter)
        break
