def incorrect_input(player_name,player_selection):
    valid_selections = ("rock", "paper", "scissors")
    if not player_selection.lower() in valid_selections:
        print(f"Invalid selection from player {player_name} : must be one of {valid_selections}")
        return enter_input(player_name)
    else:
        return player_selection

def enter_input(player_name):
    x = input(f"Enter player {player_name}'s turn: ")
    return x

play_a = enter_input('A')
play_b = enter_input('B')
incorrect_input('A',play_a)
incorrect_input('B',play_b)

if play_a == play_b:

