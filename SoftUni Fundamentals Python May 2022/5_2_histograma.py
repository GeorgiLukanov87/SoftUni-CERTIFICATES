numbers = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for number in range(0, numbers):
    current_number = int(input())

    if current_number < 200:
        p1 = p1+1
    elif current_number >=200 and current_number <400:
        p2 = p2+1
    elif current_number >=400 and current_number <600:
        p3 = p3+1
    elif current_number >=600 and current_number <800:
        p4 = p4+1
    else:
        p5 = p5+1

print('{0:.2f}'.format (p1/numbers*100)+"%")
print('{0:.2f}'.format (p2/numbers*100)+"%")
print('{0:.2f}'.format (p3/numbers*100)+"%")
print('{0:.2f}'.format (p4/numbers*100)+"%")
print('{0:.2f}'.format (p5/numbers*100)+"%")
