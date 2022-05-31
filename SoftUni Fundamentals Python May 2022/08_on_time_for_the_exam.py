exam_hours = int(input())
exam_minutes = int(input())
arrival_hours = int(input())
arrival_minutes = int(input())

exam_time = (exam_hours*60) + exam_minutes
arrival_time = (arrival_hours*60) + arrival_minutes

late_time = arrival_time -exam_time
early_time =  exam_time - arrival_time


hour = None
minutes = None
if early_time > 30 and early_time < 60:
    print("Early")
    print(f"{early_time} minutes before the start")

elif late_time <= 59 and late_time > 0:
    print("Late")
    print(f"{late_time} minutes after the start")
elif early_time >= 60:
    hour = early_time //60
    minutes = early_time % 60
    print("Early")
    print(f"{hour}:{minutes:02d} hours before the start")

elif late_time >= 60 and late_time > 0:
    hour = late_time//60
    minutes = late_time % 60
    print("Late")
    print(f"{hour}:{minutes:02d} hours after the start")
elif late_time == 0:
    print("On time")
elif early_time <= 30 and early_time >0:
    print("On time")
    print(f"{early_time} minutes before the start")






