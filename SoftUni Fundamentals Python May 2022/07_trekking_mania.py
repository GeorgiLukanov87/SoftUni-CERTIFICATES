count_group = int(input())
mountain1 = 0
mountain2 = 0
mountain3 = 0
mountain4 = 0
mountain5 = 0
members = 0
for people in range(count_group):
    group_members = int(input())
    members += group_members
    if group_members <= 5 and group_members and group_members > 0:
        mountain1 += group_members
    if group_members > 5 and group_members <= 12:
        mountain2 += group_members
    if group_members > 12 and group_members <= 25:
        mountain3 += group_members
    if group_members > 25 and group_members <= 40:
        mountain4 += group_members
    if group_members >= 41:
        mountain5 += group_members
result1 = (mountain1/members)*100
result2 = (mountain2/members)*100
result3 = (mountain3/members)*100
result4 = (mountain4/members)*100
result5 = (mountain5/members)*100
print(f'{result1:.2f}%')
print(f'{result2:.2f}%')
print(f'{result3:.2f}%')
print(f'{result4:.2f}%')
print(f'{result5:.2f}%')
