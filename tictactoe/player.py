from abc import ABC, abstractmethod
from tictactoe.board import Point
from random import randint
from time import sleep


class Player(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def move(self, board):
        pass


class HumanPlayer(Player):
    def __init__(self, name, symbol_class):
        self._name = name
        self._symbol_class = symbol_class

    @property
    def name(self):
        return self._name

    @property
    def symbol_class(self):
        return self._symbol_class

    def move(self, board=None):
        symbol = self._symbol_class.__name__
        loc = input(f"[{self.name}] Where to set \"{symbol}\"? (use \",\" to separate): ")
        x, y = loc.split(",")
        return self._symbol_class(x=x.strip(), y=y.strip())


class RoboticPlayer(Player):
    def __init__(self, name, symbol_class):
        self._name = name
        self._symbol_class = symbol_class

    @property
    def name(self):
        return self._name

    @property
    def symbol_class(self):
        return self._symbol_class

    def move(self, board):
        symbol = self._symbol_class.__name__
        winning_moves = []
        defensive_moves = []
        regular_moves = []
        empty_cells = []
        move_count = 0
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == ' ':
                    empty_cells.append(Point(x=i, y=j))
                if board[i][j] == symbol:
                    move_count += 1
            winning_moves, defensive_moves, regular_moves = self.move_analyze(count=move_count,
                                                                              empty_list=empty_cells,
                                                                              win_list=winning_moves,
                                                                              defense_list=defensive_moves,
                                                                              regular_list=regular_moves)
            empty_cells = []
            move_count = 0
        for i in range(len(board)):
            for j in range(len(board)):
                if board[j][i] == ' ':
                    empty_cells.append(Point(x=j, y=i))
                if board[j][i] == symbol:
                    move_count += 1
            winning_moves, defensive_moves, regular_moves = self.move_analyze(count=move_count,
                                                                              empty_list=empty_cells,
                                                                              win_list=winning_moves,
                                                                              defense_list=defensive_moves,
                                                                              regular_list=regular_moves)
            empty_cells = []
            move_count = 0
        for i in range(len(board)):
            if board[i][i] == ' ':
                empty_cells.append(Point(x=i, y=i))
            if board[i][i] == symbol:
                move_count += 1
        winning_moves, defensive_moves, regular_moves = self.move_analyze(count=move_count,
                                                                          empty_list=empty_cells,
                                                                          win_list=winning_moves,
                                                                          defense_list=defensive_moves,
                                                                          regular_list=regular_moves)
        empty_cells = []
        move_count = 0
        for i in range(len(board)):
            if board[len(board) - 1 - i][i] == ' ':
                empty_cells.append(Point(x=len(board) - 1 - i, y=i))
            if board[len(board) - 1 - i][i] == symbol:
                move_count += 1
        winning_moves, defensive_moves, regular_moves = self.move_analyze(count=move_count,
                                                                          empty_list=empty_cells,
                                                                          win_list=winning_moves,
                                                                          defense_list=defensive_moves,
                                                                          regular_list=regular_moves)
        print(f"[{self.name}] is thinking...")
        sleep(3)
        if len(winning_moves) > 0:
            move = winning_moves[randint(0, len(winning_moves) - 1)]
            print(f"[{self.name}] is moving: {move.x},{move.y}")
            return self._symbol_class(x=move.x, y=move.y)
        elif len(defensive_moves) > 0:
            move = defensive_moves[randint(0, len(defensive_moves) - 1)]
            print(f"[{self.name}] is moving: {move.x},{move.y}")
            return self._symbol_class(x=move.x, y=move.y)
        else:
            move = regular_moves[randint(0, len(regular_moves) - 1)]
            print(f"[{self.name}] is moving: {move.x},{move.y}")
            return self._symbol_class(x=move.x, y=move.y)

    @staticmethod
    def move_analyze(count, empty_list, win_list, defense_list, regular_list):
        is_exist = False
        if count == 2 and len(empty_list) == 1:
            for empty_item in empty_list:
                for item in win_list:
                    if empty_item.x == item.x and empty_item.y == item.y:
                        is_exist = True
                if not is_exist:
                    win_list.append(empty_item)
                is_exist = False
        elif count == 0 and len(empty_list) == 1:
            for empty_item in empty_list:
                for item in defense_list:
                    if empty_item.x == item.x and empty_item.y == item.y:
                        is_exist = True
                if not is_exist:
                    defense_list.append(empty_item)
                is_exist = False
        else:
            for empty_item in empty_list:
                for item in regular_list:
                    if empty_item.x == item.x and empty_item.y == item.y:
                        is_exist = True
                if not is_exist:
                    regular_list.append(empty_item)
                is_exist = False
        return win_list, defense_list, regular_list
