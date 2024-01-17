##############################################
#  Global state
##############################################
state = {
    'board': {
        'a1': ' ', 'b1': ' ', 'c1': ' ',
        'a2': ' ', 'b2': ' ', 'c2': ' ',
        'a3': ' ', 'b3': ' ', 'c3': ' ',
    },
    'turn': 'X'
}

##############################################
#  display welcome message
##############################################
def display_message():
    message = "Let's play Py-Pac-Poe!"
    frame = "-" * len(message)
    print(frame)
    print(message)
    print(frame)

display_message()

####################################################
#  display printed board + existing moves
####################################################
board = {
    'a1': ' ', 'b1': ' ', 'c1': ' ',
    'a2': ' ', 'b2': ' ', 'c2': ' ',
    'a3': ' ', 'b3': ' ', 'c3': ' ',
}

def display_board(player):
    valid_input = False
    move = ""

    while not valid_input:

        # Display the board first
        print(
            f"""
            A   B   C

        1)  {board['a1'] or ' '} | {board['b1'] or ' '} | {board['c1'] or ' '} 
            ----------
        2)  {board['a2'] or ' '} | {board['b2'] or ' '} | {board['c2'] or ' '}
            ----------
        3)  {board['a3'] or ' '} | {board['b3'] or ' '} | {board['c3'] or ' '}
        """
        )

        # Prompt for player's move
        move = input(f"Player {player}'s Move (example B2): ")

        # Validate the move
        if len(move) == 2 and move[0].lower() in ['a', 'b', 'c'] and move[1] in ['1', '2', '3']:
            column = move[0].lower()
            row = move[1]
            position = column + row

            if board[position] == ' ':
                valid_input = True
            else:
                print("That cell is already occupied! Try again...")
        else:
            print("Bogus move! Try again...")

    return move
    
##############################################
#  prompt players turn
##############################################
current_player = 'X'

move = display_board(current_player)


def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(1, 4):
        if board[f'a{i}'] == board[f'b{i}'] == board[f'c{i}'] == player:  # Check row
            return True
        if board[f'{chr(96 + i)}1'] == board[f'{chr(96 + i)}2'] == board[f'{chr(96 + i)}3'] == player:  # Check column
            return True

    # Check diagonals
    if board['a1'] == board['b2'] == board['c3'] == player or board['a3'] == board['b2'] == board['c1'] == player:
        return True

    return False

def is_board_full(board):
    return all(cell != ' ' for cell in board.values())

if check_winner(board, current_player):
    print(f"Player {current_player} wins the game!")
    # End the game or start a new game
elif is_board_full(board):
    print("Another tie!")
    # End the game or start a new game

# Example of how to use this in your game loop
# ... [game loop code] ...
if check_winner(board, current_player):
    print(f"Player {current_player} wins the game!")
    # End the game or start a new game