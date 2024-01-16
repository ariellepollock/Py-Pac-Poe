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
board = {}

def display_board():
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
    
##############################################
#  STEP 3 - prompt players turn
##############################################
current_player = 'X'

def prompt_player_turn(player):
    print(f"It's player {player}'s turn")
