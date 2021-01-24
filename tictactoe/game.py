from tictactoe.board import Board
from itertools import cycle


class Game:
    def __init__(self, players):
        self._board = Board()
        self._players = players

    @property
    def players(self):
        return self._players

    def _check(self, moving_player):
        board = self._board.board
        symbol = moving_player.symbol_class.__name__
        row = ''
        column = ''
        reverse_diagonal = ''
        direct_diagonal = ''
        empty_count = 0
        for i in range(len(board)):
            for j in range(len(board)):
                row += board[i][j]
                column += board[j][i]
                if board[i][j] == ' ':
                    empty_count += 1
                if i == j:
                    reverse_diagonal += board[i][j]
            if row == symbol * len(board) or column == symbol * len(board):
                print(f"[{moving_player.name}] wins!")
                return True
            row = ''
            column = ''
            direct_diagonal += board[len(board) - 1 - i][i]
        if direct_diagonal == symbol * len(board) or reverse_diagonal == symbol * len(board):
            print(f"[{moving_player.name}] wins!")
            return True
        if empty_count == 0:
            print("Draw!")
            return True
        return False

    def run(self):
        for player in cycle(self._players):
            if player.__class__.__name__ == 'RoboticPlayer':
                move = player.move(board=self._board.board)
            else:
                move = player.move()
            self._board.board = move
            print(self._board)
            if self._check(moving_player=player):
                return
