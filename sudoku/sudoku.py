from random import randint
games = [
    [[0, 3, 0, 8, 1, 0, 0, 6, 0],
    [0, 0, 0, 2, 0, 0, 8, 0, 3],
    [0, 1, 0, 0, 3, 0, 9, 4, 7],
    [0, 0, 0, 0, 5, 0, 0, 7, 0],
    [0, 0, 8, 0, 0, 0, 0, 0, 0],
    [0, 9, 7, 4, 0, 0, 0, 8, 2],
    [0, 7, 0, 0, 2, 3, 1, 0, 0],
    [0, 0, 0, 0, 0, 9, 0, 3, 6],
    [3, 5, 9, 1, 0, 0, 0, 2, 0]],

    [[8, 0, 3, 0, 0, 4, 0, 7, 6],
    [0, 5, 2, 7, 0, 3, 8, 0, 1],
    [6, 0, 0, 0, 0, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 6, 0, 5, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 4, 0, 0],
    [7, 1, 4, 0, 8, 0, 9, 0, 5],
    [0, 3, 0, 9, 0, 1, 0, 0, 4],
    [0, 2, 0, 5, 0, 0, 1, 0, 0]],

    [[0, 3, 9, 0, 0, 8, 0, 0, 0],
    [2, 5, 6, 3, 4, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 7, 6, 0, 2],
    [0, 0, 0, 0, 0, 3, 0, 0, 8],
    [0, 0, 0, 0, 2, 0, 7, 0, 3],
    [0, 2, 0, 8, 9, 5, 1, 6, 0],
    [4, 0, 0, 5, 0, 0, 3, 0, 0],
    [5, 0, 0, 4, 0, 0, 0, 0, 0],
    [0, 7, 2, 0, 0, 6, 0, 0, 5]],

    [[1, 2, 0, 0, 0, 8, 0, 0, 0],
    [8, 0, 3, 0, 5, 0, 1, 0, 0],
    [0, 0, 0, 2, 1, 0, 7, 9, 0],
    [0, 6, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 4, 0, 3, 0, 0, 0, 2],
    [3, 5, 2, 0, 6, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 2, 8, 3, 5],
    [0, 3, 7, 1, 0, 0, 2, 6, 0],
    [2, 0, 0, 3, 0, 6, 0, 0, 1]],

    [[4, 1, 0, 0, 0, 8, 0, 6, 9],
    [0, 6, 3, 4, 0, 0, 5, 0, 0],
    [9, 0, 8, 5, 0, 0, 0, 7, 0],
    [0, 7, 2, 9, 8, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 7, 0, 4, 0],
    [5, 0, 0, 6, 0, 3, 7, 2, 8],
    [0, 5, 0, 8, 0, 0, 0, 9, 4],
    [3, 0, 0, 0, 0, 0, 8, 1, 0],
    [2, 0, 4, 0, 9, 6, 3, 0, 0]]
]


class Sudoku:
    def __init__(self):
        rand_num = randint(0,4)
        self.game_field = games[rand_num]

        self.sec_0 = [
            [0, 0], [0, 1], [0, 2],
            [1, 0], [1, 1], [1, 2],
            [2, 0], [2, 1], [2, 2]
        ]
        # reverse for sec_3
        self.sec_1 = [
            [3, 0], [3, 1], [3, 2],
            [4, 0], [4, 1], [4, 2],
            [5, 0], [5, 1], [5, 2]
        ]

        # reverse for sec_6
        self.sec_2 = [
            [6, 0], [6, 1], [6, 2],
            [7, 0], [7, 1], [7, 2],
            [8, 0], [8, 1], [8, 2]
        ]

        self.sec_3 = [x[::-1] for x in self.sec_1]

        self.sec_4 = [
            [3, 3], [3, 4], [3, 5],
            [4, 3], [4, 4], [4, 5],
            [5, 3], [5, 4], [5, 5]
        ]
        # reverse for sec_7
        self.sec_5 = [
            [6, 3], [7, 4], [8, 5],
            [6, 3], [7, 4], [8, 5],
            [6, 3], [7, 4], [8, 5]
        ]

        self.sec_6 = [x[::-1] for x in self.sec_2]

        self.sec_7 = [x[::-1] for x in self.sec_5]

        self.sec_8 = [
            [6, 6], [6, 7], [6, 8],
            [7, 6], [7, 6], [7, 8],
            [8, 6], [8, 7], [8, 8]
        ]

        self.all_sec = [
            self.sec_0, self.sec_1, self.sec_2, self.sec_3, self.sec_4, self.sec_5, self.sec_6, self.sec_7, self.sec_8
        ]

    def move_is_legal(self, row_num, col_num, move):
        # get section from row_num and col_num
        sec_obj = []
        for sec in self.all_sec:
            if [row_num, col_num] in sec:
                sec_obj = sec

        # check duplicate in row
        for i in range(9):
            if i == col_num:
                continue
            if self.game_field[row_num][i] == move:
                return False

        # check duplicate in column
        for i in range(9):
            if i == row_num:
                continue
            if self.game_field[i][col_num] == move:
                return False

        # check duplicate in section
        for x in sec_obj:
            if x[0] == row_num and x[1] == col_num:
                continue
            elif self.game_field[x[0]][x[1]] == move:
                return False

        return True

    def is_solved(self, game_field):
        for i in range(9):
            for j in range(9):
                if game_field[i][j] == 0:
                    return False
                else:
                    continue

        return True

    def get_empty_field(self):
        for i in range(9):
            for j in range(9):
                if self.game_field[i][j] == 0:
                    return [i, j]
        return False

    def solve_game(self):
        # finds first empty position
        pos = self.get_empty_field()
        # if there is none, game is solved
        if not pos:
            return True

        # try integers until legal move
        for move in range(1, 10):
            if self.move_is_legal(pos[0], pos[1], move):
                self.game_field[pos[0]][pos[1]] = move

                # recursion
                if self.solve_game():
                    return True

                # if no legal move, set field to 0
                self.game_field[pos[0]][pos[1]] = 0

        # the backtrack
        return False





