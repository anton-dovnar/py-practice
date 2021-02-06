import pathlib
import tkinter as tk
from tkinter import Button, FLAT, NW, CENTER

import numpy as np
from PIL import Image, ImageTk

BASE_DIR = pathlib.Path.cwd()
alien_img = Image.open(
    BASE_DIR.joinpath('alien.png')).resize((128, 128), Image.ANTIALIAS)
skeleton_img = Image.open(
    BASE_DIR.joinpath('skeleton.png')).resize((128, 128), Image.ANTIALIAS)

FONT = "Gayathri"
BLACK = '#545454'
CYAN = '#14bdac'
LGY = '#f2ebd3'
LGR = '#f2d3da'


class TicTacToe:

    def __init__(self, board_size):
        self.root = tk.Tk()
        self.root.resizable(False, False)
        self.root.title('Tic-Tac-Toe')
        self.root.configure(background=CYAN)
        self.root.bind('<Escape>', lambda e: e.widget.quit())

        self.board_size = board_size
        self.alien = ImageTk.PhotoImage(alien_img)
        self.skeleton = ImageTk.PhotoImage(skeleton_img)

        self.canvas = tk.Canvas(
            self.root, relief=FLAT, width=board_size,
            height=board_size, bg=CYAN
        )
        self.menu()
        self.canvas.pack()

        self.board = np.zeros(shape=(3, 3))
        self.reset_board = False

        self.alien_starts = True
        self.alien_turns = True
        self.ai = False

        self.winner = None

        self.alien_idx = 1
        self.skeleton_idx = 2

        self.alien_score = 0
        self.skeleton_score = 0
        self.draw_score = 0

    def mainloop(self):
        position_right = int(self.root.winfo_screenwidth() / 2 - self.board_size / 2)
        position_down = int(self.root.winfo_screenheight() / 2 - self.board_size / 2)

        self.root.geometry("+{}+{}".format(position_right, position_down))
        self.root.mainloop()

    def menu(self):
        pvp = Button(
            self.root, text='PvP', command=self.render,
            anchor=CENTER, bg=CYAN, fg=BLACK, font=f'{FONT} 20 bold'
        )
        pvp.configure(
            width=15, activebackground=LGY, relief=FLAT)
        self.canvas.create_window(
            ((self.board_size - 253) / 2), ((self.board_size - 237) / 2),
            anchor=NW, window=pvp
        )

        pve = Button(
            self.root, text='PvE', command=lambda: self.render(ai=True),
            anchor=CENTER, bg=CYAN, fg=BLACK, font=f'{FONT} 20 bold'
        )
        pve.configure(
            width=15, activebackground=LGY, relief=FLAT)
        self.canvas.create_window(
            ((self.board_size - 253) / 2), ((self.board_size - 143) / 2),
            anchor=NW, window=pve
        )

        quit = Button(
            self.root, text="Quit", command=self.root.quit,
            anchor=CENTER, bg=CYAN, fg=BLACK, font=f'{FONT} 20 bold'
        )
        quit.configure(
            width=15, activebackground=LGY, relief=FLAT)
        self.canvas.create_window(
            ((self.board_size - 253) / 2), ((self.board_size - 48) / 2),
            anchor=NW, window=quit
        )

    def render(self, ai=False):
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

        if ai:
            self.ai = True
            if self.alien_starts is False:
                self.ai_make_move()

    def idx_to_coordinates(self, matrix_pos):
        return [axis * (self.board_size // 3) + self.board_size // 6 for axis in matrix_pos]

    def coordinates_to_idx(self, grid_position):
        return [axis // (self.board_size // 3) for axis in grid_position]

    def filled(self, matrix_pos):
        if self.board[matrix_pos[1]][matrix_pos[0]] == 0:
            return False
        else:
            return True

    def draw_skeleton(self, matrix_pos):
        grid_position = self.idx_to_coordinates(matrix_pos)
        self.canvas.create_image(
            grid_position[0], grid_position[1], image=self.skeleton)

    def draw_alien(self, matrix_pos):
        grid_position = self.idx_to_coordinates(matrix_pos)
        self.canvas.create_image(
            grid_position[0], grid_position[1], image=self.alien)

    def minimax(self, board, depth, ai):
        scorers = {1: 10, 2: -10, 'Draw': 0}
        self.check_winner(board)

        if self.winner:
            return scorers[self.winner]

        if ai:
            best_score = float('-inf')

            for y in range(3):
                for x in range(3):
                    if board[y][x] == 0:
                        board[y][x] = self.skeleton_idx
                        score = self.minimax(board, depth + 1, False)
                        board[y][x] = 0
                        best_score = max(score, best_score)

            print(f'Minimax {best_score}')
            return best_score
        else:
            best_score = float('inf')

            for y in range(3):
                for x in range(3):
                    if board[y][x] == 0:
                        board[y][x] = self.alien_idx
                        score = self.minimax(board, depth + 1, True)
                        board[y][x] = 0
                        best_score = min(score, best_score)

            print(f'Minimax {best_score}')
            return best_score

    def ai_make_move(self):
        best_score = float('-inf')
        best_move = None

        print(f'Best score {best_score}')
        print(f'Best move {best_move}')

        for y in range(3):
            for x in range(3):
                if self.board[y][x] == 0:
                    self.board[y][x] = self.skeleton_idx
                    score = self.minimax(self.board, 0, False)
                    self.board[y][x] = 0

                    if score > best_score:
                        best_score = score
                        best_move = y, x

        y, x = best_move
        self.draw_skeleton((x, y))
        self.board[y][x] = self.skeleton_idx
        self.alien_turns = not self.alien_turns
        print(f'Best score {best_score}')
        print(f'Best move {best_move}')
        print(y, x)
        print(self.board)

        self.winner = None
        self.check_winner(self.board)

    def move(self, event):
        coordinates = [event.x, event.y]
        matrix_pos = self.coordinates_to_idx(coordinates)

        if self.winner and not self.reset_board:
            self.display_gameover()
        elif not self.reset_board:
            if self.alien_turns:
                if not self.filled(matrix_pos):
                    self.draw_alien(matrix_pos)
                    self.board[matrix_pos[1]][matrix_pos[0]] = self.alien_idx
                    self.alien_turns = not self.alien_turns

                    if self.ai:
                        self.check_winner(self.board)
                        if not self.winner:
                            self.ai_make_move()
            else:
                if not self.filled(matrix_pos):
                    self.draw_skeleton(matrix_pos)
                    self.board[matrix_pos[1]][matrix_pos[0]] = self.skeleton_idx
                    self.alien_turns = not self.alien_turns

            # self.winner = self.draw_winner(self.board)
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
        for idx, diag in enumerate(diagonals):
            if np.all(diag == diag[0]) and diag[0]:
                self.winner = diag[0]
                return diag[0]

        if np.all(self.board != 0):
            self.winner = 'Draw'
            return 'Draw'

    def draw_winner(self, board):
        for i in range(board.shape[0]):
            # Horizontal
            if np.all(board[i] == board[i][0]) and board[i][0]:
                self.canvas.create_line(
                    (0, (i + 1) * self.board_size / 3 - self.board_size / 6),
                    (self.board_size, (i + 1) * self.board_size / 3 - self.board_size / 6),
                    fill=LGR
                )
                return board[i][0]

            # Vertical
            if np.all(board[:, i] == board[0][i]) and board[0][i]:
                self.canvas.create_line(
                    ((i + 1) * self.board_size / 3 - self.board_size / 6, 0),
                    ((i + 1) * self.board_size / 3 - self.board_size / 6, self.board_size),
                    fill=LGR
                )
                return board[0][i]

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
                return diag[0]

        # Draw
        if np.all(self.board != 0):
            return 'Draw'

        return False

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

        self.reset_board = True

        score_text = 'Click to play again \n'
        self.canvas.create_text(
            self.board_size / 2, 15 * self.board_size / 16, font=f'{FONT} 20 bold',
            fill=BLACK, text=score_text
        )

    def play_again(self):
        self.reset_board = False
        self.winner = None
        self.alien_starts = not self.alien_starts
        self.alien_turns = self.alien_starts
        self.board = np.zeros(shape=(3, 3))
        self.render(ai=self.ai)


game = TicTacToe(board_size=600)
game.mainloop()
