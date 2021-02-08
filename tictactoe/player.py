from abc import ABC, abstractmethod
from tictactoe.board import X, O
import random

class Player(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def is_checked(x, y):
        pass


class HumanPlayer(Player):
    def __init__(self, name, symbol_class):
        self._name = name
        self._symbol_class = symbol_class

    @property
    def symbol_class(self):
        return self._symbol_class

    @property
    def name(self):
        return self._name


    @staticmethod
    def is_checked(x, y):
        if int(x) < 4 and int(y) < 4:
            return True
        else:
            return False


    def move(self):
        symbol = self._symbol_class.__name__
        loc = input(f"[{self.name}], where to set "
                    f"your '{symbol}'? (As 'row','column'): ")
        x, y = loc.split(",")
        if self.is_checked(x=x, y=y):
            return [symbol, x, y]
        else:
            print("The board is 3x3, so rows "
                  "and columns must fit. Try again :)")
            self.move()


class RoboticPlayer(Player):
    def __init__(self, name, symbol_class):
        self._name = name
        self._symbol_class = symbol_class

    @property
    def symbol_class(self):
        return self._symbol_class

    @property
    def name(self):
        return self._name

    @staticmethod
    def is_checked(x, y):
        if x < 4 and y < 4:
            return True
        else:
            return False


    def move(self):
        x = random.randint(1, 3)
        y = random.randint(1, 3)
        print(f"ROBOT made its move with '{self._symbol_class.__name__}' "
              f"at row '{x}' and column '{y}':")
        return [self._symbol_class.__name__, x, y]


if __name__ == '__main__':
    player = HumanPlayer(name="Fedor", symbol_class=X)
    print(player.move())
