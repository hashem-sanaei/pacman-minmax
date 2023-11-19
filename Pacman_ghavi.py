import random
import copy
class Pacman_ghavi:
    def __init__(self, board):
        self.board = board
        self.position = (0, 0)  # تعیین موقعیت اولیه پک‌من
        self.score = 0
        self.moves_count = 0  # این باید در هر حرکت افزایش یابد

    def move(self, direction):
        # محاسبه موقعیت جدید بر اساس جهت
        x, y = self.position
        if direction == "up":
            x -= 1
        elif direction == "down":
            x += 1
        elif direction == "left":
            y -= 1
        elif direction == "right":
            y += 1
        if 0 <= x < self.board.height and 0 <= y < self.board.width and self.board.board[x][y] != 'X':
            if self.moves_count == 0:
                self.board.board[x][y] = '#'
            self.position = (x, y)
            self.board.board[x][y]='#'
            self.moves_count += 1  # افزایش تعداد حرکات
