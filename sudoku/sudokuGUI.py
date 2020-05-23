import pygame
from time import sleep, time
import datetime
import sudoku
pygame.init()
pygame.display.set_caption("Sudoku Solver")
pygame.font.init()

global gap
gap = 5


#######################################################################################################################

class Board:
    def __init__(self, window, width, height, game):
        self.initial_board = game.game_field
        # amount of rows and cols
        self.row_num = 9
        self.col_num = 9
        # window created in main()
        self.window = window
        # dimensions of the board(not of the window!!)
        self.width = width
        self.height = height
        # sets array of permanent values
        self.num_spaces = []
        for i in range(self.row_num):
            for j in range(self.col_num):
                self.num_spaces.append(NumSpace(i, j, self.width, self.height, self.initial_board[i][j]))
        # free squares in the board
        self.free_sqr = []
        self.draw_grid()
        self.draw_button(False, False)

    def play(self, game):
        self.initial_board = game.game_field
        self.draw_num(self.window)

    def draw_grid(self):
        line_dist = self.height / 9
        # drawing the grid
        for i in range(self.row_num + 1):
            if i % 3 == 0:
                pygame.draw.line(self.window, (0, 0, 0), (0 + gap, i * line_dist + gap),
                                 (self.width + gap, i * line_dist + gap), 4)  # horizontal
                pygame.draw.line(self.window, (0, 0, 0), (i * line_dist + gap, 0 + gap),
                                 (i * line_dist + gap, self.height + gap), 4)  # vertical
            else:
                pygame.draw.line(self.window, (0, 0, 0), (0 + gap, i * line_dist + gap),
                                 (self.width + gap, i * line_dist + gap), 1)  # horizontal
                pygame.draw.line(self.window, (0, 0, 0), (i * line_dist + gap, 0 + gap),
                                 (i * line_dist + gap, self.height + gap), 1)  # vertical

    def draw_button(self, sel_1, sel_2):
        if sel_1:
            pygame.draw.rect(self.window, (0, 248, 0), pygame.Rect(620, 20, 120, 40))
            font = pygame.font.SysFont('Arial', 30, bold=True)
            txt = font.render('Play', False, (0, 0, 0))
            self.window.blit(txt, (647, 23))
        else:
            pygame.draw.rect(self.window, (132, 248, 0), pygame.Rect(620, 20, 120, 40))
            font = pygame.font.SysFont('Arial', 30, bold=True)
            txt = font.render('Play', False, (0, 0, 0))
            self.window.blit(txt, (647, 23))

        if sel_2:
            pygame.draw.rect(self.window, (0, 248, 0), pygame.Rect(620, 100, 120, 40))
            font = pygame.font.SysFont('Arial', 30, bold=True)
            txt = font.render('Solve', False, (0, 0, 0))
            self.window.blit(txt, (640, 103))
        else:
            pygame.draw.rect(self.window, (132, 248, 0), pygame.Rect(620, 100, 120, 40))
            font = pygame.font.SysFont('Arial', 30, bold=True)
            txt = font.render('Solve', False, (0, 0, 0))
            self.window.blit(txt, (640, 103))

    def draw_num(self, window):
        for i in range(len(self.num_spaces)):
            if self.num_spaces[i].value:
                self.num_spaces[i].draw(self.window)  # draw from the NumSpace class
            else:
                self.free_sqr.append([pygame.Rect(self.num_spaces[i].col * self.num_spaces[i].width / 9 + 2 * gap,
                                                  self.num_spaces[i].row * self.num_spaces[i].height / 9 + 2 * gap,
                                                  self.width / 9 - 2 * gap, self.height / 9 - 2 * gap),
                                      self.num_spaces[i].row, self.num_spaces[i].col, False])

        for sqr in self.free_sqr:
            pygame.draw.rect(window, (255, 255, 255), sqr[0])

    def clear_board(self, window):
        for row in range(9):
            for col in range(9):
                pygame.draw.rect(window, (255, 255, 255), pygame.Rect(col * self.width / 9 + 2 * gap,
                                                                      row * self.height / 9 + 2 * gap,
                                                                      self.width / 9 - 2 * gap,
                                                                      self.height / 9 - 2 * gap))

    def draw_temp(self, window, key, is_temp):
        font = pygame.font.SysFont('Arial', 30)
        xy_centering = [self.width / 21 + gap, self.height / 35 + gap]
        # draws temporary value, else white square
        for sqr in self.free_sqr:
            if sqr[3] and is_temp and key:
                pygame.draw.rect(window, (255, 255, 255), sqr[0])
                txt = font.render(str(key), False, (0, 0, 255))
                window.blit(txt,
                            (sqr[0].left + xy_centering[0], sqr[0].top + xy_centering[1]))
                break
            elif self.initial_board[sqr[1]][sqr[2]] == 0:
                pygame.draw.rect(window, (255, 255, 255), sqr[0])

    def solve(self, game):
        game.solve_game()
        self.num_spaces = []
        for i in range(self.row_num):
            for j in range(self.col_num):
                self.num_spaces.append(NumSpace(i, j, self.width, self.height, self.initial_board[i][j]))
        for i in range(len(self.num_spaces)):
            sleep(0.02)
            self.num_spaces[i].draw(self.window)
            pygame.display.update()


