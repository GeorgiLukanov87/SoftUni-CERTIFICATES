count_people = int(input())
count_nights = int(input())
count_transport_cards = int(input())
museum_ticket = int(input())
price_night_person = count_nights * 20
price_transport_cards = count_transport_cards * 1.60
price_museum_ticket = museum_ticket * 6
final_sum_for_person = price_night_person + price_transport_cards + price_museum_ticket
print(f"{(final_sum_for_person * count_people) * 1.25:.2f}")
