number_teachers = int(input())
presentation_name = input()

grade_sum = 0
grade_counter = 0
total_grade_sum = 0

while True:
    if presentation_name == 'Finish':
        print(f"Student's final assessment is {total_grade_sum/grade_counter:.2f}.")
        break
    grade_sum = 0

    for num in range(1, number_teachers + 1):
        grade_counter += 1
        current_grade = float(input())
        total_grade_sum += current_grade
        grade_sum += current_grade

        if num == number_teachers:
            print(f"{presentation_name} - {grade_sum/num:.2f}.")

    presentation_name = input()
