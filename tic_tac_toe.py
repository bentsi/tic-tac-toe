from tictactoe.game import Game
from tictactoe.player import HumanPlayer, RoboticPlayer
from tictactoe.board import X, O


def main_human():
    game = Game(players=[
        HumanPlayer(name="Julia", symbol_class=X),
        HumanPlayer(name="Valera", symbol_class=O),
    ])
    game.game_run()

def main_robotic():
    """Robot plays with Robot"""
    game = Game(players=[
        RoboticPlayer(name="ROBOT_1", symbol_class=X),
        RoboticPlayer(name="ROBOT_2", symbol_class=O),
    ])
    game.game_run()


def main_robotic_human():
    """Robot plays with Human"""
    game = Game(players=[
        RoboticPlayer(name="ROBOT", symbol_class=X),
        HumanPlayer(name="Julia", symbol_class=O),
    ])
    game.game_run()

if __name__ == '__main__':
    # main_human()
    # main_robotic()
    main_robotic_human()
