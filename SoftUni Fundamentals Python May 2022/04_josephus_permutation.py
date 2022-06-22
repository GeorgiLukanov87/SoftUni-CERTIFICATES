soldiers = list(map(int, input().split()))
k = int(input())

position = k - 1
index = 0
len_list = (len(soldiers))
executed = []

while len_list > 0:
    index = (position + index) % len_list
    current_killed = (soldiers.pop(index))
    len_list -= 1
    executed.append(current_killed)

print(str(executed).replace(" ", ""))
