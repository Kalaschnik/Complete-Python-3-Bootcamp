print("Welcome to PyMoji Tic Tac Toe")
# print(
#     """
# ❌  ⭕  🕳️
# ⭕  🕳️  ❌
# 🕳️  ⭕  ❌
# """
# )

# print(
#     """
# 1  2  3
# 4  5  6
# 7  8  9
# """
# )

character_mapping = {"x": "❌", "o": "⭕", "-": "🕳️"}

field_state = {
    1: character_mapping["-"],
    2: character_mapping["-"],
    3: character_mapping["-"],
    4: character_mapping["-"],
    5: character_mapping["-"],
    6: character_mapping["-"],
    7: character_mapping["-"],
    8: character_mapping["-"],
    9: character_mapping["-"],
}

print(
    f"{field_state[1]}  {field_state[2]}  {field_state[3]}\n"
    f"{field_state[4]}  {field_state[5]}  {field_state[6]}\n"
    f"{field_state[7]}  {field_state[8]}  {field_state[9]}"
)

print("Player ❌  always goes first.")
input_playerx = int(input("Enter your number: "))
print(input_playerx)

# update field state
field_state[input_playerx] = "❌"

print(
    f"{field_state[1]}  {field_state[2]}  {field_state[3]}\n"
    f"{field_state[4]}  {field_state[5]}  {field_state[6]}\n"
    f"{field_state[7]}  {field_state[8]}  {field_state[9]}"
)
