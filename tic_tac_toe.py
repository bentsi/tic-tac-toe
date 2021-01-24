from tictactoe.game import Game
from tictactoe.player import HumanPlayer, RoboticPlayer
from tictactoe.board import X, O


def main_human(name_x, name_o):
    game = Game(players=[
        HumanPlayer(name=name_x, symbol_class=X),
        HumanPlayer(name=name_o, symbol_class=O),
    ])
    game.run()


def main_robotic_human(name, symbol):
    if symbol.upper() == 'X':
        game = Game(players=[HumanPlayer(name=name, symbol_class=X),
                             RoboticPlayer(name="Robot", symbol_class=O)])
    else:
        game = Game(players=[RoboticPlayer(name="Robot", symbol_class=X),
                             HumanPlayer(name=name, symbol_class=O)])
    game.run()


def main_robotic():
    game = Game(players=[
        RoboticPlayer(name="Robot1", symbol_class=X),
        RoboticPlayer(name="Robot2", symbol_class=O),
    ])
    game.run()


if __name__ == '__main__':
    mode = -1
    while mode != 0:
        print("1 - Player vs Player", "2 - Player vs Robot", "3 - Robot vs Robot", "0 - Exit", sep='\n')
        mode = int(input("Select mode: "))
        print()
        if mode == 1:
            print("\"X\" goes first!")
            player1 = input("Enter the name of \"X\" player: ")
            player2 = input("Enter the name of \"O\" player: ")
            main_human(name_x=player1, name_o=player2)
        if mode == 2:
            print("\"X\" goes first!")
            mark = input("Choose your mark (\"X\" or \"O\"): ")
            player = input("Enter your name: ")
            main_robotic_human(name=player, symbol=mark)
        if mode == 3:
            main_robotic()
        print()
