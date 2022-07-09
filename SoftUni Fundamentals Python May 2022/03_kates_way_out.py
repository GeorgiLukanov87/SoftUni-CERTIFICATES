rows = int(input())
total_moves = 0
new_list = []
for i in range(rows):
    new_list1 = input()
    new_list2 = input()
    new_list3 = input()
    new_list4 = input()

counter = 0
for el in new_list1:
    if el == '#':
        counter += 1

    if len(new_list1) == 5:
        blocked = True
    else:
        blocked = False

    if len(new_list2) == len(new_list4):
        pass
