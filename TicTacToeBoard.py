class TicTacToeBoard:
    def __init__(self):
        self.board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        self.count = 0

    def new_game(self):
        self.board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        self.count = 0

    def get_field(self):
        return self.board

    def check_field(self):
        if self.count % 2 == 0:
            mark = '0'
        else:
            mark = 'X'
        result = None
        if self.board[0][0] == self.board[0][1] == self.board[0][2] == mark or\
                self.board[1][0] == self.board[1][1] == self.board[1][2] == mark or\
                self.board[2][0] == self.board[2][1] == self.board[2][2] == mark or\
                self.board[0][0] == self.board[1][0] == self.board[2][0] == mark or\
                self.board[0][1] == self.board[1][1] == self.board[2][1] == mark or\
                self.board[0][2] == self.board[1][2] == self.board[2][2] == mark or\
                self.board[0][0] == self.board[1][1] == self.board[2][2] == mark or\
                self.board[0][2] == self.board[1][1] == self.board[2][0] == mark:
            result = mark
        elif '-' in self.board:
            result = 'D'
        return result

    def make_move(self, row, col):
        if self.check_field() is None:
            if self.board[row - 1][col - 1] == '-':
                if self.count % 2 == 0:
                    self.board[row - 1][col - 1] = 'X'
                    self.count += 1
                else:
                    self.board[row - 1][col - 1] = '0'
                    self.count += 1
                if self.check_field() is None:
                    message = 'Продолжаем играть'
                else:
                    if self.check_field() == 'D':
                        message = 'Ничья'
                    else:
                        message = f'Победил игрок {self.check_field()}'
            else:
                message = f'Клетка {row}, {col} уже занята'
        else:
            message = 'Игра уже завершена'
        return message


board = TicTacToeBoard()
print(*board.get_field(), sep="\n")
print(board.make_move(1, 1))
print(*board.get_field(), sep="\n")
print(board.make_move(1, 1))
print(board.make_move(1, 2))
print(*board.get_field(), sep="\n")
print(board.make_move(2, 1))
print(board.make_move(2, 2))
print(board.make_move(3, 1))
print(board.make_move(2, 2))
print(*board.get_field(), sep="\n")
