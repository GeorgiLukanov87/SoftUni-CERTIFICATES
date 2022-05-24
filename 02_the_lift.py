people = int(input())
wagons = list(map(int, input().split()))
for lift in range(len(wagons)):

    if wagons[lift] <= 4:
        while wagons[lift] != 4 and people > 0:
            wagons[lift] += 1
            people -= 1

available_space = False
count_wagon = len(wagons)
for wagon in wagons:
    if wagon == 4:
        count_wagon -= 1
    if count_wagon == 0:
        available_space = True

if people == 0 and available_space:
    print(f'{" ".join([str(wagon) for wagon in wagons])}')
else:
    if people > 0:
        print(f"There isn't enough space! {people} people in a queue!")
        print(f"{' '.join([str(wagon) for wagon in wagons])}")
    else:
        print(f'The lift has empty spots!')
        print(f'{" ".join([str(wagon) for wagon in wagons])}')