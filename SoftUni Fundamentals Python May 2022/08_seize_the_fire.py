fire_data = input().split('#')
total_water = int(input())
fire_cells = []

for every_fire in fire_data:
    fire_range, fire_value = every_fire.split(' = ')
    fire_value = int(fire_value)
    if fire_range == 'High' and 81 < fire_value <= 125:
        total_water -= fire_value
    elif fire_range == 'Medium' and 51 < fire_value <= 80:
        total_water -= fire_value
    elif fire_range == 'Low' and 1 < fire_value <= 50:
        total_water -= fire_value

    fire_cells.append(fire_value)

print("Cells:")
for cell in fire_cells:
    print(f" - {cell}")
effort = sum(fire_cells) * 0.25
print(f'Effort: {effort:.2f}')
total_fire = sum(fire_cells)
print(f"Total Fire: {total_fire}")
