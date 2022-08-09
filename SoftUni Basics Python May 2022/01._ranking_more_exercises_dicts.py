def calculate_max_points_func():
    max_points = {}
    for name, points in my_dict.items():
        for key, value in points.items():
            if name not in max_points:
                max_points[name] = value
            else:
                max_points[name] += value

    for name, score in sorted(max_points.items(), key=lambda kvp: -kvp[1]):
        print(f"Best candidate is {name} with total {score} points.")
        break


def print_students_func():
    print("Ranking:")
    for name, score in sorted(my_dict.items(), key=lambda kvp: kvp[0]):
        print(name)
        for contest, points in sorted(score.items(), key=lambda kvp: -kvp[1]):
            print(f"#  {contest} -> {points}")


def adding_details_func(some_contest: str, some_name: str, some_student: int):
    if some_contest in initial_dict:
        if current_password in initial_dict[some_contest]:
            if some_name not in my_dict:
                my_dict[some_name] = {}
                my_dict[some_name] = {some_contest: some_student}
            else:
                if some_contest in my_dict[some_name].keys():
                    old_points = my_dict[some_name][some_contest]
                    if old_points < some_student:
                        my_dict[some_name].update({some_contest: some_student})
                else:
                    my_dict[some_name].update({some_contest: some_student})


data = input()
initial_dict = {}

while not data == 'end of contests':
    data = data.split(":")
    current_contest = data[0]
    valid_password = data[1]
    if current_contest not in initial_dict:
        initial_dict[current_contest] = {}
    initial_dict[current_contest] = valid_password
    data = input()

data = input()
my_dict = {}

while not data == 'end of submissions':
    details = data.split("=>")
    contest = details[0]
    current_password = details[1]
    student_name = details[2]
    student_points = int(details[3])
    adding_details_func(contest, student_name, student_points)
    data = input()

calculate_max_points_func()
print_students_func()
