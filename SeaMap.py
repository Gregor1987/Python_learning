class SeaMap:

    def __init__(self):
        self.board = []
        for i in range(10):
            i = []
            self.board.append(i)
            for _ in range(10):
                i.append('.')
        self.hidden_board = []  # второе поле используется в методе around_sink_mark, чтобы код не ушел в бесконечный цикл
        for i in range(10):
            i = []
            self.hidden_board.append(i)
            for _ in range(10):
                i.append('.')

    def cell(self, row, col):
        return self.board[row][col]

    def mark(self, row, col):
        if self.board[row][col] == '.':
            self.board[row][col] = '*'

    def around_sink_mark(self, row, col):  # метод для проставления "*" вокруг потопленных кораблей
        if 0 < row < 9 and 0 < col < 9:
            if self.board[row][col] == 'x' and self.hidden_board[row][col] != 'x':
                self.hidden_board[row][col] = 'x'
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        self.mark(row + i, col + j)
                if self.board[row][col - 1] == 'x':
                    self.around_sink_mark(row, col - 1)
                if self.board[row + 1][col] == 'x':
                    self.around_sink_mark(row + 1, col)
                if self.board[row][col + 1] == 'x':
                    self.around_sink_mark(row, col + 1)
                if self.board[row - 1][col] == 'x':
                    self.around_sink_mark(row - 1, col)
        elif 0 < row < 9 and col == 0:
            if self.board[row][col] == 'x' and self.hidden_board[row][col] != 'x':
                self.hidden_board[row][col] = 'x'
                for i in range(-1, 2):
                    for j in range(2):
                        self.mark(row + i, col + j)
                if self.board[row + 1][col] == 'x':
                    self.around_sink_mark(row + 1, col)
                if self.board[row][col + 1] == 'x':
                    self.around_sink_mark(row, col + 1)
                if self.board[row - 1][col] == 'x':
                    self.around_sink_mark(row - 1, col)
        elif row == 0 and 0 < col < 9:
            if self.board[row][col] == 'x' and self.hidden_board[row][col] != 'x':
                self.hidden_board[row][col] = 'x'
                for i in range(2):
                    for j in range(-1, 2):
                        self.mark(row + i, col + j)
                if self.board[row][col - 1] == 'x':
                    self.around_sink_mark(row, col - 1)
                if self.board[row + 1][col] == 'x':
                    self.around_sink_mark(row + 1, col)
                if self.board[row][col + 1] == 'x':
                    self.around_sink_mark(row, col + 1)
        elif row == 9 and 0 < col < 9:
            if self.board[row][col] == 'x' and self.hidden_board[row][col] != 'x':
                self.hidden_board[row][col] = 'x'
                for i in range(2):
                    for j in range(-1, 2):
                        self.mark(row - i, col + j)
                if self.board[row][col - 1] == 'x':
                    self.around_sink_mark(row, col - 1)
                if self.board[row][col + 1] == 'x':
                    self.around_sink_mark(row, col + 1)
                if self.board[row - 1][col] == 'x':
                    self.around_sink_mark(row - 1, col)
        elif 0 < row < 9 and col == 9:
            if self.board[row][col] == 'x' and self.hidden_board[row][col] != 'x':
                self.hidden_board[row][col] = 'x'
                for i in range(-1, 2):
                    for j in range(2):
                        self.mark(row + i, col - j)
                if self.board[row + 1][col] == 'x':
                    self.around_sink_mark(row + 1, col)
                if self.board[row + 1][col] == 'x':
                    self.around_sink_mark(row + 1, col)
                if self.board[row + 1][col] == 'x':
                    self.around_sink_mark(row - 1, col)
        elif row == 0 and col == 0:
            if self.board[row][col] == 'x' and self.hidden_board[row][col] != 'x':
                self.hidden_board[row][col] = 'x'
                for i in range(2):
                    for j in range(2):
                        self.mark(row + i, col + j)
                if self.board[row + 1][col] == 'x':
                    self.around_sink_mark(row + 1, col)
                if self.board[row][col + 1] == 'x':
                    self.around_sink_mark(row, col + 1)
        elif row == 9 and col == 9:
            if self.board[row][col] == 'x' and self.hidden_board[row][col] != 'x':
                self.hidden_board[row][col] = 'x'
                for i in range(2):
                    for j in range(2):
                        self.mark(row - i, col - j)
                if self.board[row][col - 1] == 'x':
                    self.around_sink_mark(row, col - 1)
                if self.board[row - 1][col] == 'x':
                    self.around_sink_mark(row - 1, col)
        elif row == 0 and col == 9:
            if self.board[row][col] == 'x' and self.hidden_board[row][col] != 'x':
                self.hidden_board[row][col] = 'x'
                for i in range(2):
                    for j in range(2):
                        self.mark(row + i, col - j)
            if self.board[row][col - 1] == 'x':
                self.around_sink_mark(row, col - 1)
            if self.board[row - 1][col] == 'x':
                self.around_sink_mark(row - 1, col)
        elif row == 9 and col == 0:
            if self.board[row][col] == 'x' and self.hidden_board[row][col] != 'x':
                self.hidden_board[row][col] = 'x'
                for i in range(2):
                    for j in range(2):
                        self.mark(row - i, col + j)
            if self.board[row][col - 1] == 'x':
                self.around_sink_mark(row, col - 1)
            if self.board[row - 1][col] == 'x':
                self.around_sink_mark(row - 1, col)

    def shoot(self, row, col, result):
        if result == 'miss':
            self.board[row][col] = '*'
        elif result == 'hit':
            self.board[row][col] = 'x'
        elif result == 'sink':
            self.board[row][col] = 'x'
            self.around_sink_mark(row, col)


sm = SeaMap()
sm.shoot(2, 0, 'miss')
sm.shoot(6, 9, 'miss')
for row in range(10):
    for col in range(10):
        print(sm.cell(row, col), end='')
    print()
print()
sm_2 = SeaMap()
sm_2.shoot(2, 0, 'sink')
sm_2.shoot(6, 9, 'hit')
for row in range(10):
    for col in range(10):
        print(sm_2.cell(row, col), end='')
    print()
print()
sm_3 = SeaMap()
sm_3.shoot(0, 0, 'sink')
sm_3.shoot(0, 9, 'sink')
sm_3.shoot(9, 0, 'sink')
sm_3.shoot(9, 9, 'sink')
for row in range(10):
    for col in range(10):
        print(sm_3.cell(row, col), end='')
    print()
