import tictactoe_functions

print("+++ Welcome to PyMoji Tic Tac Toe +++")

character_mapping = {1: "❌", 0: "⭕", "-": "🕳️"}

winning_patterns = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
    (1, 4, 7),
    (2, 5, 8),
    (3, 6, 9),
    (1, 5, 9),
    (3, 5, 7),
)

state = {
    "field": {
        1: "🕳️",
        2: "🕳️",
        3: "🕳️",
        4: "🕳️",
        5: "🕳️",
        6: "🕳️",
        7: "🕳️",
        8: "🕳️",
        9: "🕳️",
    },
    "player_x": [],
    "player_y": [],
    "round": 1,
    "is_running": True,
}


def get_current_player(current_round):
    if current_round % 2 == 1:
        return "player_x"
    if current_round % 2 == 0:
        return "player_y"


def is_free(position):
    return state["field"][position] == "🕳️"


def append_position(position):
    if state["round"] % 2 == 1:
        state["player_x"].append(position)
    if state["round"] % 2 == 0:
        state["player_y"].append(position)


def is_winning(sequence):
    for winning_pattern in winning_patterns:
        if set(winning_pattern) <= set(sequence):
            state["is_running"] = False
            return True

    return False


def update_field(position):
    state["field"][position] = character_mapping[state["round"] % 2]


def print_pretty_field():
    print(
        f"{state['field'][1]}  {state['field'][2]}  {state['field'][3]}   ➡  1 2 3\n"
        f"{state['field'][4]}  {state['field'][5]}  {state['field'][6]}   ➡  4 5 6\n"
        f"{state['field'][7]}  {state['field'][8]}  {state['field'][9]}   ➡  7 8 9"
    )


print("The field is coded into a number grid, like so:")
print_pretty_field()


while state["is_running"]:
    print(f"\n+++++ ROUND {state['round']} +++++")
    print(f"Player {character_mapping[state['round'] % 2]} . Your turn...")
    current_player = get_current_player(state["round"])

    while True and state["round"] < 10:
        ui_position = tictactoe_functions.sanitised_input(
            "Enter your position: ", int, 1, 9
        )
        if not is_free(ui_position):
            print("This spot is already occupied. Choose a different spot.")

        if is_free(ui_position):
            break

    append_position(ui_position)
    update_field(ui_position)
    print_pretty_field()

    if is_winning(state[current_player]):
        print(
            f"Player {character_mapping[state['round'] % 2]}  won the match! Congratulations!"
        )

    state["round"] += 1
