class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"[{self.x},{self.y}]"


class X(Point):
    def __init__(self, x, y):
        super().__init__(x, y)

    def __str__(self):
        return "X" + super().__str__()


class O(Point):
    def __init__(self, x, y):
        super().__init__(x, y)

    def __str__(self):
        return "O" + super().__str__()


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
        x = int(val[1]) - 1
        y = int(val[2]) - 1
        self._board[x][y] = val[0]

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

# if __name__ == "__main__":
#     board = Board()
#     print(board)
#
#     x = X(x=1, y=1)
#     print(X.__name__)



