end_sector = input()
row_first_sector = int(input())
seats_odd_row = int(input())

counter = 0
start_sector = 65
start_seat = 97

for sector in range(start_sector, ord(end_sector) + 1):
    for row in range(1, row_first_sector + 1):
        if row % 2 != 0:
            for seats in range(start_seat, (start_seat + seats_odd_row)):
                print(f'{chr(sector)}{row}{chr(seats)}')
                counter += 1
        elif row % 2 == 0:
            for seats in range(start_seat, (start_seat + seats_odd_row + 2)):
                print(f'{chr(sector)}{row}{chr(seats)}')
                counter += 1
    if row_first_sector + 1 > row_first_sector:
        row_first_sector += 1

print(counter)
