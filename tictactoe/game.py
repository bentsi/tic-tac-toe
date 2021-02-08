from tictactoe.board import Board
from itertools import cycle


class Game:
    def __init__(self, players):
        self._board = Board()
        self._players = players

    @property
    def players(self):
        return self._players


    def _is_row_check(self, symbol):
        board = self._board.board
        for row in board:
            if len(set(row)) == 1 and row[0] == symbol:
                return False

    def _is_column(self, symbol):
        board = self._board.board
        for i in range(3):
            if board[0][i] == board[1][i] == board[2][0] == symbol:
                return False


    def _is_diag_1(self, symbol):
        board = self._board.board
        if len(set(board[i][i] for i in range(3))) == 1 \
                and board[0][0] == symbol:
            return False


    def _is_diag_2(self, symbol):
        board = self._board.board
        if board[0][2] == board[1][1] == board[2][0] == symbol:
            return False


    def _is_win(self, symbol):
        if self._is_row_check(symbol) is False \
            or self._is_column(symbol) is False \
            or self._is_diag_1(symbol) is False \
            or self._is_diag_2(symbol) is False:
            return False

    def _is_free_cell_check(self, move):
        board = self._board.board
        symb, x, y = move
        if board[int(x)-1][int(y)-1] != " ":
            return False
        else:
            return True


    def _game_welcome(self):
        print(f"So, we have 3x3 sized board and {self._players[0].name} "
              f"vs. {self._players[1].name}.")
        print("Let the Game begin!")


    def player_run(self, player):
        move = player.move()
        if self._is_free_cell_check(move):
            self._board.board = move
            print(self._board)
            symbol = player.symbol_class.__name__

            if self._is_win(symbol=symbol) is False:
                print(f"Stop the Game! {player.name} is our Winner!")
                exit()
        else:
            print("This cell is busy, try another one...")
            self.player_run(player)


    def game_run(self):
        self._game_welcome()
        for player in cycle(self._players):
            self.player_run(player=player)