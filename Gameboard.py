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
        self.pacman = None  # این باید بعداً مقداردهی شود
        self.ghosts = []  # این باید بعداً مقداردهی شود

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

    def is_near_high_density_area(self, x, y):
        count = 0
        for dx in range(-3, 2):  # بررسی در یک محدوده 5x5 اطراف پک‌من
            for dy in range(-3, 2):
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.height and 0 <= ny < self.width and self.board[nx][ny] == '.':
                    count += 1
        return count >= 7  # مثلاً اگر بیش از 10 نقطه در این محدوده باشد

    def is_escape_route_available(self, x, y):
        for dx in range(-1, 2):  # بررسی در محدوده مجاور پک‌من
            for dy in range(-1, 2):
                if dx == 0 and dy == 0:
                    continue  # خود خانه پک‌من را نادیده می‌گیریم
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.height and 0 <= ny < self.width and self.board[nx][ny] != 'X':
                    # اگر خانه‌ای بدون مانع و دور از روح‌ها باشد
                    if not any(abs(ghost.position[0] - nx) + abs(ghost.position[1] - ny) < 2 for ghost in self.ghosts):
                        return True
        return False

    def evaluate(self):
        score = 0
        # افزودن امتیاز برای هر نقطه‌ای که پک‌من می‌خورد
        score += sum(10 for x in range(self.height) for y in range(self.width) if self.board[x][y] == '#')

        # کسر امتیاز برای نزدیکی به روح‌ها
        for ghost in self.ghosts:
            distance = abs(ghost.position[0] - self.pacman.position[0]) + abs(ghost.position[1] - self.pacman.position[1])
            score += distance 

        # کاهش امتیاز بر اساس تعداد حرکات
        score -= self.pacman.moves_count

        # اضافه کردن امتیاز برای قرار گرفتن در موقعیت‌های استراتژیک
        strategic_positions_score = 0
        x, y = self.pacman.position
        if self.is_near_high_density_area(x, y):
            strategic_positions_score += 10
        else:
            for x in range(self.height):
                for y in range(self.width):
                    if self.board[x][y] == '.':
                        distance = abs(x - self.pacman.position[0]) + abs(y - self.pacman.position[1])
                        score -= distance
        if self.is_escape_route_available(x, y):
            strategic_positions_score +=15
        
        score += strategic_positions_score
        


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