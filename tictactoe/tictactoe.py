import time
import pygame
from pygame.locals import *


class GameLoop:
    # X / O imgages loading
    __x_img = pygame.image.load('X.png')
    __o_img = pygame.image.load('O.png')
    #resizing images
    __x = pygame.transform.scale(__x_img, (80,80))
    __o = pygame.transform.scale(__o_img, (80,80))

    def __init__(self):
        self.game_state = True
        self.player = 'x'
        self.winner = None
        self.draw = False
        self.WIDTH, self.HEIGHT = (400, 400)
        self.WHITE = (255, 255, 255)
        self.LINE_COLOR = (10, 10, 10)
        self.X = self.__x
        self.O = self.__o
        # load screen
        self.SCREEN = pygame.display.set_mode((self.WIDTH, self.HEIGHT+100), 0, 32)
        self.SCREEN.fill(self.WHITE)
        # starting
        pygame.display.set_caption("Tic Tac Toe")
        pygame.display.flip()

    def render_ui(self, gameboard):
        self.gameboard = gameboard

        while True:
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN and event.button == 1 and self.game_state:
                    self.make_move()
                    self.check_win()
                    self.draw_status()
                    pygame.display.update()
                    if not self.game_state:
                        time.sleep(1)
                        self.reset_game()
                if event.type == QUIT:
                    pygame.quit()
                self.draw_board()

            pygame.display.update()

    def draw_board(self):
        '''Draws the lines of the GameBoard'''

        # Drawing vertical lines
        pygame.draw.line(
            self.SCREEN, self.LINE_COLOR,
            (self.WIDTH/3, 0), (self.WIDTH/3, self.HEIGHT), 7
        )
        pygame.draw.line(
            self.SCREEN, self.LINE_COLOR,
            (self.WIDTH/3*2, 0),(self.WIDTH/3*2, self.HEIGHT), 7
        )
        # Drawing horizontal lines
        pygame.draw.line(
            self.SCREEN, self.LINE_COLOR,
            (0, self.HEIGHT/3), (self.WIDTH, self.HEIGHT/3), 7
        )
        pygame.draw.line(
            self.SCREEN, self.LINE_COLOR,
            (0, self.HEIGHT/3*2), (self.WIDTH, self.HEIGHT/3*2), 7
        )
        self.draw_status()

    def draw_status(self):
        """
        Draw status at the bottom
        """
        if self.winner is None:
            message = self.player.upper() + " Ходит"
        else:
            message = self.player.upper() + " Победил!"
        if self.draw:
            message = 'Ничья!'

        font = pygame.font.Font(None, 30)
        text = font.render(message, 1, (255, 255, 255))

        # copy the rendered message onto the board
        self.SCREEN.fill((0, 0, 0), (0, 400, 500, 100))
        text_rect = text.get_rect(center=(self.WIDTH/2, 500-50))
        self.SCREEN.blit(text, text_rect)

    def draw_xo(self, row, col):
        """
        Draw X O images at the board
        """
        if row == 1:
            posx = 30
        if row == 2:
            posx = self.WIDTH/3 + 30
        if row == 3:
            posx = self.WIDTH/3*2 + 30

        if col == 1:
            posy = 30
        if col == 2:
            posy = self.HEIGHT/3 + 30
        if col == 3:
            posy = self.HEIGHT/3*2 + 30

        self.gameboard[row-1][col-1] = self.player

        if self.player == 'x':
            self.SCREEN.blit(self.X, (posy,posx))
            self.check_win()
            if self.game_state:
                self.player = 'o'
        else:
            self.SCREEN.blit(self.O, (posy,posx))
            self.check_win()
            if self.game_state:
                self.player = 'x'

    def check_win(self):
        """
        Check for winner
        """
        for row in range(0,3):
            if (
                    (self.gameboard[row][0] == self.gameboard[row][1] == self.gameboard[row][2]) and
                    (self.gameboard[row][0] is not None)
            ):
                # this row won
                self.winner = self.gameboard[row][0]
                pygame.draw.line(
                    self.SCREEN, (250, 0, 0), (0, (row + 1)*self.HEIGHT/3 - self.HEIGHT/6),\
                    (self.WIDTH, (row + 1)*self.HEIGHT/3 - self.HEIGHT/6), 4)
                self.game_state = False

        # check for winning columns
        for col in range(0, 3):
            if (
                    (self.gameboard[0][col] == self.gameboard[1][col] == self.gameboard[2][col]) and
                    (self.gameboard[0][col] is not None)
            ):
                # this column won
                self.winner = self.gameboard[0][col]
                #draw winning line
                pygame.draw.line(
                    self.SCREEN, (250, 0, 0), ((col + 1)* self.WIDTH/3 - self.WIDTH/6, 0),\
                    ((col + 1)* self.WIDTH/3 - self.WIDTH/6, self.HEIGHT), 4)
                self.game_state = False

        # check for diagonal winners
        if (
                (self.gameboard[0][0] == self.gameboard[1][1] == self.gameboard[2][2])
                and (self.gameboard[0][0] is not None)
        ):
            self.winner = self.gameboard[0][0]
            # game won diagonally left to right
            pygame.draw.line(self.SCREEN, (250, 70, 70), (50, 50), (350, 350), 4)
            self.game_state = False


        if (
                (self.gameboard[0][2] == self.gameboard[1][1] == self.gameboard[2][0])
                and (self.gameboard[0][2] is not None)
        ):
            self.winner = self.gameboard[0][2]
            # game won diagonally right to left
            pygame.draw.line(self.SCREEN, (250,70,70), (350, 50), (50, 350), 4)
            self.game_state = False

        if all([all(row) for row in self.gameboard]) and self.winner is None:
            self.draw = True
            self.game_state = False


    def make_move(self):
        """
        Getting mouse click position on the board
        """
        #get coordinates of mouse click
        x, y = pygame.mouse.get_pos()

        #get column of mouse click (1-3)
        if x < self.WIDTH/3:
            col = 1
        elif x < self.WIDTH/3*2:
            col = 2
        elif x < self.WIDTH:
            col = 3
        else:
            col = None

        #get row of mouse click (1-3)
        if y < self.HEIGHT/3:
            row = 1
        elif y < self.HEIGHT/3*2:
            row = 2
        elif y < self.HEIGHT:
            row = 3
        else:
            row = None

        if (row and col and self.gameboard[row-1][col-1] is None):
            self.draw_xo(row, col)

    def reset_game(self):
        self.gameboard = [[None]*3 ,[None]*3, [None]*3]
        self.__init__()


if __name__ == "__main__":
    board = [[None]*3 ,[None]*3, [None]*3]
    pygame.init()

    GL = GameLoop()
    while True:
        GL.render_ui(board)
