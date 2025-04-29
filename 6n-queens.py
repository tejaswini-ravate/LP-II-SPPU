def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 1:
            return False
        
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1
    return True

def solve_queens(board, row, n, solutions):
    if row == n:
        solution = []
        for i in range(n):
            row_str = ''.join('Q' if board[i][j] == 1 else '.' for j in range(n))
            solution.append(row_str)
        solutions.append(solution)
        return 
    
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_queens(board, row + 1, n, solutions)
            board[row][col] = 0 

def print_sol(solutions):
    for idx, sol in enumerate(solutions):
        print(f"Solution {idx + 1}:")
        for row in sol:
            print(row)
        print()

if __name__ == "__main__":
    n = int(input("Enter value of N: "))
    board = [[0] * n for _ in range(n)]
    solutions = []

    solve_queens(board, 0, n, solutions)
    print(f"Total solutions: {len(solutions)}")
    print_sol(solutions)
