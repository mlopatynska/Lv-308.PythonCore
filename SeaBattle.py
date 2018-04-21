from random import randint

print('\nYou have 4 chances to sink my battleship! Good luck!\n')

board = [[' ', '1', '2', '3', '4', '5']]

for x in range(1, 6):
    board.append([str(x)] + ["O"] * 5)


def print_board(board_in):
    for row in board_in:
        print("  ".join(row))


print_board(board)


def random_row(board_in):
    return randint(1, len(board_in) - 1)


def random_col(board_in):
    return randint(1, len(board_in) - 1)


ship_row = random_row(board)
ship_col = random_col(board)
#print(ship_row)
#print(ship_col)

for turn in range(1, 6):
    guess_row = int(input("\nGuess Row: ")) + 1
    guess_col = int(input("Guess Col: ")) + 1

    if guess_row == ship_row + 1 and guess_col == ship_col + 1:
        print("\nCongratulations! You sunk my battleship!\n")
        board[ship_row][ship_col] = "#"
        print_board(board)
        break
    else:
        if (guess_row < 2 or guess_row > 6) or (guess_col < 2 or guess_col > 6):
            print("Oops, that's not even in the ocean.\n")
        elif board[guess_row-1][guess_col-1] == "X":
            print("You guessed that one already.\n")
        else:
            print("You missed my battleship!\n")
            board[guess_row-1][guess_col-1] = "X"
    if turn == 4:
        print(f"Game Over\n\nMy battleship was on:\nRow: {ship_row} \ Col: {ship_col}\n")
        board[ship_row][ship_col] = "#"
        print_board(board)
        break
    print(f'Turn{turn + 1}\n')
    print_board(board)
