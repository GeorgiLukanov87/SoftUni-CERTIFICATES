clients = int(input())
counter_trained = 0
counter_bought = 0
c1 = 0
c2 = 0
c3 = 0
c4 = 0
c5 = 0
c6 = 0
for i in range(clients):
    command = input()
    if command == 'Back':
        c1 += 1
        counter_trained += 1
    elif command == 'Chest':
        c2 += 1
        counter_trained += 1
    elif command == 'Legs':
        c3 += 1
        counter_trained += 1
    elif command == 'Abs':
        c4 += 1
        counter_trained += 1
    elif command == 'Protein shake':
        c5 += 1
        counter_bought += 1
    elif command == 'Protein bar':
        c6 += 1
        counter_bought += 1
print(f"{c1} - back")
print(f"{c2} - chest")
print(f"{c3} - legs")
print(f"{c4} - abs")
print(f"{c5} - protein shake")
print(f"{c6} - protein bar")
print(f"{counter_trained / clients * 100:.2f}% - work out")
print(f"{counter_bought / clients * 100:.2f}% - protein")
