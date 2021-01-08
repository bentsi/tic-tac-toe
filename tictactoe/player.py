from abc import ABC, abstractmethod
import random
import time


class Player(ABC):
    def __init__(self):
        self.list_of_moves = []

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
        super().__init__()

    @property
    def name(self):
        return self._name

    @property
    def symbol_class(self):
        return self._symbol_class

    def move(self):
        symbol = self._symbol_class.__name__

        flag = True
        while flag:
            loc = input(f"{self.name} Where to set {symbol}?")
            loc_x = int(loc.split(",")[0])
            loc_y = int(loc.split(",")[1])
            move = (loc_x, loc_y)
            if HumanPlayer.validation_move(move) and \
                    move not in self.list_of_moves:
                flag = False
        self.list_of_moves.append(move)
        return self._symbol_class(loc_x, loc_y)

    @staticmethod
    def validation_move(x):
        if (x[0] >= 0) and (x[0] <= 2) and \
           (x[1] >= 0) and (x[1] <= 2):
            return True
        else:
            print("Указанные значения должны быть в диапазоне (0, 2)")
        return False

    def __str__(self):
        return f"Human{self._name} playing {self._symbol_class.__name__}"


class RoboticPlayer(HumanPlayer):
    def __init__(self, symbol_class):
        super().__init__(name=self.definition_name(), symbol_class=symbol_class)

    @staticmethod
    def definition_name():
        return random.choice(["Железяка", "Robotic"])

    def move(self):
        symbol = self._symbol_class.__name__
        flag = True
        time.sleep(3)
        print(f"Робот {self.name} думает ...")
        while flag:
            loc_x = random.randint(0, 2)
            loc_y = random.randint(0, 2)
            move = (loc_x, loc_y)
            if HumanPlayer.validation_move(move) and \
                    move not in self.list_of_moves:
                flag = False
        self.list_of_moves.append(move)
        return self._symbol_class(loc_x, loc_y)