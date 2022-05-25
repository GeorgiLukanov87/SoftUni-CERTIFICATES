all_students = int(input())
grade1 = 0
grade2 = 0
grade3 = 0
grade4 = 0
total_grade = 0
for student in range(1,all_students+1):
    current_grade = float(input())
    total_grade += current_grade
    if current_grade >= 5:
        grade1 += 1
    elif current_grade >= 4 and current_grade <= 4.99:
        grade2 += 1
    elif current_grade >= 3 and current_grade <= 3.99:
        grade3 += 1
    else:
        grade4 += 1
print(f"Top students: {grade1/all_students*100:.2f}%")
print(f"Between 4.00 and 4.99: {grade2/all_students*100:.2f}%")
print(f"Between 3.00 and 3.99: {grade3/all_students*100:.2f}%")
print(f"Fail: {grade4/all_students*100:.2f}%")
print(f"Average: {total_grade/all_students:.2f}")
