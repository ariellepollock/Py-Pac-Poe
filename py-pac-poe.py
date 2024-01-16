##############################################
#  STEP 1 - display welcome message
##############################################
def display_message():
    message = "Let's play Py-Pac-Poe!"
    frame = "-" * len(message)
    print(frame)
    print(message)
    print(frame)

display_message()

####################################################
#  STEP 2 - display printed board + existing moves
####################################################
board = {
    'a1': ' ', 'b1': ' ', 'c1': ' ',
    'a2': ' ', 'b2': ' ', 'c2': ' ',
    'a3': ' ', 'b3': ' ', 'c3': ' ',
}

def display_board(player):
    print(
        """
        A   B   C

    1)  {} | {} | {} 
        ----------
    2)  {} | {} | {}
        ----------
    3)  {} | {} | {}
    """.format(
        str(board['a1'] or ' '), str(board['b1'] or ' '), str(board['c1'] or ' '),
        str(board['a2'] or ' '), str(board['b2'] or ' '), str(board['c2'] or ' '),
        str(board['a3'] or ' '), str(board['b3'] or ' '), str(board['c3'] or ' ')
        )
    )
    #  STEP 3 - prompt players turn
    #  STEP 4 - prompt how to enter valid move
    move = input(f"Player {player}'s move (example B2): ")
    
    #  STEP 5 - upper or lower case
    if move: 
        column = move[0].lower()
        row = move[1]
        formatted_move = column + row
    else:
        formatted_move = ""
    return formatted_move
    
##############################################
#  STEP 3 - prompt players turn
##############################################
current_player = 'X'

move = display_board(current_player)

