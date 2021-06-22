from typing import List


def is_safe(row: int, col: int, board: List[int], N: int) -> bool:
    # column check
    for r in range(N):
        if board[r][col] == 1:
            return False

    # upper right diagonal
    r = row
    c = col
    while r >= 0 and c < N:
        if board[r][c] == 1:
            return False
        r -= 1
        c += 1

    # upper left diagonal
    r = row
    c = col
    while r >= 0 and c >= 0:
        if board[r][c] == 1:
            return False
        r -= 1
        c -= 1

    return True


def n_queens(row: int, board: List[int], N: int) -> bool:
    if row >= N:
        return True

    for col in range(N):
        if is_safe(row, col, board, N):
            board[row][col] = 1
            if n_queens(row + 1, board, N):
                return True
            else:
                board[row][col] = 0
    return False


if __name__ == "__main__":
    N = int(input())
    board = [[0 for _ in range(N)] for _ in range(N)]
    row = 0
    if n_queens(row, board, N):
        for row in range(N):
            for col in range(N):
                print(board[row][col], end=" ")
            print()
    else:
        print("Not possible")
