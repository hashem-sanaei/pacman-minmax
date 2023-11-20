import random
import copy
from Ghost import*
from Pacman_ghavi import*
class Gameboard:
    def __init__(self, width=18, height=9):
        self.width = width
        self.height = height
        self.board = [['.' for _ in range(width)] for _ in range(height)]
        self.set_obstacles()
        self.pacman = None  
        self.ghosts = []  

    def set_obstacles(self):
        obstacle_count = self.width * self.height // 10
        for _ in range(obstacle_count):
            x, y = random.randint(0, self.height - 1), random.randint(0, self.width - 1)
            self.board[x][y] = 'X'

    def display(self):
        for row in self.board:
            print(' '.join(row))
        # چاپ موقعیت پک‌من و روح‌ها
        print(f'Pacman: {self.pacman.position}')
        for i, ghost in enumerate(self.ghosts):
            print(f'Ghost {i}: {ghost.position}')

        print()
        


    def is_game_over(self):
        # بررسی برخورد پک‌من با روح‌ها
        for ghost in self.ghosts:
            if ghost.position == self.pacman.position:
                return True

        # بررسی خوردن تمام نقاط توسط پک‌من
        return not any(self.board[x][y] == '.' for x in range(self.height) for y in range(self.width))


    def update_state(self, pacman, ghosts):
        self.pacman = pacman
        self.ghosts = ghosts


    def a_star_to_foods(self):
        x, y = self.pacman.position
        start_node = (x, y, 0)  # (x, y, g_cost)
        open_set = {start_node}
        came_from = {}  # to track the path
        g_score = {start_node: 0}
        f_score = {start_node: self.manhattan_distance(x, y)}

        while open_set:
            current = min(open_set, key=lambda o: f_score.get(o, float('inf')))
            if self.board[current[0]][current[1]] == '.':
                return g_score[current]
            
            open_set.remove(current)
            
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                neighbor = (current[0] + dx, current[1] + dy, g_score[current] + 1)
                if 0 <= neighbor[0] < self.height and 0 <= neighbor[1] < self.width and self.board[neighbor[0]][neighbor[1]] != 'X':
                    if neighbor not in g_score or neighbor[2] < g_score[neighbor]:
                        came_from[neighbor] = current
                        g_score[neighbor] = neighbor[2]
                        f_score[neighbor] = g_score[neighbor] + self.manhattan_distance(neighbor[0], neighbor[1])
                        if neighbor not in open_set:
                            open_set.add(neighbor)

        return float('inf')

    def manhattan_distance(self, x, y):
        # Heuristic function: Manhattan distance to the nearest food
        min_distance = float('inf')
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j] == '.':
                    min_distance = min(min_distance, abs(x - i) + abs(y - j))
        return min_distance


    def evaluate(self):
        score = 10 * sum(10 for x in range(self.height) for y in range(self.width) if self.board[x][y] == '#')
        if self.is_game_over():
            for ghost in self.ghosts:
                if ghost.position == self.pacman.position:
                    return float('-inf')
            return 1000 * score
        
        # کسر امتیاز برای نزدیکی به روح‌ها
        for ghost in self.ghosts:
            distance = abs(ghost.position[0] - self.pacman.position[0]) + abs(ghost.position[1] - self.pacman.position[1])
            score += 2 * distance 

        score -= 10 * self.a_star_to_foods()
        


        return score

    def get_children(self):
        children = []
        directions = ["up", "down", "left", "right"]
        for direction in directions:
            new_board = copy.deepcopy(self)
            new_board.pacman.move(direction)
            for ghost in new_board.ghosts:
                ghost.move()
            children.append(new_board)
        return children
