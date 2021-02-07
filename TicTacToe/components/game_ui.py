import pathlib
import tkinter as tk
from dataclasses import dataclass
from tkinter import CENTER, FLAT, NW, Button

import numpy as np
from PIL import Image, ImageTk

BASE_DIR = pathlib.Path.cwd()
alien_img = Image.open(
    BASE_DIR.joinpath('components', 'img', 'alien.png')).resize((128, 128), Image.ANTIALIAS)
skeleton_img = Image.open(
    BASE_DIR.joinpath('components', 'img', 'skeleton.png')).resize((128, 128), Image.ANTIALIAS)

FONT = "Gayathri"
BLACK = '#545454'
CYAN = '#14bdac'
LGY = '#f2ebd3'
LGR = '#f2d3da'


@dataclass
class Ui:
    root: tk.Tk = tk.Tk()
    root.resizable(False, False)
    root.title('Tic-Tac-Toe')
    root.configure(background=CYAN)
    root.bind('<Escape>', lambda e: e.widget.quit())

    alien: ImageTk.PhotoImage = ImageTk.PhotoImage(alien_img)
    skeleton: ImageTk.PhotoImage = ImageTk.PhotoImage(skeleton_img)

    board_size: int = 600

    canvas: tk.Canvas = tk.Canvas(
        root, relief=FLAT, width=board_size,
        height=board_size, bg=CYAN
    )

    def __post_init__(self):
        self.menu()
        self.canvas.pack()

    def menu(self):
        pvp = Button(
            self.root, text='PvP', command=lambda: self.play('PvP'),
            anchor=CENTER, bg=CYAN, fg=BLACK, font=f'{FONT} 20 bold'
        )
        pvp.configure(
            width=15, activebackground=LGY, relief=FLAT)
        self.canvas.create_window(
            ((self.board_size - 253) / 2), ((self.board_size - 237) / 2),
            anchor=NW, window=pvp
        )

        easy_comp = Button(
            self.root, text='Easy Comp', command=lambda: self.play('Easy'),
            anchor=CENTER, bg=CYAN, fg=BLACK, font=f'{FONT} 20 bold'
        )
        easy_comp.configure(
            width=15, activebackground=LGY, relief=FLAT)
        self.canvas.create_window(
            ((self.board_size - 253) / 2), ((self.board_size - 143) / 2),
            anchor=NW, window=easy_comp
        )

        smart_comp = Button(
            self.root, text='Ubeatable Comp', command=lambda: self.play('Unbeatable'),
            anchor=CENTER, bg=CYAN, fg=BLACK, font=f'{FONT} 20 bold'
        )
        smart_comp.configure(
            width=15, activebackground=LGY, relief=FLAT)
        self.canvas.create_window(
            ((self.board_size - 253) / 2), ((self.board_size - 48) / 2),
            anchor=NW, window=smart_comp
        )

        quit = Button(
            self.root, text="Quit", command=self.root.quit,
            anchor=CENTER, bg=CYAN, fg=BLACK, font=f'{FONT} 20 bold'
        )
        quit.configure(
            width=15, activebackground=LGY, relief=FLAT)
        self.canvas.create_window(
            ((self.board_size - 253) / 2), ((self.board_size + 46) / 2),
            anchor=NW, window=quit
        )

    def render(self):
        self.canvas.delete("all")
        self.root.bind('<Button-1>', self.move)

        for i in range(2):
            self.canvas.create_line(
                (i + 1) * self.board_size / 3, 0,
                (i + 1) * self.board_size / 3, self.board_size,
                fill=BLACK
            )

        for i in range(2):
            self.canvas.create_line(
                0, (i + 1) * self.board_size / 3,
                self.board_size, (i + 1) * self.board_size / 3,
                fill=BLACK
            )

    def draw_skeleton(self, matrix_pos):
        grid_position = self.idx_to_coordinates(matrix_pos)
        self.canvas.create_image(
            grid_position[0], grid_position[1], image=self.skeleton)

    def draw_alien(self, matrix_pos):
        grid_position = self.idx_to_coordinates(matrix_pos)
        self.canvas.create_image(
            grid_position[0], grid_position[1], image=self.alien)

    def draw_winner(self, board):
        for i in range(board.shape[0]):
            # Horizontal
            if np.all(board[i] == board[i][0]) and board[i][0]:
                self.canvas.create_line(
                    (0, (i + 1) * self.board_size / 3 - self.board_size / 6),
                    (self.board_size, (i + 1) * self.board_size / 3 - self.board_size / 6),
                    fill=LGR
                )

            # Vertical
            if np.all(board[:, i] == board[0][i]) and board[0][i]:
                self.canvas.create_line(
                    ((i + 1) * self.board_size / 3 - self.board_size / 6, 0),
                    ((i + 1) * self.board_size / 3 - self.board_size / 6, self.board_size),
                    fill=LGR
                )

        # Diagonals
        diagonals = board.diagonal(), np.fliplr(board).diagonal()
        for idx, diag in enumerate(diagonals):
            if np.all(diag == diag[0]) and diag[0]:
                if idx == 0:
                    self.canvas.create_line(
                        0, 0, self.board_size, self.board_size, fill=LGR)
                else:
                    self.canvas.create_line(
                        self.board_size, 0, 0, self.board_size, fill=LGR)

    def display_gameover(self):
        if self.winner == 1:
            self.alien_score += 1
            text = 'Alien Win'
        elif self.winner == 2:
            self.skeleton_score += 1
            text = 'Skeleton Win'
        else:
            self.draw_score += 1
            text = self.winner

        self.canvas.delete("all")
        self.canvas.create_text(
            self.board_size / 2, self.board_size / 3, font=f'{FONT} 40 bold',
            fill=BLACK, text=text
        )

        score_text = 'Table scores: \n'
        self.canvas.create_text(
            self.board_size / 2, 5 * self.board_size / 8, font=f'{FONT} 30 bold',
            fill=BLACK, text=score_text
        )

        score_text = f'Alien: {self.alien_score} \n'
        score_text += f'Skeleton: {self.skeleton_score} \n'
        score_text += f'Draw: {self.draw_score} \n'

        self.canvas.create_text(
            self.board_size / 2, 3 * self.board_size / 4, font=f'{FONT} 20 bold',
            fill=BLACK, text=score_text
        )

        score_text = 'Click to play again \n'
        self.canvas.create_text(
            self.board_size / 2, 15 * self.board_size / 16, font=f'{FONT} 20 bold',
            fill=BLACK, text=score_text
        )
