import math
import random
from dataclasses import dataclass

import numpy as np


@dataclass
class Player:
    mark: int


class RandomComputer(Player):

    def get_move(self, empty_cells: np.ndarray, instance: object) -> np.ndarray:
        move = random.choice(empty_cells)
        return move


class SmartComputer(Player):

    def get_move(self, empty_cells: np.ndarray, instance: object) -> np.ndarray:
        if len(empty_cells) == 9:
            move = random.choice(empty_cells)
        else:
            move = self.minimax(instance, self.mark)['position']

        return move

    def minimax(self, state: object, player: int):
        max_player = self.mark  # yourself
        other_player = 1 if player == 2 else 2

        # first we want to check if the previous move is a winner
        empty = len(state.get_available_moves(state.board))

        if state.check_winner(state.board) == other_player:
            result = {
                'position': None,
                'score': 1 * (empty + 1)
                if other_player == max_player
                else -1 * (empty + 1)
            }
            return result
        elif not empty:
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}  # maximize
        else:
            best = {'position': None, 'score': math.inf}  # minimize

        for move in state.get_available_moves(state.board):
            state.board[move[0]][move[1]] = player
            sim_score = self.minimax(state, other_player)  # simulate a game after making that move

            # undo move
            state.board[move[0]][move[1]] = 0
            state.winner = None
            sim_score['position'] = move  # this represents the move optimal next move

            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score

        return best
