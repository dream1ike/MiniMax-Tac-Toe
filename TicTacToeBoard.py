class TicTacToeBoard:
    def __init__(self, size_board: int, player1: int, player2: int):
        """
        :param size_board: board = size_board * size_board
        :param player1:  what will the first player play with
        :param player2: what will the second player play with
        """
        self.size_board = size_board

        # Fill board None
        self.board = [[None for _ in range(size_board)] for _ in range(size_board)]

        self.player1 = player1
        self.player2 = player2
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
        if self.board[x][y] == None:
            self.board[x][y] = player
            result = 1
        self.number_of_moves += 1
        return result

    # Ф-я которая проверяет, выиграл ли кто-то (после size_board * 2 - 1 хода)
    def check_game_status(self):
        """
        Check if someone's wins
        :return: -1 - continue, 0 - draw, 1 - player1 wins, 2 - player2 wins
        """

    # Ф-я, которая возвращает доску
    def get_board(self) -> list:
        """
        :return: board right now
        """
        return self.board