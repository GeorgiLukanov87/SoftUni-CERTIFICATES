local_time = list(map(int, input().split(':')))
steps = int(input())
seconds_for_step = int(input())
in_seconds = seconds_for_step * steps

start_time_s = local_time[2] + (local_time[1]*60) + (local_time[0] * 3600)
time = in_seconds + start_time_s
hour = time // 3600
time %= 3600
minutes = time // 60
time %= 60
seconds = time

while hour > 23:
    hour %= 24

all_time = [hour] + [minutes] + [seconds]
arrive_time = []

print('Time Arrival: ', end="")
for el in all_time:
    if len(str(el)) == 1:
        el = "0" + str(el)
        arrive_time.append(el)
    else:
        arrive_time.append(el)

print(*arrive_time, sep=":")
