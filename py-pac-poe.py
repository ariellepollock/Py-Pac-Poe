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

