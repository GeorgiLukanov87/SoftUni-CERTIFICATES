capacity_of_cine = int(input())
current_people = input()
income = 0
seat_occupied = 0
while True:
    if current_people == 'Movie time!':
        print(f"There are {capacity_of_cine - seat_occupied} seats left in the cinema.")
        break
    current_people = int(current_people)
    seat_occupied += current_people
    if seat_occupied > capacity_of_cine:
        print("The cinema is full.")
        break
    if current_people % 3 == 0:
        income += 5 * current_people - 5
    else:
        income += 5 * current_people
    current_people = input()
print(f"Cinema income - {income} lv.")
