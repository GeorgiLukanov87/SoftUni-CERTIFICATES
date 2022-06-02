a = int(input())
b = int(input())
max_passwords = int(input())
passwords_counter = 0
condition = False
for A in range(35, 55):
    for B in range(64, 96):
        for x in range(1, int(a) + 1):
            for y in range(1, int(b) + 1):
                passwords_counter += 1
                if passwords_counter > max_passwords:
                    condition = True
                    break
                print(f"{chr(A)}{chr(B)}{x}{y}{chr(B)}{chr(A)}", end="|")
                if x == a and y == b:
                    condition = True
                    break
                A += 1
                if A > 55:
                    A = 35
                B += 1
                if B > 96:
                    B = 64
            if condition:
                break
        if condition:
            break
    if condition:
        break
