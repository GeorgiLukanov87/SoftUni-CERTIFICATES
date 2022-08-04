all_students = int(input())
lectures = int(input())
additional_bonus = int(input())
total_bonus = 0
max_bonus = 0
current_lectures = 0
for student in range(1, all_students + 1):
    attendance = int(input())
    total_bonus = round(attendance / lectures * (5 + additional_bonus))
    if total_bonus > max_bonus:
        max_bonus = total_bonus
        current_lectures = attendance
print(f"Max Bonus: {max_bonus}.")
print(f"The student has attended {current_lectures} lectures.")
