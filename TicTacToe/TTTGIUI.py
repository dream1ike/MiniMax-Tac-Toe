import tkinter as tk
import numpy as np
from tkinter import messagebox

from TicTacToeBoard import TicTacToeBoard
from Brain import MiniMax

class TicTacToeGUI:
    def __init__(self, size_board):
        self.size_board = size_board
        self.board = TicTacToeBoard(size_board)
        self.current_player = None
        self.real_player = None
        self.computer_symbol = None  # Переменная для отслеживания символа, за который играет компьютер

        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")

        self.buttons = [[None for _ in range(size_board)] for _ in range(size_board)]

        for i in range(size_board):
            for j in range(size_board):
                button = tk.Button(self.root, text=" ", font=('normal', 20), width=6, height=3,
                                   command=lambda row=i, col=j: self.on_button_click(row, col))
                button.grid(row=i, column=j)
                self.buttons[i][j] = button

        self.start_new_game()


    def reset_game(self):
        for i in range(self.size_board):
            for j in range(self.size_board):
                self.buttons[i][j].config(text=" ")

    def start_new_game(self):
        self.current_player = np.random.choice(["X", "O"])
        self.real_player = self.current_player
        self.computer_symbol = "O" if self.current_player == "X" else "X"  # Устанавливаем символ компьютера
        messagebox.showinfo("New Game", f"You are playing as {self.current_player}")
        self.board = TicTacToeBoard(self.size_board)
        self.reset_game()

        if self.current_player == "O":
            self.current_player = self.computer_symbol
            self.make_computer_move()

    def check_game_result(self):
        game_status = self.board.check_game_status()
        if game_status == "X" or game_status == "O":
            messagebox.showinfo("Game Over", f"Player {game_status} wins!")
            self.start_new_game()
        elif game_status == 0:
            messagebox.showinfo("Game Over", "It's a draw!")
            self.start_new_game()

    def on_button_click(self, row, col):
        result = self.board.make_move(row, col, self.current_player)

        if result == 1:
            self.buttons[row][col].config(text=self.current_player)
            game_status = self.board.check_game_status()
            if game_status == "X" or game_status == "O":
                messagebox.showinfo("Game Over", f"Player {game_status} wins!")
                self.start_new_game()
                return
            elif game_status == 0:
                messagebox.showinfo("Game Over", "It's a draw!")
                self.start_new_game()
                return
            self.current_player = "O" if self.current_player == "X" else "X"
            if self.current_player == self.computer_symbol:
                self.make_computer_move()

    def make_computer_move(self):
        if self.current_player == self.computer_symbol:
            empty_cells = [(i, j) for i in range(self.size_board) for j in range(self.size_board) if
                           self.board.get_board()[i][j] is None]
            if empty_cells:
                # computer_move = np.random.choice(len(empty_cells))
                mm = MiniMax(self.board.number_of_moves, self.real_player, self.computer_symbol)
                row, col = mm.calculate_best_move(self.board.get_board(), self.size_board, self.current_player)
                self.board.make_move(row, col, self.computer_symbol)
                self.buttons[row][col].config(text=self.computer_symbol)
                game_status = self.board.check_game_status()
                if game_status == "X" or game_status == "O":
                    messagebox.showinfo("Game Over", f"Player {game_status} wins!")
                    self.start_new_game()
                    return
                elif game_status == 0:
                    messagebox.showinfo("Game Over", "It's a draw!")
                    self.start_new_game()
                    return
                self.current_player = "O" if self.current_player == "X" else "X"


    def run(self):
        self.root.mainloop()


