all_students = int(input())
fail_students_grade = 0
three_to_four_grade = 0
four_to_five_grade = 0
top_students = 0
counter_students = 0
counter_grade = 0

for student in range(1, all_students + 1):
    grade = float(input())

    if grade >= 2 and grade <= 2.99:
        fail_students_grade += 1
        counter_students += 1
        counter_grade += grade

    elif grade >=3 and grade <= 3.99:
        three_to_four_grade += 1
        counter_students += 1
        counter_grade += grade

    elif grade >=4 and grade <=4.99:
        four_to_five_grade += 1
        counter_students += 1
        counter_grade += grade

    elif grade >= 5:
        top_students += 1
        counter_students += 1
        counter_grade += grade

#print(counter_students)
#print(counter_grade)
#print(top_students)
#print(four_to_five_grade)
#print(three_to_four_grade)
#print(fail_students_grade)

print(f"Top students: {top_students/counter_students*100:.2f}%")
print(f"Between 4.00 and 4.99: {four_to_five_grade/counter_students*100:.2f}%")
print(f"Between 3.00 and 3.99: {three_to_four_grade/counter_students*100:.2f}%")
print(f"Fail: {fail_students_grade/counter_students*100:.2f}%")
print(f"Average: {counter_grade/counter_students:.2f}")