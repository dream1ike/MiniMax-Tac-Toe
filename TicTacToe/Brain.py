import numpy as np

from TicTacToeBoard import TicTacToeBoard


class MiniMax:
    def __init__(self, number_of_moves, player, computer_player):
        self.number_of_moves = number_of_moves
        self.player = player
        self.computer_player = computer_player
        self.size_board = 0
        pass

    @staticmethod
    def _find_single_equal_element(matrix):
        # Проверяем строки
        for row in matrix:
            if np.all(row == row[0]):
                if all(element is None for element in row):
                    break
                return row[0]

        # Проверяем столбцы
        for col in matrix.T:
            if np.all(col == col[0]):
                if all(element is None for element in col):
                    break
                return col[0]

        # Проверяем главную диагональ
        main_diagonal_set = set(matrix[i, i] for i in range(min(matrix.shape)))
        if len(main_diagonal_set) == 1 and None not in main_diagonal_set:
            return main_diagonal_set.pop()

        # Проверяем побочную диагональ
        secondary_diagonal_set = set(matrix[i, -i - 1] for i in range(min(matrix.shape)))
        if len(secondary_diagonal_set) == 1 and None not in secondary_diagonal_set:
            return secondary_diagonal_set.pop()

        # Если совпадений не найдено и в матрице нет None, возвращаем 0
        if np.any(np.equal(matrix, None)):
            return -1
        else:
            return 0

    def check_game_status(self, board):
        """
        Check if someone's wins
        :return: -1 - continue, 0 - draw, 1 - player1 wins, 2 - player2 wins
        """
        result = self._find_single_equal_element(board)
        return result

    def minimax(self, board: np.array, depth: int, isMaximizing: bool):
        winner = self.check_game_status(board)
        if winner != -1:
            if winner == self.computer_player:
                score = 1
            else:
                score = -1
            return score, depth

        if isMaximizing:
            empty_cells = [(i, j) for i in range(self.size_board) for j in range(self.size_board) if
                           board[i][j] is None]
            best_score = float('-inf')
            best_depth = float('-inf')
            if empty_cells:
                for i in range(len(empty_cells)):
                    row, column = empty_cells[i]
                    new_board = board.copy()
                    new_board[row][column] = self.computer_player
                    score, curr_depth = self.minimax(new_board, depth + 1, False)
                    if best_score < score and best_depth < curr_depth:
                        best_score = score
                        best_depth = curr_depth
            return best_score, best_depth
        else:
            empty_cells = [(i, j) for i in range(self.size_board) for j in range(self.size_board) if
                           board[i][j] is None]
            best_score = float('inf')
            best_depth = float('-inf')
            if empty_cells:
                for i in range(len(empty_cells)):
                    row, column = empty_cells[i]
                    new_board = board.copy()
                    new_board[row][column] = self.player
                    score, curr_depth = self.minimax(new_board, depth + 1, True)
                    if best_score > score and best_depth < curr_depth:
                        best_score = score
                        best_depth = curr_depth
            return best_score, best_depth

    def calculate_best_move(self, board: np.array, size_board: int, player):
        """
        Calculating Best move with algorithm Minimax
        :param board: np.array board size_board * size_board
        :param size_board: size of one of the side of the board
        :param player: for who calculate?
        :return: (row, column) - best move
        """
        empty_cells = [(i, j) for i in range(size_board) for j in range(size_board) if
                       board[i][j] is None]
        self.size_board = size_board
        best_score = float('-inf')
        best_move = (None, None)
        for i in range(len(empty_cells)):
            row, column = empty_cells[i]
            new_board = board.copy()
            new_board[row][column] = player
            score, _ = self.minimax(new_board, 1, False)
            if score > best_score:
                best_score = score
                best_move = (row, column)

        return best_move

