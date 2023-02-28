
#This sets up the board on which the participants play
game_board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
original_board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

player1 = ''
player2 = ''

isFull = False
game_on = True
winner = False

def playfield(board):
    print(board[0] + '|' + board[1] + '|' + board[2])
    print(board[3] + '|' + board[4] + '|' + board[5])
    print(board[6] + '|' + board[7] + '|' + board[8])

def player_input():
    global player1
    global player2
    while player1 != 'X' or player1 != 'O':
        player1 = input("Which do you want to be? (X or O): ")
        player1 = player1.upper()
        if player1 == 'X':
            print("Player 1 has chosen X.")
            player1 = 'X'
            player2 = 'O'
            break
        elif player1 == 'O':
            print("Player 1 has chosen O.")
            player1 = 'O'
            player2 = 'X'
            break
    return player1

def place_marker(board, player, position):
    board[position - 1] = player

    return board[position - 1]

#block that confirms if the participant has won
def win_check(board):
    global player1
    global player2
    global game_on
    global winner

    if board[0] == 'O' and board[1] == 'O' and board[2] == 'O':

        if player1 == 'O':
            print("Player 1 (O) has won!")
            game_on = False
            winner = True
        else:
            print("Player 2 (O) has won!")
            game_on = False
            winner = True

    elif board[0] == 'O' and board[4] == 'O' and board[8] == 'O':

        if player1 == 'O':
            print("Player 1 (O) has won!")
            game_on = False
            winner = True
        else:
            print("Player 2 (O) has won!")
            game_on = False
            winner = True

    elif board[2] == 'O' and board[4] == 'O' and board[6] == 'O':

        if player1 == 'O':
            print("Player 1 (O) has won!")
            game_on = False
            winner = True
        else:
            print("Player 2 (O) has won!")
            game_on = False
            winner = True

    elif board[0] == 'O' and board[3] == 'O' and board[6] == 'O':

        if player1 == 'O':
            print("Player 1 (O) has won!")
            game_on = False
            winner = True
        else:
            print("Player 2 (O) has won!")
            game_on = False
            winner = True

    elif board[1] == 'O' and board[4] == 'O' and board[7] == 'O':

        if player1 == 'O':
            print("Player 1 (O) has won!")
            game_on = False
            winner = True
        else:
            print("Player 2 (O) has won!")
            game_on = False
            winner = True

    elif board[2] == 'O' and board[5] == 'O' and board[8] == 'O':

        if player1 == 'O':
            print("Player 1 (O) has won!")
            game_on = False
            winner = True
        else:
            print("Player 2 (O) has won!")
            game_on = False
            winner = True

    elif board[3] == 'O' and board[4] == 'O' and board[5] == 'O':

        if player1 == 'O':
            print("Player 1 (O) has won!")
            game_on = False
            winner = True
        else:
            print("Player 2 (O) has won!")
            game_on = False
            winner = True

    elif board[6] == 'O' and board[7] == 'O' and board[8] == 'O':

        if player1 == 'O':
            print("Player 1 (O) has won!")
            game_on = False
            winner = True
        else:
            print("Player 2 (O) has won!")
            game_on = False
            winner = True

    if board[0] == 'X' and board[1] == 'X' and board[2] == 'X':

        if player1 == 'X':
            print("Player 1 (X) has won!")
            game_on = False
            winner = True
        else:
            print("Player 2 (X) has won!")
            game_on = False
            winner = True

    elif board[0] == 'X' and board[4] == 'X' and board[8] == 'X':

        if player1 == 'X':
            print("Player 1 (X) has won!")
            game_on = False
            winner = True
        else:
            print("Player 2 (X) has won!")
            game_on = False
            winner = True

    elif board[2] == 'X' and board[4] == 'X' and board[6] == 'X':

        if player1 == 'X':
            print("Player 1 (X) has won!")
            game_on = False
            winner = True
        else:
            print("Player 2 (X) has won!")
            game_on = False
            winner = True

    elif board[0] == 'X' and board[3] == 'X' and board[6] == 'X':

        if player1 == 'X':
            print("Player 1 (X) has won!")
            game_on = False
            winner = True
        else:
            print("Player 2 (X) has won!")
            game_on = False
            winner = True

    elif board[1] == 'X' and board[4] == 'X' and board[7] == 'X':

        if player1 == 'X':
            print("Player 1 (X) has won!")
            game_on = False
            winner = True
        else:
            print("Player 2 (X) has won!")
            game_on = False
            winner = True

    elif board[2] == 'X' and board[5] == 'X' and board[8] == 'X':

        if player1 == 'X':
            print("Player 1 (X) has won!")
            game_on = False
            winner = True
        else:
            print("Player 2 (X) has won!")
            game_on = False
            winner = True

    elif board[3] == 'X' and board[4] == 'X' and board[5] == 'X':

        if player1 == 'X':
            print("Player 1 (X) has won!")
            game_on = False
            winner = True
        else:
            print("Player 2 (X) has won!")
            game_on = False
            winner = True

    elif board[6] == 'X' and board[7] == 'X' and board[8] == 'X':

        if player1 == 'X':
            print("Player 1 (X) has won!")
            game_on = False
            winner = True
        else:
            print("Player 2 (X) has won!")
            game_on = False
            winner = True


