from random import choice
from tictactoe.game import Game
from tictactoe.player import HumanPlayer, RoboticPlayer
from tictactoe.board import X, O


def get_name_and_symboll_class(quantity_human):
    name_for_robotic = ["George(rob)", "Alexey(rob)", "Teo(rob)", "Mike(rob)",
                        "Gleb(rob)", "Anna(rob)", "Julia(rob)", "Alice(rob)"]
    symbols_list = ["X", "O"]
    players = []
    players_name = []
    symbol = None
    for i in range(2):
        determine_the_class_of_the_player = quantity_human
        if quantity_human != 0:
            name = input("Enter your name: ")
            while name in players_name:
                name = input("Enter your name: ").strip()
            while symbol not in symbols_list:
                symbol = input("Enter symbol(X or O): ")
            players_name.append(name)
            quantity_human -= 1
        else:
            name = choice(name_for_robotic)
            symbol = choice(symbols_list)
        if symbol == "X" and determine_the_class_of_the_player != 0:
            players.append(HumanPlayer(name=name, symbol_class=X))
        elif symbol == "O" and determine_the_class_of_the_player != 0:
            players.append(HumanPlayer(name=name, symbol_class=O))
        elif symbol == "X" and quantity_human == 0:
            players.append(RoboticPlayer(name=name, symbol_class=X))
        elif symbol == "O" and quantity_human == 0:
            players.append(RoboticPlayer(name=name, symbol_class=O))
        try:
            name_for_robotic.remove(name)
        except ValueError:
            pass
        symbols_list.remove(symbol)
    return players


def main_human():
    players = get_name_and_symboll_class(2)
    print_players(players)
    game = Game(players)
    game.run()


def main_robotic():
    players = get_name_and_symboll_class(0)
    print_players(players)
    game = Game(players)
    game.run()


def main_robotic_human():
    players = get_name_and_symboll_class(1)
    print_players(players)
    game = Game(players)
    game.run()


def print_players(players_list):
    for player in players_list:
        print(f"Name: {player.name};     symbol: {player._symbol_class.__name__}")


if __name__ == '__main__':
    # main_human()
    main_robotic()
    # main_robotic_human()
