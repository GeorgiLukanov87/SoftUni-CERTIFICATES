string1 = input()
string2 = input()

current_string = ""
previous_string = string1

for iteration in range(len(string1)):
    for index_str_2 in range(0, iteration + 1):
        current_string += string2[index_str_2]

    for index_str_1 in range(iteration + 1, len(string1)):
        current_string += string1[index_str_1]

    if not previous_string == current_string:
        print(current_string)

    previous_string = current_string
    current_string = ""

