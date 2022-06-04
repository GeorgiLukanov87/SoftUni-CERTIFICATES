cap = int(input())
count_fans = int(input())
sectorA = 0
sectorB = 0
sectorV = 0
sectorG = 0
fans = 0

for number in range(1, count_fans+1):
    sector = input()
    fans += len(sector)
    if sector == 'A':
        sectorA += 1
    elif sector == "B":
        sectorB += 1
    elif sector == "V":
        sectorV += 1
    elif sector == "G":
        sectorG += 1

print(f'{(sectorA/fans*100):.2f}%')
print(f'{(sectorB/fans*100):.2f}%')
print(f'{(sectorV/fans*100):.2f}%')
print(f'{(sectorG/fans*100):.2f}%')
print(f'{(fans/cap*100):.2f}%')