########################################################################################################################


class NumSpace:
    def __init__(self, row, col, width, height, value):
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.value = value

    def draw(self, window):
        font = pygame.font.SysFont('Arial', 30)
        xy_centering = [self.width / 21 + gap, self.height / 35 + gap]
        # add permanent values
        if self.value != 0:
            txt = font.render(str(self.value), False, (0, 0, 0))
            window.blit(txt,
                        (self.col * self.width / 9 + xy_centering[0], self.row * self.height / 9 + xy_centering[1]))


########################################################################################################################
def draw_timer(window, timer, timer_running):
    font = pygame.font.SysFont('Arial', 30, bold=True)
    timer = datetime.timedelta(seconds=timer)
    if timer_running:
        pygame.draw.rect(window, (255, 255, 255), pygame.Rect(620, 600, 300, 200))
        txt = font.render(str(timer), False, (0, 0, 0))
        window.blit(txt, (625, 640))


def make_move(row, col, move, game, board, window, sqr):
    if game.move_is_legal(row, col, move):
        pygame.draw.rect(window, (255, 255, 255), sqr[0])
        board.initial_board[row][col] = move
        font = pygame.font.SysFont('Arial', 30)
        xy_centering = [board.width / 21 + gap, board.height / 35 + gap]
        if board.initial_board[row][col] != 0:
            txt = font.render(str(board.initial_board[row][col]), False, (0, 0, 0))
            window.blit(txt,
                        (col * board.width / 9 + xy_centering[0], row * board.height / 9 + xy_centering[1]))
    else:
        pygame.draw.rect(window, (255, 255, 255), sqr[0])


def main():
    sudoku_game = sudoku.Sudoku()
    window = pygame.display.set_mode((750, 700))
    window.fill((255, 255, 255))
    board = Board(window, 600, 600, sudoku_game)
    pygame.display.flip()
    beg_time = 0
    running = True
    playing = False
    key = 0
    while running:
        timer = round(time() - beg_time)
        if playing and not sudoku_game.is_solved(board.initial_board):
            draw_timer(window, timer, True)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    key = 0
                if event.key == pygame.K_1:
                    key = 1
                if event.key == pygame.K_2:
                    key = 2
                if event.key == pygame.K_3:
                    key = 3
                if event.key == pygame.K_4:
                    key = 4
                if event.key == pygame.K_5:
                    key = 5
                if event.key == pygame.K_6:
                    key = 6
                if event.key == pygame.K_7:
                    key = 7
                if event.key == pygame.K_8:
                    key = 8
                if event.key == pygame.K_9:
                    key = 9
                if event.key == pygame.K_DELETE:
                    key = 0
                    board.draw_temp(board.window, key, False)
                    for sqr in board.free_sqr:
                        if sqr[3]:
                            make_move(sqr[1], sqr[2], key, sudoku_game, board, window, sqr)
                            sudoku_game.game_field[sqr[1]][sqr[2]] = key

                board.draw_temp(board.window, key, True)

                if event.key == pygame.K_RETURN:
                    board.draw_temp(board.window, key, False)
                    for sqr in board.free_sqr:
                        if sqr[3]:
                            make_move(sqr[1], sqr[2], key, sudoku_game, board, window, sqr)
                            if sudoku_game.move_is_legal(sqr[1], sqr[2], key):
                                sudoku_game.game_field[sqr[1]][sqr[2]] = key

            if event.type == pygame.MOUSEBUTTONDOWN:
                m_pos = pygame.mouse.get_pos()

                # solve button
                if 620 < m_pos[0] < 740 and 100 < m_pos[1] < 140:
                    board.draw_button(False, True)
                    pygame.display.update()
                    sleep(0.07)
                    board.draw_button(False, False)
                    pygame.display.update()
                    board.solve(sudoku_game)
                # play button
                elif 620 < m_pos[0] < 740 and 20 < m_pos[1] < 60:
                    board.clear_board(window)
                    board.draw_button(True, False)
                    sleep(0.07)
                    board.draw_button(False, False)
                    pygame.display.update()
                    sudoku_game = sudoku.Sudoku()
                    beg_time = time()
                    playing = True
                    draw_timer(window, timer, playing)
                    board = Board(window, 600, 600, sudoku_game)
                    board.play(sudoku_game)

                else:
                    key = 0
                    for sqr in board.free_sqr:
                        if sqr[0].collidepoint(m_pos):
                            pygame.draw.circle(window, (0, 255, 0), (sqr[0].left + 5, sqr[0].top + 5), 5)
                            sqr[3] = True
                        else:
                            pygame.draw.circle(window, (255, 255, 255), (sqr[0].left + 5, sqr[0].top + 5), 5)
                            sqr[3] = False

        pygame.display.update()


main()
