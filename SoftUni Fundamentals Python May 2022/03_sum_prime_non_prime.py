command = input()

prime_sum = 0
non_prime_sum = 0

while command != 'stop':
    current_number = int(command)
    if current_number < 0:
        print("Number is negative.")
    else:
        number_is_prime = True
        for num in range(2, current_number):
            if current_number % num == 0:
                number_is_prime = False
                break
        if number_is_prime:
            prime_sum += current_number
        else:
            non_prime_sum += current_number

    command = input()

print(f"Sum of all prime numbers is: {prime_sum}")
print(f"Sum of all non prime numbers is: {non_prime_sum}")
########################################################
current_number = int(input())
bol = True
for divisor in range(2, current_number):
    if current_number % divisor == 0:
        bol = False
        break
if bol:
    print("Prime")
else:
    print("NOT Prime")