import numpy as np


class TicTacToeBoard:
    def __init__(self, size_board: int):
        """
        player1 - 1
        player2 - 2
        :param size_board: board = size_board * size_board
        """
        self.size_board = size_board

        # Fill board None
        self.board = np.array([[None for _ in range(size_board)] for _ in range(size_board)])

        self.number_of_moves = 0

    # Ф-я которая делает ход на доску (подаем в нее (x,y,player) и она заполняет доску
    def make_move(self, x, y, player) -> int:
        """
        Fill the board
        :param x: x-axis
        :param y: y-axis
        :param player: player1 or player2
        :return: 0 - can not fill, 1 - filled success
        """
        result = 0
        if self.board[x][y] is None:
            self.board[x][y] = player
            result = 1
        self.number_of_moves += 1
        return result

    @staticmethod
    def _find_single_equal_element(matrix):
        matrix = np.array(matrix)

        # Проверяем строки
        for row in matrix:
            if np.all(row == row[0]):
                return row[0]

        # Проверяем столбцы
        for col in matrix.T:
            if np.all(col == col[0]):
                return col[0]

        # Проверяем главную диагональ
        main_diagonal_set = set(matrix[i, i] for i in range(min(matrix.shape)))
        if len(main_diagonal_set) == 1:
            return main_diagonal_set.pop()

        # Проверяем побочную диагональ
        secondary_diagonal_set = set(matrix[i, -i - 1] for i in range(min(matrix.shape)))
        if len(secondary_diagonal_set) == 1:
            return secondary_diagonal_set.pop()

        # Если совпадений не найдено и в матрице нет None, возвращаем 0
        if np.any(matrix == None):
            return -1
        else:
            return 0

    # Ф-я которая проверяет, выиграл ли кто-то (после size_board * 2 - 1 хода)
    def check_game_status(self):
        """
        Check if someone's wins
        :return: -1 - continue, 0 - draw, player1 - player1 wins, player2 - player2 wins
        """
        if self.number_of_moves > 4:
            result = self._find_single_equal_element(self.board)
            return result
        else:
            return -1

    def get_board(self):
        """
        :return: board right now
        """
        return self.board
