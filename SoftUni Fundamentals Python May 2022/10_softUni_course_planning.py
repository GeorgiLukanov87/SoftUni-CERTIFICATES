course = input().split(', ')
command = input()
while not command == 'course start':
    command = command.split(':')
    lesson = command[1]
    exercise = f"{lesson}-Exercise"

    if command[0] == 'Add':
        if lesson not in course:
            course.append(lesson)

    elif command[0] == 'Insert':
        index = int(command[2])
        if lesson not in course:
            course.insert(index, lesson)

    elif command[0] == 'Remove':
        if lesson in course:
            course.remove(lesson)
        if exercise in course:
            course.remove(exercise)

    elif command[0] == 'Swap':
        lesson1 = command[1]
        lesson2 = command[2]
        if lesson1 in course and lesson2 in course:
            modified_course = []
            for lesson in course:
                if lesson == lesson1:
                    modified_course.append(lesson2)
                elif lesson == lesson2:
                    modified_course.append(lesson1)
                else:
                    modified_course.append(lesson)
            course.clear()
            course = modified_course

        if 'Exercise' in lesson:
            for index in range(len(course)):
                if course[index] == lesson2:
                    course.remove(lesson)
                    course.insert(index+1, lesson)
                    break

    elif command[0] == 'Exercise':
        if lesson not in course:
            course.append(lesson)
            course.append(exercise)
        elif lesson in course and exercise not in course:
            for index in range(len(course)):
                if course[index] == lesson:
                    course.insert(index + 1, exercise)
                    break

    command = input()

for el in range(len(course)):
    print(f"{el+1}.{course[el]}")
