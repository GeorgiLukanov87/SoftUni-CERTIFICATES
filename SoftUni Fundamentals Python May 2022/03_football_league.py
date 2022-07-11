def clean_string(some_str: str, some_key: str, to_add):
    start_index = some_str.index(some_key[0])
    to_add = 0
    for all_indexes in range(len(some_key)):
        if some_key[all_indexes].lower() == key[-1].lower():
            to_add += 1

    word = some_str[start_index + len(some_key):]
    word = word[::-1]
    new_index = word[::-1].index(f"{key[0]}")
    new_word = word[::-1][:new_index + to_add]
    result = new_word.upper()[::-1]
    return result, to_add


def who_won(result1, result2):
    team_1 = False
    team_2 = False
    draw = False
    if result1 > result2:
        team_1 = True
    elif result1 < result2:
        team_2 = True
    else:
        draw = True
    current_status = [team_1, team_2, draw]
    return current_status


def making_teams_inside_dict(team_one, team_two, some_dict):
    if team_one not in all_teams_scores:
        all_teams_scores[team_one] = 0
    else:
        all_teams_scores[team_one] += 0

    if team_two not in all_teams_scores:
        all_teams_scores[team_two] = 0
    else:
        all_teams_scores[team_two] += 0
    return some_dict


def if_result_match(some_dict):
    results = []
    zero_result_counter = 0
    for key, value in some_dict.items():
        if value > 0:
            results.append(value)
        else:
            zero_result_counter += 1

    if (len(some_dict) - zero_result_counter) != len(set(some_dict)):
        return True
    return False


key = input()
data = input()
score = []
all_teams_scores = {}
all_teams_goals = {}
to_add = 0
while not data == 'final':
    data = data.split(' ')
    score = data[-1]
    goals1 = int(score[0])
    goals2 = int(score[-1])
    status = who_won(goals1, goals2)
    team1 = data[0]
    team1, to_add = clean_string(team1, key, to_add)
    team1 = team1[to_add:]
    team2 = data[1]
    team2, to_add = clean_string(team2, key, to_add)
    team2 = team2[to_add:]
    # /////////////////////////////////////////////////////////////////////////////////////////////////
    if team1 not in all_teams_goals:
        all_teams_goals[team1] = goals1
    else:
        all_teams_goals[team1] += goals1

    if team2 not in all_teams_goals:
        all_teams_goals[team2] = goals2
    else:
        all_teams_goals[team2] += goals2
    # ////////////////////////////////////////////////////////////////////////////////////////////////////
    all_teams_scores = making_teams_inside_dict(team1, team2, all_teams_scores)
    if team1 in all_teams_scores:
        if status[0]:
            all_teams_scores[team1] += 3
        elif not status[0] and not status[2]:
            all_teams_scores[team1] += 0
        else:
            all_teams_scores[team1] += 1
    if team2 in all_teams_scores:
        if status[1]:
            all_teams_scores[team2] += 3
        elif not status[1] and not status[2]:
            all_teams_scores[team2] += 0
        else:
            all_teams_scores[team2] += 1
    # ////////////////////////////////////////////////////////////////////////////////////////////////////
    data = input()

print('League standings:')
is_matched1 = (if_result_match(all_teams_scores))
is_matched2 = (if_result_match(all_teams_goals))

if is_matched1 or is_matched2:
    sorted_score = sorted(all_teams_scores.items(), key=lambda x: x[0])
    sorted_goals = sorted(all_teams_goals.items(), key=lambda x: x[0])

sorted_score = sorted(all_teams_scores.items(), key=lambda x: x[1], reverse=True)
sorted_goals = sorted(all_teams_goals.items(), key=lambda x: x[1], reverse=True)

position = 0
for team in sorted_score:
    position += 1
    print(f"{position}. {team[0]} {team[1]}")

print('Top 3 scored goals:')
counter = 0
for team in sorted_goals:
    counter += 1
    print(f"- {team[0]} -> {team[1]}")
    if counter == 3:
        break
