population = list(map(int, input().split(", ")))
min_wealth = int(input())
biggest = -111111111

if sum(population) < len(population) * min_wealth:
    print('No equal distribution possible')
    exit()

for element in range(len(population)):
    index = population.index(max(population))
    current_element = population[element]
    if current_element < min_wealth:
        dif = min_wealth - population[element]
        population[index] -= dif
        population[element] += dif

print(population)
