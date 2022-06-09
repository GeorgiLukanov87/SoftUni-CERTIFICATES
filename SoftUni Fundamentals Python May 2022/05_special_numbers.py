number = int(input())
for current_num in range(1111, 9999 + 1):
    number_is_magic = True
    current_num_as_string = str(current_num)
    for current_digit in current_num_as_string:
        if int(current_digit) == 0 or number % int(current_digit) != 0:
            number_is_magic = False
            break
    if number_is_magic:
        print(current_num, end=" ")
