##############################################
#  display welcome message
##############################################
def display_message():
    message = "Let's play Py-Pac-Poe!"
    frame = "-" * len(message)
    print(frame)
    print(message)
    print(frame)

##############################################
#  Global state
##############################################
score = {'X': 0, 'O': 0, 'T': 0}
num_wins = int(input("How many wins to play to? "))
board = {}
turn = 'X'
winner = None

##############################################
#  display board
##############################################
def display_board():
    board = state['board']
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
    
##############################################
#  prompt players turn
##############################################
def prompt_player_turn():
    player = state['turn']
    board = state['board']
    valid_input = False
    move = ""

    while not valid_input:
        move = input(f"Player {player}'s Move (example B2): ").lower()

        if len(move) == 2 and move[0] in ['a', 'b', 'c'] and move[1] in ['1', '2', '3']:
            if state['board'][move] == ' ':
                valid_input = True
            else:
                print("That cell is already occupied! Try again...")
        else:
            print("Bogus move! Try again...")

    return move

##############################################
#  Check winner or tie
##############################################
def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(1, 4):
        if board[f'a{i}'] == board[f'b{i}'] == board[f'c{i}'] == player and board[f'a{i}'] != ' ':  # Check row
            return True
        if board[f'{chr(96 + i)}1'] == board[f'{chr(96 + i)}2'] == board[f'{chr(96 + i)}3'] == player and board[f'{chr(96 + i)}1'] != ' ':  # Check column
            return True

    # Check diagonals
    if (board['a1'] == board['b2'] == board['c3'] == player or board['a3'] == board['b2'] == board['c1'] == player) and board['b2'] != ' ':
        return True

    return False

def is_board_full(board):
    return all(cell != ' ' for cell in board.values())

##############################################
#  Game loop
##############################################
def game_loop():
    display_message()

    while True:
        display_board()
        move = prompt_player_turn()
        state['board'][move] = state['turn']

        if check_winner(state['board'], state['turn']):
            print(f"Player {state['turn']} wins the game!")
            break
        elif is_board_full(state['board']):
            print("Another tie!")
            break

        # Toggle player
        state['turn'] = 'X' if state['turn'] == 'O' else 'O'

game_loop()