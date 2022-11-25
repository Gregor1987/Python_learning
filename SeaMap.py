class SeaMap:

    def __init__(self):
        self.board = [['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                      ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                      ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                      ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                      ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                      ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                      ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                      ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                      ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                      ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']]

    def cell(self, row, col):
        return self.board[row][col]

    def sink(self, row, col):
        if 9 > row > 0 and 9 > col > 0:
            if self.board[row][col] == 'x':
                if self.board[row - 1][col - 1] == '.':
                    self.board[row - 1][col - 1] = '*'
                if self.board[row - 1][col] == '.':
                    self.board[row - 1][col] = '*'
                if self.board[row - 1][col + 1] == '.':
                    self.board[row - 1][col + 1] = '*'
                if self.board[row][col + 1] == '.':
                    self.board[row][col + 1] = '*'
                if self.board[row + 1][col + 1] == '.':
                    self.board[row + 1][col + 1] = '*'
                if self.board[row + 1][col] == '.':
                    self.board[row + 1][col] = '*'
                if self.board[row + 1][col - 1] == '.':
                    self.board[row + 1][col - 1] = '*'
                if self.board[row][col - 1] == '.':
                    self.board[row][col - 1] = '*'
                if self.board[row][col - 1] == 'x':
                    self.sink(row, col - 1)
                if self.board[row + 1][col] == 'x':
                    self.sink(row + 1, col)
                if self.board[row][col + 1] == 'x':
                    self.sink(row, col + 1)
                if self.board[row - 1][col] == 'x':
                    self.sink(row - 1, col)
        if 9 > row > 0 and col == 0:
            if self.board[row][col] == 'x':
                if self.board[row - 1][col] == '.':
                    self.board[row - 1][col] = '*'
                if self.board[row - 1][col + 1] == '.':
                    self.board[row - 1][col + 1] = '*'
                if self.board[row][col + 1] == '.':
                    self.board[row][col + 1] = '*'
                if self.board[row + 1][col + 1] == '.':
                    self.board[row + 1][col + 1] = '*'
                if self.board[row][col + 1] == '.':
                    self.board[row][col + 1] = '*'
                if self.board[row + 1][col] == 'x':
                    self.sink(row + 1, col)
                if self.board[row][col + 1] == 'x':
                    self.sink(row, col + 1)
                if self.board[row - 1][col] == 'x':
                    self.sink(row - 1, col)
        if row == 0 and 9 > col > 0:
            if self.board[row][col] == 'x':
                if self.board[row][col + 1] == '.':
                    self.board[row][col + 1] = '*'
                if self.board[row + 1][col + 1] == '.':
                    self.board[row + 1][col + 1] = '*'
                if self.board[row + 1][col] == '.':
                    self.board[row + 1][col] = '*'
                if self.board[row + 1][col - 1] == '.':
                    self.board[row + 1][col - 1] = '*'
                if self.board[row][col - 1] == '.':
                    self.board[row][col - 1] = '*'
                if self.board[row][col - 1] == 'x':
                    self.sink(row, col - 1)
                if self.board[row + 1][col] == 'x':
                    self.sink(row + 1, col)
                if self.board[row][col + 1] == 'x':
                    self.sink(row, col + 1)
        elif row == 0 and col == 0:
            if self.board[row][col] == 'x':
                if self.board[row][col + 1] == '.':
                    self.board[row][col + 1] = '*'
                if self.board[row + 1][col + 1] == '.':
                    self.board[row + 1][col + 1] = '*'
                if self.board[row + 1][col] == '.':
                    self.board[row + 1][col] = '*'
                if self.board[row + 1][col] == 'x':
                    self.sink(row + 1, col)
                if self.board[row][col + 1] == 'x':
                    self.sink(row, col + 1)
        elif row == 9 and col == 9:
            if self.board[row][col] == 'x':
                if self.board[row - 1][col - 1] == '.':
                    self.board[row - 1][col - 1] = '*'
                if self.board[row - 1][col] == '.':
                    self.board[row - 1][col] = '*'
                if self.board[row][col - 1] == '.':
                    self.board[row][col - 1] = '*'
                if self.board[row][col - 1] == 'x':
                    self.sink(row, col - 1)
                if self.board[row - 1][col] == 'x':
                    self.sink(row - 1, col)
        elif row == 9 and 0 < col < 9:
            if self.board[row][col] == 'x':
                if self.board[row - 1][col - 1] == '.':
                    self.board[row - 1][col - 1] = '*'
                if self.board[row - 1][col] == '.':
                    self.board[row - 1][col] = '*'
                if self.board[row - 1][col + 1] == '.':
                    self.board[row - 1][col + 1] = '*'
                if self.board[row][col + 1] == '.':
                    self.board[row][col + 1] = '*'
                if self.board[row][col - 1] == '.':
                    self.board[row][col - 1] = '*'
                if self.board[row][col - 1] == 'x':
                    self.sink(row, col - 1)
                if self.board[row][col + 1] == 'x':
                    self.sink(row, col + 1)
                if self.board[row - 1][col] == 'x':
                    self.sink(row - 1, col)
        elif 0 < row < 9 and col == 9:
            if self.board[row][col] == 'x':
                if self.board[row - 1][col - 1] == '.':
                    self.board[row - 1][col - 1] = '*'
                if self.board[row - 1][col] == '.':
                    self.board[row - 1][col] = '*'
                if self.board[row + 1][col] == '.':
                    self.board[row + 1][col] = '*'
                if self.board[row + 1][col - 1] == '.':
                    self.board[row + 1][col - 1] = '*'
                if self.board[row][col - 1] == '.':
                    self.board[row][col - 1] = '*'
                if self.board[row + 1][col] == 'x':
                    self.sink(row + 1, col)
                if self.board[row + 1][col] == 'x':
                    self.sink(row + 1, col)
                if self.board[row + 1][col] == 'x':
                    self.sink(row - 1, col)

    def shoot(self, row, col, result):
        if result == 'miss':
            self.board[row][col] = '*'
        elif result == 'hit':
            self.board[row][col] = 'x'
        elif result == 'sink':
            self.board[row][col] = 'x'
            self.sink(row, col)


sm = SeaMap()
sm.shoot(9, 8, 'hit')
sm.shoot(9, 9, 'sink')
for row in range(10):
    for col in range(10):
        print(sm.cell(row, col), end='')
    print()
