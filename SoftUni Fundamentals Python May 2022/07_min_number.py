import sys
stop_number = input()
new_stop_number = 0
min_number = sys.maxsize

while stop_number != "Stop":
    new_stop_number = int(stop_number)
    if new_stop_number < min_number:
        min_number = new_stop_number
    stop_number = input()
print(min_number)