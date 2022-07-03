n = int(input())
number = 0
new_number = 0

while not number == n:
    new_number = int(input())
    number += new_number
    if number >= n:
        break
print(number)
