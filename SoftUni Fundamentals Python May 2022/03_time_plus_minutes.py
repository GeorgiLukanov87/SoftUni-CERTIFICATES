hour = int(input())
minutes = int(input())
mins = minutes + 15

if mins >= 60:
    hour += 1
    mins -= 60

if hour >= 24:
    hour -= hour
    mins %= 60

if mins < 10:
    print(f"{hour}:0{mins}")
else:
    print(f"{hour}:{mins}")
