class Point:
    def __init__(self, x, y):
        self._x = int(x)
        self._y = int(y)

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def __str__(self):
        return self.__class__.__name__


class X(Point):
    pass


class O(Point):
    pass


class Board:
    def __init__(self):
        self._board = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "],
        ]

    @property
    def board(self):
        return self._board

    @board.setter
    def board(self, val):
        self._board[val.x][val.y] = str(val)

    def __str__(self):
        """
        | X | O |   |
        | O |   |   |
        |   | X |   |
        """
        board_str = ""
        for line in self._board:
            board_str += "| " + " | ".join(line) + " |\n"
        return board_str
