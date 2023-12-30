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

    def minimax(self, board, depth, maximizing_player):
        winner = self.check_game_status(board)
        if winner == self.computer_player or winner == self.player:
            return -1 if maximizing_player else 1
        elif winner == 0:
            return 0
        scores = []
        empty_cells = [(i, j) for i in range(self.size_board) for j in range(self.size_board) if
                       board[i][j] is None]
        for i, j in empty_cells:
            board[i][j] = self.computer_player if maximizing_player else self.player
            score = self.minimax(board, depth + 1, not maximizing_player)
            scores.append(score)
            board[i][j] = None
        if maximizing_player:
            max_score_index = scores.index(max(scores))
            return scores[max_score_index]
        else:
            min_score_index = scores.index(min(scores))
            return scores[min_score_index]

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
        if len(empty_cells) >= 9:
            return 1, 1
        self.size_board = size_board
        best_score = float('-inf')
        best_move = (None, None)
        for i in range(len(empty_cells)):
            row, column = empty_cells[i]
            board[row][column] = player
            score = self.minimax(board, 0, False)
            board[row][column] = None
            if score > best_score:
                best_score = score
                best_move = (row, column)

        return best_move

