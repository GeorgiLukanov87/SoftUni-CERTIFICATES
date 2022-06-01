clock = int(input())
day = input()

status = 0

if clock >= 10 and clock <=18 and day != 'Sunday':
    status ='open'
    print(status)
else:
    print('closed')

