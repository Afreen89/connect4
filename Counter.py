import random


def create_board():
    return [[0] * 7 for _ in range(6)]


def print_board(board):
    for row in board:
        print(' '.join(str(cell) for cell in row))
    print()


def is_valid_move(board, col):
    return board[0][col] == 0


def drop_counter(board, col, player):
    for row in range(5, -1, -1):
        if board[row][col] == 0:
            board[row][col] = player
            return row


def check_win(board, row, col, player):
    # Check horizontal
    if col <= 3 and all(board[row][col + i] == player for i in range(4)):
        return True

    # Check vertical
    if row <= 2 and all(board[row + i][col] == player for i in range(4)):
        return True

    return False


def is_stalemate(board):
    return all(board[0][col] != 0 for col in range(7))


def main():
    board = create_board()
    turn = 1

    while True:
        print_board(board)

        if turn == 1:
            player_col = int(input("Player 1's turn - Enter column (0-6): "))
        else:
            player_col = random.randint(0, 6)  # Computer's random move

        if not (0 <= player_col <= 6):
            print("Invalid column. Please choose a column between 0 and 6.")
            continue

        if is_valid_move(board, player_col):
            player_row = drop_counter(board, player_col, turn)

            if check_win(board, player_row, player_col, turn):
                print_board(board)
                print(f"Player {turn} wins!")
                break

            if is_stalemate(board):
                print_board(board)
                print("Stalemate! The grid is full and there is no winner.")
                break

            turn = 3 - turn  # Switch player's turn (1 -> 2 or 2 -> 1)
        else:
            print("Column is already full. Please choose another column.")


if __name__ == "__main__":
    main()