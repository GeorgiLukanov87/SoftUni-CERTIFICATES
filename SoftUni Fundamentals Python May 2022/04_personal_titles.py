age = float(input())
gender = input()

if gender == 'm' and age >=16:
    print("Mr.")
elif gender == 'm' and age <16:
    print('Master')
elif gender == 'f' and age >=16:
    print('Ms.')
else:
    print('Miss')