name_one = input()
name_two = input()
card_counter = 0
result_first_player = 0
result_second_player = 0
wars_winner_name = ''
wars_winner_points = 0
game_ended = False
command = input()
while command != 'End of game':
    first_player_card = int(command)
    second_player_card = int(input())
    card_counter += 2
    if first_player_card > second_player_card:
        result_first_player += first_player_card - second_player_card
    elif second_player_card > first_player_card:
        result_second_player += second_player_card - first_player_card
    elif first_player_card == second_player_card:
        extra_card1 = int(input())
        extra_card2 = int(input())
        card_counter += 2
        if extra_card1 > extra_card2:
            wars_winner_name = name_one
            wars_winner_points = result_first_player
        elif extra_card2 > extra_card1:
            wars_winner_name = name_two
            wars_winner_points = result_second_player
        print(f"Number wars!")
        print(f"{wars_winner_name} is winner with {wars_winner_points} points")
        game_ended = True
        break
    if card_counter == 0:
        break
    command = input()
if not game_ended:
    print(f"{name_one} has {result_first_player} points")
    print(f"{name_two} has {result_second_player} points")
