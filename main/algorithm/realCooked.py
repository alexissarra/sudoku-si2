# Define a class for the Sudoku Solver
class SudokuSolver:
    # Initialize the solver with the board
    def __init__(self, board):
        self.board = board

    # Find the next empty square (denoted by 0)
    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return (i, j)  # row, col
        return None  # No empty square found, puzzle is solved

    # Check if a number can be placed at a position
    def is_valid(self, num, pos):
        # Check row
        for i in range(9):
            if self.board[pos[0]][i] == num and pos[1] != i:
                return False  # Number already in row

        # Check column
        for i in range(9):
            if self.board[i][pos[1]] == num and pos[0] != i:
                return False  # Number already in column

        # Check 3x3 box
        box_x = pos[1] // 3
        box_y = pos[0] // 3

        for i in range(box_y*3, box_y*3 + 3):
            for j in range(box_x*3, box_x*3 + 3):
                if self.board[i][j] == num and (i,j) != pos:
                    return False  # Number already in box
        return True  # Number can be placed

    # Solve the puzzle using backtracking
    def solve(self):
        find = self.find_empty()
        if not find:
            return True  # Puzzle solved
        else:
            row, col = find

        for i in range(1,10):
            if self.is_valid(i, (row, col)):
                self.board[row][col] = i  # Place number

                if self.solve():
                    return True  # Recursively solve rest of puzzle

                self.board[row][col] = 0  # Undo placement if it leads to no solution

        return False  # Trigger backtracking

    # Print the board
    def print_board(self):
        for i in range(len(self.board)):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - - - ")  # Print horizontal line every 3 rows
            for j in range(len(self.board[0])):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")  # Print vertical line every 3 columns
                if j == 8:
                    print(self.board[i][j])  # Print number
                else:
                    print(str(self.board[i][j]) + " ", end="")

# Main function to test the Sudoku Solver
if __name__ == "__main__":
    board = [
        [5, 1, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    solver = SudokuSolver(board)  # Create a solver with the board
    solver.solve()  # Solve the puzzle
    solver.print_board()  # Print the solved board