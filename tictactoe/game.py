from tictactoe.board import Board


class Game:
    def __init__(self, player_one, player_two):
        self._board = Board()
        self._player_one = player_one
        self._player_two = player_two

    @property
    def player_one(self):
        return self._player_one

    @property
    def player_two(self):
        return self._player_two

    def run(self):
        player_one = self._player_one
        player_two = self._player_two
        flag = 0
        game = self._board
        while True:
            while True:
                if self.check_progress(player=player_one):
                    break
            print(game)
            if self.check_win():
                print(f"Ура игра окончена выиграл игрок {self._player_one.name} "
                      f"который играет за '{self._player_one.symbol_class.__name__}'")
                break
            if not self.check_draw():
                print("Внимание ничья!!!")
                break
            while True:
                if self.check_progress(player=player_two):
                    break
            print(game)
            if self.check_win():
                print(f"Ура игра окончена выиграл игрок {self._player_two.name} "
                      f"который играет за '{self._player_two.symbol_class.__name__}'")
                break
            if not self.check_draw():
                print("Внимание ничья!!!")
                break

    def validator_move(self, player):
        player = player.move()
        if self._board[player.x][player.y] == "X" or \
                self._board[player.x][player.y] == "O":
            return False
        return True

    def check_progress(self, player):
        counter = player.move()
        if self._board.validator_bord(val=counter):
            self._board.board = counter
            return True
        return False

    def check_win(self):
        line1 = self._board.board[0][0] == self._board.board[0][1] == self._board.board[0][2] == "X" or \
                self._board.board[0][0] == self._board.board[0][1] == self._board.board[0][2] == "O"
        line2 = self._board.board[1][0] == self._board.board[1][1] == self._board.board[1][2] == "X" or \
                self._board.board[1][0] == self._board.board[1][1] == self._board.board[1][2] == "O"
        line3 = self._board.board[2][0] == self._board.board[2][1] == self._board.board[2][2] == "X" or \
                self._board.board[2][0] == self._board.board[2][1] == self._board.board[2][2] == "O"
        columns1 = self._board.board[0][0] == self._board.board[1][0] == self._board.board[2][0] == "X" or \
                   self._board.board[0][0] == self._board.board[1][0] == self._board.board[2][0] == "O"
        columns2 = self._board.board[0][1] == self._board.board[1][1] == self._board.board[2][1] == "X" or \
                   self._board.board[0][1] == self._board.board[1][1] == self._board.board[2][1] == "O"
        columns3 = self._board.board[0][2] == self._board.board[1][2] == self._board.board[2][2] == "X" or \
                   self._board.board[0][2] == self._board.board[1][2] == self._board.board[2][2] == "O"
        diagonal_main = self._board.board[0][0] == self._board.board[1][1] == self._board.board[2][2] == "X" or \
                        self._board.board[0][0] == self._board.board[1][1] == self._board.board[2][2] == "O"
        diagonal_collateral = self._board.board[0][2] == self._board.board[1][1] == self._board.board[2][0] == "X" or \
                              self._board.board[0][2] == self._board.board[1][1] == self._board.board[2][0] == "O"
        winning_combinations = [
            line1, line2, line3, columns1, columns2, columns3, diagonal_main, diagonal_collateral]
        for win in winning_combinations:
            if win:
                return win
        return False

    def check_draw(self):
        for i in range(0, 3):
            for j in range(0, 3):
                if self._board.board[i][j] == ' ':
                    return True
        return False
