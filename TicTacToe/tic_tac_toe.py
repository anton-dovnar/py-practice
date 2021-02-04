import pathlib
import tkinter as tk

import numpy as np
from PIL import Image, ImageTk

BASE_DIR = pathlib.Path.cwd()
alien_img = Image.open(
    BASE_DIR.joinpath('alien.png')).resize((128, 128), Image.ANTIALIAS)
skeleton_img = Image.open(
    BASE_DIR.joinpath('skeleton.png')).resize((128, 128), Image.ANTIALIAS)


class TicTacToe:

    def __init__(self, board_size):
        self.root = tk.Tk()
        self.root.title('Tic-Tac-Toe')
        self.root.configure(background='#14bdac')
        self.root.bind('<Button-1>', self.move)
        self.root.bind('<Escape>', lambda e: e.widget.quit())

        self.board_size = board_size
        self.alien = ImageTk.PhotoImage(alien_img)
        self.skeleton = ImageTk.PhotoImage(skeleton_img)

        self.canvas = tk.Canvas(self.root, width=board_size, height=board_size, bg='#14bdac')
        self.canvas.pack()
        self.render()

        self.board = np.zeros(shape=(3, 3))
        self.reset_board = False

        self.alien_starts = True
        self.alien_turns = True

        self.draw = False
        self.winner = None

        self.alien_score = 0
        self.skeleton_score = 0
        self.draw_score = 0

    def mainloop(self):
        self.root.mainloop()

    def render(self):
        for i in range(2):
            self.canvas.create_line(
                (i + 1) * self.board_size / 3, 0,
                (i + 1) * self.board_size / 3, self.board_size,
                fill='#545454'
            )

        for i in range(2):
            self.canvas.create_line(
                0, (i + 1) * self.board_size / 3,
                self.board_size, (i + 1) * self.board_size / 3,
                fill='#545454'
            )

    def convert_logical_to_grid_position(self, logical_position):
        logical_position = np.array(logical_position, dtype=int)
        return (self.board_size / 3) * logical_position + self.board_size / 6

    def convert_grid_to_logical_position(self, grid_position):
        grid_position = np.array(grid_position)
        return np.array(grid_position // (self.board_size / 3), dtype=int)

    def filled(self, logical_position):
        if self.board[logical_position[0]][logical_position[1]] == 0:
            return False
        else:
            return True

    def draw_skeleton(self, logical_position):
        logical_position = np.array(logical_position)
        grid_position = self.convert_logical_to_grid_position(logical_position)
        self.canvas.create_image(
            grid_position[0], grid_position[1], image=self.skeleton)

    def draw_alien(self, logical_position):
        grid_position = self.convert_logical_to_grid_position(logical_position)
        self.canvas.create_image(
            grid_position[0], grid_position[1], image=self.alien)

    def move(self, event):
        grid_position = [event.x, event.y]
        logical_position = self.convert_grid_to_logical_position(grid_position)

        if self.winner and not self.reset_board:
            self.display_gameover(self.winner)
        elif not self.reset_board:
            if self.alien_turns:
                if not self.filled(logical_position):
                    self.draw_alien(logical_position)
                    self.board[logical_position[0]][logical_position[1]] = 1
                    self.alien_turns = not self.alien_turns
            else:
                if not self.filled(logical_position):
                    self.draw_skeleton(logical_position)
                    self.board[logical_position[0]][logical_position[1]] = -1
                    self.alien_turns = not self.alien_turns
            self.winner = self.check_winner(self.board)
        else:
            self.canvas.delete("all")
            self.play_again()

    def check_winner(self, board):
        for i in range(board.shape[0]):
            # Vertical
            if np.all(board[i] == board[i][0]) and board[i][0]:
                self.canvas.create_line(
                    ((i + 1) * self.board_size / 3 - self.board_size / 6, 0),
                    ((i + 1) * self.board_size / 3 - self.board_size / 6, self.board_size),
                    fill='red'
                )
                return board[i][0]

            # Horizontal
            if np.all(board[:, i] == board[0][i]) and board[0][i]:
                self.canvas.create_line(
                    (0, (i + 1) * self.board_size / 3 - self.board_size / 6),
                    (self.board_size, (i + 1) * self.board_size / 3 - self.board_size / 6),
                    fill='red'
                )
                return board[0][i]

        # Diagonals
        diagonals = board.diagonal(), np.fliplr(board).diagonal()
        for idx, diag in enumerate(diagonals):
            if np.all(diag == diag[0]) and diag[0]:
                if idx == 0:
                    self.canvas.create_line(
                        0, 0, self.board_size, self.board_size, fill='red')
                else:
                    self.canvas.create_line(
                        self.board_size, 0, 0, self.board_size, fill='red')
                return diag[0]

        # Draw
        if np.all(self.board != 0):
            self.draw = True
            return 'Draw'

        return False

    def display_gameover(self, status):
        if status == 1:
            self.alien_score += 1
            text = 'Alien Win'
        elif status == -1:
            self.skeleton_score += 1
            text = 'Skeleton Win'
        else:
            self.draw_score += 1
            text = status

        self.canvas.delete("all")
        self.canvas.create_text(
            self.board_size / 2, self.board_size / 3, font="Gayathri 40 bold",
            fill='#545454', text=text
        )

        score_text = 'Table scores: \n'
        self.canvas.create_text(
            self.board_size / 2, 5 * self.board_size / 8, font="Gayathri 30 bold",
            fill='#545454', text=score_text
        )

        score_text = f'Alien: {self.alien_score} \n'
        score_text += f'Skeleton: {self.skeleton_score} \n'
        score_text += f'Draw: {self.draw_score} \n'

        self.canvas.create_text(
            self.board_size / 2, 3 * self.board_size / 4, font="Gayathri 20 bold",
            fill='#545454', text=score_text
        )

        self.reset_board = True

        score_text = 'Click to play again \n'
        self.canvas.create_text(
            self.board_size / 2, 15 * self.board_size / 16, font="Gayathri 20 bold",
            fill="#545454", text=score_text
        )

    def play_again(self):
        self.reset_board = False
        self.winner = None
        self.render()
        self.alien_starts = not self.alien_starts
        self.alien_turns = self.alien_starts
        self.board = np.zeros(shape=(3, 3))


game = TicTacToe(board_size=600)
game.mainloop()
