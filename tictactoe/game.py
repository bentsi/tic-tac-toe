from tictactoe.board import Board
from itertools import cycle
from time import sleep


class Game:
    def __init__(self, players):
        self._board = Board()
        self._players = players

    @property
    def board(self):
        return self._board

    @board.setter
    def board(self, val):
        self._board = val

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

    def print_score(self):
        print("\nThe score of the game")
        print(self._players[0].name, "---", self._players[0].win)
        print(self._players[1].name, "---", self._players[1].win)

    def run(self):
        for player in cycle(self._players):
            ok = True
            if player.__class__.__name__ == "HumanPlayer":
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
            else:
                sleep(1)
                move = player.move()
                while self._board.board[int(move.x)][int(move.y)] != " ":
                    move = player.move()
                self._board.board = move
                print(f"{player.name} went to the coordinates({move.x}, {move.y})")
            print(self._board)
            win, drawn = self._check()
            if win:
                if drawn:
                    print("Drawn")
                else:
                    print(f"{player.name} win")
                    print()
                    player.win += 1
                self.print_score()
                play_again = input("\nAgain?(yes or no)")
                while play_again != "yes" and play_again != "no":
                    play_again = input("Again?(yes or no)")
                if play_again == "yes":
                    self.board = Board()
                    self.run()
                break

