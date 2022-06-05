record = float(input())
meters = float(input())
time_seconds_for_meter = float(input())

total_time = meters*time_seconds_for_meter
slowed_in_seconds = (meters//15)*12.5
sum_time = (total_time + slowed_in_seconds)

if sum_time >= record:
    print(f"No, he failed! He was {sum_time-record:.2f} seconds slower.")

else:
    print(f" Yes, he succeeded! The new world record is {sum_time:.2f} seconds.")


