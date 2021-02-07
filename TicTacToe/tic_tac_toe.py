import numpy as np
from components.game_ui import Ui
from components.player import (
    Human,
    RandomComputer,
    SmartComputer,
)


class TicTacToe(Ui):

    def __init__(self, board_size):
        super().__init__(board_size)

        self.board = np.zeros(shape=(3, 3))
        self.reset_board = False
        self.winner = None

        self.alien_starts = True
        self.alien_turns = True
        self.computer = False

        self.alien_score = 0
        self.skeleton_score = 0
        self.draw_score = 0

    def mainloop(self):
        position_right = int(self.root.winfo_screenwidth() / 2 - self.board_size / 2)
        position_down = int(self.root.winfo_screenheight() / 2 - self.board_size / 2)

        self.root.geometry("+{}+{}".format(position_right, position_down))
        self.root.mainloop()

    def play(self, mode):
        if mode == 'Easy':
            self.player1 = Human(1)
            self.player2 = RandomComputer(2)
            self.computer = True
        elif mode == 'Unbeatable':
            self.player1 = Human(1)
            self.player2 = SmartComputer(2)
            self.computer = True
        else:
            self.player1 = Human(1)
            self.player2 = Human(2)

        self.render()

    def idx_to_coordinates(self, matrix_pos):
        return [axis * (self.board_size // 3) + self.board_size // 6 for axis in matrix_pos]

    def coordinates_to_idx(self, grid_position):
        return [axis // (self.board_size // 3) for axis in grid_position]

    def get_available_moves(self, board):
        empty_cells = np.argwhere(self.board == 0)
        return empty_cells

    def computer_move(self, empty_cells):
        move = self.player2.get_move(empty_cells, self)
        self.draw_skeleton((move[1], move[0]))
        self.board[move[0]][move[1]] = self.player2.mark
        self.alien_turns = not self.alien_turns

    def move(self, event):
        coordinates = [event.x, event.y]
        matrix_pos = self.coordinates_to_idx(coordinates)

        if self.winner and not self.reset_board:
            self.reset_board = True
            self.display_gameover()

        elif not self.reset_board:
            if self.alien_turns:
                if self.board[matrix_pos[1]][matrix_pos[0]] == 0:
                    self.draw_alien(matrix_pos)
                    self.board[matrix_pos[1]][matrix_pos[0]] = self.player1.mark
                    self.alien_turns = not self.alien_turns

                    empty_cells = self.get_available_moves(self.board)
                    self.check_winner(self.board)

                    if self.computer and empty_cells.any() and not self.winner:
                        self.computer_move(empty_cells)

            else:
                if self.board[matrix_pos[1]][matrix_pos[0]] == 0:
                    self.draw_skeleton(matrix_pos)
                    self.board[matrix_pos[1]][matrix_pos[0]] = self.player2.mark
                    self.alien_turns = not self.alien_turns

            self.check_winner(self.board)
            if self.winner:
                self.draw_winner(self.board)
        else:
            self.canvas.delete("all")
            self.play_again()

    def check_winner(self, board):
        for i in range(board.shape[0]):
            # Horizontal
            if np.all(board[i] == board[i][0]) and board[i][0]:
                self.winner = board[i][0]
                return board[i][0]

            # Vertical
            if np.all(board[:, i] == board[0][i]) and board[0][i]:
                self.winner = board[0][i]
                return board[0][i]

        # Diagonals
        diagonals = board.diagonal(), np.fliplr(board).diagonal()
        for diag in diagonals:
            if np.all(diag == diag[0]) and diag[0]:
                self.winner = diag[0]
                return diag[0]

        if np.all(self.board != 0):
            self.winner = 'Draw'
            return 'Draw'

    def play_again(self):
        self.reset_board = False
        self.winner = None
        self.alien_starts = not self.alien_starts
        self.alien_turns = self.alien_starts
        self.board = np.zeros(shape=(3, 3))
        self.render()

        if self.alien_starts is False and self.computer:
            empty_cells = self.get_available_moves(self.board)
            self.computer_move(empty_cells)


game = TicTacToe(600)
game.mainloop()
