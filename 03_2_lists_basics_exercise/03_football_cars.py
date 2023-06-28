red_cards = input().split(' ')
red_card_team_A = 0
red_card_team_B = 0
players_with_red_cards = []
playing = True

for element in red_cards:
    if element in players_with_red_cards:
        continue
    else:
        players_with_red_cards.append(element)

    red_card = element.split('-')
    if red_card[0] == 'A':
        red_card_team_A += 1
    elif red_card[0] == 'B':
        red_card_team_B += 1
    if 11 - red_card_team_A < 7 or 11 - red_card_team_B < 7:
        playing = False
        break

if playing:
    print(f"Team A - {11-red_card_team_A}; Team B - {11-red_card_team_B}")
else:
    print(f"Team A - {11 - red_card_team_A}; Team B - {11 - red_card_team_B}")
    print("Game was terminated")