import random
class Ghost:
    def __init__(self, board):
        self.board = board
        self.position = (8, 8)  # تعیین موقعیت اولیه روح

    def move(self):
        directions = ["up", "down", "left", "right"]
        while True:
            direction = random.choice(directions)
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
                self.position = (x, y)
                break  