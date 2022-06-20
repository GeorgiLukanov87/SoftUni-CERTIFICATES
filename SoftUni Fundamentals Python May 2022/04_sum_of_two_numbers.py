start_interval = int(input())
end_interval = int(input())
magic_number = int(input())

combinations = 0
condition = False

for num1 in range(start_interval, end_interval + 1):
    for num2 in range(start_interval, end_interval + 1):
        combinations += 1
        if num1 + num2 == magic_number:
            print(f"Combination N:{combinations} ({num1} + {num2} = {magic_number})")
            condition = True
            break

    if condition:
        break

if not condition:
    print(f"{combinations} combinations - neither equals {magic_number}")

