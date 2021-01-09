from tictactoe.game import Game
from tictactoe.player import HumanPlayer, RoboticPlayer
from tictactoe.board import X, O
import random


def choice():
    while True:
        choice_value = int(input("Введите Ваш выбор > "))
        if choice_value == -1:
            return -1
        try:
            if (choice_value < 1) or (choice_value > 4):
                raise Exception("Разрешенный диапазон данных от 1 до 4, -1 для выхода")
        except Exception:
            print("Разрешенный диапазон данных от 1 до 4, -1 для выхода")
        else:
            return choice_value


def definition_symbol_class():
    symbol_1 = random.choice([X, O])
    if symbol_1 == X:
        return X, O
    else:
        return O, X


def main():
    player_first = ''
    player_second = ''
    print("Меню".center(32, '*'))
    print("1. знакомится с правилами игры")
    print("2. Играть с другим человеком")
    print("3. Играть с роботом")
    print("4. посмотреть игру двух роботов")
    print("5. Для выхода из программы нажмите '-1' ")
    while True:
        choice_you = choice()
        if choice_you == 1:
            with open("tictactoe/rules_of_the_game", "r", encoding='utf-8') as file:
                rules_the_game = file.read()
                print(rules_the_game)
                return 0
        elif choice_you == 2:
            player_first, player_second = main_human()
        elif choice_you == -1:
            return 0
        elif choice_you == 3:
            player_first, player_second = main_robotic_human()
        elif choice_you == 4:
            player_first, player_second = main_robotic()
        game = Game(player_one=player_first, player_two=player_second)
        game.run()


def main_human():
    class_symbol_1, class_symbol_2 = definition_symbol_class()
    name_first_player = input("Введите имя первого игрока:> ")
    name_second_player = input("Введите имя второго игрока:> ")
    print(f"Первый игрок {name_first_player} играет {class_symbol_1.__name__}")
    print(f"Второй игрок {name_second_player} играет {class_symbol_2.__name__}")
    player_first = HumanPlayer(name=name_first_player, symbol_class=class_symbol_1)
    player_second = HumanPlayer(name=name_second_player, symbol_class=class_symbol_2)
    return player_first, player_second


def main_robotic():
    class_symbol_1, class_symbol_2 = definition_symbol_class()
    player_first = RoboticPlayer(symbol_class=class_symbol_1)
    player_second = RoboticPlayer(symbol_class=class_symbol_2)
    print(f"Первый игрок {player_first.name} играет {class_symbol_1.__name__}")
    print(f"Первый игрок {player_second.name} играет {class_symbol_2.__name__}")
    return player_first, player_second


def main_robotic_human():
    class_symbol_1, class_symbol_2 = definition_symbol_class()
    name_first_player = input("Введите имя первого игрока:> ")
    player_second = RoboticPlayer(symbol_class=class_symbol_2)
    print(f"Первый игрок {name_first_player} играет {class_symbol_1.__name__}")
    print(f"Первый игрок {player_second.name} играет {class_symbol_2.__name__}")
    player_first = HumanPlayer(name=name_first_player, symbol_class=class_symbol_1)
    return player_first, player_second


if __name__ == '__main__':
    main()
