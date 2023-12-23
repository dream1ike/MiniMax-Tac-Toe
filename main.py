
class TicTacToeBoard:
    def __init__(self, a, b):
        self.a = a
        self.sum = None
        self.b = b

    def Printab(self):
        print(f"a = {self.a}, b = {self.b}")

    def CalcSum(self):
        self.sum = self.a + self.b

    def PrintSum(self):
        print(f"sum = {self.sum}")


board = TicTacToeBoard(1,2)

TicTacToeBoard.CalcSum(board)

TicTacToeBoard.PrintSum(board)
