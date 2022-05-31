name_student = input()
counter_years = 0
counter_fails = 0
total_years = 0
sum_grades = 0
current_grade = 0

while counter_fails != 2:
    current_grade = float(input())
    if current_grade >= 4:
        sum_grades += current_grade
        counter_years += 1
    elif current_grade < 4:
        counter_fails += 1
    total_years = counter_years + counter_fails
    if total_years == 12 and counter_fails != 2:
        print(f"{name_student} graduated. Average grade: {(sum_grades / counter_years):.2f}")
        break
    elif counter_fails == 2:
        print(f"{name_student} has been excluded at {total_years-1} grade")
