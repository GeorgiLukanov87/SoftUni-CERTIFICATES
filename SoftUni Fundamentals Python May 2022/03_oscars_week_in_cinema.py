movie_name = input()
type_cine = input()
tickets_sold = int(input())
ticket_price = 0
if type_cine == 'normal':
    if movie_name == "A Star Is Born":
        ticket_price = 7.50
    elif movie_name == "Bohemian Rhapsody":
        ticket_price = 7.35
    elif movie_name == "Green Book":
        ticket_price = 8.15
    else:
        ticket_price = 8.75
elif type_cine == 'luxury':
    if movie_name == "A Star Is Born":
        ticket_price = 10.50
    elif movie_name == "Bohemian Rhapsody":
        ticket_price = 9.45
    elif movie_name == "Green Book":
        ticket_price = 10.25
    else:
        ticket_price = 11.55
else:
    if movie_name == "A Star Is Born":
        ticket_price = 13.50
    elif movie_name == "Bohemian Rhapsody":
        ticket_price = 12.75
    elif movie_name == "Green Book":
        ticket_price = 13.25
    else:
        ticket_price = 13.95

total_sum = tickets_sold * ticket_price
print(f"{movie_name} -> {total_sum:.2f} lv.")
