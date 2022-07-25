#!/usr/bin/python3
from sys import argv


n = int(argv[1])


def validate(chess_board: dict, queen_key: int) -> bool:
    """Confirms that a queen meets all constraints.
    Returns True if it does. Otherwise, returns False.

    Constraints: Two queens cannot be on the same row, column,
                or diagonal.
    """
    queen = chess_board[queen_key]

    if queen[1] > len(chess_board.keys()) - 1:
        # print("Out of bound")
        return False

    # confirm that queen is not on the same column of another queen
    for i in range(1, queen_key + 1):
        if queen[1] == chess_board[i][1] and queen_key != i:
            # print("Same column:")
            # print("queen({}) row: {} and chess_board[{}] row: {}".format(
            #     queen_key, queen[1], i, chess_board[i][1]
            # ))
            return False

    # Confirm that queen is not on the same diagonal of another queen
    i = queen_key - 1
    j = 1
    while i > 0:
        # Check the left diagonal
        if chess_board[i][1] == queen[1] - j:
            # print("diagonal left:")
            # print("queen({}) row: {} and chess_board[{}] row: {}".format(
            #     queen_key, queen[1], i, chess_board[i][1]
            # ))
            return False
        # Check the right diagonal
        if chess_board[i][1] == queen[1] + j:
            # print("diagonal right:")
            # print("queen({}) row: {} and chess_board[{}] row: {}".format(
            #     queen_key, queen[1], i, chess_board[i][1]
            # ))
            return False
        i -= 1
        j += 1
    return True


row = [i for i in range(n)]
column = [i for i in range(n)]
chess_board = {i + 1: [column[i], row[0]] for i in row}


def backtrack(chess_board: dict, queen_key: int):
    """Rearrange queens in chess_board until there's a solution.

    Parameters:
        chess_board: A dictionary containing the f_queen of all queens in
                     chess_board.
        queen_key: The key of a queen in chess_board.
    """
    if chess_board[1][1] > n - 1:
        return None

    for queen_key in range(queen_key, n + 1):
        queen = chess_board[queen_key]

        while validate(chess_board, queen_key) is False:
            # move the queen to the next cell
            if queen[1] > n - 1:
                queen[1] = 0
                chess_board[queen_key - 1][1] += 1
                chess_board = backtrack(chess_board, queen_key - 1)
                if chess_board is None:
                    break
            else:
                queen[1] += 1
        if chess_board is None:
            break

    return chess_board


if __name__ == "__main__":
    solution = ''
    while solution is not None:
        solution = backtrack(chess_board, 1)
        f_queen = chess_board[1][1]
        if solution:
            print([queen for k, queen in solution.items()])
        chess_board = {i + 1: [column[i], row[0], ] for i in row}
        f_queen += 1
        chess_board[1][1] = f_queen
