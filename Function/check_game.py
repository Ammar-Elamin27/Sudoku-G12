yyy
def by def



def load_labeled_sudoku():
    puzzle = np.array([
        [7, 2, 0, 0, 0, 1, 0, 0, 0],
        [8, 0, 0, 0, 0, 0, 0, 1, 9],
        [4, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 6, 9, 0, 0, 1, 0, 3],
        [0, 4, 0, 0, 0, 0, 9, 2, 0],
        [9, 0, 2, 1, 0, 8, 0, 7, 0],
        [2, 0, 0, 0, 0, 6, 0, 9, 0],
        [3, 9, 0, 0, 0, 7, 0, 0, 0],
        [6, 8, 0, 3, 0, 0, 5, 4, 1]
    ])

    solution = np.array([
        [7, 2, 3, 8, 9, 1, 6, 5, 4],
        [8, 6, 5, 2, 3, 4, 7, 1, 9],
        [4, 1, 9, 7, 6, 5, 8, 3, 2],
        [5, 7, 6, 9, 4, 2, 1, 8, 3],
        [1, 4, 8, 6, 7, 3, 9, 2, 5],
        [9, 3, 2, 1, 5, 8, 4, 7, 6],
        [2, 5, 1, 4, 8, 6, 3, 9, 7],
        [3, 9, 4, 5, 1, 7, 2, 6, 8],
        [6, 8, 7, 3, 2, 9, 5, 4, 1]
    ])

    return puzzle, solution

def display_board(board):
    print("   A B C   D E F   G H I")
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("   ------+-------+------")
        row_display = f"{i+1}  "
        for j in range(9):
            if j % 3 == 0 and j != 0:
                row_display += "| "
            cell = board[i][j]
            row_display += ". " if cell == 0 else f"{cell} "
        print(row_display)

def input_number(board, number, position):
    row, col = position
    board[row][col] = number
    return board

def play_sudoku():
    puzzle, solution = load_labeled_sudoku()
    strikes = 0
    max_strikes = 5

   
       
