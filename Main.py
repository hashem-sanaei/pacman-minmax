from Gameboard import*
from Pacman_ghavi import*
from Ghost import *

from Gameboard import Gameboard


def minimax(board, depth, isMaximizing):
        if depth == 0 or board.is_game_over():
            return board.evaluate()

        if isMaximizing:
            best_score = float('-inf')
            for direction in ["up", "down", "left", "right"]:
                new_board = copy.deepcopy(board)
                new_board.pacman.move(direction)
                score = minimax(new_board, depth - 1, False)
                best_score = max(best_score, score)
            return best_score
        else:
            best_score = float('inf')
            for direction in ["up", "down", "left", "right"]:
                for direction2 in ["up", "down", "left", "right"]:
                    new_board = copy.deepcopy(board)
                    new_board.ghosts[0].move(direction)
                    new_board.ghosts[1].move(direction2)
                    score = minimax(new_board, depth - 1, True)
                    best_score = min(best_score, score)
            return best_score


def run_game():
    board = Gameboard()
    pacman = Pacman_ghavi(board)
    ghosts = [Ghost(board) for _ in range(2)]
    board.update_state(pacman, ghosts)  # مقداردهی اولیه pacman و ghosts در GameBoard

    while not board.is_game_over():
        board.display()
        best_move = None
        best_score = float('-inf')
        for direction in ["up", "down", "left", "right"]:
            new_board = copy.deepcopy(board)
            new_board.pacman.move(direction)
            score = minimax(new_board, 2, False)
            if score > best_score:
                best_score = score
                best_move = direction
        print(best_move)
        if best_move:
            pacman.move(best_move)

        for ghost in ghosts:
            ghost.move()

        # اضافه کردن متد به‌روزرسانی وضعیت بازی
        board.update_state(pacman, ghosts)
    
    print(score)

run_game()
