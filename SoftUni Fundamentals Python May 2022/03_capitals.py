country = input().split(', ')
capitals = input().split(', ')

for index, el in enumerate(country):
    my_dict = {}
    my_dict[el] = capitals[index]
    print(f"{el} -> {my_dict[el]}")