def space_check(board, position):
    isTaken = False
    if board[position - 1] == 'X' or board[position - 1] == 'O':
        print("That position is already taken choose again.")
        isTaken = True
    else:
        pass
    return isTaken


def full_board_check(board):
    global isFull
    global original_board

    for num in range(9):
        if board[num] == original_board[num]:
            return isFull
    else:
        isFull = True
    return isFull


def player_choice(board):
    good = False
    while good == False:
        choice = int(input("Choose a spot: "))
        space_check(board, choice)
        if space_check(board, choice) == False:
            good = True
            return choice
    return choice


def replay():
    global game_board
    global player1
    global player2
    global isFull
    global game_on

    keep_playing = True

    while keep_playing == True:
        replay = input("Do you want to replay? (Y or N): ")
        replay = replay.upper()
        if replay == 'Y':
            game_board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
            player1 = ''
            player2 = ''
            game_on = True
            isFull = False
        elif replay == 'N':
            keep_playing = False
            print("Thanks for playing!")


print("Welcome to Tic Tac Toe!")
while isFull == False:
    playfield(game_board)
    player_input()
    while game_on:

        full_board_check(game_board)
        if isFull == True and winner == False:
            print("The game is a tie!")
            game_on = False
            break
        if game_on:
            print("Player 1's turn.")
            place_marker(game_board, player1, player_choice(game_board))
            playfield(game_board)
            win_check(game_board)

        full_board_check(game_board)
        if isFull == True and winner == False:
            print("The game is a tie!")
            game_on = False
            break
        if game_on:
            print("Player 2's turn.")
            place_marker(game_board, player2, player_choice(game_board))
            playfield(game_board)
            win_check(game_board)

    break



class TicTacToeBoard:
    def __init__(self):
        self.board = None
        self.moves = 0
        self.game_status = 'ongoing'

        self.create_board()

    def create_board(self):
        self.board = [[TicTacToeSquare() for _ in range(0, 3)] for _ in range(0,3)]

    def update_board(self, row, col, player):

        if self.board[row][col].set_player(player):
            self.moves += 1
            self.check_win()
            self.check_draws()

    def check_draws(self):
        if self.is_full():
            self.game_status = 'draw'


    def check_win(self):
        winner = None

        if not winner:
            winner = self.check_rows()

        if not winner:
            winner = self.check_cols()

        if not winner:
            winner = self.check_dias()

        if winner:
            self.game_status = 'winner is ' + winner
            return winner

    def is_full(self):
        return self.moves < 9


    def check_rows(self):
        for row in self.board:
            if (row[0].current_player == row[1].current_player == row[2].current_player) and (row[0] is not None):
                return row[0].current_player

    def check_cols(self):
        (row_1, row_2, row_3) = zip(self.board)
        for i in range(0,3):
            if (row_1[i] == row_2[i] == row_3[i]) and row_1[i] is not None:
                return row_1[i].current_player

    def check_dias(self):

        if self.board[1][1] is not None:
            if self.board[0][0].current_player == self.board[1][1].current_player == self.board[2][2].current_player:
                return self.board[0][0].current_player
            if self.board[0][2].current_player == self.board[1][1].current_player == self.board[2][0].current_player:
                return self.board[0][0].current_player


class TicTacToeSquare:
    def __init__(self):
        self.current_player = None

    def set_player(self, player):
        if not self.current_player:
            self.current_player = player
            return True
        else:
            print('Place has already been taken')
            return False
