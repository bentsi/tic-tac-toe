
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class X(Point):
    def __init__(self, x, y):
        super().__init__(x, y)

    def __str__(self):
        return "X"


class O(Point):
    def __init__(self, x, y):
        super().__init__(x, y)

    def __str__(self):
        return "O"


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
        board_str = ""
        for line in self._board:
            board_str += "|" + "|".join(line) + "|\n"
        return board_str

    def validator_bord(self, val):
        value = self._board[val.x][val.y]
        if value == 'X' or value == 'O':
            return False
        return True


if __name__ == '__main__':
    b = Board()
    x = X(0, 0)  # Обьявляем координату x(0,0)
    b.board = x  # Через сеттер присваевымаем ячейке значение X
    print(b.validator_bord(x))  # Проверяем хранятся ли ячейка с координатами (0, 0)
