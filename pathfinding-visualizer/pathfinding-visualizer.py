import pygame
import time
import queue
pygame.init()
pygame.display.set_caption("Pathfinding Visualizer")

global gap
gap = 0.5


class Grid:
    def __init__(self, window, rows, cols, width, height):
        self.window = window
        self.rows = rows
        self.cols = cols
        self.width = width
        self.height = height
        self.nodes = []
        for row in range(self.rows):
            for col in range(self.cols):
                self.nodes.append(
                    [pygame.Rect(col * self.height / self.cols + gap, row * self.width / self.rows + gap,
                                 self.width / self.rows - gap, self.height / self.cols - gap),
                     Node(row, col, False, False, False), row, col])

    def draw_grid(self):
        for node in self.nodes:
            if node[1].start:
                pygame.draw.rect(self.window, (0, 0, 255), node[0])
            elif node[1].end:
                pygame.draw.rect(self.window, (255, 0, 0), node[0])
            elif node[1].vis and not node[1].wall:
                pygame.draw.rect(self.window, (0, 255, 255), node[0])
            elif node[1].wall:
                pygame.draw.rect(self.window, (255, 255, 255), node[0])
            else:
                pygame.draw.rect(self.window, (0, 0, 0), node[0])
        pygame.display.update()

    def get_start(self):
        for node in self.nodes:
            if node[1].start:
                return node
        return None

    def get_end(self):
        for node in self.nodes:
            if node[1].end:
                return node
        return None

    def get_node(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            for node in self.nodes:
                if node[1].row == row and node[1].col == col:
                    return node

    def unvisit_all(self):
        for node in self.nodes:
            if not node[1].start:
                node[1].dist = 100000
                node[1].pre = None
                node[1].g_cost = 100000
                node[1].h_cost = 100000
                node[1].f_val = node[1].g_cost + node[1].h_cost
            node[1].vis = False

    def get_neighbours(self, my_node):
        neighbours = []
        (neighbours.append(self.get_node(my_node.row - 1, my_node.col)) if
         self.get_node(my_node.row - 1, my_node.col) is not None else None)
        (neighbours.append(self.get_node(my_node.row + 1, my_node.col)) if
         self.get_node(my_node.row + 1, my_node.col) is not None else None)
        (neighbours.append(self.get_node(my_node.row, my_node.col - 1)) if
         self.get_node(my_node.row, my_node.col - 1) is not None else None)
        (neighbours.append(self.get_node(my_node.row, my_node.col + 1)) if
         self.get_node(my_node.row, my_node.col + 1) is not None else None)

        return neighbours

    @staticmethod
    def update_distance(prev_node, node):
        new_dist = prev_node.dist + 1
        if new_dist < node[1].dist:
            node[1].dist = new_dist
            node[1].pre = prev_node

    def get_shortest_path(self, my_node, path):
        if not my_node[1].start:
            path.append(my_node)
            pre_row = my_node[1].pre.row
            pre_col = my_node[1].pre.col
            for node in self.nodes:
                if node[1].row == pre_row and node[1].col == pre_col:
                    pre_node = node
                    self.get_shortest_path(pre_node, path)
        return path

    def draw_shortest_path(self, path):
        for node in path:
            if not node[1].end:
                pygame.draw.rect(self.window, (255, 255, 0), node[0])
                time.sleep(0.02)
                pygame.display.update()


########################################################################################################################


class Node:
    def __init__(self, row, col, vis, start, end):
        self.row = row
        self.col = col
        self.dist = 100000  # distance to start node (dijksrtra)
        self.vis = vis  # visited (True, False)
        self.start = start  # True, False
        self.end = end  # True, False
        self.wall = False
        self.pre = None  # predecessor
        self.g_cost = 100000 # distance from start node (a-star)
        self.h_cost = 100000 # shortest distance to end node (a-star)
        self.f_val = self.g_cost + self.h_cost


########################################################################################################################


def dijkstra(grid):

    def get_next_node():
        next_node = None
        dist = 1000
        for node in grid.nodes:
            if not node[1].vis and node[1].dist < dist:
                dist = node[1].dist
                next_node = node
        return next_node

    if grid.get_start() is not None and grid.get_end() is not None:
        shortest_path = []
        while True:
            my_node = get_next_node()[1]
            my_node.vis = True
            if my_node.end:
                break
            if my_node.wall:
                continue

            neighbours = grid.get_neighbours(my_node)

            for neighbour in neighbours:
                if not neighbour[1].vis:
                    grid.update_distance(my_node, neighbour)

            grid.draw_grid()

        grid.draw_shortest_path(grid.get_shortest_path(grid.get_end(), shortest_path))


def a_star(grid):

    def get_next_node():
        next_node = None
        f_val = 100
        for node in open_lis:
            if not node[1].vis and node[1].f_val <= f_val:
                f_val = node[1].f_val
                next_node = node
        return next_node

    start_node = grid.get_start()
    end_node = grid.get_end()
    open_lis = [start_node]
    closed_lis = []
    shortest_path = []
    while True:
        my_node = get_next_node()
        my_node[1].vis = True
        if my_node == end_node:
            break
        if my_node[1].wall:
            continue

        for obj in open_lis:
            if obj[1].row == my_node[1].row and obj[1].col == my_node[1].col:
                open_lis.remove(obj)
        closed_lis.append(my_node)

        neighbours = grid.get_neighbours(my_node[1])

        for neighbour in neighbours:
            new_g_cost = my_node[1].g_cost + 1
            if new_g_cost < neighbour[1].g_cost:
                neighbour[1].pre = my_node[1]
                neighbour[1].g_cost = new_g_cost
                neighbour[1].h_cost = (abs(neighbour[1].row - end_node[1].row) + abs(neighbour[1].col - end_node[1].col))
                neighbour[1].f_val = neighbour[1].g_cost + neighbour[1].h_cost
                if neighbour not in closed_lis:
                    open_lis.append(neighbour)

        grid.draw_grid()

    grid.draw_shortest_path(grid.get_shortest_path(grid.get_end(), shortest_path))


def breadth_first(grid):
    if grid.get_start() is not None and grid.get_end() is not None:
        node_queue = queue.Queue()
        start_node = grid.get_start()
        end_node = grid.get_end()
        node_queue.put(start_node)
        shortest_path = []
        while True:
            my_node = node_queue.get()[1]
            my_node.vis = True
            if my_node.end:
                break
            if my_node.wall:
                continue

            neighbours = grid.get_neighbours(my_node)

            for neighbour in neighbours:
                if not neighbour[1].vis:
                    node_queue.put(neighbour)
                    neighbour[1].vis = True
                    neighbour[1].pre = my_node

            grid.draw_grid()

        grid.draw_shortest_path(grid.get_shortest_path(end_node, shortest_path))


def greedy_best_first(grid):

    def get_next_node():
        next_node = None
        h_cost = 1000
        for node in grid.nodes:
            if not node[1].vis and node[1].h_cost < h_cost:
                h_cost = node[1].h_cost
                next_node = node
        return next_node

    if grid.get_start() is not None and grid.get_end() is not None:
        end_node = grid.get_end()
        shortest_path = []
        while True:
            my_node = get_next_node()[1]
            my_node.vis = True
            if my_node.end:
                break
            if my_node.wall:
                continue

            neighbours = grid.get_neighbours(my_node)

            for neighbour in neighbours:
                neighbour[1].h_cost = (abs(neighbour[1].row - end_node[1].row) + abs(neighbour[1].col - end_node[1].col))
                if not neighbour[1].vis:
                    neighbour[1].pre = my_node

            grid.draw_grid()

        grid.draw_shortest_path(grid.get_shortest_path(end_node, shortest_path))


########################################################################################################################


def main():
    window = pygame.display.set_mode((700, 700))
    window.fill((255, 255, 255))
    grid = Grid(window, 50, 50, 700, 700)
    grid.draw_grid()
    pygame.display.flip()
    running = True
    start_selected = False
    end_selected = False
    key = 0

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                m_pos = pygame.mouse.get_pos()
                for node in grid.nodes:
                    # left mouse click
                    if node[0].collidepoint(m_pos) and not start_selected and pygame.mouse.get_pressed()[0]:
                        start_selected = True
                        node[1].start = True
                        node[1].dist = 0
                        node[1].h_cost = 0
                        node[1].g_cost = 0
                        node[1].f_val = 0
                        grid.draw_grid()
                    elif node[0].collidepoint(m_pos) and not end_selected and not node[1].start \
                            and pygame.mouse.get_pressed()[0]:
                        end_selected = True
                        node[1].end = True
                        grid.draw_grid()
                # right mouse click
                if pygame.mouse.get_pressed()[2]:
                    start_selected = False
                    end_selected = False
                    grid = Grid(window, 50, 50, 700, 700)
                    grid.draw_grid()

            if pygame.mouse.get_pressed()[0] and start_selected and end_selected:
                m_pos = pygame.mouse.get_pos()
                for node in grid.nodes:
                    if node[0].collidepoint(m_pos):
                        node[1].wall = True
                        grid.draw_grid()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    key = 1
                if event.key == pygame.K_2:
                    key = 2
                if event.key == pygame.K_3:
                    key = 3
                if event.key == pygame.K_4:
                    key = 4
                if event.key == pygame.K_SPACE and key == 1:
                    dijkstra(grid)
                    grid.unvisit_all()
                if event.key == pygame.K_SPACE and key == 2:
                    a_star(grid)
                    grid.unvisit_all()
                if event.key == pygame.K_SPACE and key == 3:
                    breadth_first(grid)
                    grid.unvisit_all()
                if event.key == pygame.K_SPACE and key == 4:
                    greedy_best_first(grid)
                    grid.unvisit_all()

    pygame.display.update()


main()
