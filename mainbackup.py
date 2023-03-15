class TicTacToeBoard:
    def __init__(self):
        self.board = None
        self.moves = 0
        self.game_status = 'ongoing'

        self.create_board()

    def create_board(self):
        self.board = [[TicTacToeSquare() for _ in range(0, 3)] for _ in range(0, 3)]

    def update_board(self, row, col, player):

        if self.board[row][col].set_player(player):
            self.moves += 1

    def get_board_square(self, row, col):
        return self.board[row][col].current_player

    def check_draws(self):
        if self.is_full():
            self.game_status = 'draw'

    def check_win(self):
        winner = None
        print("Checking Winning func check rows")
        if not winner:
            winner = self.check_rows()
        print("Checking Winning func check col")

        if not winner:
            winner = self.check_cols()
        print("Checking Winning func check daigs")

        if not winner:
            winner = self.check_dias()

        if winner:
            self.game_status = 'winner is ' + winner
            return winner

    def is_full(self):
        return self.moves >= 9

    def check_rows(self):
        for row in self.board:
            if (row[0].current_player == row[1].current_player == row[2].current_player) and (
                    row[0].current_player is not None):
                return row[0].current_player

    def check_cols(self):
        row_1, row_2, row_3 = self.board
        for i in range(0, 3):
            if (row_1[i].current_player == row_2[i].current_player == row_3[i].current_player) and row_1[
                i].current_player is not None:
                return row_1[i].current_player

    def check_dias(self):

        if self.board[1][1].current_player is not None:

            if self.board[0][0].current_player == self.board[1][1].current_player == self.board[2][2].current_player:
                return self.board[0][0].current_player
            if self.board[0][2].current_player == self.board[1][1].current_player == self.board[2][0].current_player:
                return self.board[0][0].current_player

    def playfield(self):
        print(str(board.get_board_square(0, 0)) + '|' + str(board.get_board_square(0, 1)) + '|' + str(
            board.get_board_square(0, 2)))
        print(str(board.get_board_square(1, 0)) + '|' + str(board.get_board_square(1, 1)) + '|' + str(
            board.get_board_square(1, 2)))
        print(str(board.get_board_square(2, 0)) + '|' + str(board.get_board_square(2, 1)) + '|' + str(
            board.get_board_square(2, 2)))


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


player1 = None
player2 = None


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
    return player1, player2


def player_choice():
    row = int(input("Choose a row: "))
    col = int(input("Choose a column: "))
    return row, col


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


if __name__ == '__main__':
    board = TicTacToeBoard()

    print("Welcome to Tic Tac Toe!")
    while not board.is_full():
        board.playfield()
        player1, player2 = player_input()
        while True:

            print("Player 1's turn.")
            player1_row, player1_col = player_choice()
            board.update_board(player1_row, player1_col, player1)
            board.playfield()
            board.check_win()
            board.check_draws()
            if board.game_status != "ongoing":
                break

            print("Player 2's turn.")
            player2_row, player2_col = player_choice()
            board.update_board(player2_row, player2_col, player2)

            board.playfield()
            board.check_win()
            board.check_draws()
            if board.game_status != "ongoing":
                break
        break
    print('Game Over. Result is: ' + board.game_status)