cards = input().split()
n = int(input())

first_card = cards[0]
last_card = cards[-1]

half_deck = len(cards) // 2
shuffle_cards = []
for shuffles in range(n):
    left_side = []
    right_side = []

    for index in range(1, half_deck):
        left_side.append(cards[index])

    for index in range(half_deck, len(cards)-1):
        right_side.append(cards[index])

    for index in range(len(left_side)):
        shuffle_cards.append(right_side[index])
        shuffle_cards.append(left_side[index])

    cards = shuffle_cards.copy()
    shuffle_cards = []

    cards.append(last_card)
    cards.insert(0, first_card)

print(cards)
