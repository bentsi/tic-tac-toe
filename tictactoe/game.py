from tictactoe.board import Board
from itertools import cycle


class Game:
    def __init__(self, players):
        self._board = Board()
        self._players = players

    @property
    def players(self):
        return self._players

    def _check(self):
        # Horizontal checking
        for line in self._board.board:
            if line[0] == line[1] == line[2]:
                if line[0] != " ":
                    return True, None
        # Vertical checking
        for i in range(3):
            first_vertical = self._board.board[0][i]
            second_vertical = self._board.board[1][i]
            third_vertical = self._board.board[2][i]
            if first_vertical == second_vertical == third_vertical != " ":
                return True, None
        # Diagonal checking
        if self._board.board[0][0] == self._board.board[1][1] == self._board.board[2][2] != " ":
            return True, None
        if self._board.board[0][2] == self._board.board[1][1] == self._board.board[2][0] != " ":
            return True, None
        # Checking empty cells
        for line in self._board.board:
            for element in line:
                if element == " ":
                    return False, None
        return True, True

    def run(self):
        for player in cycle(self._players):
            ok = True
            while ok:
                try:
                    move = player.move()
                    while self._board.board[int(move.x)][int(move.y)] != " ":
                        print("This cell is occupied")
                        move = player.move()
                    self._board.board = move
                    ok = False
                except IndexError:
                    print("Values out of range(0-2)")
                    ok = True
                except ValueError:
                    print("Invalid values")
                    ok = True
            print(self._board)
            win, drawn = self._check()
            if  win:
                if drawn:
                    print("Drawn")
                    break
                print(f"{player.name} win")
                break
