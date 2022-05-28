pokemons = [int(x) for x in input().split()]
removed_elements = []
while not len(pokemons) == 0:
    index = int(input())
    removed = 0
    weird = False

    if index < 0:
        removed = pokemons.pop(0)
        new_copy = pokemons[-1]
        pokemons.insert(0, new_copy)
        removed_elements.append(removed)
        weird = True
    if index >= len(pokemons):
        removed = pokemons.pop(-1)
        new_copy = pokemons[0]
        pokemons.append(new_copy)
        removed_elements.append(removed)
        weird = True

    if weird:
        for i in range(len(pokemons)):
            if pokemons[i] <= removed:
                pokemons[i] += removed
            else:
                pokemons[i] -= removed
    if not weird:
        removed = pokemons.pop(index)
        removed_elements.append(removed)

        for i in range(len(pokemons)):
            if pokemons[i] <= removed:
                pokemons[i] += removed
            else:
                pokemons[i] -= removed

print(sum(removed_elements))
