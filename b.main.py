import csv
import random

analytics_strings = []


class Player:

    def __init__(self, is_human):
        """
        This class represents players that can be human or simulated
        :param is_human: defines if the participant of the game is a human or computer
        """
        self.is_human = is_human
        self.sign = None

    def set_sign(self, sign):
        """
        This function assigns the player a sign
        :param sign:
        """
        self.sign = sign

    def player_choice(self):
        """
        This function allows the player to choose which space on the game board to place their sign on,
        first choosing the row and then the column
        :return: the row and column the player has chosen
        """
        row = int(input("Choose a row: "))
        col = int(input("Choose a column: "))
        return row, col

    def get_input(self):
        """
        This function, if self.is_human is set to false, the row and column are randomized for the computer.
        Otherwise self.player_choice is called to get the rows and column
        :return: The row and column
        """
        if not self.is_human:
            row = random.randint(0, 2)
            col = random.randint(0, 2)

        else:
            row, col = self.player_choice()

        return row, col


class TicTacToeBoard:
    def __init__(self):
        """
        This class represents the workings of the board and the rules for the game, and updating the board.
        """
        self.board = None
        self.moves = 0
        self.game_status = 'ongoing'

        self.create_board()

    def create_board(self):
        """
        This function created the board
        """
        self.board = [[TicTacToeSquare() for _ in range(0, 3)] for _ in range(0, 3)]

    def update_board(self, row, col, player):
        """

        :param row: The row to be updated
        :param col: The Column to be updated
        :param player: The player
        :return: return true if the board was updated, else return false
        """
        if self.board[row][col].set_player(player):
            self.moves += 1
            return True
        return False

    def get_board_square(self, row, col):
        """
        Helper function to retrieve the row and column from the board
        :param row: the row to retrieve
        :param col: the column to retrieve
        :return: returns the place on the board that was requested
        """
        return self.board[row][col].current_player

    def check_draws(self):
        """
        Function to check if the board is full to indicate that the game has ended in a draw
        """
        if self.is_full():
            self.game_status = 'draw'

    def check_win(self):
        """
        Calls subfunctions to check if the player has won the game
        :return:
        """
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
        """
        Helper function to see if there have been 9 moves made which would fill the board
        :return: it returns if there have been 9 moves made
        """
        return self.moves >= 9

    def check_rows(self):
        """
        Function to check all the rows if they have been taken up by the same sign
        :return: returns player if there is a row full of the same sign
        """
        for row in self.board:
            if (row[0].current_player == row[1].current_player == row[2].current_player) and (
                    row[0].current_player is not None):
                return row[0].current_player

    def check_cols(self):
        """
        Function to check all the columns for if they have been taken up by the same sign
        :return: returns the player if there is a column full of the same sign
        """
        row_1, row_2, row_3 = self.board
        for i in range(0, 3):
            if (row_1[i].current_player == row_2[i].current_player == row_3[i].current_player) and row_1[
                i].current_player is not None:
                return row_1[i].current_player

    def check_dias(self):
        """
        Function to check the diagonals of the baord for if they have been taken up by the same sign
        :return: returns the player if there is a diagonal full of the same sign
        """

        if self.board[1][1].current_player is not None:

            if self.board[0][0].current_player == self.board[1][1].current_player == self.board[2][2].current_player:
                return self.board[0][0].current_player
            if self.board[0][2].current_player == self.board[1][1].current_player == self.board[2][0].current_player:
                return self.board[0][0].current_player

    def playfield(self):
        """
        Function to create the cisual border of the board
        """
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
            print('Place has already been taken, go again')
            return False


player1 = None
player2 = None


def player_input():
    """
    Function that allows the the player/computer to choose their sign
    :return:
    """
    global player1
    global player2
    signs = ['X', 'O']
    num_player = input(
        "enter the number of players \n 0 - simulation \n 1 - player vs computer \n 2 - player vs player \n \n enter: ")
    if num_player == '0':
        players = (Player(is_human=False), Player(is_human=False))
        player1 = random.choice(signs)
        players[0].set_sign(player1)
        players[1].set_sign(list((set(signs) - set(player1)))[0])

    if num_player == '1':
        while player1 != 'X' or player1 != 'O':
            print(player1)
            player1 = input("Which do you want to be? (X or O): ")
            player1 = player1.upper()
            break
        players = (Player(is_human=True), Player(is_human=False))
        players[0].set_sign(player1)
        players[1].set_sign(list((set(signs) - set(player1)))[0])

    if num_player == '2':
        while player1 != 'X' or player1 != 'O':
            player1 = input("Which do you want to be? (X or O): ")
            player1 = player1.upper()
            break
        players = (Player(is_human=True), Player(is_human=True))
        players[0].set_sign(player1)
        players[1].set_sign(list((set(signs) - set(player1)))[0])

    return players


def replay():
    """
    Function to allow the player to either return to the menu or end the game after a match has been concluded
    :return: true if the player wished to go to the menu, false if the player wishes to exit
    """
    replay = input("\nDo you want to continue playing \n \n y - return to menu \n n - quit \n\n enter: ")
    replay = replay.upper()
    if replay == 'Y':
        return True
    elif replay == 'N':
        print("Thanks for playing!")
        return False


def write_csv(analytics_strings):
    """
    Function to gather the data from the game such as the number of the game, the player, the move, the row and the
    column the the player chose :param analytics_strings:
    """
    row_labels = ['Game Number', 'Player', 'Move Count', 'Row', 'Column']
    with  open('boardmovedata.csv', 'w') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter=',')
        csv_writer.writerow(row_labels)

        csv_writer.writerows(analytics_strings)


if __name__ == '__main__':
    replay_game = True
    game_count = 0
    while replay_game:
        print('creating new board')
        board = TicTacToeBoard()
        game_count += 1
        game_move_count = 0

        print("Welcome to Tic Tac Toe!")

        while not board.is_full():
            board.playfield()
            player1, player2 = player_input()
            while True:
                player1_placed = False
                player2_placed = False

                print("Player 1's turn.")
                while not player1_placed:
                    player1_row, player1_col = player1.get_input()
                    player1_placed = board.update_board(player1_row, player1_col, player1.sign)
                else:
                    game_move_count += 1
                    board.playfield()
                    board.check_win()
                    board.check_draws()
                    analytics_strings.append([game_count, player1.sign, game_move_count, player1_row, player1_col])
                if board.game_status != "ongoing":
                    break

                print("Player 2's turn.")
                while not player2_placed:
                    player2_row, player2_col = player2.get_input()
                    player2_placed = board.update_board(player2_row, player2_col, player2.sign)
                else:
                    game_move_count += 1
                    board.playfield()
                    board.check_win()
                    board.check_draws()
                    analytics_strings.append([game_count, player2.sign, game_move_count, player2_row, player2_col])
                if board.game_status != "ongoing":
                    break
            break
        print('Game Over. Result is: ' + board.game_status)
        replay_game = replay()

    write_csv(analytics_strings)

