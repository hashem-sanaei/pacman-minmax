from Gameboard import*
from Pacman_ghavi import*
from Ghost import*

from Gameboard import Gameboard


def minimax(board, depth, isMaximizing):
        if depth == 0 or board.is_game_over():
            return board.evaluate()

        if isMaximizing:
            maxEval = float('-inf')
            for child in board.get_children():
                eval = minimax(child, depth - 1, False)
                maxEval = max(maxEval, eval)
            return maxEval
        else:
            minEval = float('inf')
            for child in board.get_children():
                eval = minimax(child, depth - 1, True)
                minEval = min(minEval, eval)
            return minEval


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
            score = minimax(new_board, 3, False)
            if score > best_score:
                best_score = score
                best_move = direction

        if best_move:
            pacman.move(best_move)

        for ghost in ghosts:
            ghost.move()

        # اضافه کردن متد به‌روزرسانی وضعیت بازی
        board.update_state(pacman, ghosts)
    
    print(score)

run_game()
