from random import randint
from abc import ABC, abstractmethod


class Player(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def move(self):
        pass


class HumanPlayer(Player):

    def __init__(self, name, symbol_class):
        self._name = name
        self._symbol_class = symbol_class
        self._win = 0

    @property
    def name(self):
        return self._name
    @property
    def win(self):
        return self._win

    @win.setter
    def win(self, val):
        self._win = val

    def move(self):
        symbol = self._symbol_class.__name__
        ok = True
        x = y =None
        while ok:
            try:
                loc = input(f"[{self.name}] Where to set {symbol}? (use , to separate) ")
                x, y = loc.split(",")
                ok = False
            except ValueError:
                ok = True
                print("Enter the correct arguments(two arguments)")
        return self._symbol_class(x=x, y=y)


class RoboticPlayer(Player):

    def __init__(self, name, symbol_class):
        self._name = name
        self._symbol_class = symbol_class
        self._win = 0

    @property
    def name(self):
        return self._name

    @property
    def win(self):
        return self._win

    @win.setter
    def win(self, val):
        self._win = val

    def move(self):
        x = randint(0, 2)
        y = randint(0, 2)
        return self._symbol_class(x=x, y=y)
