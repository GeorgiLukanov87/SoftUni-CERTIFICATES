command = input()
BASE_LAGER = 5364
counter_days = 1
condition = False
day_meters = 0
while command != 'END':
    pause = command
    meters = int(input())
    if pause == 'Yes':
        counter_days += 1
        BASE_LAGER += meters
    else:
        BASE_LAGER += meters
    if BASE_LAGER >= 8848:
        print(f'Goal reached {counter_days} days!')
        condition = True
        break
    if counter_days == 5:
        break
    command = input()
if not condition:
    print("Failed!")
    print(f"{BASE_LAGER}")
    print(counter_days)
